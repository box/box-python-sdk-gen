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
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/watermark']), FetchOptions(method='GET', auth=self.auth))
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/watermark']), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), auth=self.auth))
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/watermark']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content