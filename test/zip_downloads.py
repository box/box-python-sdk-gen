from box_sdk_gen.utils import to_string

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import File

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.managers.zip_downloads import DownloadZipItemsArg

from box_sdk_gen.managers.zip_downloads import DownloadZipItemsArgTypeField

from box_sdk_gen.schemas import ZipDownload

from box_sdk_gen.managers.zip_downloads import CreateZipDownloadItemsArg

from box_sdk_gen.schemas import ZipDownloadStatus

from test.commons import get_default_client

from test.commons import upload_new_file

from test.commons import create_new_folder

from box_sdk_gen.utils import buffer_equals

from box_sdk_gen.utils import read_byte_stream

from box_sdk_gen.utils import generate_byte_buffer

client: BoxClient = get_default_client()


def testZipDownload():
    file_1: File = upload_new_file()
    file_2: File = upload_new_file()
    folder_1: FolderFull = create_new_folder()
    zip_stream: ByteStream = client.zip_downloads.download_zip(
        items=[
            DownloadZipItemsArg(
                id=file_1.id, type=DownloadZipItemsArgTypeField.FILE.value
            ),
            DownloadZipItemsArg(
                id=file_2.id, type=DownloadZipItemsArgTypeField.FILE.value
            ),
            DownloadZipItemsArg(
                id=folder_1.id, type=DownloadZipItemsArgTypeField.FOLDER.value
            ),
        ],
        download_file_name='zip',
    )
    assert (
        buffer_equals(read_byte_stream(zip_stream), generate_byte_buffer(10)) == False
    )
    client.files.delete_file_by_id(file_id=file_1.id)
    client.files.delete_file_by_id(file_id=file_2.id)
    client.folders.delete_folder_by_id(folder_id=folder_1.id)


def testManualZipDownloadAndCheckStatus():
    file_1: File = upload_new_file()
    file_2: File = upload_new_file()
    folder_1: FolderFull = create_new_folder()
    zip_download: ZipDownload = client.zip_downloads.create_zip_download(
        items=[
            CreateZipDownloadItemsArg(
                id=file_1.id, type=DownloadZipItemsArgTypeField.FILE.value
            ),
            CreateZipDownloadItemsArg(
                id=file_2.id, type=DownloadZipItemsArgTypeField.FILE.value
            ),
            CreateZipDownloadItemsArg(
                id=folder_1.id, type=DownloadZipItemsArgTypeField.FOLDER.value
            ),
        ],
        download_file_name='zip',
    )
    assert not zip_download.download_url == ''
    assert not zip_download.status_url == ''
    assert not zip_download.expires_at == ''
    zip_stream: ByteStream = client.zip_downloads.get_zip_download_content(
        download_url=zip_download.download_url
    )
    assert (
        buffer_equals(read_byte_stream(zip_stream), generate_byte_buffer(10)) == False
    )
    zip_download_status: ZipDownloadStatus = (
        client.zip_downloads.get_zip_download_status(status_url=zip_download.status_url)
    )
    assert zip_download_status.total_file_count == 2
    assert zip_download_status.downloaded_file_count == 2
    assert zip_download_status.skipped_file_count == 0
    assert zip_download_status.skipped_folder_count == 0
    assert not to_string(zip_download_status.state) == 'failed'
    client.files.delete_file_by_id(file_id=file_1.id)
    client.files.delete_file_by_id(file_id=file_2.id)
    client.folders.delete_folder_by_id(folder_id=folder_1.id)
