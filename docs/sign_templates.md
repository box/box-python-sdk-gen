<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [SignTemplatesManager](#signtemplatesmanager)
  - [List Box Sign templates](#list-box-sign-templates)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Get Box Sign template by ID](#get-box-sign-template-by-id)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

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


