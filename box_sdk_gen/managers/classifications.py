from enum import Enum

from typing import Optional

from typing import Dict

import json

from typing import List

from typing import Union

from box_sdk_gen.base_object import BaseObject

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

class CreateMetadataTemplateSchemaClassificationScopeArg(str, Enum):
    ENTERPRISE = 'enterprise'

class CreateMetadataTemplateSchemaClassificationTemplateKeyArg(str, Enum):
    SECURITYCLASSIFICATION_6VMVOCHWUWO = 'securityClassification-6VMVochwUWo'

class CreateMetadataTemplateSchemaClassificationDisplayNameArg(str, Enum):
    CLASSIFICATION = 'Classification'

class ClassificationsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_metadata_template_enterprise_security_classification_schema(self, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> ClassificationTemplate:
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema']), FetchOptions(method='GET', headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return ClassificationTemplate.from_dict(json.loads(response.text))
    def delete_metadata_template_enterprise_security_classification_schema(self, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> None:
        """
        Delete all classifications by deleting the classification
        
        metadata template.

        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema']), FetchOptions(method='DELETE', headers=headers_map, response_format=None, auth=self.auth, network_session=self.network_session))
        return None
    def create_metadata_template_schema_classification(self, scope: CreateMetadataTemplateSchemaClassificationScopeArg, display_name: CreateMetadataTemplateSchemaClassificationDisplayNameArg, template_key: Optional[CreateMetadataTemplateSchemaClassificationTemplateKeyArg] = None, hidden: Optional[bool] = None, copy_instance_on_item_copy: Optional[bool] = None, fields: Optional[List] = None, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> ClassificationTemplate:
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
        :param display_name: `Classification`
        :type display_name: CreateMetadataTemplateSchemaClassificationDisplayNameArg
        :param template_key: `securityClassification-6VMVochwUWo`
        :type template_key: Optional[CreateMetadataTemplateSchemaClassificationTemplateKeyArg], optional
        :param hidden: `false`
        :type hidden: Optional[bool], optional
        :param copy_instance_on_item_copy: `false`
        :type copy_instance_on_item_copy: Optional[bool], optional
        :param fields: The classification template holds one field, which holds
            all the valid classification values.
        :type fields: Optional[List], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: BaseObject = BaseObject(scope=scope, template_key=template_key, display_name=display_name, hidden=hidden, copy_instance_on_item_copy=copy_instance_on_item_copy, fields=fields)
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/schema#classifications']), FetchOptions(method='POST', headers=headers_map, body=json.dumps(request_body.to_dict()), content_type='application/json', response_format='json', auth=self.auth, network_session=self.network_session))
        return ClassificationTemplate.from_dict(json.loads(response.text))