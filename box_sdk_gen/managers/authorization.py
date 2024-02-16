from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import serialize

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.schemas import PostOAuth2TokenGrantTypeField

from box_sdk_gen.schemas import PostOAuth2TokenSubjectTokenTypeField

from box_sdk_gen.schemas import PostOAuth2TokenBoxSubjectTypeField

from box_sdk_gen.schemas import AccessToken

from box_sdk_gen.schemas import OAuth2Error

from box_sdk_gen.schemas import PostOAuth2Token

from box_sdk_gen.schemas import PostOAuth2TokenRefreshAccessToken

from box_sdk_gen.schemas import PostOAuth2Revoke

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json_data import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json_data import SerializedData


class AuthorizeUserResponseType(str, Enum):
    CODE = 'code'


class RequestAccessTokenGrantType(str, Enum):
    AUTHORIZATION_CODE = 'authorization_code'
    REFRESH_TOKEN = 'refresh_token'
    CLIENT_CREDENTIALS = 'client_credentials'
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER = (
        'urn:ietf:params:oauth:grant-type:jwt-bearer'
    )
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE = (
        'urn:ietf:params:oauth:grant-type:token-exchange'
    )


class RequestAccessTokenSubjectTokenType(str, Enum):
    URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_ACCESS_TOKEN = (
        'urn:ietf:params:oauth:token-type:access_token'
    )


class RequestAccessTokenActorTokenType(str, Enum):
    URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_ID_TOKEN = (
        'urn:ietf:params:oauth:token-type:id_token'
    )


class RequestAccessTokenBoxSubjectType(str, Enum):
    ENTERPRISE = 'enterprise'
    USER = 'user'


class RefreshAccessTokenGrantType(str, Enum):
    REFRESH_TOKEN = 'refresh_token'


class AuthorizationManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: NetworkSession = None,
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session

    def authorize_user(
        self,
        response_type: AuthorizeUserResponseType,
        client_id: str,
        redirect_uri: Optional[str] = None,
        state: Optional[str] = None,
        scope: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Authorize a user by sending them through the [Box](https://box.com)

        website and request their permission to act on their behalf.


        This is the first step when authenticating a user using


        OAuth 2.0. To request a user's authorization to use the Box APIs


        on their behalf you will need to send a user to the URL with this


        format.

        :param response_type: The type of response we'd like to receive.
        :type response_type: AuthorizeUserResponseType
        :param client_id: The Client ID of the application that is requesting to authenticate
            the user. To get the Client ID for your application, log in to your
            Box developer console and click the **Edit Application** link for
            the application you're working with. In the OAuth 2.0 Parameters section
            of the configuration page, find the item labelled `client_id`. The
            text of that item is your application's Client ID.
        :type client_id: str
        :param redirect_uri: The URI to which Box redirects the browser after the user has granted
            or denied the application permission. This URI match one of the redirect
            URIs in the configuration of your application. It must be a
            valid HTTPS URI and it needs to be able to handle the redirection to
            complete the next step in the OAuth 2.0 flow.
            Although this parameter is optional, it must be a part of the
            authorization URL if you configured multiple redirect URIs
            for the application in the developer console. A missing parameter causes
            a `redirect_uri_missing` error after the user grants application access.
        :type redirect_uri: Optional[str], optional
        :param state: A custom string of your choice. Box will pass the same string to
            the redirect URL when authentication is complete. This parameter
            can be used to identify a user on redirect, as well as protect
            against hijacked sessions and other exploits.
        :type state: Optional[str], optional
        :param scope: A space-separated list of application scopes you'd like to
            authenticate the user for. This defaults to all the scopes configured
            for the application in its configuration page.
        :type scope: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {
                'response_type': to_string(response_type),
                'client_id': to_string(client_id),
                'redirect_uri': to_string(redirect_uri),
                'state': to_string(state),
                'scope': to_string(scope),
            }
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([self.network_session.base_urls.oauth_2_url, '/authorize']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def request_access_token(
        self,
        grant_type: RequestAccessTokenGrantType,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        refresh_token: Optional[str] = None,
        assertion: Optional[str] = None,
        subject_token: Optional[str] = None,
        subject_token_type: Optional[RequestAccessTokenSubjectTokenType] = None,
        actor_token: Optional[str] = None,
        actor_token_type: Optional[RequestAccessTokenActorTokenType] = None,
        scope: Optional[str] = None,
        resource: Optional[str] = None,
        box_subject_type: Optional[RequestAccessTokenBoxSubjectType] = None,
        box_subject_id: Optional[str] = None,
        box_shared_link: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> AccessToken:
        """
        Request an Access Token using either a client-side obtained OAuth 2.0

        authorization code or a server-side JWT assertion.


        An Access Token is a string that enables Box to verify that a


        request belongs to an authorized session. In the normal order of


        operations you will begin by requesting authentication from the


        [authorize](#get-authorize) endpoint and Box will send you an


        authorization code.


        You will then send this code to this endpoint to exchange it for


        an Access Token. The returned Access Token can then be used to to make


        Box API calls.

        :param grant_type: The type of request being made, either using a client-side obtained
            authorization code, a refresh token, a JWT assertion, client credentials
            grant or another access token for the purpose of downscoping a token.
        :type grant_type: RequestAccessTokenGrantType
        :param client_id: The Client ID of the application requesting an access token.
            Used in combination with `authorization_code`, `client_credentials`, or
            `urn:ietf:params:oauth:grant-type:jwt-bearer` as the `grant_type`.
        :type client_id: Optional[str], optional
        :param client_secret: The client secret of the application requesting an access token.
            Used in combination with `authorization_code`, `client_credentials`, or
            `urn:ietf:params:oauth:grant-type:jwt-bearer` as the `grant_type`.
        :type client_secret: Optional[str], optional
        :param code: The client-side authorization code passed to your application by
            Box in the browser redirect after the user has successfully
            granted your application permission to make API calls on their
            behalf.
            Used in combination with `authorization_code` as the `grant_type`.
        :type code: Optional[str], optional
        :param refresh_token: A refresh token used to get a new access token with.
            Used in combination with `refresh_token` as the `grant_type`.
        :type refresh_token: Optional[str], optional
        :param assertion: A JWT assertion for which to request a new access token.
            Used in combination with `urn:ietf:params:oauth:grant-type:jwt-bearer`
            as the `grant_type`.
        :type assertion: Optional[str], optional
        :param subject_token: The token to exchange for a downscoped token. This can be a regular
            access token, a JWT assertion, or an app token.
            Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange`
            as the `grant_type`.
        :type subject_token: Optional[str], optional
        :param subject_token_type: The type of `subject_token` passed in.
            Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange`
            as the `grant_type`.
        :type subject_token_type: Optional[RequestAccessTokenSubjectTokenType], optional
        :param actor_token: The token used to create an annotator token.
            This is a JWT assertion.
            Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange`
            as the `grant_type`.
        :type actor_token: Optional[str], optional
        :param actor_token_type: The type of `actor_token` passed in.
            Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange`
            as the `grant_type`.
        :type actor_token_type: Optional[RequestAccessTokenActorTokenType], optional
        :param scope: The space-delimited list of scopes that you want apply to the
            new access token.
            The `subject_token` will need to have all of these scopes or
            the call will error with **401 Unauthorized**.
        :type scope: Optional[str], optional
        :param resource: Full URL for the file that the token should be generated for.
        :type resource: Optional[str], optional
        :param box_subject_type: Used in combination with `client_credentials` as the `grant_type`.
        :type box_subject_type: Optional[RequestAccessTokenBoxSubjectType], optional
        :param box_subject_id: Used in combination with `client_credentials` as the `grant_type`.
            Value is determined by `box_subject_type`. If `user` use user ID and if
            `enterprise` use enterprise ID.
        :type box_subject_id: Optional[str], optional
        :param box_shared_link: Full URL of the shared link on the file or folder
            that the token should be generated for.
        :type box_shared_link: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'grant_type': grant_type,
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'refresh_token': refresh_token,
            'assertion': assertion,
            'subject_token': subject_token,
            'subject_token_type': subject_token_type,
            'actor_token': actor_token,
            'actor_token_type': actor_token_type,
            'scope': scope,
            'resource': resource,
            'box_subject_type': box_subject_type,
            'box_subject_id': box_subject_id,
            'box_shared_link': box_shared_link,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/oauth2/token']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/x-www-form-urlencoded',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, AccessToken)

    def refresh_access_token(
        self,
        grant_type: RefreshAccessTokenGrantType,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> AccessToken:
        """
        Refresh an Access Token using its client ID, secret, and refresh token.
        :param grant_type: The type of request being made, in this case a refresh request.
        :type grant_type: RefreshAccessTokenGrantType
        :param client_id: The client ID of the application requesting to refresh the token.
        :type client_id: str
        :param client_secret: The client secret of the application requesting to refresh the token.
        :type client_secret: str
        :param refresh_token: The refresh token to refresh.
        :type refresh_token: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'grant_type': grant_type,
            'client_id': client_id,
            'client_secret': client_secret,
            'refresh_token': refresh_token,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/oauth2/token#refresh']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/x-www-form-urlencoded',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, AccessToken)

    def revoke_access_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        token: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Revoke an active Access Token, effectively logging a user out

        that has been previously authenticated.

        :param client_id: The Client ID of the application requesting to revoke the
            access token.
        :type client_id: Optional[str], optional
        :param client_secret: The client secret of the application requesting to revoke
            an access token.
        :type client_secret: Optional[str], optional
        :param token: The access token to revoke.
        :type token: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'client_id': client_id,
            'client_secret': client_secret,
            'token': token,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/oauth2/revoke']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/x-www-form-urlencoded',
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None
