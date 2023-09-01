from box_sdk_gen.schemas import Users

from box_sdk_gen.schemas import UserFull

from box_sdk_gen.schemas import User

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
)

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)


def test_get_users():
    users: Users = client.users.get_users()
    assert users.total_count >= 0


def test_get_user_me():
    current_user: UserFull = client.users.get_user_me()
    assert current_user.type == 'user'


def test_create_update_get_delete_user():
    user_name: str = get_uuid()
    user_login: str = ''.join([get_uuid(), '@gmail.com'])
    user: User = client.users.create_user(
        name=user_name, login=user_login, is_platform_access_only=True
    )
    assert user.name == user_name
    user_by_id: UserFull = client.users.get_user_by_id(user_id=user.id)
    assert user_by_id.id == user.id
    updated_user_name: str = get_uuid()
    updated_user: UserFull = client.users.update_user_by_id(
        user_id=user.id, name=updated_user_name
    )
    assert updated_user.name == updated_user_name
    client.users.delete_user_by_id(user_id=user.id)
