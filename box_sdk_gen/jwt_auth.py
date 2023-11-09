from datetime import datetime, timedelta
import random
import string

from typing import Optional, Any
from urllib.parse import urlencode

try:
    import jwt
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization
except ImportError:
    jwt, default_backend, serialization = None, None, None

from .auth import Authentication
from .token_storage import TokenStorage, InMemoryTokenStorage
from .auth_schemas import (
    TokenRequestBoxSubjectType,
    TokenRequest,
    TokenRequestGrantType,
)
from .fetch import fetch, FetchResponse, FetchOptions
from .network import NetworkSession
from .schemas import AccessToken
from .json import json_to_serialized_data


class JWTConfig:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        jwt_key_id: str,
        private_key: str,
        private_key_passphrase: str,
        enterprise_id: Optional[str] = None,
        user_id: Optional[str] = None,
        jwt_algorithm: str = 'RS256',
        token_storage: TokenStorage = None,
        **_kwargs
    ):
        """
        :param client_id:
            Box API key used for identifying the application the user is authenticating with.
        :param client_secret:
            Box API secret used for making auth requests.
        :param jwt_key_id:
            Key ID for the JWT assertion.
        :param private_key:
            Contents of RSA private key, used for signing the JWT assertion.
        :param private_key_passphrase:
            Passphrase used to unlock the private key.
        :param enterprise_id:
            The ID of the Box Developer Edition enterprise.

            May be `None`, if the caller knows that it will not be
            authenticating as an enterprise instance / service account.

            If `user_id` is passed, this value is not used, unless
            `authenticate_enterprise()` is called to authenticate as the enterprise instance.
        :param user_id:
            The user id to authenticate. This value is not required. But if it is provided, then the user
            will be auto-authenticated at the time of the first API call.

            Should be `None` if the intention is to authenticate as the
            enterprise instance / service account. If both `enterprise_id` and
            `user_id` are non-`None`, the `user` takes precedense when `refresh()`
            is called.

            <https://developer.box.com/en/guides/applications/>
            <https://developer.box.com/en/guides/authentication/select/>
        :param jwt_algorithm:
            Which algorithm to use for signing the JWT assertion. Must be one of 'RS256', 'RS384', 'RS512'.
        :param token_storage:
            Object responsible for storing token. If no custom implementation provided,
            the token will be stored in memory.
        """
        if token_storage is None:
            token_storage = InMemoryTokenStorage()
        if not enterprise_id and not user_id:
            raise Exception("Enterprise ID or User ID is needed")

        self.client_id = client_id
        self.client_secret = client_secret
        self.enterprise_id = enterprise_id
        self.user_id = user_id
        self.jwt_key_id = jwt_key_id
        self.private_key = private_key
        self.private_key_passphrase = private_key_passphrase
        self.jwt_algorithm = jwt_algorithm
        self.token_storage = token_storage

    @classmethod
    def from_config_json_string(
        cls, config_json_string: str, token_storage: TokenStorage = None, **kwargs: Any
    ) -> 'JWTConfig':
        """
        Create an auth instance as defined by a string content of JSON file downloaded from the Box Developer Console.
        See https://developer.box.com/en/guides/authentication/jwt/ for more information.

        :param config_json_string:
             String content of JSON file containing the configuration.
        :param token_storage:
            Object responsible for storing token. If no custom implementation provided,
            the token will be stored in memory.
        :return:
            Auth instance configured as specified by the config dictionary.
        """
        config_dict: dict = json_to_serialized_data(config_json_string)
        if 'boxAppSettings' not in config_dict:
            raise ValueError('boxAppSettings not present in configuration')
        return cls(
            client_id=config_dict['boxAppSettings']['clientID'],
            client_secret=config_dict['boxAppSettings']['clientSecret'],
            enterprise_id=config_dict.get('enterpriseID', None),
            jwt_key_id=config_dict['boxAppSettings']['appAuth'].get(
                'publicKeyID', None
            ),
            private_key=config_dict['boxAppSettings']['appAuth'].get(
                'privateKey', None
            ),
            private_key_passphrase=config_dict['boxAppSettings']['appAuth'].get(
                'passphrase', None
            ),
            token_storage=token_storage,
            **kwargs
        )

    @classmethod
    def from_config_file(
        cls, config_file_path: str, token_storage: TokenStorage = None, **kwargs: Any
    ) -> 'JWTConfig':
        """
        Create an auth instance as defined by a JSON file downloaded from the Box Developer Console.
        See https://developer.box.com/en/guides/authentication/jwt/ for more information.

        :param config_file_path:
            Path to the JSON file containing the configuration.
        :param token_storage:
            Object responsible for storing token. If no custom implementation provided,
            the token will be stored in memory.
        :return:
            Auth instance configured as specified by the JSON file.
        """
        with open(config_file_path, encoding='utf-8') as config_file:
            return cls.from_config_json_string(
                config_file.read(), token_storage, **kwargs
            )


class BoxJWTAuth(Authentication):
    def __init__(self, config: JWTConfig):
        """
        :param config:
            Configuration object of Client Credentials Grant auth.
        """
        if None in (default_backend, serialization, jwt):
            raise Exception(
                'Missing dependencies required for JWTAuth. To install them use'
                ' command: `pip install box-sdk-gen[jwt]`'
            )

        self.config = config
        self.token_storage = config.token_storage

        if config.enterprise_id:
            self.subject_type = TokenRequestBoxSubjectType.ENTERPRISE
            self.subject_id = self.config.enterprise_id
        else:
            self.subject_id = self.config.user_id
            self.subject_type = TokenRequestBoxSubjectType.USER

        self._rsa_private_key = self._get_rsa_private_key(
            config.private_key, config.private_key_passphrase
        )

    def retrieve_token(
        self, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
        Return a current token or get a new one when not available.
        :param network_session: An object to keep network session state
        :return: Access token
        """
        token = self.token_storage.get()
        if token is None:
            return self.refresh_token(network_session=network_session)
        return token

    def refresh_token(
        self, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
        Fetch a new access token
        :param network_session: An object to keep network session state
        :return: New access token
        """
        system_random = random.SystemRandom()
        jti_length = system_random.randint(16, 128)
        ascii_alphabet = string.ascii_letters + string.digits
        ascii_len = len(ascii_alphabet)
        jti = ''.join(
            ascii_alphabet[int(system_random.random() * ascii_len)]
            for _ in range(jti_length)
        )
        now_time = datetime.utcnow()
        now_plus_30 = now_time + timedelta(seconds=30)
        assertion = jwt.encode(
            {
                'iss': self.config.client_id,
                'sub': self.subject_id,
                'box_sub_type': self.subject_type,
                'aud': 'https://api.box.com/oauth2/token',
                'jti': jti,
                'exp': int((now_plus_30 - datetime(1970, 1, 1)).total_seconds()),
            },
            self._rsa_private_key,
            algorithm=self.config.jwt_algorithm,
            headers={
                'kid': self.config.jwt_key_id,
            },
        )

        request_body = TokenRequest(
            grant_type=TokenRequestGrantType.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER,
            client_id=self.config.client_id,
            client_secret=self.config.client_secret,
            assertion=assertion,
        )

        response: FetchResponse = fetch(
            'https://api.box.com/oauth2/token',
            FetchOptions(
                method='POST',
                data=request_body.to_dict(),
                content_type='application/x-www-form-urlencoded',
                network_session=network_session,
            ),
        )

        new_token = AccessToken.from_dict(response.data)
        self.token_storage.store(new_token)
        return new_token

    def as_user(self, user_id: str):
        """
        Set authentication as user. The new token will be automatically fetched with a next API call.

        May be one of this application's created App User. Depending on the
        configured User Access Level, may also be any other App User or Managed
        User in the enterprise.

        <https://developer.box.com/en/guides/applications/>
        <https://developer.box.com/en/guides/authentication/select/>

        :param user_id:
            The id of the user to authenticate.
        """
        self.subject_id = user_id
        self.subject_type = TokenRequestBoxSubjectType.USER
        self.token_storage.clear()

    def as_enterprise(self, enterprise_id: str):
        """
        Set authentication as enterprise. The new token will be automatically fetched with a next API call.

        :param enterprise_id:
            The ID of the Box Developer Edition enterprise.
        """
        self.subject_id = enterprise_id
        self.subject_type = TokenRequestBoxSubjectType.ENTERPRISE
        self.token_storage.clear()

    @classmethod
    def _get_rsa_private_key(
        cls,
        private_key: str,
        passphrase: str,
    ) -> Any:
        encoded_private_key = cls._encode_str_ascii_or_raise(private_key)
        encoded_passphrase = cls._encode_str_ascii_or_raise(passphrase)

        return serialization.load_pem_private_key(
            encoded_private_key,
            password=encoded_passphrase,
            backend=default_backend(),
        )

    @staticmethod
    def _encode_str_ascii_or_raise(passphrase: str) -> bytes:
        try:
            return passphrase.encode('ascii')
        except UnicodeError as unicode_error:
            raise TypeError(
                "private_key and private_key_passphrase must contain binary data"
                " (bytes/str), not a text/unicode string"
            ) from unicode_error
