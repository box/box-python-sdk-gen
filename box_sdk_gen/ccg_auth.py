import json
from urllib.parse import urlencode
from typing import Union, Optional

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


class CCGConfig:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        enterprise_id: Union[None, str] = None,
        user_id: Union[None, str] = None,
        token_storage: TokenStorage = None,
    ):
        """
        :param client_id:
            Box API key used for identifying the application the user is authenticating with.
        :param client_secret:
            Box API secret used for making auth requests.
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
        self.token_storage = token_storage


class BoxCCGAuth(Authentication):
    def __init__(self, config: CCGConfig):
        """
        :param config:
            Configuration object of Client Credentials Grant auth.
        """
        self.config = config
        self.token_storage = config.token_storage

        if config.user_id:
            self.subject_id = self.config.user_id
            self.subject_type = TokenRequestBoxSubjectType.USER
        else:
            self.subject_type = TokenRequestBoxSubjectType.ENTERPRISE
            self.subject_id = self.config.enterprise_id

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
        Return a current token or get a new one when not available.
        :param network_session: An object to keep network session state
        :return: Access token
        """
        request_body = TokenRequest(
            grant_type=TokenRequestGrantType.CLIENT_CREDENTIALS,
            client_id=self.config.client_id,
            client_secret=self.config.client_secret,
            box_subject_id=self.subject_id,
            box_subject_type=self.subject_type,
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
