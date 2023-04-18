from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import ClientError

from box_sdk.schemas import Files

from box_sdk.schemas import UploadUrl

from box_sdk.schemas import ConflictError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

from box_sdk.fetch import MultipartItem

class DownloadFileOptionsArg(BaseObject):
    def __init__(self, range: Union[None, str] = None, boxapi: Union[None, str] = None, version: Union[None, str] = None, access_token: Union[None, str] = None, **kwargs):
        """
        :param range: The byte range of the content to download.
            The format `bytes={start_byte}-{end_byte}` can be used to specify
            what section of the file to download.
        :type range: Union[None, str], optional
        :param boxapi: The URL, and optional password, for the shared link of this item.
            This header can be used to access items that have not been
            explicitly shared with a user.
            Use the format `shared_link=[link]` or if a password is required then
            use `shared_link=[link]&shared_link_password=[password]`.
            This header can be used on the file or folder shared, as well as on any files
            or folders nested within the item.
        :type boxapi: Union[None, str], optional
        :param version: The file version to download
        :type version: Union[None, str], optional
        :param access_token: An optional access token that can be used to pre-authenticate this request, which means that a download link can be shared with a browser or a third party service without them needing to know how to handle the authentication.
            When using this parameter, please make sure that the access token is sufficiently scoped down to only allow read access to that file and no other files or folders.
        :type access_token: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.range = range
        self.boxapi = boxapi
        self.version = version
        self.access_token = access_token

class UploadFileVersionRequestBodyArgAttributesField(BaseObject):
    def __init__(self, name: str, content_modified_at: Union[None, str] = None, **kwargs):
        """
        :param name: An optional new name for the file. If specified, the file
            will be renamed when the new version is uploaded.
        :type name: str
        :param content_modified_at: Defines the time the file was last modified at.
            If not set, the upload time will be used.
        :type content_modified_at: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.content_modified_at = content_modified_at

class UploadFileVersionRequestBodyArg(BaseObject):
    def __init__(self, attributes: UploadFileVersionRequestBodyArgAttributesField, file: str, **kwargs):
        """
        :param attributes: The additional attributes of the file being uploaded. Mainly the
            name and the parent folder. These attributes are part of the multi
            part request body and are in JSON format.
            <Message warning>
              The `attributes` part of the body must come **before** the
              `file` part. Requests that do not follow this format when
              uploading the file will receive a HTTP `400` error with a
              `metadata_after_file_contents` error code.
            </Message>
        :type attributes: UploadFileVersionRequestBodyArgAttributesField
        :param file: The content of the file to upload to Box.
            <Message warning>
              The `attributes` part of the body must come **before** the
              `file` part. Requests that do not follow this format when
              uploading the file will receive a HTTP `400` error with a
              `metadata_after_file_contents` error code.
            </Message>
        :type file: str
        """
        super().__init__(**kwargs)
        self.attributes = attributes
        self.file = file

class UploadFileVersionOptionsArg(BaseObject):
    def __init__(self, if_match: Union[None, str] = None, fields: Union[None, str] = None, content_md_5: Union[None, str] = None, **kwargs):
        """
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Union[None, str], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        :param content_md_5: An optional header containing the SHA1 hash of the file to
            ensure that the file was not corrupted in transit.
        :type content_md_5: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.if_match = if_match
        self.fields = fields
        self.content_md_5 = content_md_5

class UploadFileRequestBodyArgAttributesFieldParentField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The id of the parent folder. Use
            `0` for the user's root folder.
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class UploadFileRequestBodyArgAttributesField(BaseObject):
    def __init__(self, name: str, parent: UploadFileRequestBodyArgAttributesFieldParentField, content_created_at: Union[None, str] = None, content_modified_at: Union[None, str] = None, **kwargs):
        """
        :param name: The name of the file
        :type name: str
        :param parent: The parent folder to upload the file to
        :type parent: UploadFileRequestBodyArgAttributesFieldParentField
        :param content_created_at: Defines the time the file was originally created at.
            If not set, the upload time will be used.
        :type content_created_at: Union[None, str], optional
        :param content_modified_at: Defines the time the file was last modified at.
            If not set, the upload time will be used.
        :type content_modified_at: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.parent = parent
        self.content_created_at = content_created_at
        self.content_modified_at = content_modified_at

class UploadFileRequestBodyArg(BaseObject):
    def __init__(self, attributes: UploadFileRequestBodyArgAttributesField, file: str, **kwargs):
        """
        :param attributes: The additional attributes of the file being uploaded. Mainly the
            name and the parent folder. These attributes are part of the multi
            part request body and are in JSON format.
            <Message warning>
              The `attributes` part of the body must come **before** the
              `file` part. Requests that do not follow this format when
              uploading the file will receive a HTTP `400` error with a
              `metadata_after_file_contents` error code.
            </Message>
        :type attributes: UploadFileRequestBodyArgAttributesField
        :param file: The content of the file to upload to Box.
            <Message warning>
              The `attributes` part of the body must come **before** the
              `file` part. Requests that do not follow this format when
              uploading the file will receive a HTTP `400` error with a
              `metadata_after_file_contents` error code.
            </Message>
        :type file: str
        """
        super().__init__(**kwargs)
        self.attributes = attributes
        self.file = file

class UploadFileOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, content_md_5: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        :param content_md_5: An optional header containing the SHA1 hash of the file to
            ensure that the file was not corrupted in transit.
        :type content_md_5: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.content_md_5 = content_md_5

class PreflightFileUploadRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class PreflightFileUploadRequestBodyArg(BaseObject):
    def __init__(self, name: Union[None, str] = None, size: Union[None, int] = None, parent: Union[None, PreflightFileUploadRequestBodyArgParentField] = None, **kwargs):
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
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def download_file(self, file_id: str, options: DownloadFileOptionsArg = None):
        """
        Returns the contents of a file in binary format.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        if options is None:
            options = DownloadFileOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/content']), FetchOptions(method='GET', params={'version': options.version, 'access_token': options.access_token}, headers={'range': options.range, 'boxapi': options.boxapi}, auth=self.auth))
        return response.content
    def upload_file_version(self, file_id: str, request_body: UploadFileVersionRequestBodyArg, options: UploadFileVersionOptionsArg = None) -> Files:
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
        """
        if options is None:
            options = UploadFileVersionOptionsArg()
        response: FetchResponse = fetch(''.join(['https://upload.box.com/api/2.0/files/', file_id, '/content']), FetchOptions(method='POST', params={'fields': options.fields}, headers={'if-match': options.if_match, 'content-md5': options.content_md_5}, multipart_data=[MultipartItem(part_name='attributes', body=json.dumps(request_body.attributes.to_dict())), MultipartItem(part_name='file', file_stream=request_body.file)], content_type='multipart/form-data', auth=self.auth))
        return Files.from_dict(json.loads(response.text))
    def upload_file(self, request_body: UploadFileRequestBodyArg, options: UploadFileOptionsArg = None) -> Files:
        """
        Uploads a small file to Box. For file sizes over 50MB we recommend
        
        using the Chunk Upload APIs.

        
        # Request body order

        
        The `attributes` part of the body must come **before** the

        
        `file` part. Requests that do not follow this format when

        
        uploading the file will receive a HTTP `400` error with a

        
        `metadata_after_file_contents` error code.

        """
        if options is None:
            options = UploadFileOptionsArg()
        response: FetchResponse = fetch(''.join(['https://upload.box.com/api/2.0/files/content']), FetchOptions(method='POST', params={'fields': options.fields}, headers={'content-md5': options.content_md_5}, multipart_data=[MultipartItem(part_name='attributes', body=json.dumps(request_body.attributes.to_dict())), MultipartItem(part_name='file', file_stream=request_body.file)], content_type='multipart/form-data', auth=self.auth))
        return Files.from_dict(json.loads(response.text))
    def preflight_file_upload(self, request_body: PreflightFileUploadRequestBodyArg) -> UploadUrl:
        """
        Performs a check to verify that a file will be accepted by Box
        
        before you upload the entire file.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/content']), FetchOptions(method='OPTIONS', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return UploadUrl.from_dict(json.loads(response.text))