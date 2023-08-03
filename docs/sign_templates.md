# SignTemplatesManager

## List Box Sign templates

Gets Box Sign templates created by a user.

This operation is performed by calling function `get_sign_templates`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-sign-templates/).

*Currently we don't have an example for calling `get_sign_templates` in integration tests*

### Arguments

- query_params `GetSignTemplatesQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `SignTemplates`.

Returns a collection of templates.


## Get Box Sign template by ID

Fetches details of a specific Box Sign template.

This operation is performed by calling function `get_sign_template_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-sign-templates-id/).

*Currently we don't have an example for calling `get_sign_template_by_id` in integration tests*

### Arguments

- template_id `str`
  - The ID of a Box Sign template.
  - Used as `template_id` in path `path` of the API call


### Returns

This function returns a value of type `SignTemplate`.

Returns details of a template.


