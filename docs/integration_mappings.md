# IntegrationMappingsManager

- [List Slack integration mappings](#list-slack-integration-mappings)
- [Create Slack integration mapping](#create-slack-integration-mapping)
- [Update Slack integration mapping](#update-slack-integration-mapping)
- [Delete Slack integration mapping](#delete-slack-integration-mapping)

## List Slack integration mappings

Lists [Slack integration mappings](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack) in a users' enterprise.

You need Admin or Co-Admin role to
use this endpoint.

This operation is performed by calling function `get_slack_integration_mapping`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-integration-mappings-slack/).

<!-- sample get_integration_mappings_slack -->

```python
user_client.integration_mappings.get_slack_integration_mapping()
```

### Arguments

- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination. This requires `usemarker` to be set to `true`.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- partner_item_type `Optional[GetSlackIntegrationMappingPartnerItemType]`
  - Mapped item type, for which the mapping should be returned
- partner_item_id `Optional[str]`
  - ID of the mapped item, for which the mapping should be returned
- box_item_id `Optional[str]`
  - Box item ID, for which the mappings should be returned
- box_item_type `Optional[GetSlackIntegrationMappingBoxItemType]`
  - Box item type, for which the mappings should be returned
- is_manually_created `Optional[bool]`
  - Whether the mapping has been manually created
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `IntegrationMappings`.

Returns a collection of integration mappings

## Create Slack integration mapping

Creates a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack)
by mapping a Slack channel to a Box item.

You need Admin or Co-Admin role to
use this endpoint.

This operation is performed by calling function `create_slack_integration_mapping`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-integration-mappings-slack/).

<!-- sample post_integration_mappings_slack -->

```python
user_client.integration_mappings.create_slack_integration_mapping(IntegrationMappingPartnerItemSlack(id=partner_item_id, slack_org_id=slack_org_id), IntegrationMappingBoxItemSlack(id=folder.id))
```

### Arguments

- partner_item `IntegrationMappingPartnerItemSlack`
  -
- box_item `IntegrationMappingBoxItemSlack`
  -
- options `Optional[IntegrationMappingSlackOptions]`
  -
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `IntegrationMapping`.

Returns the created integration mapping.

## Update Slack integration mapping

Updates a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack).
Supports updating the Box folder ID and options.

You need Admin or Co-Admin role to
use this endpoint.

This operation is performed by calling function `update_slack_integration_mapping_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-integration-mappings-slack-id/).

_Currently we don't have an example for calling `update_slack_integration_mapping_by_id` in integration tests_

### Arguments

- integration_mapping_id `str`
  - An ID of an integration mapping Example: "11235432"
- box_item `Optional[IntegrationMappingBoxItemSlack]`
  -
- options `Optional[IntegrationMappingSlackOptions]`
  -
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `IntegrationMapping`.

Returns the updated integration mapping object.

## Delete Slack integration mapping

Deletes a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack).

You need Admin or Co-Admin role to
use this endpoint.

This operation is performed by calling function `delete_slack_integration_mapping_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-integration-mappings-slack-id/).

_Currently we don't have an example for calling `delete_slack_integration_mapping_by_id` in integration tests_

### Arguments

- integration_mapping_id `str`
  - An ID of an integration mapping Example: "11235432"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `None`.

Empty body in response
