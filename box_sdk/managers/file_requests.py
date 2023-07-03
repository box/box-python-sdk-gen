from typing import Optional

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import FileRequest

from box_sdk.schemas import ClientError

from box_sdk.schemas import FileRequestUpdateRequest

from box_sdk.schemas import FileRequestCopyRequest

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class UpdateFileRequestByIdOptionsArg(BaseObject):
    def __init__(self, if_match: Optional[str] = None, **kwargs):
        """
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.if_match = if_match

class FileRequestsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_file_request_by_id(self, file_request_id: str) -> FileRequest:
        """
        Retrieves the information about a file request.
        :param file_request_id: The unique identifier that represent a file request.
            The ID for any file request can be determined
            by visiting a file request builder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/filerequest/123`
            the `file_request_id` is `123`.
            Example: "123"
        :type file_request_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_requests/', file_request_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return FileRequest.from_dict(json.loads(response.text))
    def update_file_request_by_id(self, file_request_id: str, request_body: FileRequestUpdateRequest, options: UpdateFileRequestByIdOptionsArg = None) -> FileRequest:
        """
        Updates a file request. This can be used to activate or
        
        deactivate a file request.

        :param file_request_id: The unique identifier that represent a file request.
            The ID for any file request can be determined
            by visiting a file request builder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/filerequest/123`
            the `file_request_id` is `123`.
            Example: "123"
        :type file_request_id: str
        """
        if options is None:
            options = UpdateFileRequestByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_requests/', file_request_id]), FetchOptions(method='PUT', headers={'if-match': options.if_match}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return FileRequest.from_dict(json.loads(response.text))
    def delete_file_request_by_id(self, file_request_id: str):
        """
        Deletes a file request permanently.
        :param file_request_id: The unique identifier that represent a file request.
            The ID for any file request can be determined
            by visiting a file request builder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/filerequest/123`
            the `file_request_id` is `123`.
            Example: "123"
        :type file_request_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_requests/', file_request_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content
    def create_file_request_copy(self, file_request_id: str, request_body: FileRequestCopyRequest) -> FileRequest:
        """
        Copies an existing file request that is already present on one folder,
        
        and applies it to another folder.

        :param file_request_id: The unique identifier that represent a file request.
            The ID for any file request can be determined
            by visiting a file request builder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/filerequest/123`
            the `file_request_id` is `123`.
            Example: "123"
        :type file_request_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_requests/', file_request_id, '/copy']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return FileRequest.from_dict(json.loads(response.text))