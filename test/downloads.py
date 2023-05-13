from box_sdk.utils import decode_base_64

from box_sdk.utils import get_env_var

from box_sdk.utils import get_uuid

from box_sdk.utils import generate_byte_stream

from box_sdk.utils import read_byte_stream

from box_sdk.managers.uploads import UploadFileRequestBodyArg

from box_sdk.managers.uploads import UploadFileRequestBodyArgAttributesField

from box_sdk.managers.uploads import UploadFileRequestBodyArgAttributesFieldParentField

from box_sdk.client import Client

from box_sdk.jwt_auth import JWTAuth

from box_sdk.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def test_download_file():
    new_file_name: str = get_uuid()
    file_content_stream = generate_byte_stream()
    uploaded_files: Files = client.uploads.upload_file(UploadFileRequestBodyArg(attributes=UploadFileRequestBodyArgAttributesField(name=new_file_name, parent=UploadFileRequestBodyArgAttributesFieldParentField(id='0')), file=file_content_stream))
    uploaded_file: Files = uploaded_files.entries[0]
    downloaded_file_content = client.downloads.download_file(uploaded_file.id)
    assert downloaded_file_content == read_byte_stream(file_content_stream)
    client.files.delete_file_by_id(uploaded_file.id)