from typing import Union

from base_object import BaseObject

from typing import List

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import ClassificationTemplate

from schemas import ClientError

class PostMetadataTemplatesSchemaClassificationsRequestBodyArgScopeField:
    pass

class PostMetadataTemplatesSchemaClassificationsRequestBodyArgTemplateKeyField:
    pass

class PostMetadataTemplatesSchemaClassificationsRequestBodyArgDisplayNameField:
    pass

class PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldTypeField:
    pass

class PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldKeyField:
    pass

class PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldDisplayNameField:
    pass

class PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldOptionsFieldStaticConfigFieldClassificationField(BaseObject):
    def __init__(self, classificationDefinition: Union[None, str] = None, colorID: Union[None, int] = None, **kwargs):
        """
        :param classificationDefinition: A longer description of the classification.
        :type classificationDefinition: Union[None, str], optional
        :param colorID: An identifier used to assign a color to
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
        :type colorID: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.classificationDefinition = classificationDefinition
        self.colorID = colorID

class PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldOptionsFieldStaticConfigField(BaseObject):
    def __init__(self, classification: Union[None, PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldOptionsFieldStaticConfigFieldClassificationField] = None, **kwargs):
        """
        :param classification: Additional information about the classification.
        :type classification: Union[None, PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldOptionsFieldStaticConfigFieldClassificationField], optional
        """
        super().__init__(**kwargs)
        self.classification = classification

class PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldOptionsField(BaseObject):
    def __init__(self, key: Union[None, str] = None, staticConfig: Union[None, PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldOptionsFieldStaticConfigField] = None, **kwargs):
        """
        :param key: The display name and key this classification. This
            will be show in the Box UI.
        :type key: Union[None, str], optional
        :param staticConfig: Additional information about the classification.
        :type staticConfig: Union[None, PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldOptionsFieldStaticConfigField], optional
        """
        super().__init__(**kwargs)
        self.key = key
        self.staticConfig = staticConfig

class PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsField(BaseObject):
    def __init__(self, type: Union[None, PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldTypeField] = None, key: Union[None, PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldKeyField] = None, displayName: Union[None, PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldDisplayNameField] = None, hidden: Union[None, bool] = None, options: Union[None, List[PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldOptionsField]] = None, **kwargs):
        """
        :param type: `enum`
        :type type: Union[None, PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldTypeField], optional
        :param key: `Box__Security__Classification__Key`
        :type key: Union[None, PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldKeyField], optional
        :param displayName: `Classification`
        :type displayName: Union[None, PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldDisplayNameField], optional
        :param hidden: `false`
        :type hidden: Union[None, bool], optional
        :param options: The actual list of classifications that are present on
            this template.
        :type options: Union[None, List[PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsFieldOptionsField]], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.key = key
        self.displayName = displayName
        self.hidden = hidden
        self.options = options

class PostMetadataTemplatesSchemaClassificationsRequestBodyArg(BaseObject):
    def __init__(self, scope: PostMetadataTemplatesSchemaClassificationsRequestBodyArgScopeField, displayName: PostMetadataTemplatesSchemaClassificationsRequestBodyArgDisplayNameField, templateKey: Union[None, PostMetadataTemplatesSchemaClassificationsRequestBodyArgTemplateKeyField] = None, hidden: Union[None, bool] = None, copyInstanceOnItemCopy: Union[None, bool] = None, fields: Union[None, List[PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsField]] = None, **kwargs):
        """
        :param scope: The scope in which to create the classifications. This should
            be `enterprise` or `enterprise_{id}` where `id` is the unique
            ID of the enterprise.
        :type scope: PostMetadataTemplatesSchemaClassificationsRequestBodyArgScopeField
        :param displayName: `Classification`
        :type displayName: PostMetadataTemplatesSchemaClassificationsRequestBodyArgDisplayNameField
        :param templateKey: `securityClassification-6VMVochwUWo`
        :type templateKey: Union[None, PostMetadataTemplatesSchemaClassificationsRequestBodyArgTemplateKeyField], optional
        :param hidden: `false`
        :type hidden: Union[None, bool], optional
        :param copyInstanceOnItemCopy: `false`
        :type copyInstanceOnItemCopy: Union[None, bool], optional
        :param fields: The classification template holds one field, which holds
            all the valid classification values.
        :type fields: Union[None, List[PostMetadataTemplatesSchemaClassificationsRequestBodyArgFieldsField]], optional
        """
        super().__init__(**kwargs)
        self.scope = scope
        self.displayName = displayName
        self.templateKey = templateKey
        self.hidden = hidden
        self.copyInstanceOnItemCopy = copyInstanceOnItemCopy
        self.fields = fields

class ClassificationsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getMetadataTemplatesEnterpriseSecurityClassification6VmVochwUWoSchema(self) -> ClassificationTemplate:
        """
        Retrieves the classification metadata template and lists all the
        
        classifications available to this enterprise.

        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema']), FetchOptions(method='GET', auth=self.auth))
        return ClassificationTemplate.from_dict(json.loads(response.text))
    def deleteMetadataTemplatesEnterpriseSecurityClassification6VmVochwUWoSchema(self):
        """
        Delete all classifications by deleting the classification
        
        metadata template.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def postMetadataTemplatesSchemaClassifications(self, requestBody: PostMetadataTemplatesSchemaClassificationsRequestBodyArg) -> ClassificationTemplate:
        """
        When an enterprise does not yet have any classifications, this API call
        
        initializes the classification template with an initial set of

        
        classifications.

        
        If an enterprise already has a classification, the template will already

        
        exist and instead an API call should be made to add additional

        
        classifications.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_templates/schema#classifications']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return ClassificationTemplate.from_dict(json.loads(response.text))