from box_sdk_gen.utils import ByteStream

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.schemas import File

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
)

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)


def testChunkedUpload():
    file_size: int = (20 * 1024) * 1024
    file_byte_stream: ByteStream = generate_byte_stream(file_size)
    file_name: str = get_uuid()
    parent_folder_id: str = '0'
    uploaded_file: File = client.chunked_uploads.upload_big_file(
        file_byte_stream, file_name, file_size, parent_folder_id
    )
    assert uploaded_file.name == file_name
    assert uploaded_file.size == file_size
    assert uploaded_file.parent.id == parent_folder_id
    client.files.delete_file_by_id(file_id=uploaded_file.id)
