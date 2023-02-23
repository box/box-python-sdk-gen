from base_object import BaseObject

from typing import Union

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import Watermark

from schemas import ClientError

class PutFilesIdWatermarkRequestBodyArgWatermarkFieldImprintField:
    pass

class PutFilesIdWatermarkRequestBodyArgWatermarkField(BaseObject):
    def __init__(self, imprint: PutFilesIdWatermarkRequestBodyArgWatermarkFieldImprintField, **kwargs):
        """
        :param imprint: The type of watermark to apply.
            Currently only supports one option.
        :type imprint: PutFilesIdWatermarkRequestBodyArgWatermarkFieldImprintField
        """
        super().__init__(**kwargs)
        self.imprint = imprint

class PutFilesIdWatermarkRequestBodyArg(BaseObject):
    def __init__(self, watermark: PutFilesIdWatermarkRequestBodyArgWatermarkField, **kwargs):
        """
        :param watermark: The watermark to imprint on the file
        :type watermark: PutFilesIdWatermarkRequestBodyArgWatermarkField
        """
        super().__init__(**kwargs)
        self.watermark = watermark

class FileWatermarksManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFilesIdWatermark(self, fileId: str) -> Watermark:
        """
        Retrieve the watermark for a file.
        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/watermark']), FetchOptions(method='GET', auth=self.auth))
        return Watermark.from_dict(json.loads(response.text))
    def putFilesIdWatermark(self, fileId: str, requestBody: PutFilesIdWatermarkRequestBodyArg) -> Watermark:
        """
        Applies or update a watermark on a file.
        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/watermark']), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Watermark.from_dict(json.loads(response.text))
    def deleteFilesIdWatermark(self, fileId: str):
        """
        Removes the watermark from a file.
        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/watermark']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content