from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.base_object import BaseObject

from typing import List

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import ClassificationTemplate

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json_data import SerializedData


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgOpField(
    str, Enum
):
    ADDENUMOPTION = 'addEnumOption'


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgFieldKeyField(
    str, Enum
):
    BOX__SECURITY__CLASSIFICATION__KEY = 'Box__Security__Classification__Key'


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgDataFieldStaticConfigFieldClassificationField(
    BaseObject
):
    _fields_to_json_mapping: Dict[str, str] = {
        'classification_definition': 'classificationDefinition',
        'color_id': 'colorID',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'classificationDefinition': 'classification_definition',
        'colorID': 'color_id',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        classification_definition: Optional[str] = None,
        color_id: Optional[int] = None,
        **kwargs
    ):
        """
        :param classification_definition: A longer description of the classification.
        :type classification_definition: Optional[str], optional
        :param color_id: An internal Box identifier used to assign a color to
            a classification label.
            Mapping between a `colorID` and a color may change
            without notice. Currently, the color mappings are as
            follows.
            * `0`: Yellow
            * `1`: Orange
            * `2`: Watermelon red
            * `3`: Purple rain
            * `4`: Light blue
            * `5`: Dark blue
            * `6`: Light green
            * `7`: Gray
        :type color_id: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.classification_definition = classification_definition
        self.color_id = color_id


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgDataFieldStaticConfigField(
    BaseObject
):
    def __init__(
        self,
        classification: Optional[
            UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgDataFieldStaticConfigFieldClassificationField
        ] = None,
        **kwargs
    ):
        """
        :param classification: Additional details for the classification.
        :type classification: Optional[UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgDataFieldStaticConfigFieldClassificationField], optional
        """
        super().__init__(**kwargs)
        self.classification = classification


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgDataField(
    BaseObject
):
    _fields_to_json_mapping: Dict[str, str] = {
        'static_config': 'staticConfig',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'staticConfig': 'static_config',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        key: str,
        static_config: Optional[
            UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgDataFieldStaticConfigField
        ] = None,
        **kwargs
    ):
        """
        :param key: The label of the classification as shown in the web and
            mobile interfaces. This is the only field required to
            add a classification.
        :type key: str
        :param static_config: A static configuration for the classification.
        :type static_config: Optional[UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgDataFieldStaticConfigField], optional
        """
        super().__init__(**kwargs)
        self.key = key
        self.static_config = static_config


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArg(
    BaseObject
):
    _fields_to_json_mapping: Dict[str, str] = {
        'field_key': 'fieldKey',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'fieldKey': 'field_key',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        op: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgOpField,
        field_key: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgFieldKeyField,
        data: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgDataField,
        **kwargs
    ):
        """
        :param op: The type of change to perform on the classification
            object.
        :type op: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgOpField
        :param field_key: Defines classifications
            available in the enterprise.
        :type field_key: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgFieldKeyField
        :param data: The details of the classification to add.
        :type data: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArgDataField
        """
        super().__init__(**kwargs)
        self.op = op
        self.field_key = field_key
        self.data = data


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgOpField(
    str, Enum
):
    EDITENUMOPTION = 'editEnumOption'


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgFieldKeyField(
    str, Enum
):
    BOX__SECURITY__CLASSIFICATION__KEY = 'Box__Security__Classification__Key'


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgDataFieldStaticConfigFieldClassificationField(
    BaseObject
):
    _fields_to_json_mapping: Dict[str, str] = {
        'classification_definition': 'classificationDefinition',
        'color_id': 'colorID',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'classificationDefinition': 'classification_definition',
        'colorID': 'color_id',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        classification_definition: Optional[str] = None,
        color_id: Optional[int] = None,
        **kwargs
    ):
        """
        :param classification_definition: A longer description of the classification.
        :type classification_definition: Optional[str], optional
        :param color_id: An internal Box identifier used to assign a color to
            a classification label.
            Mapping between a `colorID` and a color may change
            without notice. Currently, the color mappings are as
            follows.
            * `0`: Yellow
            * `1`: Orange
            * `2`: Watermelon red
            * `3`: Purple rain
            * `4`: Light blue
            * `5`: Dark blue
            * `6`: Light green
            * `7`: Gray
        :type color_id: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.classification_definition = classification_definition
        self.color_id = color_id


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgDataFieldStaticConfigField(
    BaseObject
):
    def __init__(
        self,
        classification: Optional[
            UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgDataFieldStaticConfigFieldClassificationField
        ] = None,
        **kwargs
    ):
        """
        :param classification: Additional details for the classification.
        :type classification: Optional[UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgDataFieldStaticConfigFieldClassificationField], optional
        """
        super().__init__(**kwargs)
        self.classification = classification


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgDataField(
    BaseObject
):
    _fields_to_json_mapping: Dict[str, str] = {
        'static_config': 'staticConfig',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'staticConfig': 'static_config',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        key: str,
        static_config: Optional[
            UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgDataFieldStaticConfigField
        ] = None,
        **kwargs
    ):
        """
        :param key: A new label for the classification, as it will be
            shown in the web and mobile interfaces.
        :type key: str
        :param static_config: A static configuration for the classification.
        :type static_config: Optional[UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgDataFieldStaticConfigField], optional
        """
        super().__init__(**kwargs)
        self.key = key
        self.static_config = static_config


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArg(
    BaseObject
):
    _fields_to_json_mapping: Dict[str, str] = {
        'field_key': 'fieldKey',
        'enum_option_key': 'enumOptionKey',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'fieldKey': 'field_key',
        'enumOptionKey': 'enum_option_key',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        op: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgOpField,
        field_key: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgFieldKeyField,
        enum_option_key: str,
        data: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgDataField,
        **kwargs
    ):
        """
        :param op: The type of change to perform on the classification
            object.
        :type op: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgOpField
        :param field_key: Defines classifications
            available in the enterprise.
        :type field_key: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgFieldKeyField
        :param enum_option_key: The original label of the classification to change.
        :type enum_option_key: str
        :param data: The details of the updated classification.
        :type data: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArgDataField
        """
        super().__init__(**kwargs)
        self.op = op
        self.field_key = field_key
        self.enum_option_key = enum_option_key
        self.data = data


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaDeleteRequestBodyArgOpField(
    str, Enum
):
    REMOVEENUMOPTION = 'removeEnumOption'


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaDeleteRequestBodyArgFieldKeyField(
    str, Enum
):
    BOX__SECURITY__CLASSIFICATION__KEY = 'Box__Security__Classification__Key'


class UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaDeleteRequestBodyArg(
    BaseObject
):
    _fields_to_json_mapping: Dict[str, str] = {
        'field_key': 'fieldKey',
        'enum_option_key': 'enumOptionKey',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'fieldKey': 'field_key',
        'enumOptionKey': 'enum_option_key',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        op: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaDeleteRequestBodyArgOpField,
        field_key: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaDeleteRequestBodyArgFieldKeyField,
        enum_option_key: str,
        **kwargs
    ):
        """
        :param op: The type of change to perform on the classification
            object.
        :type op: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaDeleteRequestBodyArgOpField
        :param field_key: Defines classifications
            available in the enterprise.
        :type field_key: UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaDeleteRequestBodyArgFieldKeyField
        :param enum_option_key: The label of the classification to remove.
        :type enum_option_key: str
        """
        super().__init__(**kwargs)
        self.op = op
        self.field_key = field_key
        self.enum_option_key = enum_option_key


class CreateMetadataTemplateSchemaClassificationScopeArg(str, Enum):
    ENTERPRISE = 'enterprise'


class CreateMetadataTemplateSchemaClassificationTemplateKeyArg(str, Enum):
    SECURITYCLASSIFICATION_6VMVOCHWUWO = 'securityClassification-6VMVochwUWo'


class CreateMetadataTemplateSchemaClassificationDisplayNameArg(str, Enum):
    CLASSIFICATION = 'Classification'


class CreateMetadataTemplateSchemaClassificationFieldsArgTypeField(str, Enum):
    ENUM = 'enum'


class CreateMetadataTemplateSchemaClassificationFieldsArgKeyField(str, Enum):
    BOX__SECURITY__CLASSIFICATION__KEY = 'Box__Security__Classification__Key'


class CreateMetadataTemplateSchemaClassificationFieldsArgDisplayNameField(str, Enum):
    CLASSIFICATION = 'Classification'


class CreateMetadataTemplateSchemaClassificationFieldsArgOptionsFieldStaticConfigFieldClassificationField(
    BaseObject
):
    _fields_to_json_mapping: Dict[str, str] = {
        'classification_definition': 'classificationDefinition',
        'color_id': 'colorID',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'classificationDefinition': 'classification_definition',
        'colorID': 'color_id',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        classification_definition: Optional[str] = None,
        color_id: Optional[int] = None,
        **kwargs
    ):
        """
        :param classification_definition: A longer description of the classification.
        :type classification_definition: Optional[str], optional
        :param color_id: An identifier used to assign a color to
            a classification label.
            Mapping between a `colorID` and a color may
            change without notice. Currently, the color
            mappings are as follows.
            * `0`: Yellow
            * `1`: Orange
            * `2`: Watermelon red
            * `3`: Purple rain
            * `4`: Light blue
            * `5`: Dark blue
            * `6`: Light green
            * `7`: Gray
        :type color_id: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.classification_definition = classification_definition
        self.color_id = color_id


class CreateMetadataTemplateSchemaClassificationFieldsArgOptionsFieldStaticConfigField(
    BaseObject
):
    def __init__(
        self,
        classification: Optional[
            CreateMetadataTemplateSchemaClassificationFieldsArgOptionsFieldStaticConfigFieldClassificationField
        ] = None,
        **kwargs
    ):
        """
        :param classification: Additional information about the classification.
        :type classification: Optional[CreateMetadataTemplateSchemaClassificationFieldsArgOptionsFieldStaticConfigFieldClassificationField], optional
        """
        super().__init__(**kwargs)
        self.classification = classification


class CreateMetadataTemplateSchemaClassificationFieldsArgOptionsField(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'static_config': 'staticConfig',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'staticConfig': 'static_config',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        key: str,
        static_config: Optional[
            CreateMetadataTemplateSchemaClassificationFieldsArgOptionsFieldStaticConfigField
        ] = None,
        **kwargs
    ):
        """
        :param key: The display name and key this classification. This
            will be show in the Box UI.
        :type key: str
        :param static_config: Additional information about the classification.
        :type static_config: Optional[CreateMetadataTemplateSchemaClassificationFieldsArgOptionsFieldStaticConfigField], optional
        """
        super().__init__(**kwargs)
        self.key = key
        self.static_config = static_config


class CreateMetadataTemplateSchemaClassificationFieldsArg(BaseObject):
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
        type: CreateMetadataTemplateSchemaClassificationFieldsArgTypeField,
        key: CreateMetadataTemplateSchemaClassificationFieldsArgKeyField,
        display_name: CreateMetadataTemplateSchemaClassificationFieldsArgDisplayNameField,
        options: List[CreateMetadataTemplateSchemaClassificationFieldsArgOptionsField],
        hidden: Optional[bool] = None,
        **kwargs
    ):
        """
        :param type: The type of the field
            that is always enum.
        :type type: CreateMetadataTemplateSchemaClassificationFieldsArgTypeField
        :param key: Defines classifications
            available in the enterprise.
        :type key: CreateMetadataTemplateSchemaClassificationFieldsArgKeyField
        :param display_name: A display name for the classification.
        :type display_name: CreateMetadataTemplateSchemaClassificationFieldsArgDisplayNameField
        :param options: The actual list of classifications that are present on
            this template.
        :type options: List[CreateMetadataTemplateSchemaClassificationFieldsArgOptionsField]
        :param hidden: Determines if the classification
            template is
            hidden or available on
            web and mobile
            devices.
        :type hidden: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.key = key
        self.display_name = display_name
        self.options = options
        self.hidden = hidden


class ClassificationsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_metadata_template_enterprise_security_classification_schema(
        self, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> ClassificationTemplate:
        """
        Retrieves the classification metadata template and lists all the

        classifications available to this enterprise.


        This API can also be called by including the enterprise ID in the


        URL explicitly, for example


        `/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema'
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, ClassificationTemplate)

    def delete_metadata_template_enterprise_security_classification_schema(
        self, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> None:
        """
        Delete all classifications by deleting the classification

        metadata template.

        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema'
            ]),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def update_metadata_template_enterprise_security_classification_schema_add(
        self,
        request_body: List[
            UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArg
        ],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ClassificationTemplate:
        """
        Adds one or more new classifications to the list of classifications

        available to the enterprise.


        This API can also be called by including the enterprise ID in the


        URL explicitly, for example


        `/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

        :param request_body: Request body of updateMetadataTemplateEnterpriseSecurityClassificationSchemaAdd method
        :type request_body: List[UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaAddRequestBodyArg]
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema#add'
            ]),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, ClassificationTemplate)

    def update_metadata_template_enterprise_security_classification_schema_update(
        self,
        request_body: List[
            UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArg
        ],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ClassificationTemplate:
        """
        Updates the labels and descriptions of one or more classifications

        available to the enterprise.


        This API can also be called by including the enterprise ID in the


        URL explicitly, for example


        `/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

        :param request_body: Request body of updateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdate method
        :type request_body: List[UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaUpdateRequestBodyArg]
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema#update'
            ]),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json-patch+json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, ClassificationTemplate)

    def update_metadata_template_enterprise_security_classification_schema_delete(
        self,
        request_body: List[
            UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaDeleteRequestBodyArg
        ],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ClassificationTemplate:
        """
        Removes a classification from the list of classifications

        available to the enterprise.


        This API can also be called by including the enterprise ID in the


        URL explicitly, for example


        `/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

        :param request_body: Request body of updateMetadataTemplateEnterpriseSecurityClassificationSchemaDelete method
        :type request_body: List[UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaDeleteRequestBodyArg]
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema#delete'
            ]),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json-patch+json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, ClassificationTemplate)

    def create_metadata_template_schema_classification(
        self,
        scope: CreateMetadataTemplateSchemaClassificationScopeArg,
        template_key: CreateMetadataTemplateSchemaClassificationTemplateKeyArg,
        display_name: CreateMetadataTemplateSchemaClassificationDisplayNameArg,
        fields: List[CreateMetadataTemplateSchemaClassificationFieldsArg],
        hidden: Optional[bool] = None,
        copy_instance_on_item_copy: Optional[bool] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ClassificationTemplate:
        """
        When an enterprise does not yet have any classifications, this API call

        initializes the classification template with an initial set of


        classifications.


        If an enterprise already has a classification, the template will already


        exist and instead an API call should be made to add additional


        classifications.

        :param scope: The scope in which to create the classifications. This should
            be `enterprise` or `enterprise_{id}` where `id` is the unique
            ID of the enterprise.
        :type scope: CreateMetadataTemplateSchemaClassificationScopeArg
        :param template_key: Defines the list of metadata templates.
        :type template_key: CreateMetadataTemplateSchemaClassificationTemplateKeyArg
        :param display_name: The name of the
            template as shown in web and mobile interfaces.
        :type display_name: CreateMetadataTemplateSchemaClassificationDisplayNameArg
        :param fields: The classification template requires exactly
            one field, which holds
            all the valid classification values.
        :type fields: List[CreateMetadataTemplateSchemaClassificationFieldsArg]
        :param hidden: Determines if the classification template is
            hidden or available on web and mobile
            devices.
        :type hidden: Optional[bool], optional
        :param copy_instance_on_item_copy: Determines if classifications are
            copied along when the file or folder is
            copied.
        :type copy_instance_on_item_copy: Optional[bool], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'scope': scope,
            'templateKey': template_key,
            'displayName': display_name,
            'hidden': hidden,
            'copyInstanceOnItemCopy': copy_instance_on_item_copy,
            'fields': fields,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/metadata_templates/schema#classifications'
            ]),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, ClassificationTemplate)
