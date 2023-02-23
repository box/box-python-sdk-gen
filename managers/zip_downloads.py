from typing import Union

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

import json

from fetch import fetch, FetchOptions, FetchResponse

from base_object import BaseObject

from schemas import ZipDownload

from schemas import ClientError

from schemas import ZipDownloadRequest

from schemas import ZipDownloadStatus

class ZipDownloadsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def postZipDownloads(self, requestBody: ZipDownloadRequest) -> ZipDownload:
        """
        Creates a request to download multiple files and folders as a single `zip`
        
        archive file. This API does not return the archive but instead performs all

        
        the checks to ensure that the user has access to all the items, and then

        
        returns a `download_url` and a `status_url` that can be used to download the

        
        archive.

        
        The limit for an archive is either the Account's upload limit or

        
        10,000 files, whichever is met first

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/zip_downloads']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return ZipDownload.from_dict(json.loads(response.text))
    def getZipDownloadsIdContent(self, zipDownloadId: str):
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

        :param zipDownloadId: The unique identifier that represent this `zip` archive.
            Example: "Lu6fA9Ob-jyysp3AAvMF4AkLEwZwAYbL=tgj2zIC=eK9RvJnJbjJl9rNh2qBgHDpyOCAOhpM=vajg2mKq8Mdd"
        :type zipDownloadId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/zip_downloads/', zipDownloadId, '/content']), FetchOptions(method='GET', auth=self.auth))
        return response.content
    def getZipDownloadsIdStatus(self, zipDownloadId: str) -> ZipDownloadStatus:
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

        :param zipDownloadId: The unique identifier that represent this `zip` archive.
            Example: "Lu6fA9Ob-jyysp3AAvMF4AkLEwZwAYbL=tgj2zIC=eK9RvJnJbjJl9rNh2qBgHDpyOCAOhpM=vajg2mKq8Mdd"
        :type zipDownloadId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/zip_downloads/', zipDownloadId, '/status']), FetchOptions(method='GET', auth=self.auth))
        return ZipDownloadStatus.from_dict(json.loads(response.text))