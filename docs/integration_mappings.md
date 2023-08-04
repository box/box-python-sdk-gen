<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [IntegrationMappingsManager](#integrationmappingsmanager)
  - [List Slack integration mappings](#list-slack-integration-mappings)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Create Slack integration mapping](#create-slack-integration-mapping)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Update Slack integration mapping](#update-slack-integration-mapping)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Delete Slack integration mapping](#delete-slack-integration-mapping)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# IntegrationMappingsManager

## List Slack integration mappings

Lists [Slack integration mappings](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack) in a users&#x27; enterprise.

You need Admin or Co-Admin role to
use this endpoint.

This operation is performed by calling function `get_integration_mapping_slack`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-integration-mappings-slack/).

*Currently we don't have an example for calling `get_integration_mapping_slack` in integration tests*

### Arguments

- query_params `GetIntegrationMappingSlackQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `IntegrationMappings`.

Returns a collection of integration mappings


## Create Slack integration mapping

Creates a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack)
by mapping a Slack channel to a Box item.

You need Admin or Co-Admin role to
use this endpoint.

This operation is performed by calling function `create_integration_mapping_slack`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-integration-mappings-slack/).

*Currently we don't have an example for calling `create_integration_mapping_slack` in integration tests*

### Arguments

- request_body `IntegrationMappingSlackCreateRequest`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `IntegrationMapping`.

Returns the created integration mapping.


## Update Slack integration mapping

Updates a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack).
Supports updating the Box folder ID and options.

You need Admin or Co-Admin role to
use this endpoint.

This operation is performed by calling function `update_integration_mapping_slack_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-integration-mappings-slack-id/).

*Currently we don't have an example for calling `update_integration_mapping_slack_by_id` in integration tests*

### Arguments

- integration_mapping_id `str`
  - An ID of an integration mapping
  - Used as `integration_mapping_id` in path `path` of the API call
- request_body `UpdateIntegrationMappingSlackByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `IntegrationMapping`.

Returns the updated integration mapping object.


## Delete Slack integration mapping

Deletes a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack).


You need Admin or Co-Admin role to
use this endpoint.

This operation is performed by calling function `delete_integration_mapping_slack_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-integration-mappings-slack-id/).

*Currently we don't have an example for calling `delete_integration_mapping_slack_by_id` in integration tests*

### Arguments

- integration_mapping_id `str`
  - An ID of an integration mapping
  - Used as `integration_mapping_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Empty body in response


