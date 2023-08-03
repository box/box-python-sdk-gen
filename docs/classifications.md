# ClassificationsManager


- [List all classifications](#list-all-classifications)
- [Delete all classifications](#delete-all-classifications)
- [Add initial classifications](#add-initial-classifications)

## List all classifications

Retrieves the classification metadata template and lists all the
classifications available to this enterprise.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

This operation is performed by calling function `get_metadata_template_enterprise_security_classification_schema`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-metadata-templates-enterprise-security-classification-6-vm-vochw-u-wo-schema/).

*Currently we don't have an example for calling `get_metadata_template_enterprise_security_classification_schema` in integration tests*

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

*Currently we don't have an example for calling `delete_metadata_template_enterprise_security_classification_schema` in integration tests*

### Arguments

- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `None`.

Returns an empty response when the metadata
template for classifications is successfully deleted.


## Add initial classifications

When an enterprise does not yet have any classifications, this API call
initializes the classification template with an initial set of
classifications.

If an enterprise already has a classification, the template will already
exist and instead an API call should be made to add additional
classifications.

This operation is performed by calling function `create_metadata_template_schema_classification`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-metadata-templates-schema-classifications/).

*Currently we don't have an example for calling `create_metadata_template_schema_classification` in integration tests*

### Arguments

- scope `CreateMetadataTemplateSchemaClassificationScopeArg`
  - The scope in which to create the classifications. This should be `enterprise` or `enterprise_{id}` where `id` is the unique ID of the enterprise.
- template_key `Optional[CreateMetadataTemplateSchemaClassificationTemplateKeyArg]`
  - `securityClassification-6VMVochwUWo`
- display_name `CreateMetadataTemplateSchemaClassificationDisplayNameArg`
  - `Classification`
- hidden `Optional[bool]`
  - `false`
- copy_instance_on_item_copy `Optional[bool]`
  - `false`
- fields `Optional[List]`
  - The classification template holds one field, which holds all the valid classification values.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `ClassificationTemplate`.

Returns a new `securityClassification` metadata template, which
contains a `Box__Security__Classification__Key` field that lists all
the classifications available to this enterprise.


