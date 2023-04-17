from box_sdk.utils import decode_base_64

from box_sdk.utils import get_env_var

from box_sdk.utils import get_uuid

from box_sdk.utils import generate_byte_stream

from box_sdk.utils import read_byte_stream

from box_sdk.managers.uploads import UploadFileRequestBodyArg

from box_sdk.managers.uploads import UploadFileRequestBodyArgAttributesField

from box_sdk.managers.uploads import UploadFileRequestBodyArgAttributesFieldParentField

from box_sdk.managers.uploads import UploadFileVersionRequestBodyArg

from box_sdk.managers.uploads import UploadFileVersionRequestBodyArgAttributesField

from box_sdk.client import Client

from box_sdk.jwt_auth import JWTAuth

from box_sdk.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def test_upload_file_and_file_version():
    new_file_name = get_uuid()
    file_content_stream = generate_byte_stream()
    uploaded_files = client.uploads.upload_file(UploadFileRequestBodyArg(attributes=UploadFileRequestBodyArgAttributesField(name=new_file_name, parent=UploadFileRequestBodyArgAttributesFieldParentField(id='0')), file=file_content_stream))
    uploaded_file = uploaded_files.entries[0]
    assert uploaded_file.name == new_file_name
    new_file_version_name = get_uuid()
    uploaded_files_version = client.uploads.upload_file_version(uploaded_file.id, UploadFileVersionRequestBodyArg(attributes=UploadFileVersionRequestBodyArgAttributesField(name=new_file_version_name), file=file_content_stream))
    new_file_version = uploaded_files_version.entries[0]
    assert new_file_version.name == new_file_version_name
    client.files.delete_file_by_id(new_file_version.id)