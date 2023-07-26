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

- query_params `Optional[GetMetadataTemplateGlobalQueryParamsArg]`
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

- query_params `Optional[GetMetadataTemplateEnterpriseQueryParamsArg]`
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


