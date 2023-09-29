from enum import Enum

from typing import Optional

from typing import Dict

from typing import List

from box_sdk_gen.base_object import BaseObject

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

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


class UpdateMetadataTemplateSchemaScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'


class UpdateMetadataTemplateSchemaRequestBodyArgOpField(str, Enum):
    EDITTEMPLATE = 'editTemplate'
    ADDFIELD = 'addField'
    REORDERFIELDS = 'reorderFields'
    ADDENUMOPTION = 'addEnumOption'
    REORDERENUMOPTIONS = 'reorderEnumOptions'
    REORDERMULTISELECTOPTIONS = 'reorderMultiSelectOptions'
    ADDMULTISELECTOPTION = 'addMultiSelectOption'
    EDITFIELD = 'editField'
    REMOVEFIELD = 'removeField'
    EDITENUMOPTION = 'editEnumOption'
    REMOVEENUMOPTION = 'removeEnumOption'
    EDITMULTISELECTOPTION = 'editMultiSelectOption'
    REMOVEMULTISELECTOPTION = 'removeMultiSelectOption'


class UpdateMetadataTemplateSchemaRequestBodyArg(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'field_key': 'fieldKey',
        'field_keys': 'fieldKeys',
        'enum_option_key': 'enumOptionKey',
        'enum_option_keys': 'enumOptionKeys',
        'multi_select_option_key': 'multiSelectOptionKey',
        'multi_select_option_keys': 'multiSelectOptionKeys',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'fieldKey': 'field_key',
        'fieldKeys': 'field_keys',
        'enumOptionKey': 'enum_option_key',
        'enumOptionKeys': 'enum_option_keys',
        'multiSelectOptionKey': 'multi_select_option_key',
        'multiSelectOptionKeys': 'multi_select_option_keys',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        op: UpdateMetadataTemplateSchemaRequestBodyArgOpField,
        data: Optional[Dict[str, str]] = None,
        field_key: Optional[str] = None,
        field_keys: Optional[List[str]] = None,
        enum_option_key: Optional[str] = None,
        enum_option_keys: Optional[List[str]] = None,
        multi_select_option_key: Optional[str] = None,
        multi_select_option_keys: Optional[List[str]] = None,
        **kwargs
    ):
        """
        :param op: The type of change to perform on the template. Some
            of these are hazardous as they will change existing templates.
        :type op: UpdateMetadataTemplateSchemaRequestBodyArgOpField
        :param data: The data for the operation. This will vary depending on the
            operation being performed.
        :type data: Optional[Dict[str, str]], optional
        :param field_key: For operations that affect a single field this defines the key of
            the field that is affected.
        :type field_key: Optional[str], optional
        :param field_keys: For operations that affect multiple fields this defines the keys
            of the fields that are affected.
        :type field_keys: Optional[List[str]], optional
        :param enum_option_key: For operations that affect a single `enum` option this defines
            the key of the option that is affected.
        :type enum_option_key: Optional[str], optional
        :param enum_option_keys: For operations that affect multiple `enum` options this defines
            the keys of the options that are affected.
        :type enum_option_keys: Optional[List[str]], optional
        :param multi_select_option_key: For operations that affect a single multi select option this
            defines the key of the option that is affected.
        :type multi_select_option_key: Optional[str], optional
        :param multi_select_option_keys: For operations that affect multiple multi select options this
            defines the keys of the options that are affected.
        :type multi_select_option_keys: Optional[List[str]], optional
        """
        super().__init__(**kwargs)
        self.op = op
        self.data = data
        self.field_key = field_key
        self.field_keys = field_keys
        self.enum_option_key = enum_option_key
        self.enum_option_keys = enum_option_keys
        self.multi_select_option_key = multi_select_option_key
        self.multi_select_option_keys = multi_select_option_keys


class DeleteMetadataTemplateSchemaScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'


class CreateMetadataTemplateSchemaFieldsArgTypeField(str, Enum):
    STRING = 'string'
    FLOAT = 'float'
    DATE = 'date'
    ENUM = 'enum'
    MULTISELECT = 'multiSelect'


class CreateMetadataTemplateSchemaFieldsArgOptionsField(BaseObject):
    def __init__(self, key: str, **kwargs):
        """
        :param key: The text value of the option. This represents both the display name of the
            option and the internal key used when updating templates.
        :type key: str
        """
        super().__init__(**kwargs)
        self.key = key


class CreateMetadataTemplateSchemaFieldsArg(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'display_name': 'displayName',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'displayName': 'display_name',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        type: CreateMetadataTemplateSchemaFieldsArgTypeField,
        key: str,
        display_name: str,
        description: Optional[str] = None,
        hidden: Optional[bool] = None,
        options: Optional[
            List[CreateMetadataTemplateSchemaFieldsArgOptionsField]
        ] = None,
        **kwargs
    ):
        """
        :param type: The type of field. The basic fields are a `string` field for text, a
            `float` field for numbers, and a `date` fields to present the user with a
            date-time picker.
            Additionally, metadata templates support an `enum` field for a basic list
            of items, and ` multiSelect` field for a similar list of items where the
            user can select more than one value.
        :type type: CreateMetadataTemplateSchemaFieldsArgTypeField
        :param key: A unique identifier for the field. The identifier must
            be unique within the template to which it belongs.
        :type key: str
        :param display_name: The display name of the field as it is shown to the user in the web and
            mobile apps.
        :type display_name: str
        :param description: A description of the field. This is not shown to the user.
        :type description: Optional[str], optional
        :param hidden: Whether this field is hidden in the UI for the user and can only be set
            through the API instead.
        :type hidden: Optional[bool], optional
        :param options: A list of options for this field. This is used in combination with the
            `enum` and `multiSelect` field types.
        :type options: Optional[List[CreateMetadataTemplateSchemaFieldsArgOptionsField]], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.key = key
        self.display_name = display_name
        self.description = description
        self.hidden = hidden
        self.options = options


class MetadataTemplatesManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_metadata_templates(
        self,
        metadata_instance_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> MetadataTemplates:
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
        query_params_map: Dict[str, str] = prepare_params(
            {'metadata_instance_id': to_string(metadata_instance_id)}
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/metadata_templates']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, MetadataTemplates)

    def get_metadata_template_schema(
        self,
        scope: GetMetadataTemplateSchemaScopeArg,
        template_key: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> MetadataTemplate:
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
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://api.box.com/2.0/metadata_templates/',
                    to_string(scope),
                    '/',
                    to_string(template_key),
                    '/schema',
                ]
            ),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, MetadataTemplate)

    def update_metadata_template_schema(
        self,
        scope: UpdateMetadataTemplateSchemaScopeArg,
        template_key: str,
        request_body: List[UpdateMetadataTemplateSchemaRequestBodyArg],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> MetadataTemplate:
        """
        Updates a metadata template.

        The metadata template can only be updated if the template


        already exists.


        The update is applied atomically. If any errors occur during the


        application of the operations, the metadata template will not be changed.

        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: UpdateMetadataTemplateSchemaScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        :param request_body: Request body of updateMetadataTemplateSchema method
        :type request_body: List[UpdateMetadataTemplateSchemaRequestBodyArg]
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://api.box.com/2.0/metadata_templates/',
                    to_string(scope),
                    '/',
                    to_string(template_key),
                    '/schema',
                ]
            ),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json-patch+json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, MetadataTemplate)

    def delete_metadata_template_schema(
        self,
        scope: DeleteMetadataTemplateSchemaScopeArg,
        template_key: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
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
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://api.box.com/2.0/metadata_templates/',
                    to_string(scope),
                    '/',
                    to_string(template_key),
                    '/schema',
                ]
            ),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def get_metadata_template_by_id(
        self, template_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> MetadataTemplate:
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
        response: FetchResponse = fetch(
            ''.join(
                ['https://api.box.com/2.0/metadata_templates/', to_string(template_id)]
            ),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, MetadataTemplate)

    def get_metadata_template_global(
        self,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> MetadataTemplates:
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
        query_params_map: Dict[str, str] = prepare_params(
            {'marker': to_string(marker), 'limit': to_string(limit)}
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/metadata_templates/global']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, MetadataTemplates)

    def get_metadata_template_enterprise(
        self,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> MetadataTemplates:
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
        query_params_map: Dict[str, str] = prepare_params(
            {'marker': to_string(marker), 'limit': to_string(limit)}
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/metadata_templates/enterprise']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, MetadataTemplates)

    def create_metadata_template_schema(
        self,
        scope: str,
        display_name: str,
        template_key: Optional[str] = None,
        hidden: Optional[bool] = None,
        fields: Optional[List[CreateMetadataTemplateSchemaFieldsArg]] = None,
        copy_instance_on_item_copy: Optional[bool] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> MetadataTemplate:
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
        :type fields: Optional[List[CreateMetadataTemplateSchemaFieldsArg]], optional
        :param copy_instance_on_item_copy: Whether or not to copy any metadata attached to a file or folder
            when it is copied. By default, metadata is not copied along with a
            file or folder when it is copied.
        :type copy_instance_on_item_copy: Optional[bool], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = BaseObject(
            scope=scope,
            templateKey=template_key,
            displayName=display_name,
            hidden=hidden,
            fields=fields,
            copyInstanceOnItemCopy=copy_instance_on_item_copy,
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/metadata_templates/schema']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, MetadataTemplate)
