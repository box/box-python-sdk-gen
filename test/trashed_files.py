from box_sdk_gen.utils import to_string

import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributesArg

from box_sdk_gen.managers.uploads import UploadFileAttributesArgParentField

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.schemas import TrashFile

from box_sdk_gen.schemas import TrashFileRestored

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_stream

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testTrashedFiles():
    file_size: int = 1024 * 1024
    file_name: str = get_uuid()
    file_byte_stream: ByteStream = generate_byte_stream(file_size)
    files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributesArg(
            name=file_name, parent=UploadFileAttributesArgParentField(id='0')
        ),
        file=file_byte_stream,
    )
    file: FileFull = files.entries[0]
    client.files.delete_file_by_id(file_id=file.id)
    from_trash: TrashFile = client.trashed_files.get_file_trash(file_id=file.id)
    assert from_trash.id == file.id
    assert from_trash.name == file.name
    from_api_after_trashed: FileFull = client.files.get_file_by_id(file_id=file.id)
    assert to_string(from_api_after_trashed.item_status) == 'trashed'
    restored_file: TrashFileRestored = client.trashed_files.restore_file_from_trash(
        file_id=file.id
    )
    from_api_after_restore: FileFull = client.files.get_file_by_id(file_id=file.id)
    assert restored_file.id == from_api_after_restore.id
    assert restored_file.name == from_api_after_restore.name
    assert to_string(from_api_after_restore.item_status) == 'active'
    client.files.delete_file_by_id(file_id=file.id)
    client.trashed_files.delete_file_trash(file_id=file.id)
    with pytest.raises(Exception):
        client.trashed_files.get_file_trash(file_id=file.id)
