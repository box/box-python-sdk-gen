from enum import Enum

from base_object import BaseObject

from typing import Union

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import Metadatas

from schemas import ClientError

from schemas import Metadata

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
    def getFilesIdMetadata(self, fileId: str) -> Metadatas:
        """
        Retrieves all metadata for a given file.
        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/metadata']), FetchOptions(method='GET', auth=self.auth))
        return Metadatas.from_dict(json.loads(response.text))
    def getFilesIdMetadataIdId(self, fileId: str, scope: GetFilesIdMetadataIdIdScopeArg, templateKey: str) -> Metadata:
        """
        Retrieves the instance of a metadata template that has been applied to a
        
        file.

        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: GetFilesIdMetadataIdIdScopeArg
        :param templateKey: The name of the metadata template
            Example: "properties"
        :type templateKey: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/metadata/', scope, '/', templateKey]), FetchOptions(method='GET', auth=self.auth))
        return Metadata.from_dict(json.loads(response.text))
    def postFilesIdMetadataIdId(self, fileId: str, scope: PostFilesIdMetadataIdIdScopeArg, templateKey: str, requestBody: PostFilesIdMetadataIdIdRequestBodyArg) -> Metadata:
        """
        Applies an instance of a metadata template to a file.
        
        In most cases only values that are present in the metadata template

        
        will be accepted, except for the `global.properties` template which accepts

        
        any key-value pair.

        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: PostFilesIdMetadataIdIdScopeArg
        :param templateKey: The name of the metadata template
            Example: "properties"
        :type templateKey: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/metadata/', scope, '/', templateKey]), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Metadata.from_dict(json.loads(response.text))
    def deleteFilesIdMetadataIdId(self, fileId: str, scope: DeleteFilesIdMetadataIdIdScopeArg, templateKey: str):
        """
        Deletes a piece of file metadata.
        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: DeleteFilesIdMetadataIdIdScopeArg
        :param templateKey: The name of the metadata template
            Example: "properties"
        :type templateKey: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/metadata/', scope, '/', templateKey]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content