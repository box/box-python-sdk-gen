from box_sdk_gen.schemas import AccessToken

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import buffer_equals

from box_sdk_gen.utils import read_byte_stream

from box_sdk_gen.utils import generate_byte_buffer

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.utils import decode_base_64_byte_stream

from box_sdk_gen.client import BoxClient

from box_sdk_gen.ccg_auth import BoxCCGAuth

from box_sdk_gen.ccg_auth import CCGConfig

from box_sdk_gen.developer_token_auth import BoxDeveloperTokenAuth

from box_sdk_gen.oauth import BoxOAuth

from box_sdk_gen.oauth import OAuthConfig

from box_sdk_gen.schemas import UserFull

from box_sdk_gen.jwt_auth import BoxJWTAuth

from box_sdk_gen.jwt_auth import JWTConfig


def test_jwt_auth():
    user_id: str = get_env_var('USER_ID')
    enterprise_id: str = get_env_var('ENTERPRISE_ID')
    jwt_config: JWTConfig = JWTConfig.from_config_json_string(
        decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
    )
    auth: BoxJWTAuth = BoxJWTAuth(config=jwt_config)
    client: BoxClient = BoxClient(auth=auth)
    auth.as_user(user_id)
    current_user: UserFull = client.users.get_user_me()
    assert current_user.id == user_id
    auth.as_enterprise(enterprise_id)
    new_user: UserFull = client.users.get_user_me(fields=['enterprise'])
    assert not new_user.enterprise == None
    assert new_user.enterprise.id == enterprise_id
    assert not new_user.id == user_id


def test_oauth_auth_authorizeUrl():
    config: OAuthConfig = OAuthConfig(
        client_id='OAUTH_CLIENT_ID', client_secret='OAUTH_CLIENT_SECRET'
    )
    auth: BoxOAuth = BoxOAuth(config=config)
    auth_url: str = auth.get_authorize_url()
    assert (
        auth_url
        == 'https://account.box.com/api/oauth2/authorize?client_id=OAUTH_CLIENT_ID&response_type=code'
        or auth_url
        == 'https://account.box.com/api/oauth2/authorize?response_type=code&client_id=OAUTH_CLIENT_ID'
    )


def test_ccg_auth():
    user_id: str = get_env_var('USER_ID')
    enterprise_id: str = get_env_var('ENTERPRISE_ID')
    ccg_config: CCGConfig = CCGConfig(
        client_id=get_env_var('CLIENT_ID'),
        client_secret=get_env_var('CLIENT_SECRET'),
        enterprise_id=enterprise_id,
        user_id=user_id,
    )
    auth: BoxCCGAuth = BoxCCGAuth(config=ccg_config)
    client: BoxClient = BoxClient(auth=auth)
    auth.as_user(user_id)
    current_user: UserFull = client.users.get_user_me()
    assert current_user.id == user_id
    auth.as_enterprise(enterprise_id)
    new_user: UserFull = client.users.get_user_me(fields=['enterprise'])
    assert not new_user.enterprise == None
    assert new_user.enterprise.id == enterprise_id
    assert not new_user.id == user_id


def get_access_token() -> AccessToken:
    user_id: str = get_env_var('USER_ID')
    enterprise_id: str = get_env_var('ENTERPRISE_ID')
    ccg_config: CCGConfig = CCGConfig(
        client_id=get_env_var('CLIENT_ID'),
        client_secret=get_env_var('CLIENT_SECRET'),
        enterprise_id=enterprise_id,
        user_id=user_id,
    )
    auth: BoxCCGAuth = BoxCCGAuth(config=ccg_config)
    auth.as_user(user_id)
    token: AccessToken = auth.retrieve_token()
    return token


def test_developer_token_auth():
    user_id: str = get_env_var('USER_ID')
    token: AccessToken = get_access_token()
    dev_auth: BoxDeveloperTokenAuth = BoxDeveloperTokenAuth(token=token.access_token)
    client: BoxClient = BoxClient(auth=dev_auth)
    current_user: UserFull = client.users.get_user_me()
    assert current_user.id == user_id
