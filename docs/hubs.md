# HubsManager

- [List all hubs](#list-all-hubs)
- [List all hubs for requesting enterprise](#list-all-hubs-for-requesting-enterprise)
- [Get hub information by ID](#get-hub-information-by-id)
- [Delete hub](#delete-hub)

## List all hubs

Retrieves all hubs for requesting user.

This operation is performed by calling function `get_hubs_v2025_r0`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/v2025.0/get-hubs/).

_Currently we don't have an example for calling `get_hubs_v2025_r0` in integration tests_

### Arguments

- query `Optional[str]`
  - The query string to search for hubs.
- scope `Optional[str]`
  - The scope of the hubs to retrieve. Possible values include `editable`, `view_only`, and `all`. Default is `all`.
- sort `Optional[str]`
  - The field to sort results by. Possible values include `name`, `updated_at`, `last_accessed_at`, `view_count`, and `relevance`. Default is `relevance`.
- direction `Optional[GetHubsV2025R0Direction]`
  - The direction to sort results in. This can be either in alphabetical ascending (`ASC`) or descending (`DESC`) order.
- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- box_version `BoxVersionHeaderV2025R0`
  - Version header.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `HubsV2025R0`.

Returns all hubs for the given user or enterprise.

## List all hubs for requesting enterprise

Retrieves all hubs for a given enterprise.

Admins or Hub Co-admins of an enterprise
with GCM scope can make this call.

This operation is performed by calling function `get_enterprise_hubs_v2025_r0`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/v2025.0/get-enterprise-hubs/).

_Currently we don't have an example for calling `get_enterprise_hubs_v2025_r0` in integration tests_

### Arguments

- query `Optional[str]`
  - The query string to search for hubs.
- sort `Optional[str]`
  - The field to sort results by. Possible values include `name`, `updated_at`, `last_accessed_at`, `view_count`, and `relevance`. Default is `relevance`.
- direction `Optional[GetEnterpriseHubsV2025R0Direction]`
  - The direction to sort results in. This can be either in alphabetical ascending (`ASC`) or descending (`DESC`) order.
- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- box_version `BoxVersionHeaderV2025R0`
  - Version header.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `HubsV2025R0`.

Returns all hubs for the given user or enterprise.

## Get hub information by ID

Retrieves details for a hub by its ID.

This operation is performed by calling function `get_hub_by_id_v2025_r0`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/v2025.0/get-hubs-id/).

_Currently we don't have an example for calling `get_hub_by_id_v2025_r0` in integration tests_

### Arguments

- hub_id `str`
  - The unique identifier that represent a hub. The ID for any hub can be determined by visiting this hub in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/hubs/123` the `hub_id` is `123`. Example: "12345"
- box_version `BoxVersionHeaderV2025R0`
  - Version header.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `HubV2025R0`.

Returns a hub object.

## Delete hub

Deletes a single hub.

This operation is performed by calling function `delete_hub_by_id_v2025_r0`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/v2025.0/delete-hubs-id/).

_Currently we don't have an example for calling `delete_hub_by_id_v2025_r0` in integration tests_

### Arguments

- hub_id `str`
  - The unique identifier that represent a hub. The ID for any hub can be determined by visiting this hub in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/hubs/123` the `hub_id` is `123`. Example: "12345"
- box_version `BoxVersionHeaderV2025R0`
  - Version header.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `None`.

A blank response is returned if the hub was
successfully deleted.
