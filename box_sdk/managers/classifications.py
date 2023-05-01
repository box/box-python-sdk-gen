from enum import Enum

from typing import Optional

from box_sdk.base_object import BaseObject

from typing import List

from typing import Union

import json

from box_sdk.schemas import ClassificationTemplate

from box_sdk.schemas import ClientError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateMetadataTemplateSchemaClassificationRequestBodyArgScopeField(str, Enum):
    ENTERPRISE = 'enterprise'

class CreateMetadataTemplateSchemaClassificationRequestBodyArgTemplateKeyField(str, Enum):
    SECURITYCLASSIFICATION_6VMVOCHWUWO = 'securityClassification-6VMVochwUWo'

class CreateMetadataTemplateSchemaClassificationRequestBodyArgDisplayNameField(str, Enum):
    CLASSIFICATION = 'Classification'

class CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldTypeField(str, Enum):
    ENUM = 'enum'

class CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldKeyField(str, Enum):
    BOX__SECURITY__CLASSIFICATION__KEY = 'Box__Security__Classification__Key'

class CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldDisplayNameField(str, Enum):
    CLASSIFICATION = 'Classification'

class CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldOptionsFieldStaticConfigFieldClassificationField(BaseObject):
    def __init__(self, classification_definition: Optional[str] = None, color_id: Optional[int] = None, **kwargs):
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

class CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldOptionsFieldStaticConfigField(BaseObject):
    def __init__(self, classification: Optional[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldOptionsFieldStaticConfigFieldClassificationField] = None, **kwargs):
        """
        :param classification: Additional information about the classification.
        :type classification: Optional[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldOptionsFieldStaticConfigFieldClassificationField], optional
        """
        super().__init__(**kwargs)
        self.classification = classification

class CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldOptionsField(BaseObject):
    def __init__(self, key: Optional[str] = None, static_config: Optional[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldOptionsFieldStaticConfigField] = None, **kwargs):
        """
        :param key: The display name and key this classification. This
            will be show in the Box UI.
        :type key: Optional[str], optional
        :param static_config: Additional information about the classification.
        :type static_config: Optional[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldOptionsFieldStaticConfigField], optional
        """
        super().__init__(**kwargs)
        self.key = key
        self.static_config = static_config

class CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsField(BaseObject):
    def __init__(self, type: Optional[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldTypeField] = None, key: Optional[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldKeyField] = None, display_name: Optional[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldDisplayNameField] = None, hidden: Optional[bool] = None, options: Optional[List[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldOptionsField]] = None, **kwargs):
        """
        :param type: `enum`
        :type type: Optional[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldTypeField], optional
        :param key: `Box__Security__Classification__Key`
        :type key: Optional[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldKeyField], optional
        :param display_name: `Classification`
        :type display_name: Optional[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldDisplayNameField], optional
        :param hidden: `false`
        :type hidden: Optional[bool], optional
        :param options: The actual list of classifications that are present on
            this template.
        :type options: Optional[List[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsFieldOptionsField]], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.key = key
        self.display_name = display_name
        self.hidden = hidden
        self.options = options

class CreateMetadataTemplateSchemaClassificationRequestBodyArg(BaseObject):
    def __init__(self, scope: CreateMetadataTemplateSchemaClassificationRequestBodyArgScopeField, display_name: CreateMetadataTemplateSchemaClassificationRequestBodyArgDisplayNameField, template_key: Optional[CreateMetadataTemplateSchemaClassificationRequestBodyArgTemplateKeyField] = None, hidden: Optional[bool] = None, copy_instance_on_item_copy: Optional[bool] = None, fields: Optional[List[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsField]] = None, **kwargs):
        """
        :param scope: The scope in which to create the classifications. This should
            be `enterprise` or `enterprise_{id}` where `id` is the unique
            ID of the enterprise.
        :type scope: CreateMetadataTemplateSchemaClassificationRequestBodyArgScopeField
        :param display_name: `Classification`
        :type display_name: CreateMetadataTemplateSchemaClassificationRequestBodyArgDisplayNameField
        :param template_key: `securityClassification-6VMVochwUWo`
        :type template_key: Optional[CreateMetadataTemplateSchemaClassificationRequestBodyArgTemplateKeyField], optional
        :param hidden: `false`
        :type hidden: Optional[bool], optional
        :param copy_instance_on_item_copy: `false`
        :type copy_instance_on_item_copy: Optional[bool], optional
        :param fields: The classification template holds one field, which holds
            all the valid classification values.
        :type fields: Optional[List[CreateMetadataTemplateSchemaClassificationRequestBodyArgFieldsField]], optional
        """
        super().__init__(**kwargs)
        self.scope = scope
        self.display_name = display_name
        self.template_key = template_key
        self.hidden = hidden
        self.copy_instance_on_item_copy = copy_instance_on_item_copy
        self.fields = fields

class ClassificationsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_metadata_template_enterprise_security_classification_schema(self) -> ClassificationTemplate:
        """
        Retrieves the classification metadata template and lists all the
        
        classifications available to this enterprise.

        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema']), FetchOptions(method='GET', auth=self.auth))
        return ClassificationTemplate.from_dict(json.loads(response.text))
    def delete_metadata_template_enterprise_security_classification_schema(self):
        """
        Delete all classifications by deleting the classification
        
        metadata template.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def create_metadata_template_schema_classification(self, request_body: CreateMetadataTemplateSchemaClassificationRequestBodyArg) -> ClassificationTemplate:
        """
        When an enterprise does not yet have any classifications, this API call
        
        initializes the classification template with an initial set of

        
        classifications.

        
        If an enterprise already has a classification, the template will already

        
        exist and instead an API call should be made to add additional

        
        classifications.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/schema#classifications']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return ClassificationTemplate.from_dict(json.loads(response.text))