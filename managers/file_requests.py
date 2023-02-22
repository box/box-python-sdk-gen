from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import FileRequest

from schemas import ClientError

from schemas import FileRequestUpdateRequest

from schemas import FileRequestCopyRequest

class PutFileRequestsIdOptionsArg(BaseObject):
    def __init__(self, ifMatch: Union[None, str] = None, **kwargs):
        """
        :param ifMatch: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type ifMatch: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.ifMatch = ifMatch

class FileRequestsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFileRequestsId(self, fileRequestId: str) -> FileRequest:
        """
        Retrieves the information about a file request.
        :param fileRequestId: The unique identifier that represent a file request.
            The ID for any file request can be determined
            by visiting a file request builder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/filerequest/123`
            the `file_request_id` is `123`.
            Example: "123"
        :type fileRequestId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_requests/', fileRequestId]), FetchOptions(method='GET', auth=self.auth))
        return FileRequest.from_dict(json.loads(response.text))
    def putFileRequestsId(self, fileRequestId: str, requestBody: FileRequestUpdateRequest, options: PutFileRequestsIdOptionsArg = None) -> FileRequest:
        """
        Updates a file request. This can be used to activate or
        
        deactivate a file request.

        :param fileRequestId: The unique identifier that represent a file request.
            The ID for any file request can be determined
            by visiting a file request builder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/filerequest/123`
            the `file_request_id` is `123`.
            Example: "123"
        :type fileRequestId: str
        """
        if options is None:
            options = PutFileRequestsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_requests/', fileRequestId]), FetchOptions(method='PUT', headers={'if-match': options.ifMatch}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return FileRequest.from_dict(json.loads(response.text))
    def deleteFileRequestsId(self, fileRequestId: str):
        """
        Deletes a file request permanently.
        :param fileRequestId: The unique identifier that represent a file request.
            The ID for any file request can be determined
            by visiting a file request builder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/filerequest/123`
            the `file_request_id` is `123`.
            Example: "123"
        :type fileRequestId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_requests/', fileRequestId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def postFileRequestsIdCopy(self, fileRequestId: str, requestBody: FileRequestCopyRequest) -> FileRequest:
        """
        Copies an existing file request that is already present on one folder,
        
        and applies it to another folder.

        :param fileRequestId: The unique identifier that represent a file request.
            The ID for any file request can be determined
            by visiting a file request builder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/filerequest/123`
            the `file_request_id` is `123`.
            Example: "123"
        :type fileRequestId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_requests/', fileRequestId, '/copy']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return FileRequest.from_dict(json.loads(response.text))