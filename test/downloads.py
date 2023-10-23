from box_sdk_gen.client import BoxClient

from box_sdk_gen.utils import Buffer

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributesArg

from box_sdk_gen.managers.uploads import UploadFileAttributesArgParentField

from box_sdk_gen.schemas import File

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_buffer

from box_sdk_gen.utils import generate_byte_stream_from_buffer

from box_sdk_gen.utils import buffer_equals

from box_sdk_gen.utils import read_byte_stream

from test.commons import get_default_client

client: BoxClient = get_default_client()


def test_download_file():
    new_file_name: str = get_uuid()
    file_buffer: Buffer = generate_byte_buffer(1048576)
    file_content_stream: ByteStream = generate_byte_stream_from_buffer(file_buffer)
    uploaded_files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributesArg(
            name=new_file_name, parent=UploadFileAttributesArgParentField(id='0')
        ),
        file=file_content_stream,
    )
    uploaded_file: File = uploaded_files.entries[0]
    downloaded_file_content: ByteStream = client.downloads.download_file(
        file_id=uploaded_file.id
    )
    assert buffer_equals(read_byte_stream(downloaded_file_content), file_buffer)
    client.files.delete_file_by_id(file_id=uploaded_file.id)
