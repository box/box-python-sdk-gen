from box_sdk.base_object import BaseObject

from typing import Optional

from typing import List

import json

from box_sdk.schemas import UploadSession

from box_sdk.schemas import ClientError

from box_sdk.schemas import UploadedPart

from box_sdk.schemas import UploadParts

from box_sdk.schemas import Files

from box_sdk.schemas import UploadPart

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateFileUploadSessionRequestBodyArg(BaseObject):
    def __init__(self, folder_id: str, file_size: int, file_name: str, **kwargs):
        """
        :param folder_id: The ID of the folder to upload the new file to.
        :type folder_id: str
        :param file_size: The total number of bytes of the file to be uploaded
        :type file_size: int
        :param file_name: The name of new file
        :type file_name: str
        """
        super().__init__(**kwargs)
        self.folder_id = folder_id
        self.file_size = file_size
        self.file_name = file_name

class CreateFileUploadSessionForExistingFileRequestBodyArg(BaseObject):
    def __init__(self, file_size: int, file_name: Optional[str] = None, **kwargs):
        """
        :param file_size: The total number of bytes of the file to be uploaded
        :type file_size: int
        :param file_name: The optional new name of new file
        :type file_name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.file_size = file_size
        self.file_name = file_name

class GetFileUploadSessionPartsOptionsArg(BaseObject):
    def __init__(self, offset: Optional[int] = None, limit: Optional[int] = None, **kwargs):
        """
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.offset = offset
        self.limit = limit

class CreateFileUploadSessionCommitRequestBodyArg(BaseObject):
    def __init__(self, parts: List[UploadPart], **kwargs):
        """
        :param parts: The list details for the uploaded parts
        :type parts: List[UploadPart]
        """
        super().__init__(**kwargs)
        self.parts = parts

class CreateFileUploadSessionCommitOptionsArg(BaseObject):
    def __init__(self, if_match: Optional[str] = None, if_none_match: Optional[str] = None, **kwargs):
        """
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Optional[str], optional
        :param if_none_match: Ensures an item is only returned if it has changed.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `304 Not Modified` if the item has not
            changed since.
        :type if_none_match: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.if_match = if_match
        self.if_none_match = if_none_match

class ChunkedUploadsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def create_file_upload_session(self, request_body: CreateFileUploadSessionRequestBodyArg) -> UploadSession:
        """
        Creates an upload session for a new file.
        """
        response: FetchResponse = fetch(''.join(['https://upload.box.com/api/2.0/files/upload_sessions']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return UploadSession.from_dict(json.loads(response.text))
    def create_file_upload_session_for_existing_file(self, file_id: str, request_body: CreateFileUploadSessionForExistingFileRequestBodyArg) -> UploadSession:
        """
        Creates an upload session for an existing file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        response: FetchResponse = fetch(''.join(['https://upload.box.com/api/2.0/files/', file_id, '/upload_sessions']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return UploadSession.from_dict(json.loads(response.text))
    def get_file_upload_session_by_id(self, upload_session_id: str) -> UploadSession:
        """
        Return information about an upload session.
        :param upload_session_id: The ID of the upload session.
            Example: "D5E3F7A"
        :type upload_session_id: str
        """
        response: FetchResponse = fetch(''.join(['https://upload.box.com/api/2.0/files/upload_sessions/', upload_session_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return UploadSession.from_dict(json.loads(response.text))
    def delete_file_upload_session_by_id(self, upload_session_id: str):
        """
        Abort an upload session and discard all data uploaded.
        
        This cannot be reversed.

        :param upload_session_id: The ID of the upload session.
            Example: "D5E3F7A"
        :type upload_session_id: str
        """
        response: FetchResponse = fetch(''.join(['https://upload.box.com/api/2.0/files/upload_sessions/', upload_session_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content
    def get_file_upload_session_parts(self, upload_session_id: str, options: GetFileUploadSessionPartsOptionsArg = None) -> UploadParts:
        """
        Return a list of the chunks uploaded to the upload
        
        session so far.

        :param upload_session_id: The ID of the upload session.
            Example: "D5E3F7A"
        :type upload_session_id: str
        """
        if options is None:
            options = GetFileUploadSessionPartsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://upload.box.com/api/2.0/files/upload_sessions/', upload_session_id, '/parts']), FetchOptions(method='GET', params={'offset': options.offset, 'limit': options.limit}, auth=self.auth, network_session=self.network_session))
        return UploadParts.from_dict(json.loads(response.text))
    def create_file_upload_session_commit(self, upload_session_id: str, digest: str, request_body: CreateFileUploadSessionCommitRequestBodyArg, options: CreateFileUploadSessionCommitOptionsArg = None) -> Files:
        """
        Close an upload session and create a file from the
        
        uploaded chunks.

        :param upload_session_id: The ID of the upload session.
            Example: "D5E3F7A"
        :type upload_session_id: str
        :param digest: The [RFC3230][1] message digest of the whole file.
            Only SHA1 is supported. The SHA1 digest must be Base64
            encoded. The format of this header is as
            `sha=BASE64_ENCODED_DIGEST`.
            [1]: https://tools.ietf.org/html/rfc3230
            Example: "sha=fpRyg5eVQletdZqEKaFlqwBXJzM="
        :type digest: str
        """
        if options is None:
            options = CreateFileUploadSessionCommitOptionsArg()
        response: FetchResponse = fetch(''.join(['https://upload.box.com/api/2.0/files/upload_sessions/', upload_session_id, '/commit']), FetchOptions(method='POST', headers={'digest': digest, 'if-match': options.if_match, 'if-none-match': options.if_none_match}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return Files.from_dict(json.loads(response.text))