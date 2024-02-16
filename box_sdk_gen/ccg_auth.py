from typing import Optional

from typing import List

from box_sdk_gen.schemas import PostOAuth2TokenGrantTypeField

from box_sdk_gen.schemas import PostOAuth2TokenSubjectTokenTypeField

from box_sdk_gen.schemas import AccessToken

from box_sdk_gen.schemas import PostOAuth2TokenBoxSubjectTypeField

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.token_storage import TokenStorage

from box_sdk_gen.token_storage import InMemoryTokenStorage

from box_sdk_gen.managers.authorization import AuthorizationManager

from box_sdk_gen.errors import BoxSDKError


class CCGConfig:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        enterprise_id: Optional[str] = None,
        user_id: Optional[str] = None,
        token_storage: TokenStorage = None,
    ):
        """
        :param client_id: Box API key used for identifying the application the user is authenticating with
        :type client_id: str
        :param client_secret: Box API secret used for making auth requests.
        :type client_secret: str
        :param enterprise_id: The ID of the Box Developer Edition enterprise.
        :type enterprise_id: Optional[str], optional
        :param user_id: The user id to authenticate. This value is not required. But if it is provided, then the user will be auto-authenticated at the time of the first API call.
        :type user_id: Optional[str], optional
        :param token_storage: Object responsible for storing token. If no custom implementation provided,the token will be stored in memory.
        :type token_storage: TokenStorage, optional
        """
        if token_storage is None:
            token_storage = InMemoryTokenStorage()
        self.client_id = client_id
        self.client_secret = client_secret
        self.enterprise_id = enterprise_id
        self.user_id = user_id
        self.token_storage = token_storage


class BoxCCGAuth(Authentication):
    def __init__(self, config: CCGConfig, **kwargs):
        """
        :param config: Configuration object of Client Credentials Grant auth.
        :type config: CCGConfig
        """
        super().__init__(**kwargs)
        self.config = config
        self.token_storage = (
            InMemoryTokenStorage()
            if self.config.token_storage == None
            else self.config.token_storage
        )
        self.subject_id = (
            self.config.user_id
            if not self.config.user_id == None
            else self.config.enterprise_id
        )
        self.subject_type = (
            PostOAuth2TokenBoxSubjectTypeField.USER.value
            if not self.config.user_id == None
            else PostOAuth2TokenBoxSubjectTypeField.ENTERPRISE.value
        )

    def refresh_token(
        self, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
        Get a new access token using CCG auth
        :param network_session: An object to keep network session state
        :type network_session: Optional[NetworkSession], optional
        """
        auth_manager: AuthorizationManager = (
            AuthorizationManager(network_session=network_session)
            if not network_session == None
            else AuthorizationManager()
        )
        token: Optional[AccessToken] = auth_manager.request_access_token(
            grant_type=PostOAuth2TokenGrantTypeField.CLIENT_CREDENTIALS.value,
            client_id=self.config.client_id,
            client_secret=self.config.client_secret,
            box_subject_type=self.subject_type,
            box_subject_id=self.subject_id,
        )
        self.token_storage.store(token)
        return token

    def retrieve_token(
        self, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
        Return a current token or get a new one when not available.
        :param network_session: An object to keep network session state
        :type network_session: Optional[NetworkSession], optional
        """
        old_token: Optional[AccessToken] = self.token_storage.get()
        if old_token == None:
            new_token: AccessToken = self.refresh_token(network_session)
            return new_token
        return old_token

    def as_user(self, user_id: str, token_storage: TokenStorage = None) -> 'BoxCCGAuth':
        """
        Create a new BoxCCGAuth instance that uses the provided user ID as the subject ID.

        May be one of this application's created App User. Depending on the configured User Access Level, may also be any other App User or Managed User in the enterprise.


        <https://developer.box.com/en/guides/applications/>


        <https://developer.box.com/en/guides/authentication/select/>

        :param user_id: The id of the user to authenticate
        :type user_id: str
        :param token_storage: Object responsible for storing token in newly created BoxCCGAuth. If no custom implementation provided, the token will be stored in memory.
        :type token_storage: TokenStorage, optional
        """
        if token_storage is None:
            token_storage = InMemoryTokenStorage()
        new_config: CCGConfig = CCGConfig(
            client_id=self.config.client_id,
            client_secret=self.config.client_secret,
            enterprise_id=self.config.enterprise_id,
            user_id=user_id,
            token_storage=token_storage,
        )
        return BoxCCGAuth(config=new_config)

    def as_enterprise(
        self, enterprise_id: str, token_storage: TokenStorage = None
    ) -> 'BoxCCGAuth':
        """
        Create a new BoxCCGAuth instance that uses the provided enterprise ID as the subject ID.
        :param enterprise_id: The id of the enterprise to authenticate
        :type enterprise_id: str
        :param token_storage: Object responsible for storing token in newly created BoxCCGAuth. If no custom implementation provided, the token will be stored in memory.
        :type token_storage: TokenStorage, optional
        """
        if token_storage is None:
            token_storage = InMemoryTokenStorage()
        new_config: CCGConfig = CCGConfig(
            client_id=self.config.client_id,
            client_secret=self.config.client_secret,
            enterprise_id=enterprise_id,
            user_id=None,
            token_storage=token_storage,
        )
        return BoxCCGAuth(config=new_config)

    def downscope_token(
        self,
        scopes: List[str],
        resource: Optional[str] = None,
        shared_link: Optional[str] = None,
        network_session: Optional[NetworkSession] = None,
    ) -> AccessToken:
        """
        Downscope access token to the provided scopes. Returning a new access token with the provided scopes, with the original access token unchanged.
        :param scopes: The scope(s) to apply to the resulting token.
        :type scopes: List[str]
        :param resource: The file or folder to get a downscoped token for. If None and shared_link None, the resulting token will not be scoped down to just a single item. The resource should be a full URL to an item, e.g. https://api.box.com/2.0/files/123456.
        :type resource: Optional[str], optional
        :param shared_link: The shared link to get a downscoped token for. If None and item None, the resulting token will not be scoped down to just a single item.
        :type shared_link: Optional[str], optional
        :param network_session: An object to keep network session state
        :type network_session: Optional[NetworkSession], optional
        """
        token: Optional[AccessToken] = self.token_storage.get()
        if token == None:
            raise BoxSDKError(
                message='No access token is available. Make an API call to retrieve a token before calling this method.'
            )
        auth_manager: AuthorizationManager = (
            AuthorizationManager(network_session=network_session)
            if not network_session == None
            else AuthorizationManager()
        )
        downscoped_token: AccessToken = auth_manager.request_access_token(
            grant_type=PostOAuth2TokenGrantTypeField.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE.value,
            subject_token=token.access_token,
            subject_token_type=PostOAuth2TokenSubjectTokenTypeField.URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_ACCESS_TOKEN.value,
            resource=resource,
            scope=' '.join(scopes),
            box_shared_link=shared_link,
        )
        return downscoped_token

    def revoke_token(self, network_session: Optional[NetworkSession] = None) -> None:
        """
        Revoke the current access token and remove it from token storage.
        :param network_session: An object to keep network session state
        :type network_session: Optional[NetworkSession], optional
        """
        old_token: Optional[AccessToken] = self.token_storage.get()
        if old_token == None:
            return None
        auth_manager: AuthorizationManager = (
            AuthorizationManager(network_session=network_session)
            if not network_session == None
            else AuthorizationManager()
        )
        auth_manager.revoke_access_token(
            self.config.client_id, self.config.client_secret, old_token.access_token
        )
        return self.token_storage.clear()
