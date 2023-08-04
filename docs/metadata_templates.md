<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [MetadataTemplatesManager](#metadatatemplatesmanager)
  - [Find metadata template by instance ID](#find-metadata-template-by-instance-id)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Get metadata template by name](#get-metadata-template-by-name)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Remove metadata template](#remove-metadata-template)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Get metadata template by ID](#get-metadata-template-by-id)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)
  - [List all global metadata templates](#list-all-global-metadata-templates)
    - [Arguments](#arguments-4)
    - [Returns](#returns-4)
  - [List all metadata templates for enterprise](#list-all-metadata-templates-for-enterprise)
    - [Arguments](#arguments-5)
    - [Returns](#returns-5)
  - [Create metadata template](#create-metadata-template)
    - [Arguments](#arguments-6)
    - [Returns](#returns-6)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# MetadataTemplatesManager

## Find metadata template by instance ID

Finds a metadata template by searching for the ID of an instance of the
template.

This operation is performed by calling function `get_metadata_templates`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-metadata-templates/).

*Currently we don't have an example for calling `get_metadata_templates` in integration tests*

### Arguments

- query_params `GetMetadataTemplatesQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `MetadataTemplates`.

Returns a list containing the 1 metadata template that matches the
instance ID.


## Get metadata template by name

Retrieves a metadata template by its &#x60;scope&#x60; and &#x60;templateKey&#x60; values.

To find the &#x60;scope&#x60; and &#x60;templateKey&#x60; for a template, list all templates for
an enterprise or globally, or list all templates applied to a file or folder.

This operation is performed by calling function `get_metadata_template_schema`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-metadata-templates-id-id-schema/).

*Currently we don't have an example for calling `get_metadata_template_schema` in integration tests*

### Arguments

- scope `GetMetadataTemplateSchemaScopeArg`
  - The scope of the metadata template
  - Used as `scope` in path `path` of the API call
- template_key `str`
  - The name of the metadata template
  - Used as `template_key` in path `path` of the API call


### Returns

This function returns a value of type `MetadataTemplate`.

Returns the metadata template matching the &#x60;scope&#x60;
and &#x60;template&#x60; name.


## Remove metadata template

Delete a metadata template and its instances.
This deletion is permanent and can not be reversed.

This operation is performed by calling function `delete_metadata_template_schema`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-metadata-templates-id-id-schema/).

*Currently we don't have an example for calling `delete_metadata_template_schema` in integration tests*

### Arguments

- scope `DeleteMetadataTemplateSchemaScopeArg`
  - The scope of the metadata template
  - Used as `scope` in path `path` of the API call
- template_key `str`
  - The name of the metadata template
  - Used as `template_key` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Returns an empty response when the metadata
template is successfully deleted.


## Get metadata template by ID

Retrieves a metadata template by its ID.

This operation is performed by calling function `get_metadata_template_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-metadata-templates-id/).

*Currently we don't have an example for calling `get_metadata_template_by_id` in integration tests*

### Arguments

- template_id `str`
  - The ID of the template
  - Used as `template_id` in path `path` of the API call


### Returns

This function returns a value of type `MetadataTemplate`.

Returns the metadata template that matches the ID.


## List all global metadata templates

Used to retrieve all generic, global metadata templates available to all
enterprises using Box.

This operation is performed by calling function `get_metadata_template_global`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-metadata-templates-global/).

*Currently we don't have an example for calling `get_metadata_template_global` in integration tests*

### Arguments

- query_params `GetMetadataTemplateGlobalQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `MetadataTemplates`.

Returns all of the metadata templates available to all enterprises
and their corresponding schema.


## List all metadata templates for enterprise

Used to retrieve all metadata templates created to be used specifically within
the user&#x27;s enterprise

This operation is performed by calling function `get_metadata_template_enterprise`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-metadata-templates-enterprise/).

*Currently we don't have an example for calling `get_metadata_template_enterprise` in integration tests*

### Arguments

- query_params `GetMetadataTemplateEnterpriseQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `MetadataTemplates`.

Returns all of the metadata templates within an enterprise
and their corresponding schema.


## Create metadata template

Creates a new metadata template that can be applied to
files and folders.

This operation is performed by calling function `create_metadata_template_schema`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-metadata-templates-schema/).

*Currently we don't have an example for calling `create_metadata_template_schema` in integration tests*

### Arguments

- request_body `CreateMetadataTemplateSchemaRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `MetadataTemplate`.

The schema representing the metadata template created.


