from enum import Enum

from box_sdk_gen.base_object import BaseObject

from typing import Optional

import json

from box_sdk_gen.base_object import BaseObject

from box_sdk_gen.schemas import Watermark

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

class UpdateFileWatermarkWatermarkArgImprintField(str, Enum):
    DEFAULT = 'default'

class UpdateFileWatermarkWatermarkArg(BaseObject):
    def __init__(self, imprint: UpdateFileWatermarkWatermarkArgImprintField, **kwargs):
        """
        :param imprint: The type of watermark to apply.
            Currently only supports one option.
        :type imprint: UpdateFileWatermarkWatermarkArgImprintField
        """
        super().__init__(**kwargs)
        self.imprint = imprint

class FileWatermarksManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/watermark']), FetchOptions(method='GET', response_format='json', auth=self.auth, network_session=self.network_session))
        return Watermark.from_dict(json.loads(response.text))
    def update_file_watermark(self, file_id: str, watermark: UpdateFileWatermarkWatermarkArg) -> Watermark:
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
        :param watermark: The watermark to imprint on the file
        :type watermark: UpdateFileWatermarkWatermarkArg
        """
        request_body: BaseObject = BaseObject(watermark=watermark)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/watermark']), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', response_format='json', auth=self.auth, network_session=self.network_session))
        return Watermark.from_dict(json.loads(response.text))
    def delete_file_watermark(self, file_id: str) -> None:
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/watermark']), FetchOptions(method='DELETE', response_format=None, auth=self.auth, network_session=self.network_session))
        return None