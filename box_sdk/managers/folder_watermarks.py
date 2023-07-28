from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Optional

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import Watermark

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import prepare_params

from box_sdk.utils import to_string

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class UpdateFolderWatermarkWatermarkArgImprintField(str, Enum):
    DEFAULT = 'default'

class UpdateFolderWatermarkWatermarkArg(BaseObject):
    def __init__(self, imprint: UpdateFolderWatermarkWatermarkArgImprintField, **kwargs):
        """
        :param imprint: The type of watermark to apply.
            Currently only supports one option.
        :type imprint: UpdateFolderWatermarkWatermarkArgImprintField
        """
        super().__init__(**kwargs)
        self.imprint = imprint

class FolderWatermarksManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/watermark']), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return Watermark.from_dict(json.loads(response.text))
    def update_folder_watermark(self, folder_id: str, watermark: UpdateFolderWatermarkWatermarkArg) -> Watermark:
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
        :param watermark: The watermark to imprint on the folder
        :type watermark: UpdateFolderWatermarkWatermarkArg
        """
        request_body: BaseObject = BaseObject(watermark=watermark)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/watermark']), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/watermark']), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content