from box_sdk.base_object import BaseObject

from typing import Union

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import Watermark

from box_sdk.schemas import ClientError

class PutFoldersIdWatermarkRequestBodyArgWatermarkFieldImprintField:
    pass

class PutFoldersIdWatermarkRequestBodyArgWatermarkField(BaseObject):
    def __init__(self, imprint: PutFoldersIdWatermarkRequestBodyArgWatermarkFieldImprintField, **kwargs):
        """
        :param imprint: The type of watermark to apply.
            Currently only supports one option.
        :type imprint: PutFoldersIdWatermarkRequestBodyArgWatermarkFieldImprintField
        """
        super().__init__(**kwargs)
        self.imprint = imprint

class PutFoldersIdWatermarkRequestBodyArg(BaseObject):
    def __init__(self, watermark: PutFoldersIdWatermarkRequestBodyArgWatermarkField, **kwargs):
        """
        :param watermark: The watermark to imprint on the folder
        :type watermark: PutFoldersIdWatermarkRequestBodyArgWatermarkField
        """
        super().__init__(**kwargs)
        self.watermark = watermark

class FolderWatermarksManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFoldersIdWatermark(self, folderId: str) -> Watermark:
        """
        Retrieve the watermark for a folder.
        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/watermark']), FetchOptions(method='GET', auth=self.auth))
        return Watermark.from_dict(json.loads(response.text))
    def putFoldersIdWatermark(self, folderId: str, requestBody: PutFoldersIdWatermarkRequestBodyArg) -> Watermark:
        """
        Applies or update a watermark on a folder.
        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/watermark']), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Watermark.from_dict(json.loads(response.text))
    def deleteFoldersIdWatermark(self, folderId: str):
        """
        Removes the watermark from a folder.
        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/watermark']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content