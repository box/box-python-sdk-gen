from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

from box_sdk_gen.ccg_auth import CCGAuth

from box_sdk_gen.ccg_auth import CCGConfig

from box_sdk_gen.developer_token_auth import DeveloperTokenAuth

from box_sdk_gen.oauth import OAuth

from box_sdk_gen.oauth import OAuthConfig

from box_sdk_gen.schemas import UserFull


def test_ccg_auth():
    user_id: str = get_env_var("USER_ID")
    enterprise_id: str = get_env_var("ENTERPRISE_ID")
    ccg_config: CCGConfig = CCGConfig(
        client_id=get_env_var("CLIENT_ID"),
        client_secret=get_env_var("CLIENT_SECRET"),
        enterprise_id=enterprise_id,
        user_id=user_id,
    )
    auth: CCGAuth = CCGAuth(config=ccg_config)
    client: Client = Client(auth=auth)
    auth.as_user(user_id)
    current_user: UserFull = client.users.get_user_me()
    assert current_user.id == user_id
    auth.as_enterprise(enterprise_id)
    new_user: UserFull = client.users.get_user_me(fields="enterprise")
    assert not new_user.enterprise == None and new_user.enterprise.id == enterprise_id
    assert not new_user.id == user_id


def test_jwt_auth():
    user_id: str = get_env_var("USER_ID")
    enterprise_id: str = get_env_var("ENTERPRISE_ID")
    jwt_config: JWTConfig = JWTConfig.from_config_json_string(
        decode_base_64(get_env_var("JWT_CONFIG_BASE_64"))
    )
    auth: JWTAuth = JWTAuth(config=jwt_config)
    client: Client = Client(auth=auth)
    auth.as_user(user_id)
    current_user: UserFull = client.users.get_user_me()
    assert current_user.id == user_id
    auth.as_enterprise(enterprise_id)
    new_user: UserFull = client.users.get_user_me(fields="enterprise")
    assert not new_user.enterprise == None and new_user.enterprise.id == enterprise_id
    assert not new_user.id == user_id


def test_developer_token_auth():
    user_id: str = get_env_var("USER_ID")
    jwt_config: JWTConfig = JWTConfig.from_config_json_string(
        decode_base_64(get_env_var("JWT_CONFIG_BASE_64"))
    )
    auth: JWTAuth = JWTAuth(config=jwt_config)
    auth.as_user(user_id)
    token: str = auth.retrieve_token()
    dev_auth: DeveloperTokenAuth = DeveloperTokenAuth(token=token)
    client: Client = Client(auth=dev_auth)
    current_user: UserFull = client.users.get_user_me()
    assert current_user.id == user_id


def test_oauth_auth():
    config: OAuthConfig = OAuthConfig(
        client_id="OAUTH_CLIENT_ID", client_secret="OAUTH_CLIENT_SECRET"
    )
    auth: OAuth = OAuth(config=config)
    auth_url: str = auth.get_authorize_url()
    expected_auth_url: str = "https://account.box.com/api/oauth2/authorize?client_id=OAUTH_CLIENT_ID&response_type=code"
    assert auth_url == expected_auth_url
