from urllib.parse import urlencode, urlunsplit
from typing import Optional

from .auth import Authentication
from .token_storage import TokenStorage, InMemoryTokenStorage
from .auth_schemas import TokenRequest, TokenRequestGrantType
from .fetch import fetch, FetchResponse, FetchOptions
from .network import NetworkSession
from .schemas import AccessToken
from .json import json_to_serialized_data


class OAuthConfig:
    def __init__(
        self, client_id: str, client_secret: str, token_storage: TokenStorage = None
    ):
        """
        :param client_id:
            Box API key used for identifying the application the user is authenticating with.
        :param client_secret:
            Box API secret used for making auth requests.
        :param token_storage:
            Object responsible for storing token. If no custom implementation provided,
            the token will be stored in memory.
        """

        if token_storage is None:
            token_storage = InMemoryTokenStorage()
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_storage = token_storage


class GetAuthorizeUrlOptions:
    def __init__(
        self,
        client_id: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        response_type: Optional[str] = None,
        state: Optional[str] = None,
        scope: Optional[str] = None,
    ):
        """
        :param client_id: The Client ID of the application that is requesting to authenticate the user.
        :param redirect_uri: The URI to which Box redirects the browser after the user has granted or
         denied the application permission.
        :param response_type: The type of response we'd like to receive. Must be 'code'.
        :param state: A custom string of your choice. Box will pass the same string to the redirect
         URL when authentication is complete.
        :param scope: A comma-separated list of application scopes you'd like to authenticate the user for.
        """
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.response_type = response_type
        self.state = state
        self.scope = scope


class BoxOAuth(Authentication):
    OAUTH2_AUTHORIZE_URL = 'https://account.box.com/api/oauth2/authorize'

    def __init__(self, config: OAuthConfig):
        """
        :param config:
            Configuration object of OAuth.
        """
        self.config = config
        self.token_storage = config.token_storage

    def get_authorize_url(
        self, options: Optional[GetAuthorizeUrlOptions] = None
    ) -> str:
        """
        Get the authorization URL for the app user.
        :param options: Options class for getting authorization url
        :return: Authorization url
        """
        if options is None:
            options = GetAuthorizeUrlOptions()

        params = [
            (
                'client_id',
                (
                    options.client_id
                    if options.client_id is not None
                    else self.config.client_id
                ),
            ),
            (
                'response_type',
                options.response_type if options.response_type is not None else 'code',
            ),
        ]

        if options.redirect_uri is not None:
            params.append(('redirect_uri', options.redirect_uri))

        if options.state is not None:
            params.append(('state', options.state))

        if options.scope is not None:
            params.append(('scope', options.scope))

        params = [
            (key.encode('utf-8'), value.encode('utf-8')) for (key, value) in params
        ]
        query_string = urlencode(params)
        return urlunsplit(('', '', self.OAUTH2_AUTHORIZE_URL, query_string, ''))

    def get_tokens_authorization_code_grant(
        self, authorization_code: str, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
        Send token request and return the access_token
        :param authorization_code: Short-lived authorization code
        :param network_session: An object to keep network session state
        :return: Access token
        """
        request_body = TokenRequest(
            grant_type=TokenRequestGrantType.AUTHORIZATION_CODE,
            client_id=self.config.client_id,
            client_secret=self.config.client_secret,
            code=authorization_code,
        )

        token: AccessToken = self._send_token_request(request_body, network_session)
        self.token_storage.store(token)
        return token

    def retrieve_token(
        self, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
         Return a current token or get a new one when not available.
        :param network_session: An object to keep network session state
        :return: Valid access token
        """
        token = self.token_storage.get()
        if token is None:
            raise Exception(
                "Access and refresh tokens not available. Authenticate before making"
                " any API call first."
            )
        return token

    def refresh_token(
        self,
        network_session: Optional[NetworkSession] = None,
        refresh_token: Optional[str] = None,
    ) -> AccessToken:
        """
        Refresh outdated access token with refresh token
        :param network_session: An object to keep network session state
        :param refresh_token: Refresh token, which can be used to obtain a new access token
        :return: Valid access token
        """
        old_token: Optional[AccessToken] = self.token_storage.get()
        token_used_for_refresh = (
            refresh_token or old_token.refresh_token if old_token else None
        )

        if token_used_for_refresh is None:
            raise Exception("No refresh_token is available.")

        request_body = TokenRequest(
            grant_type=TokenRequestGrantType.REFRESH_TOKEN,
            client_id=self.config.client_id,
            client_secret=self.config.client_secret,
            refresh_token=refresh_token or old_token.refresh_token,
        )

        new_token = self._send_token_request(request_body, network_session)
        self.token_storage.store(new_token)
        return new_token

    @staticmethod
    def _send_token_request(
        request_body: TokenRequest, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        response: FetchResponse = fetch(
            'https://api.box.com/oauth2/token',
            FetchOptions(
                method='POST',
                data=request_body.to_dict(),
                content_type='application/x-www-form-urlencoded',
                network_session=network_session,
            ),
        )

        return AccessToken.from_dict(json_to_serialized_data(response.text))
