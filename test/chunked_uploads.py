from box_sdk_gen.client import BoxClient

from box_sdk_gen.internal.utils import ByteStream

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import generate_byte_stream

from test.commons import get_default_client

from box_sdk_gen.schemas import File

client: BoxClient = get_default_client()


def testChunkedUpload():
    file_size: int = (20 * 1024) * 1024
    file_byte_stream: ByteStream = generate_byte_stream(file_size)
    file_name: str = get_uuid()
    parent_folder_id: str = '0'
    uploaded_file: File = client.chunked_uploads.upload_big_file(
        file_byte_stream, file_name, file_size, parent_folder_id
    )
    assert uploaded_file.name == file_name
    assert uploaded_file.size == file_size
    assert uploaded_file.parent.id == parent_folder_id
    client.files.delete_file_by_id(file_id=uploaded_file.id)
