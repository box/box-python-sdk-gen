from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Union

import json

from box_sdk.schemas import Watermark

from box_sdk.schemas import ClientError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class UpdateFolderWatermarkRequestBodyArgWatermarkFieldImprintField(str, Enum):
    DEFAULT = 'default'

class UpdateFolderWatermarkRequestBodyArgWatermarkField(BaseObject):
    def __init__(self, imprint: UpdateFolderWatermarkRequestBodyArgWatermarkFieldImprintField, **kwargs):
        """
        :param imprint: The type of watermark to apply.
            Currently only supports one option.
        :type imprint: UpdateFolderWatermarkRequestBodyArgWatermarkFieldImprintField
        """
        super().__init__(**kwargs)
        self.imprint = imprint

class UpdateFolderWatermarkRequestBodyArg(BaseObject):
    def __init__(self, watermark: UpdateFolderWatermarkRequestBodyArgWatermarkField, **kwargs):
        """
        :param watermark: The watermark to imprint on the folder
        :type watermark: UpdateFolderWatermarkRequestBodyArgWatermarkField
        """
        super().__init__(**kwargs)
        self.watermark = watermark

class FolderWatermarksManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_folder_watermark(self, folder_id: str) -> Watermark:
        """
        Retrieve the watermark for a folder.
        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/watermark']), FetchOptions(method='GET', auth=self.auth))
        return Watermark.from_dict(json.loads(response.text))
    def update_folder_watermark(self, folder_id: str, request_body: UpdateFolderWatermarkRequestBodyArg) -> Watermark:
        """
        Applies or update a watermark on a folder.
        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/watermark']), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return Watermark.from_dict(json.loads(response.text))
    def delete_folder_watermark(self, folder_id: str):
        """
        Removes the watermark from a folder.
        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/watermark']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content