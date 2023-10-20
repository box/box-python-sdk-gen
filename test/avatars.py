import pytest

from box_sdk_gen.schemas import UserFull

from box_sdk_gen.schemas import UserAvatar

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import buffer_equals

from box_sdk_gen.utils import read_byte_stream

from box_sdk_gen.utils import generate_byte_buffer

from box_sdk_gen.utils import decode_base_64_byte_stream

from box_sdk_gen.client import BoxClient

from box_sdk_gen.jwt_auth import BoxJWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
)

auth: BoxJWTAuth = BoxJWTAuth(config=jwt_config)

client: BoxClient = BoxClient(auth=auth)


def testAvatars():
    user: UserFull = client.users.get_user_me()
    created_avatar: UserAvatar = client.avatars.create_user_avatar(
        user_id=user.id,
        pic=decode_base_64_byte_stream(
            'iVBORw0KGgoAAAANSUhEUgAAAQAAAAEAAQMAAABmvDolAAAAA1BMVEW10NBjBBbqAAAAH0lEQVRoge3BAQ0AAADCoPdPbQ43oAAAAAAAAAAAvg0hAAABmmDh1QAAAABJRU5ErkJggg=='
        ),
        pic_file_name='avatar.png',
        pic_content_type='image/png',
    )
    assert not created_avatar.pic_urls.small == None
    assert not created_avatar.pic_urls.large == None
    assert not created_avatar.pic_urls.preview == None
    response: ByteStream = client.avatars.get_user_avatar(user_id=user.id)
    assert buffer_equals(read_byte_stream(response), generate_byte_buffer(0)) == False
    client.avatars.delete_user_avatar(user_id=user.id)
    with pytest.raises(Exception):
        client.avatars.get_user_avatar(user_id=user.id)
