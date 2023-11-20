# ClassificationsManager

- [List all classifications](#list-all-classifications)
- [Delete all classifications](#delete-all-classifications)
- [Add classification](#add-classification)
- [Update classification](#update-classification)
- [Delete classification](#delete-classification)
- [Add initial classifications](#add-initial-classifications)

## List all classifications

Retrieves the classification metadata template and lists all the
classifications available to this enterprise.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

This operation is performed by calling function `get_classification_template`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-metadata-templates-enterprise-security-classification-6-vm-vochw-u-wo-schema/).

<!-- sample get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema -->

```python
client.classifications.get_classification_template()
```

### Arguments

- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `ClassificationTemplate`.

Returns the `securityClassification` metadata template, which contains
a `Box__Security__Classification__Key` field that lists all the
classifications available to this enterprise.

## Delete all classifications

Delete all classifications by deleting the classification
metadata template.

This operation is performed by calling function `delete_metadata_template_enterprise_security_classification_schema`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-metadata-templates-enterprise-security-classification-6-vm-vochw-u-wo-schema/).

_Currently we don't have an example for calling `delete_metadata_template_enterprise_security_classification_schema` in integration tests_

### Arguments

- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `None`.

Returns an empty response when the metadata
template for classifications is successfully deleted.

## Add classification

Adds one or more new classifications to the list of classifications
available to the enterprise.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

This operation is performed by calling function `add_classification`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-metadata-templates-enterprise-security-classification-6-vm-vochw-u-wo-schema-add/).

<!-- sample put_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema#add -->

```python
client.classifications.add_classification(request_body=[AddClassificationRequestBodyArg(op=AddClassificationRequestBodyArgOpField.ADDENUMOPTION.value, field_key=AddClassificationRequestBodyArgFieldKeyField.BOX__SECURITY__CLASSIFICATION__KEY.value, data=AddClassificationRequestBodyArgDataField(key=get_uuid(), static_config=AddClassificationRequestBodyArgDataFieldStaticConfigField(classification=AddClassificationRequestBodyArgDataFieldStaticConfigFieldClassificationField(color_id=3, classification_definition='Some description'))))])
```

### Arguments

- request_body `List[AddClassificationRequestBodyArg]`
  - Request body of addClassification method
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `ClassificationTemplate`.

Returns the updated `securityClassification` metadata template, which
contains a `Box__Security__Classification__Key` field that lists all
the classifications available to this enterprise.

## Update classification

Updates the labels and descriptions of one or more classifications
available to the enterprise.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

This operation is performed by calling function `update_classification`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-metadata-templates-enterprise-security-classification-6-vm-vochw-u-wo-schema-update/).

<!-- sample put_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema#update -->

```python
client.classifications.update_classification(request_body=[UpdateClassificationRequestBodyArg(op=UpdateClassificationRequestBodyArgOpField.EDITENUMOPTION.value, field_key=UpdateClassificationRequestBodyArgFieldKeyField.BOX__SECURITY__CLASSIFICATION__KEY.value, enum_option_key=classification.key, data=UpdateClassificationRequestBodyArgDataField(key=updated_classification_name, static_config=UpdateClassificationRequestBodyArgDataFieldStaticConfigField(classification=UpdateClassificationRequestBodyArgDataFieldStaticConfigFieldClassificationField(color_id=2, classification_definition=updated_classification_description))))])
```

### Arguments

- request_body `List[UpdateClassificationRequestBodyArg]`
  - Request body of updateClassification method
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `ClassificationTemplate`.

Returns the updated `securityClassification` metadata template, which
contains a `Box__Security__Classification__Key` field that lists all
the classifications available to this enterprise.

## Delete classification

Removes a classification from the list of classifications
available to the enterprise.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

This operation is performed by calling function `update_metadata_template_enterprise_security_classification_schema_delete`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-metadata-templates-enterprise-security-classification-6-vm-vochw-u-wo-schema-delete/).

_Currently we don't have an example for calling `update_metadata_template_enterprise_security_classification_schema_delete` in integration tests_

### Arguments

- request_body `List[UpdateMetadataTemplateEnterpriseSecurityClassificationSchemaDeleteRequestBodyArg]`
  - Request body of updateMetadataTemplateEnterpriseSecurityClassificationSchemaDelete method
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `ClassificationTemplate`.

Returns the updated `securityClassification` metadata template, which
contains a `Box__Security__Classification__Key` field that lists all
the classifications available to this enterprise.

## Add initial classifications

When an enterprise does not yet have any classifications, this API call
initializes the classification template with an initial set of
classifications.

If an enterprise already has a classification, the template will already
exist and instead an API call should be made to add additional
classifications.

This operation is performed by calling function `create_classification_template`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-metadata-templates-schema-classifications/).

_Currently we don't have an example for calling `create_classification_template` in integration tests_

### Arguments

- scope `CreateClassificationTemplateScopeArg`
  - The scope in which to create the classifications. This should be `enterprise` or `enterprise_{id}` where `id` is the unique ID of the enterprise.
- template_key `CreateClassificationTemplateTemplateKeyArg`
  - Defines the list of metadata templates.
- display_name `CreateClassificationTemplateDisplayNameArg`
  - The name of the template as shown in web and mobile interfaces.
- hidden `Optional[bool]`
  - Determines if the classification template is hidden or available on web and mobile devices.
- copy_instance_on_item_copy `Optional[bool]`
  - Determines if classifications are copied along when the file or folder is copied.
- fields `List[CreateClassificationTemplateFieldsArg]`
  - The classification template requires exactly one field, which holds all the valid classification values.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `ClassificationTemplate`.

Returns a new `securityClassification` metadata template, which
contains a `Box__Security__Classification__Key` field that lists all
the classifications available to this enterprise.
