from box_sdk_gen.client import BoxClient

from box_sdk_gen.internal.utils import Buffer

from box_sdk_gen.internal.utils import ByteStream

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributes

from box_sdk_gen.managers.uploads import UploadFileAttributesParentField

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import generate_byte_buffer

from box_sdk_gen.internal.utils import generate_byte_stream_from_buffer

from box_sdk_gen.internal.utils import buffer_equals

from box_sdk_gen.internal.utils import read_byte_stream

from test.commons import get_default_client

from box_sdk_gen.networking.fetch import FetchOptions

from box_sdk_gen.networking.fetch import FetchResponse

client: BoxClient = get_default_client()


def test_download_file():
    new_file_name: str = get_uuid()
    file_buffer: Buffer = generate_byte_buffer(1024 * 1024)
    file_content_stream: ByteStream = generate_byte_stream_from_buffer(file_buffer)
    uploaded_files: Files = client.uploads.upload_file(
        UploadFileAttributes(
            name=new_file_name, parent=UploadFileAttributesParentField(id='0')
        ),
        file_content_stream,
    )
    uploaded_file: FileFull = uploaded_files.entries[0]
    downloaded_file_content: ByteStream = client.downloads.download_file(
        uploaded_file.id
    )
    assert buffer_equals(read_byte_stream(downloaded_file_content), file_buffer)
    client.files.delete_file_by_id(uploaded_file.id)
