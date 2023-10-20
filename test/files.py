import pytest

from box_sdk_gen.schemas import File

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributesArg

from box_sdk_gen.managers.uploads import UploadFileAttributesArgParentField

from box_sdk_gen.managers.files import GetFileThumbnailByIdExtensionArg

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.schemas import TrashFile

from box_sdk_gen.managers.files import CopyFileParentArg

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.utils import read_byte_stream

from box_sdk_gen.utils import buffer_equals

from box_sdk_gen.client import BoxClient

from box_sdk_gen.jwt_auth import BoxJWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

from test.commons import upload_new_file

from box_sdk_gen.utils import ByteStream

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
)

auth: BoxJWTAuth = BoxJWTAuth(config=jwt_config)

client: BoxClient = BoxClient(auth=auth)


def upload_file(file_name: str, file_stream: ByteStream) -> File:
    uploaded_files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributesArg(
            name=file_name, parent=UploadFileAttributesArgParentField(id='0')
        ),
        file=file_stream,
    )
    return uploaded_files.entries[0]


def testGetFileThumbnail():
    thumbnail_file_name: str = get_uuid()
    thumbnail_content_stream: ByteStream = generate_byte_stream(1048576)
    thumbnail_file: File = upload_file(thumbnail_file_name, thumbnail_content_stream)
    assert (
        not buffer_equals(
            read_byte_stream(
                client.files.get_file_thumbnail_by_id(
                    file_id=thumbnail_file.id,
                    extension=GetFileThumbnailByIdExtensionArg.PNG.value,
                )
            ),
            read_byte_stream(thumbnail_content_stream),
        )
        == True
    )
    client.files.delete_file_by_id(file_id=thumbnail_file.id)


def testGetFileFullExtraFields():
    new_file_name: str = get_uuid()
    file_content: ByteStream = generate_byte_stream(1048576)
    uploaded_file: File = upload_file(new_file_name, file_content)
    file: FileFull = client.files.get_file_by_id(
        file_id=uploaded_file.id, fields=['is_externally_owned', 'has_collaborations']
    )
    assert file.is_externally_owned == False
    assert file.has_collaborations == False
    client.files.delete_file_by_id(file_id=file.id)


def testCreateGetAndDeleteFile():
    new_file_name: str = get_uuid()
    updated_content_stream: ByteStream = generate_byte_stream(1048576)
    uploaded_file: File = upload_file(new_file_name, updated_content_stream)
    file: FileFull = client.files.get_file_by_id(file_id=uploaded_file.id)
    with pytest.raises(Exception):
        client.files.get_file_by_id(
            file_id=uploaded_file.id,
            fields=['name'],
            extra_headers={'if-none-match': file.etag},
        )
    assert file.name == new_file_name
    client.files.delete_file_by_id(file_id=uploaded_file.id)
    trashed_file: TrashFile = client.trashed_files.get_file_trash(
        file_id=uploaded_file.id
    )
    assert file.id == trashed_file.id


def testUpdateFile():
    file_to_update: File = upload_new_file()
    updated_name: str = get_uuid()
    updated_file: FileFull = client.files.update_file_by_id(
        file_id=file_to_update.id, name=updated_name, description='Updated description'
    )
    assert updated_file.name == updated_name
    assert updated_file.description == 'Updated description'
    client.files.delete_file_by_id(file_id=updated_file.id)


def testCopyFile():
    file_origin: File = upload_new_file()
    copied_file_name: str = get_uuid()
    copied_file: FileFull = client.files.copy_file(
        file_id=file_origin.id, name=copied_file_name, parent=CopyFileParentArg(id='0')
    )
    assert copied_file.parent.id == '0'
    assert copied_file.name == copied_file_name
    client.files.delete_file_by_id(file_id=file_origin.id)
    client.files.delete_file_by_id(file_id=copied_file.id)
