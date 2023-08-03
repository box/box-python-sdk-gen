from box_sdk_gen.managers.uploads import UploadFileAttributesArg

from box_sdk_gen.managers.uploads import UploadFileAttributesArgParentField

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_buffer

from box_sdk_gen.utils import generate_byte_stream_from_buffer

from box_sdk_gen.utils import buffer_equals

from box_sdk_gen.utils import read_byte_stream

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def test_download_file():
    new_file_name: str = get_uuid()
    file_buffer: Buffer = generate_byte_buffer(1048576)
    file_content_stream: ByteStream = generate_byte_stream_from_buffer(file_buffer)
    uploaded_files: Files = client.uploads.upload_file(attributes=UploadFileAttributesArg(name=new_file_name, parent=UploadFileAttributesArgParentField(id='0')), file=file_content_stream)
    uploaded_file: Files = uploaded_files.entries[0]
    downloaded_file_content: ByteStream = client.downloads.download_file(file_id=uploaded_file.id)
    assert buffer_equals(read_byte_stream(downloaded_file_content), file_buffer)
    client.files.delete_file_by_id(file_id=uploaded_file.id)