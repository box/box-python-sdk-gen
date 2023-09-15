from box_sdk_gen.schemas import RecentItems

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import BoxClient

from box_sdk_gen.jwt_auth import BoxJWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
)

auth: BoxJWTAuth = BoxJWTAuth(config=jwt_config)


def testRecentItems():
    auth.as_user(get_env_var('USER_ID'))
    client: BoxClient = BoxClient(auth=auth)
    recent_items: RecentItems = client.recent_items.get_recent_items()
    assert len(recent_items.entries) >= 0
