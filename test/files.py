import pytest

from box_sdk.utils import decode_base_64

from box_sdk.utils import get_env_var

from box_sdk.utils import get_uuid

from box_sdk.utils import generate_byte_stream

from box_sdk.utils import read_byte_stream

from box_sdk.managers.uploads import UploadFileRequestBodyArg

from box_sdk.managers.uploads import UploadFileRequestBodyArgAttributesField

from box_sdk.managers.uploads import UploadFileRequestBodyArgAttributesFieldParentField

from box_sdk.managers.files import UpdateFileByIdRequestBodyArg

from box_sdk.managers.files import CopyFileRequestBodyArgParentField

from box_sdk.managers.files import CopyFileRequestBodyArg

from box_sdk.managers.files import GetFileThumbnailByIdExtensionArg

from box_sdk.client import Client

from box_sdk.jwt_auth import JWTAuth

from box_sdk.jwt_auth import JWTConfig

from test.commons import upload_new_file

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def upload_file(file_name, file_stream):
    uploaded_files = client.uploads.upload_file(UploadFileRequestBodyArg(attributes=UploadFileRequestBodyArgAttributesField(name=file_name, parent=UploadFileRequestBodyArgAttributesFieldParentField(id='0')), file=file_stream))
    return uploaded_files.entries[0]

def testGetFileThumbnail():
    thumbnail_file_name: str = get_uuid()
    thumbnail_content_stream = generate_byte_stream()
    thumbnail_file = upload_file(thumbnail_file_name, thumbnail_content_stream)
    assert not client.files.get_file_thumbnail_by_id(thumbnail_file.id, GetFileThumbnailByIdExtensionArg.PNG.value) == read_byte_stream(thumbnail_content_stream)
    client.files.delete_file_by_id(thumbnail_file.id)

def testCreateandDeleteFile():
    new_file_name: str = get_uuid()
    updated_content_stream = generate_byte_stream()
    uploaded_file = upload_file(new_file_name, updated_content_stream)
    file = client.files.get_file_by_id(uploaded_file.id)
    assert file.name == new_file_name
    client.files.delete_file_by_id(uploaded_file.id)
    with pytest.raises(Exception):
        client.files.get_file_by_id(uploaded_file.id)

def testUpdateFile():
    file_to_update = upload_new_file()
    updated_name: str = get_uuid()
    updated_file = client.files.update_file_by_id(file_to_update.id, UpdateFileByIdRequestBodyArg(name=updated_name, description='Updated description'))
    assert updated_file.name == updated_name
    assert updated_file.description == 'Updated description'
    client.files.delete_file_by_id(updated_file.id)

def testCopyFile():
    file_origin = upload_new_file()
    copied_file_name: str = get_uuid()
    copied_file = client.files.copy_file(file_origin.id, CopyFileRequestBodyArg(parent=CopyFileRequestBodyArgParentField(id='0'), name=copied_file_name))
    assert copied_file.parent.id == '0'
    assert copied_file.name == copied_file_name
    client.files.delete_file_by_id(file_origin.id)
    client.files.delete_file_by_id(copied_file.id)