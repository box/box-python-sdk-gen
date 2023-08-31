# SharedLinksWebLinksManager

- [Find web link for shared link](#find-web-link-for-shared-link)
- [Get shared link for web link](#get-shared-link-for-web-link)
- [Add shared link to web link](#add-shared-link-to-web-link)
- [Update shared link on web link](#update-shared-link-on-web-link)
- [Remove shared link from web link](#remove-shared-link-from-web-link)

## Find web link for shared link

Returns the web link represented by a shared link.

A shared web link can be represented by a shared link,
which can originate within the current enterprise or within another.

This endpoint allows an application to retrieve information about a
shared web link when only given a shared link.

This operation is performed by calling function `get_shared_item_web_links`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shared-items-web-links/).

_Currently we don't have an example for calling `get_shared_item_web_links` in integration tests_

### Arguments

- fields `Optional[str]`
  - A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.
- if_none_match `Optional[str]`
  - Ensures an item is only returned if it has changed. Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `304 Not Modified` if the item has not changed since.
- boxapi `str`
  - A header containing the shared link and optional password for the shared link. The format for this header is as follows. `shared_link=[link]&shared_link_password=[password]`
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `WebLink`.

Returns a full file resource if the shared link is valid and
the user has access to it.

## Get shared link for web link

Gets the information for a shared link on a web link.

This operation is performed by calling function `get_web_link_get_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-web-links-id-get-shared-link/).

_Currently we don't have an example for calling `get_web_link_get_shared_link` in integration tests_

### Arguments

- web_link_id `str`
  - The ID of the web link. Example: "12345"
- fields `str`
  - Explicitly request the `shared_link` fields to be returned for this item.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `WebLink`.

Returns the base representation of a web link with the
additional shared link information.

## Add shared link to web link

Adds a shared link to a web link.

This operation is performed by calling function `update_web_link_add_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-web-links-id-add-shared-link/).

_Currently we don't have an example for calling `update_web_link_add_shared_link` in integration tests_

### Arguments

- web_link_id `str`
  - The ID of the web link. Example: "12345"
- shared_link `Optional[UpdateWebLinkAddSharedLinkSharedLinkArg]`
  - The settings for the shared link to create on the web link. Use an empty object (`{}`) to use the default settings for shared links.
- fields `str`
  - Explicitly request the `shared_link` fields to be returned for this item.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `WebLink`.

Returns the base representation of a web link with a new shared
link attached.

## Update shared link on web link

Updates a shared link on a web link.

This operation is performed by calling function `update_web_link_update_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-web-links-id-update-shared-link/).

_Currently we don't have an example for calling `update_web_link_update_shared_link` in integration tests_

### Arguments

- web_link_id `str`
  - The ID of the web link. Example: "12345"
- shared_link `Optional[UpdateWebLinkUpdateSharedLinkSharedLinkArg]`
  - The settings for the shared link to update.
- fields `str`
  - Explicitly request the `shared_link` fields to be returned for this item.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `WebLink`.

Returns a basic representation of the web link, with the updated shared
link attached.

## Remove shared link from web link

Removes a shared link from a web link.

This operation is performed by calling function `update_web_link_remove_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-web-links-id-remove-shared-link/).

_Currently we don't have an example for calling `update_web_link_remove_shared_link` in integration tests_

### Arguments

- web_link_id `str`
  - The ID of the web link. Example: "12345"
- shared_link `Optional[UpdateWebLinkRemoveSharedLinkSharedLinkArg]`
  - By setting this value to `null`, the shared link is removed from the web link.
- fields `str`
  - Explicitly request the `shared_link` fields to be returned for this item.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `WebLink`.

Returns a basic representation of a web link, with the
shared link removed.
