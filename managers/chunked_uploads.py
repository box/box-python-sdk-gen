from base_object import BaseObject

from typing import Union

from typing import List

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

import json

from fetch import fetch, FetchOptions, FetchResponse

from schemas import UploadSession

from schemas import ClientError

from schemas import UploadedPart

from schemas import UploadParts

from schemas import Files

from schemas import UploadPart

class PostFilesUploadSessionsRequestBodyArg(BaseObject):
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

class PostFilesIdUploadSessionsRequestBodyArg(BaseObject):
    def __init__(self, file_size: int, file_name: Union[None, str] = None, **kwargs):
        """
        :param file_size: The total number of bytes of the file to be uploaded
        :type file_size: int
        :param file_name: The optional new name of new file
        :type file_name: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.file_size = file_size
        self.file_name = file_name

class GetFilesUploadSessionsIdPartsOptionsArg(BaseObject):
    def __init__(self, offset: Union[None, int] = None, limit: Union[None, int] = None, **kwargs):
        """
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Union[None, int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.offset = offset
        self.limit = limit

class PostFilesUploadSessionsIdCommitRequestBodyArg(BaseObject):
    def __init__(self, parts: List[UploadPart], **kwargs):
        """
        :param parts: The list details for the uploaded parts
        :type parts: List[UploadPart]
        """
        super().__init__(**kwargs)
        self.parts = parts

class PostFilesUploadSessionsIdCommitOptionsArg(BaseObject):
    def __init__(self, ifMatch: Union[None, str] = None, ifNoneMatch: Union[None, str] = None, **kwargs):
        """
        :param ifMatch: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type ifMatch: Union[None, str], optional
        :param ifNoneMatch: Ensures an item is only returned if it has changed.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `304 Not Modified` if the item has not
            changed since.
        :type ifNoneMatch: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.ifMatch = ifMatch
        self.ifNoneMatch = ifNoneMatch

class ChunkedUploadsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def postFilesUploadSessions(self, requestBody: PostFilesUploadSessionsRequestBodyArg) -> UploadSession:
        """
        Creates an upload session for a new file.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/upload_sessions']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return UploadSession.from_dict(json.loads(response.text))
    def postFilesIdUploadSessions(self, fileId: str, requestBody: PostFilesIdUploadSessionsRequestBodyArg) -> UploadSession:
        """
        Creates an upload session for an existing file.
        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/upload_sessions']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return UploadSession.from_dict(json.loads(response.text))
    def getFilesUploadSessionsId(self, uploadSessionId: str) -> UploadSession:
        """
        Return information about an upload session.
        :param uploadSessionId: The ID of the upload session.
            Example: "D5E3F7A"
        :type uploadSessionId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/upload_sessions/', uploadSessionId]), FetchOptions(method='GET', auth=self.auth))
        return UploadSession.from_dict(json.loads(response.text))
    def deleteFilesUploadSessionsId(self, uploadSessionId: str):
        """
        Abort an upload session and discard all data uploaded.
        
        This cannot be reversed.

        :param uploadSessionId: The ID of the upload session.
            Example: "D5E3F7A"
        :type uploadSessionId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/upload_sessions/', uploadSessionId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def getFilesUploadSessionsIdParts(self, uploadSessionId: str, options: GetFilesUploadSessionsIdPartsOptionsArg = None) -> UploadParts:
        """
        Return a list of the chunks uploaded to the upload
        
        session so far.

        :param uploadSessionId: The ID of the upload session.
            Example: "D5E3F7A"
        :type uploadSessionId: str
        """
        if options is None:
            options = GetFilesUploadSessionsIdPartsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/upload_sessions/', uploadSessionId, '/parts']), FetchOptions(method='GET', params={'offset': options.offset, 'limit': options.limit}, auth=self.auth))
        return UploadParts.from_dict(json.loads(response.text))
    def postFilesUploadSessionsIdCommit(self, uploadSessionId: str, digest: str, requestBody: PostFilesUploadSessionsIdCommitRequestBodyArg, options: PostFilesUploadSessionsIdCommitOptionsArg = None) -> Files:
        """
        Close an upload session and create a file from the
        
        uploaded chunks.

        :param uploadSessionId: The ID of the upload session.
            Example: "D5E3F7A"
        :type uploadSessionId: str
        :param digest: The [RFC3230][1] message digest of the whole file.
            Only SHA1 is supported. The SHA1 digest must be Base64
            encoded. The format of this header is as
            `sha=BASE64_ENCODED_DIGEST`.
            [1]: https://tools.ietf.org/html/rfc3230
            Example: "sha=fpRyg5eVQletdZqEKaFlqwBXJzM="
        :type digest: str
        """
        if options is None:
            options = PostFilesUploadSessionsIdCommitOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/upload_sessions/', uploadSessionId, '/commit']), FetchOptions(method='POST', headers={'digest': digest, 'if-match': options.ifMatch, 'if-none-match': options.ifNoneMatch}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Files.from_dict(json.loads(response.text))