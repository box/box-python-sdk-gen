from enum import Enum

from typing import Optional

from typing import Dict

import json

from typing import List

from typing import Union

from box_sdk_gen.base_object import BaseObject

from box_sdk_gen.schemas import MetadataTemplates

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import MetadataTemplate

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

class GetMetadataTemplateSchemaScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class DeleteMetadataTemplateSchemaScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class MetadataTemplatesManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_metadata_templates(self, metadata_instance_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> MetadataTemplates:
        """
        Finds a metadata template by searching for the ID of an instance of the
        
        template.

        :param metadata_instance_id: The ID of an instance of the metadata template to find.
        :type metadata_instance_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({'metadata_instance_id': to_string(metadata_instance_id)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates']), FetchOptions(method='GET', params=query_params_map, headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return MetadataTemplates.from_dict(json.loads(response.text))
    def get_metadata_template_schema(self, scope: GetMetadataTemplateSchemaScopeArg, template_key: str, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> MetadataTemplate:
        """
        Retrieves a metadata template by its `scope` and `templateKey` values.
        
        To find the `scope` and `templateKey` for a template, list all templates for

        
        an enterprise or globally, or list all templates applied to a file or folder.

        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: GetMetadataTemplateSchemaScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/', scope, '/', template_key, '/schema']), FetchOptions(method='GET', headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return MetadataTemplate.from_dict(json.loads(response.text))
    def delete_metadata_template_schema(self, scope: DeleteMetadataTemplateSchemaScopeArg, template_key: str, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> None:
        """
        Delete a metadata template and its instances.
        
        This deletion is permanent and can not be reversed.

        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: DeleteMetadataTemplateSchemaScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/', scope, '/', template_key, '/schema']), FetchOptions(method='DELETE', headers=headers_map, response_format=None, auth=self.auth, network_session=self.network_session))
        return None
    def get_metadata_template_by_id(self, template_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> MetadataTemplate:
        """
        Retrieves a metadata template by its ID.
        :param template_id: The ID of the template
            Example: "f7a9891f"
        :type template_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/', template_id]), FetchOptions(method='GET', headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return MetadataTemplate.from_dict(json.loads(response.text))
    def get_metadata_template_global(self, marker: Optional[str] = None, limit: Optional[int] = None, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> MetadataTemplates:
        """
        Used to retrieve all generic, global metadata templates available to all
        
        enterprises using Box.

        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({'marker': to_string(marker), 'limit': to_string(limit)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/global']), FetchOptions(method='GET', params=query_params_map, headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return MetadataTemplates.from_dict(json.loads(response.text))
    def get_metadata_template_enterprise(self, marker: Optional[str] = None, limit: Optional[int] = None, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> MetadataTemplates:
        """
        Used to retrieve all metadata templates created to be used specifically within
        
        the user's enterprise

        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({'marker': to_string(marker), 'limit': to_string(limit)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/enterprise']), FetchOptions(method='GET', params=query_params_map, headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return MetadataTemplates.from_dict(json.loads(response.text))
    def create_metadata_template_schema(self, scope: str, display_name: str, template_key: Optional[str] = None, hidden: Optional[bool] = None, fields: Optional[List] = None, copy_instance_on_item_copy: Optional[bool] = None, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> MetadataTemplate:
        """
        Creates a new metadata template that can be applied to
        
        files and folders.

        :param scope: The scope of the metadata template to create. Applications can
            only create templates for use within the authenticated user's
            enterprise.
            This value needs to be set to `enterprise`, as `global` scopes can
            not be created by applications.
        :type scope: str
        :param display_name: The display name of the template.
        :type display_name: str
        :param template_key: A unique identifier for the template. This identifier needs to be
            unique across the enterprise for which the metadata template is
            being created.
            When not provided, the API will create a unique `templateKey`
            based on the value of the `displayName`.
        :type template_key: Optional[str], optional
        :param hidden: Defines if this template is visible in the Box web app UI, or if
            it is purely intended for usage through the API.
        :type hidden: Optional[bool], optional
        :param fields: An ordered list of template fields which are part of the template.
            Each field can be a regular text field, date field, number field,
            as well as a single or multi-select list.
        :type fields: Optional[List], optional
        :param copy_instance_on_item_copy: Whether or not to copy any metadata attached to a file or folder
            when it is copied. By default, metadata is not copied along with a
            file or folder when it is copied.
        :type copy_instance_on_item_copy: Optional[bool], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: BaseObject = BaseObject(scope=scope, template_key=template_key, display_name=display_name, hidden=hidden, fields=fields, copy_instance_on_item_copy=copy_instance_on_item_copy)
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/schema']), FetchOptions(method='POST', headers=headers_map, body=json.dumps(request_body.to_dict()), content_type='application/json', response_format='json', auth=self.auth, network_session=self.network_session))
        return MetadataTemplate.from_dict(json.loads(response.text))