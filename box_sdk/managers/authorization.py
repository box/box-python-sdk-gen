from enum import Enum

from typing import Optional

from box_sdk.base_object import BaseObject

from box_sdk.schemas import AccessToken

from box_sdk.schemas import OAuth2Error

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetAuthorizeResponseTypeArg(str, Enum):
    CODE = 'code'

class GetAuthorizeOptionsArg(BaseObject):
    def __init__(self, redirect_uri: Optional[str] = None, state: Optional[str] = None, scope: Optional[str] = None, **kwargs):
        """
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
        """
        super().__init__(**kwargs)
        self.redirect_uri = redirect_uri
        self.state = state
        self.scope = scope

class AuthorizationManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_authorize(self, response_type: GetAuthorizeResponseTypeArg, client_id: str, options: GetAuthorizeOptionsArg = None) -> None:
        """
        Authorize a user by sending them through the [Box](https://box.com)
        
        website and request their permission to act on their behalf.

        
        This is the first step when authenticating a user using

        
        OAuth 2.0. To request a user's authorization to use the Box APIs

        
        on their behalf you will need to send a user to the URL with this

        
        format.

        :param response_type: The type of response we'd like to receive.
            Example: "code"
        :type response_type: GetAuthorizeResponseTypeArg
        :param client_id: The Client ID of the application that is requesting to authenticate
            the user. To get the Client ID for your application, log in to your
            Box developer console and click the **Edit Application** link for
            the application you're working with. In the OAuth 2.0 Parameters section
            of the configuration page, find the item labelled `client_id`. The
            text of that item is your application's Client ID.
            Example: "ly1nj6n11vionaie65emwzk575hnnmrk"
        :type client_id: str
        """
        if options is None:
            options = GetAuthorizeOptionsArg()
        response: FetchResponse = fetch(''.join(['https://account.box.com/api/oauth2/authorize']), FetchOptions(method='GET', params={'response_type': response_type, 'client_id': client_id, 'redirect_uri': options.redirect_uri, 'state': options.state, 'scope': options.scope}, auth=self.auth, network_session=self.network_session))
        return None