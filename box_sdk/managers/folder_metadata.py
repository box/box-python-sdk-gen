from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Union

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import Metadatas

from box_sdk.schemas import ClientError

from box_sdk.schemas import Metadata

class GetFoldersIdMetadataIdIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class PostFoldersIdMetadataIdIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class PostFoldersIdMetadataIdIdRequestBodyArg(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class DeleteFoldersIdMetadataIdIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class FolderMetadataManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFoldersIdMetadata(self, folderId: str) -> Metadatas:
        """
        Retrieves all metadata for a given folder. This can not be used on the root
        
        folder with ID `0`.

        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/metadata']), FetchOptions(method='GET', auth=self.auth))
        return Metadatas.from_dict(json.loads(response.text))
    def getFoldersIdMetadataIdId(self, folderId: str, scope: GetFoldersIdMetadataIdIdScopeArg, templateKey: str) -> Metadata:
        """
        Retrieves the instance of a metadata template that has been applied to a
        
        folder. This can not be used on the root folder with ID `0`.

        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: GetFoldersIdMetadataIdIdScopeArg
        :param templateKey: The name of the metadata template
            Example: "properties"
        :type templateKey: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/metadata/', scope, '/', templateKey]), FetchOptions(method='GET', auth=self.auth))
        return Metadata.from_dict(json.loads(response.text))
    def postFoldersIdMetadataIdId(self, folderId: str, scope: PostFoldersIdMetadataIdIdScopeArg, templateKey: str, requestBody: PostFoldersIdMetadataIdIdRequestBodyArg) -> Metadata:
        """
        Applies an instance of a metadata template to a folder.
        
        In most cases only values that are present in the metadata template

        
        will be accepted, except for the `global.properties` template which accepts

        
        any key-value pair.

        
        To display the metadata template in the Box web app the enterprise needs to be

        
        configured to enable **Cascading Folder Level Metadata** for the user in the

        
        admin console.

        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: PostFoldersIdMetadataIdIdScopeArg
        :param templateKey: The name of the metadata template
            Example: "properties"
        :type templateKey: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/metadata/', scope, '/', templateKey]), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Metadata.from_dict(json.loads(response.text))
    def deleteFoldersIdMetadataIdId(self, folderId: str, scope: DeleteFoldersIdMetadataIdIdScopeArg, templateKey: str):
        """
        Deletes a piece of folder metadata.
        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: DeleteFoldersIdMetadataIdIdScopeArg
        :param templateKey: The name of the metadata template
            Example: "properties"
        :type templateKey: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/metadata/', scope, '/', templateKey]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content