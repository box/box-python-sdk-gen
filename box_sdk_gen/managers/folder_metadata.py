from enum import Enum

from typing import Optional

from typing import Dict

import json

from box_sdk_gen.base_object import BaseObject

from box_sdk_gen.schemas import Metadatas

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import Metadata

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

class GetFolderMetadataByIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class CreateFolderMetadataByIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class DeleteFolderMetadataByIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class FolderMetadataManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_folder_metadata(self, folder_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> Metadatas:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata']), FetchOptions(method='GET', headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return Metadatas.from_dict(json.loads(response.text))
    def get_folder_metadata_by_id(self, folder_id: str, scope: GetFolderMetadataByIdScopeArg, template_key: str, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> Metadata:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata/', scope, '/', template_key]), FetchOptions(method='GET', headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return Metadata.from_dict(json.loads(response.text))
    def create_folder_metadata_by_id(self, folder_id: str, scope: CreateFolderMetadataByIdScopeArg, template_key: str, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> Metadata:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: BaseObject = BaseObject()
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata/', scope, '/', template_key]), FetchOptions(method='POST', headers=headers_map, body=json.dumps(request_body.to_dict()), content_type='application/json', response_format='json', auth=self.auth, network_session=self.network_session))
        return Metadata.from_dict(json.loads(response.text))
    def delete_folder_metadata_by_id(self, folder_id: str, scope: DeleteFolderMetadataByIdScopeArg, template_key: str, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> None:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata/', scope, '/', template_key]), FetchOptions(method='DELETE', headers=headers_map, response_format=None, auth=self.auth, network_session=self.network_session))
        return None