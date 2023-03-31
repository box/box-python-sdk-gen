from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import Files

from box_sdk.schemas import ClientError

from box_sdk.schemas import UploadUrl

from box_sdk.schemas import ConflictError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class PreflightFileUploadRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class PreflightFileUploadRequestBodyArg(BaseObject):
    def __init__(self, name: Union[None, str] = None, size: Union[None, int] = None, parent: Union[None, PreflightFileUploadRequestBodyArgParentField] = None, **kwargs):
        """
        :param name: The name for the file
        :type name: Union[None, str], optional
        :param size: The size of the file in bytes
        :type size: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.size = size
        self.parent = parent

class UploadsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def preflight_file_upload(self, request_body: PreflightFileUploadRequestBodyArg) -> UploadUrl:
        """
        Performs a check to verify that a file will be accepted by Box
        
        before you upload the entire file.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/content']), FetchOptions(method='OPTIONS', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return UploadUrl.from_dict(json.loads(response.text))