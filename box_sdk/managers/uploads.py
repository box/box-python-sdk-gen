from typing import Optional

from box_sdk.base_object import BaseObject

from typing import Dict

import json

import re

from box_sdk.base_object import BaseObject

from box_sdk.schemas import Files

from box_sdk.schemas import ClientError

from box_sdk.schemas import UploadUrl

from box_sdk.schemas import ConflictError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import to_map

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

from box_sdk.fetch import MultipartItem

class UploadFileVersionAttributesArg(BaseObject):
    def __init__(self, name: str, content_modified_at: Optional[str] = None, **kwargs):
        """
        :param name: An optional new name for the file. If specified, the file
            will be renamed when the new version is uploaded.
        :type name: str
        :param content_modified_at: Defines the time the file was last modified at.
            If not set, the upload time will be used.
        :type content_modified_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.content_modified_at = content_modified_at

class UploadFileAttributesArgParentField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The id of the parent folder. Use
            `0` for the user's root folder.
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class UploadFileAttributesArg(BaseObject):
    def __init__(self, name: str, parent: UploadFileAttributesArgParentField, content_created_at: Optional[str] = None, content_modified_at: Optional[str] = None, **kwargs):
        """
        :param name: The name of the file
        :type name: str
        :param parent: The parent folder to upload the file to
        :type parent: UploadFileAttributesArgParentField
        :param content_created_at: Defines the time the file was originally created at.
            If not set, the upload time will be used.
        :type content_created_at: Optional[str], optional
        :param content_modified_at: Defines the time the file was last modified at.
            If not set, the upload time will be used.
        :type content_modified_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.parent = parent
        self.content_created_at = content_created_at
        self.content_modified_at = content_modified_at

class PreflightFileUploadParentArg(BaseObject):
    def __init__(self, id: Optional[str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class UploadsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def upload_file_version(self, file_id: str, attributes: UploadFileVersionAttributesArg, file: str, fields: Optional[str] = None, if_match: Optional[str] = None, content_md_5: Optional[str] = None) -> Files:
        """
        Update a file's content. For file sizes over 50MB we recommend
        
        using the Chunk Upload APIs.

        
        # Request body order

        
        The `attributes` part of the body must come **before** the

        
        `file` part. Requests that do not follow this format when

        
        uploading the file will receive a HTTP `400` error with a

        
        `metadata_after_file_contents` error code.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param attributes: The additional attributes of the file being uploaded. Mainly the
            name and the parent folder. These attributes are part of the multi
            part request body and are in JSON format.
            <Message warning>
              The `attributes` part of the body must come **before** the
              `file` part. Requests that do not follow this format when
              uploading the file will receive a HTTP `400` error with a
              `metadata_after_file_contents` error code.
            </Message>
        :type attributes: UploadFileVersionAttributesArg
        :param file: The content of the file to upload to Box.
            <Message warning>
              The `attributes` part of the body must come **before** the
              `file` part. Requests that do not follow this format when
              uploading the file will receive a HTTP `400` error with a
              `metadata_after_file_contents` error code.
            </Message>
        :type file: str
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Optional[str], optional
        :param content_md_5: An optional header containing the SHA1 hash of the file to
            ensure that the file was not corrupted in transit.
        :type content_md_5: Optional[str], optional
        """
        if isinstance(file, str) and not re.match('^[01]+$', file):
            raise Exception('Invalid binary provided to function upload_file_version in argument file')
        request_body: BaseObject = BaseObject(attributes=attributes, file=file)
        query_params: Dict = {'fields': fields}
        headers: Dict = {'if_match': if_match, 'content_md_5': content_md_5}
        response: FetchResponse = fetch(''.join(['https://upload.box.com/api/2.0/files/', file_id, '/content']), FetchOptions(method='POST', params=to_map(query_params), headers=to_map(headers), multipart_data=[MultipartItem(part_name='attributes', body=json.dumps(to_map(request_body.attributes))), MultipartItem(part_name='file', file_stream=request_body.file)], content_type='multipart/form-data', auth=self.auth, network_session=self.network_session))
        return Files.from_dict(json.loads(response.text))
    def upload_file(self, attributes: UploadFileAttributesArg, file: str, fields: Optional[str] = None, content_md_5: Optional[str] = None) -> Files:
        """
        Uploads a small file to Box. For file sizes over 50MB we recommend
        
        using the Chunk Upload APIs.

        
        # Request body order

        
        The `attributes` part of the body must come **before** the

        
        `file` part. Requests that do not follow this format when

        
        uploading the file will receive a HTTP `400` error with a

        
        `metadata_after_file_contents` error code.

        :param attributes: The additional attributes of the file being uploaded. Mainly the
            name and the parent folder. These attributes are part of the multi
            part request body and are in JSON format.
            <Message warning>
              The `attributes` part of the body must come **before** the
              `file` part. Requests that do not follow this format when
              uploading the file will receive a HTTP `400` error with a
              `metadata_after_file_contents` error code.
            </Message>
        :type attributes: UploadFileAttributesArg
        :param file: The content of the file to upload to Box.
            <Message warning>
              The `attributes` part of the body must come **before** the
              `file` part. Requests that do not follow this format when
              uploading the file will receive a HTTP `400` error with a
              `metadata_after_file_contents` error code.
            </Message>
        :type file: str
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param content_md_5: An optional header containing the SHA1 hash of the file to
            ensure that the file was not corrupted in transit.
        :type content_md_5: Optional[str], optional
        """
        if isinstance(file, str) and not re.match('^[01]+$', file):
            raise Exception('Invalid binary provided to function upload_file in argument file')
        request_body: BaseObject = BaseObject(attributes=attributes, file=file)
        query_params: Dict = {'fields': fields}
        headers: Dict = {'content_md_5': content_md_5}
        response: FetchResponse = fetch(''.join(['https://upload.box.com/api/2.0/files/content']), FetchOptions(method='POST', params=to_map(query_params), headers=to_map(headers), multipart_data=[MultipartItem(part_name='attributes', body=json.dumps(to_map(request_body.attributes))), MultipartItem(part_name='file', file_stream=request_body.file)], content_type='multipart/form-data', auth=self.auth, network_session=self.network_session))
        return Files.from_dict(json.loads(response.text))
    def preflight_file_upload(self, name: Optional[str] = None, size: Optional[int] = None, parent: Optional[PreflightFileUploadParentArg] = None) -> UploadUrl:
        """
        Performs a check to verify that a file will be accepted by Box
        
        before you upload the entire file.

        :param name: The name for the file
        :type name: Optional[str], optional
        :param size: The size of the file in bytes
        :type size: Optional[int], optional
        """
        request_body: BaseObject = BaseObject(name=name, size=size, parent=parent)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/content']), FetchOptions(method='OPTIONS', body=json.dumps(to_map(request_body)), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return UploadUrl.from_dict(json.loads(response.text))