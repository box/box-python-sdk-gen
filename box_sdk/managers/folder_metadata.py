from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Union

import json

from box_sdk.schemas import Metadatas

from box_sdk.schemas import ClientError

from box_sdk.schemas import Metadata

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetFolderMetadataByIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class CreateFolderMetadataByIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class CreateFolderMetadataByIdRequestBodyArg(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class DeleteFolderMetadataByIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class FolderMetadataManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_folder_metadata(self, folder_id: str) -> Metadatas:
        """
        Retrieves all metadata for a given folder. This can not be used on the root
        
        folder with ID `0`.

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
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata']), FetchOptions(method='GET', auth=self.auth))
        return Metadatas.from_dict(json.loads(response.text))
    def get_folder_metadata_by_id(self, folder_id: str, scope: GetFolderMetadataByIdScopeArg, template_key: str) -> Metadata:
        """
        Retrieves the instance of a metadata template that has been applied to a
        
        folder. This can not be used on the root folder with ID `0`.

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
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: GetFolderMetadataByIdScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata/', scope, '/', template_key]), FetchOptions(method='GET', auth=self.auth))
        return Metadata.from_dict(json.loads(response.text))
    def create_folder_metadata_by_id(self, folder_id: str, scope: CreateFolderMetadataByIdScopeArg, template_key: str, request_body: CreateFolderMetadataByIdRequestBodyArg) -> Metadata:
        """
        Applies an instance of a metadata template to a folder.
        
        In most cases only values that are present in the metadata template

        
        will be accepted, except for the `global.properties` template which accepts

        
        any key-value pair.

        
        To display the metadata template in the Box web app the enterprise needs to be

        
        configured to enable **Cascading Folder Level Metadata** for the user in the

        
        admin console.

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
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: CreateFolderMetadataByIdScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata/', scope, '/', template_key]), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return Metadata.from_dict(json.loads(response.text))
    def delete_folder_metadata_by_id(self, folder_id: str, scope: DeleteFolderMetadataByIdScopeArg, template_key: str):
        """
        Deletes a piece of folder metadata.
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
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: DeleteFolderMetadataByIdScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata/', scope, '/', template_key]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content