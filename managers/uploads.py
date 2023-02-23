from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

import json

from fetch import fetch, FetchOptions, FetchResponse

from schemas import Files

from schemas import ClientError

from schemas import UploadUrl

from schemas import ConflictError

class OptionsFilesContentRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class OptionsFilesContentRequestBodyArg(BaseObject):
    def __init__(self, name: Union[None, str] = None, size: Union[None, int] = None, parent: Union[None, OptionsFilesContentRequestBodyArgParentField] = None, **kwargs):
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
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def optionsFilesContent(self, requestBody: OptionsFilesContentRequestBodyArg) -> UploadUrl:
        """
        Performs a check to verify that a file will be accepted by Box
        
        before you upload the entire file.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/content']), FetchOptions(method='OPTIONS', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return UploadUrl.from_dict(json.loads(response.text))