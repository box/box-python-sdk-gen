from typing import Optional

import json

from box_sdk.schemas import ZipDownload

from box_sdk.schemas import ClientError

from box_sdk.schemas import ZipDownloadRequest

from box_sdk.schemas import ZipDownloadStatus

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class ZipDownloadsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def create_zip_download(self, request_body: ZipDownloadRequest) -> ZipDownload:
        """
        Creates a request to download multiple files and folders as a single `zip`
        
        archive file. This API does not return the archive but instead performs all

        
        the checks to ensure that the user has access to all the items, and then

        
        returns a `download_url` and a `status_url` that can be used to download the

        
        archive.

        
        The limit for an archive is either the Account's upload limit or

        
        10,000 files, whichever is met first

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/zip_downloads']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return ZipDownload.from_dict(json.loads(response.text))
    def get_zip_download_content(self, zip_download_id: str):
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
        """
        response: FetchResponse = fetch(''.join(['https://dl.boxcloud.com/2.0/zip_downloads/', zip_download_id, '/content']), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return response.content
    def get_zip_download_status(self, zip_download_id: str) -> ZipDownloadStatus:
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
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/zip_downloads/', zip_download_id, '/status']), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return ZipDownloadStatus.from_dict(json.loads(response.text))