from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Union

import json

from box_sdk.schemas import Metadatas

from box_sdk.schemas import ClientError

from box_sdk.schemas import Metadata

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetFilesIdMetadataIdIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class PostFilesIdMetadataIdIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class PostFilesIdMetadataIdIdRequestBodyArg(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class DeleteFilesIdMetadataIdIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class FileMetadataManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_files_id_metadata(self, file_id: str) -> Metadatas:
        """
        Retrieves all metadata for a given file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata']), FetchOptions(method='GET', auth=self.auth))
        return Metadatas.from_dict(json.loads(response.text))
    def get_files_id_metadata_id_id(self, file_id: str, scope: GetFilesIdMetadataIdIdScopeArg, template_key: str) -> Metadata:
        """
        Retrieves the instance of a metadata template that has been applied to a
        
        file.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: GetFilesIdMetadataIdIdScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/', scope, '/', template_key]), FetchOptions(method='GET', auth=self.auth))
        return Metadata.from_dict(json.loads(response.text))
    def post_files_id_metadata_id_id(self, file_id: str, scope: PostFilesIdMetadataIdIdScopeArg, template_key: str, request_body: PostFilesIdMetadataIdIdRequestBodyArg) -> Metadata:
        """
        Applies an instance of a metadata template to a file.
        
        In most cases only values that are present in the metadata template

        
        will be accepted, except for the `global.properties` template which accepts

        
        any key-value pair.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: PostFilesIdMetadataIdIdScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/', scope, '/', template_key]), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return Metadata.from_dict(json.loads(response.text))
    def delete_files_id_metadata_id_id(self, file_id: str, scope: DeleteFilesIdMetadataIdIdScopeArg, template_key: str):
        """
        Deletes a piece of file metadata.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: DeleteFilesIdMetadataIdIdScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/', scope, '/', template_key]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content