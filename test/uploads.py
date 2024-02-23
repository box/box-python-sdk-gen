from box_sdk_gen.internal.utils import ByteStream

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributes

from box_sdk_gen.managers.uploads import UploadFileAttributesParentField

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.managers.uploads import UploadFileVersionAttributes

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import generate_byte_stream

from box_sdk_gen.client import BoxClient

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testUploadFileAndFileVersion():
    new_file_name: str = get_uuid()
    file_content_stream: ByteStream = generate_byte_stream(1024 * 1024)
    uploaded_files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributes(
            name=new_file_name, parent=UploadFileAttributesParentField(id='0')
        ),
        file=file_content_stream,
    )
    uploaded_file: FileFull = uploaded_files.entries[0]
    assert uploaded_file.name == new_file_name
    new_file_version_name: str = get_uuid()
    new_file_content_stream: ByteStream = generate_byte_stream(1024 * 1024)
    uploaded_files_version: Files = client.uploads.upload_file_version(
        file_id=uploaded_file.id,
        attributes=UploadFileVersionAttributes(name=new_file_version_name),
        file=new_file_content_stream,
    )
    new_file_version: FileFull = uploaded_files_version.entries[0]
    assert new_file_version.name == new_file_version_name
    client.files.delete_file_by_id(file_id=new_file_version.id)
