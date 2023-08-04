import json
from urllib.parse import urlencode, urlunsplit
from typing import Union, Optional

from .auth import Authentication
from .auth_schemas import TokenRequest, TokenRequestGrantType, AccessToken
from .fetch import fetch, FetchResponse, FetchOptions
from .network import NetworkSession


class OAuthConfig:
    def __init__(
            self,
            client_id: str,
            client_secret: str,
    ):
        """
        :param client_id:
            Box API key used for identifying the application the user is authenticating with.
        :param client_secret:
            Box API secret used for making auth requests.
        """
        self.client_id = client_id
        self.client_secret = client_secret


class GetAuthorizeUrlOptions:
    def __init__(
            self,
            client_id: Optional[str] = None,
            redirect_uri: Optional[str] = None,
            response_type: Optional[str] = None,
            state: Optional[str] = None,
            scope: Optional[str] = None
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


class OAuth(Authentication):
    OAUTH2_AUTHORIZE_URL = 'https://account.box.com/api/oauth2/authorize'

    def __init__(self,  config: OAuthConfig):
        """
        :param config:
            Configuration object of OAuth.
        """
        self.config = config
        self.token: Union[None, AccessToken] = None

    def get_authorize_url(self, options: Optional[GetAuthorizeUrlOptions] = None) -> str:
        """
        Get the authorization URL for the app user.
        :param options: Options class for getting authorization url
        :return: Authorization url
        """
        if options is None:
            options = GetAuthorizeUrlOptions()

        params = [
            ('client_id', options.client_id if options.client_id is not None else self.config.client_id),
            ('response_type', options.response_type if options.response_type is not None else 'code'),
        ]

        if options.redirect_uri is not None:
            params.append(('redirect_uri', options.redirect_uri))

        if options.state is not None:
            params.append(('state', options.state))

        if options.scope is not None:
            params.append(('scope', options.scope))

        params = [(key.encode('utf-8'), value.encode('utf-8'))
                  for (key, value) in params]
        query_string = urlencode(params)
        return urlunsplit(('', '', self.OAUTH2_AUTHORIZE_URL, query_string, ''))

    def get_tokens_authorization_code_grant(
            self,
            authorization_code: str,
            network_session: Optional[NetworkSession] = None
    ) -> str:
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
            code=authorization_code
        )

        self.token = self._send_token_request(request_body, network_session)
        return self.token.access_token

    def retrieve_token(self, network_session: Optional[NetworkSession] = None) -> str:
        """
         Return a current token or get a new one when not available.
        :param network_session: An object to keep network session state
        :return: Valid access token
        """
        if self.token is None:
            raise Exception(
                "Access and refresh tokens not available. Authenticate before making any API call first.")
        return self.token.access_token

    def refresh(self, network_session: Optional[NetworkSession] = None) -> str:
        """
        Refresh outdated access token with refresh token
        :param network_session: An object to keep network session state
        :return: Valid access token
        """
        request_body = TokenRequest(
            grant_type=TokenRequestGrantType.REFRESH_TOKEN,
            client_id=self.config.client_id,
            client_secret=self.config.client_secret,
            refresh_token=self.token.refresh_token
        )

        self.token = self._send_token_request(request_body, network_session)
        return self.token.access_token

    @staticmethod
    def _send_token_request(
            request_body: TokenRequest,
            network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        response: FetchResponse = fetch(
            'https://api.box.com/oauth2/token',
            FetchOptions(
                method='POST',
                body=urlencode(request_body.to_dict()),
                headers={'content-type': 'application/x-www-form-urlencoded'},
                network_session=network_session
            )
        )

        return AccessToken.from_dict(json.loads(response.text))
