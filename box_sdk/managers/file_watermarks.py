from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Optional

import json

from typing import Dict

from box_sdk.schemas import Watermark

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class UpdateFileWatermarkRequestBodyArgWatermarkFieldImprintField(str, Enum):
    DEFAULT = 'default'

class UpdateFileWatermarkRequestBodyArgWatermarkField(BaseObject):
    def __init__(self, imprint: UpdateFileWatermarkRequestBodyArgWatermarkFieldImprintField, **kwargs):
        """
        :param imprint: The type of watermark to apply.
            Currently only supports one option.
        :type imprint: UpdateFileWatermarkRequestBodyArgWatermarkFieldImprintField
        """
        super().__init__(**kwargs)
        self.imprint = imprint

class UpdateFileWatermarkRequestBodyArg(BaseObject):
    def __init__(self, watermark: UpdateFileWatermarkRequestBodyArgWatermarkField, **kwargs):
        """
        :param watermark: The watermark to imprint on the file
        :type watermark: UpdateFileWatermarkRequestBodyArgWatermarkField
        """
        super().__init__(**kwargs)
        self.watermark = watermark

class FileWatermarksManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def get_file_watermark(self, file_id: str) -> Watermark:
        """
        Retrieve the watermark for a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/watermark']), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return Watermark.from_dict(json.loads(response.text))
    def update_file_watermark(self, file_id: str, request_body: UpdateFileWatermarkRequestBodyArg) -> Watermark:
        """
        Applies or update a watermark on a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/watermark']), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return Watermark.from_dict(json.loads(response.text))
    def delete_file_watermark(self, file_id: str):
        """
        Removes the watermark from a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/watermark']), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content