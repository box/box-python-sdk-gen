from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.schemas import AccessToken

from box_sdk_gen.schemas import OAuth2Error

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class GetAuthorizeResponseTypeArg(str, Enum):
    CODE = 'code'


class AuthorizationManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_authorize(
        self,
        response_type: GetAuthorizeResponseTypeArg,
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
        :type response_type: GetAuthorizeResponseTypeArg
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
        :param scope: A comma-separated list of application scopes you'd like to
            authenticate the user for. This defaults to all the scopes configured
            for the application in its configuration page.
        :type scope: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({
            'response_type': to_string(response_type),
            'client_id': to_string(client_id),
            'redirect_uri': to_string(redirect_uri),
            'state': to_string(state),
            'scope': to_string(scope),
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://account.box.com/api/oauth2/authorize']),
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
