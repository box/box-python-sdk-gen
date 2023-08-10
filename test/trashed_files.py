import pytest

from box_sdk_gen.managers.uploads import UploadFileAttributesArg

from box_sdk_gen.managers.uploads import UploadFileAttributesArgParentField

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def testTrashedFiles():
    file_size = 1024 * 1024
    file_name: str = get_uuid()
    file_byte_stream: ByteStream = generate_byte_stream(file_size)
    files: Files = client.uploads.upload_file(attributes=UploadFileAttributesArg(name=file_name, parent=UploadFileAttributesArgParentField(id='0')), file=file_byte_stream)
    file: Files = files.entries[0]
    client.files.delete_file_by_id(file_id=file.id)
    from_trash: TrashFile = client.trashed_files.get_file_trash(file_id=file.id)
    assert from_trash.id == file.id
    assert from_trash.name == file.name
    from_api_after_trashed: FileFull = client.files.get_file_by_id(file_id=file.id)
    assert from_api_after_trashed.item_status == 'trashed'
    restored_file: TrashFileRestored = client.trashed_files.restore_file_from_trash(file_id=file.id)
    from_api_after_restore: FileFull = client.files.get_file_by_id(file_id=file.id)
    assert restored_file.id == from_api_after_restore.id
    assert restored_file.name == from_api_after_restore.name
    assert from_api_after_restore.item_status == 'active'
    client.files.delete_file_by_id(file_id=file.id)
    client.trashed_files.delete_file_trash(file_id=file.id)
    with pytest.raises(Exception):
        client.trashed_files.get_file_trash(file_id=file.id)