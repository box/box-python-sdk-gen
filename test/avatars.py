import pytest

from box_sdk_gen.utils import decode_base_64_byte_stream

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def testAvatars():
    user: UserFull = client.users.get_user_me()
    created_avatar: UserAvatar = client.avatars.create_user_avatar(user.id, decode_base_64_byte_stream('iVBORw0KGgoAAAANSUhEUgAAAQAAAAEAAQMAAABmvDolAAAAA1BMVEW10NBjBBbqAAAAH0lEQVRoge3BAQ0AAADCoPdPbQ43oAAAAAAAAAAAvg0hAAABmmDh1QAAAABJRU5ErkJggg=='), 'avatar.png', 'image/png')
    assert not created_avatar.pic_urls.small == None
    assert not created_avatar.pic_urls.large == None
    assert not created_avatar.pic_urls.preview == None
    assert client.avatars.get_user_avatar(user.id)
    client.avatars.delete_user_avatar(user.id)
    with pytest.raises(Exception):
        client.avatars.get_user_avatar(user.id)