from enum import Enum

from box_sdk_gen.base_object import BaseObject

from typing import Optional

from typing import List

from typing import Dict

from box_sdk_gen.serialization import serialize

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.utils import to_string

from box_sdk_gen.schemas import ZipDownload

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import ZipDownloadRequest

from box_sdk_gen.schemas import ZipDownloadStatus

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class CreateZipDownloadItemsArgTypeField(str, Enum):
    FILE = 'file'
    FOLDER_ = 'folder.'


class CreateZipDownloadItemsArg(BaseObject):
    def __init__(self, type: CreateZipDownloadItemsArgTypeField, id: str, **kwargs):
        """
        :param type: The type of the item to add to the archive.
        :type type: CreateZipDownloadItemsArgTypeField
        :param id: The identifier of the item to add to the archive. When this item is
            a folder then this can not be the root folder with ID `0`.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class ZipDownloadsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def create_zip_download(
        self,
        items: List[CreateZipDownloadItemsArg],
        download_file_name: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ZipDownload:
        """
        Creates a request to download multiple files and folders as a single `zip`

        archive file. This API does not return the archive but instead performs all


        the checks to ensure that the user has access to all the items, and then


        returns a `download_url` and a `status_url` that can be used to download the


        archive.


        The limit for an archive is either the Account's upload limit or


        10,000 files, whichever is met first.


        **Note**: Downloading a large file can be


        affected by various


        factors such as distance, network latency,


        bandwidth, and congestion, as well as packet loss


        ratio and current server load.


        For these reasons we recommend that a maximum ZIP archive


        total size does not exceed 25GB.

        :param items: A list of items to add to the `zip` archive. These can
            be folders or files.
        :type items: List[CreateZipDownloadItemsArg]
        :param download_file_name: The optional name of the `zip` archive. This name will be appended by the
            `.zip` file extension, for example `January Financials.zip`.
        :type download_file_name: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = {'items': items, 'download_file_name': download_file_name}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/zip_downloads']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, ZipDownload)

    def get_zip_download_content(
        self,
        zip_download_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ByteStream:
        """
        Returns the contents of a `zip` archive in binary format. This URL does not

        require any form of authentication and could be used in a user's browser to


        download the archive to a user's device.


        By default, this URL is only valid for a few seconds from the creation of


        the request for this archive. Once a download has started it can not be


        stopped and resumed, instead a new request for a zip archive would need to


        be created.


        The URL of this endpoint should not be considered as fixed. Instead, use


        the [Create zip download](e://post_zip_downloads) API to request to create a


        `zip` archive, and then follow the `download_url` field in the response to


        this endpoint.

        :param zip_download_id: The unique identifier that represent this `zip` archive.
            Example: "Lu6fA9Ob-jyysp3AAvMF4AkLEwZwAYbL=tgj2zIC=eK9RvJnJbjJl9rNh2qBgHDpyOCAOhpM=vajg2mKq8Mdd"
        :type zip_download_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://dl.boxcloud.com/2.0/zip_downloads/',
                    to_string(zip_download_id),
                    '/content',
                ]
            ),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='binary',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return response.content

    def get_zip_download_status(
        self,
        zip_download_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ZipDownloadStatus:
        """
        Returns the download status of a `zip` archive, allowing an application to

        inspect the progress of the download as well as the number of items that


        might have been skipped.


        This endpoint can only be accessed once the download has started.


        Subsequently this endpoint is valid for 12 hours from the start of the


        download.


        The URL of this endpoint should not be considered as fixed. Instead, use


        the [Create zip download](e://post_zip_downloads) API to request to create a


        `zip` archive, and then follow the `status_url` field in the response to


        this endpoint.

        :param zip_download_id: The unique identifier that represent this `zip` archive.
            Example: "Lu6fA9Ob-jyysp3AAvMF4AkLEwZwAYbL=tgj2zIC=eK9RvJnJbjJl9rNh2qBgHDpyOCAOhpM=vajg2mKq8Mdd"
        :type zip_download_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://api.box.com/2.0/zip_downloads/',
                    to_string(zip_download_id),
                    '/status',
                ]
            ),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, ZipDownloadStatus)
