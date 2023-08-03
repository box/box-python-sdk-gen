from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Optional

from typing import Dict

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import Watermark

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import prepare_params

from box_sdk.utils import to_string

from box_sdk.utils import ByteStream

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
    def get_folder_watermark(self, folder_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = {}) -> Watermark:
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
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to {}
        :type extra_headers: Optional[Dict[str, Optional[str]]]
        """
        headers_map: Dict[str, str] = prepare_params({**{}, **extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/watermark']), FetchOptions(method='GET', headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return Watermark.from_dict(json.loads(response.text))
    def update_folder_watermark(self, folder_id: str, watermark: UpdateFolderWatermarkWatermarkArg, extra_headers: Optional[Dict[str, Optional[str]]] = {}) -> Watermark:
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
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to {}
        :type extra_headers: Optional[Dict[str, Optional[str]]]
        """
        request_body: BaseObject = BaseObject(watermark=watermark)
        headers_map: Dict[str, str] = prepare_params({**{}, **extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/watermark']), FetchOptions(method='PUT', headers=headers_map, body=json.dumps(request_body.to_dict()), content_type='application/json', response_format='json', auth=self.auth, network_session=self.network_session))
        return Watermark.from_dict(json.loads(response.text))
    def delete_folder_watermark(self, folder_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = {}) -> None:
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
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to {}
        :type extra_headers: Optional[Dict[str, Optional[str]]]
        """
        headers_map: Dict[str, str] = prepare_params({**{}, **extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/watermark']), FetchOptions(method='DELETE', headers=headers_map, response_format=None, auth=self.auth, network_session=self.network_session))
        return None