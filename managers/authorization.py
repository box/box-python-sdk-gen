from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

from schemas import AccessToken

from schemas import OAuth2Error

class GetAuthorizeResponseTypeArg:
    pass

class GetAuthorizeOptionsArg(BaseObject):
    def __init__(self, redirectUri: Union[None, str] = None, state: Union[None, str] = None, scope: Union[None, str] = None, **kwargs):
        """
        :param redirectUri: The URI to which Box redirects the browser after the user has granted
            or denied the application permission. This URI match one of the redirect
            URIs in the configuration of your application. It must be a
            valid HTTPS URI and it needs to be able to handle the redirection to
            complete the next step in the OAuth 2.0 flow.
            Although this parameter is optional, it must be a part of the
            authorization URL if you configured multiple redirect URIs
            for the application in the developer console. A missing parameter causes
            a `redirect_uri_missing` error after the user grants application access.
        :type redirectUri: Union[None, str], optional
        :param state: A custom string of your choice. Box will pass the same string to
            the redirect URL when authentication is complete. This parameter
            can be used to identify a user on redirect, as well as protect
            against hijacked sessions and other exploits.
        :type state: Union[None, str], optional
        :param scope: A comma-separated list of application scopes you'd like to
            authenticate the user for. This defaults to all the scopes configured
            for the application in its configuration page.
        :type scope: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.redirectUri = redirectUri
        self.state = state
        self.scope = scope

class AuthorizationManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getAuthorize(self, responseType: GetAuthorizeResponseTypeArg, clientId: str, options: GetAuthorizeOptionsArg = None) -> None:
        """
        Authorize a user by sending them through the [Box](https://box.com)
        
        website and request their permission to act on their behalf.

        
        This is the first step when authenticating a user using

        
        OAuth 2.0. To request a user's authorization to use the Box APIs

        
        on their behalf you will need to send a user to the URL with this

        
        format.

        :param responseType: The type of response we'd like to receive.
            Example: "code"
        :type responseType: GetAuthorizeResponseTypeArg
        :param clientId: The Client ID of the application that is requesting to authenticate
            the user. To get the Client ID for your application, log in to your
            Box developer console and click the **Edit Application** link for
            the application you're working with. In the OAuth 2.0 Parameters section
            of the configuration page, find the item labelled `client_id`. The
            text of that item is your application's Client ID.
            Example: "ly1nj6n11vionaie65emwzk575hnnmrk"
        :type clientId: str
        """
        if options is None:
            options = GetAuthorizeOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/authorize']), FetchOptions(method='GET', params={'response_type': responseType, 'client_id': clientId, 'redirect_uri': options.redirectUri, 'state': options.state, 'scope': options.scope}, auth=self.auth))
        return None