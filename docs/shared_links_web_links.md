# SharedLinksWebLinksManager

## Find web link for shared link

Returns the web link represented by a shared link.

A shared web link can be represented by a shared link,
which can originate within the current enterprise or within another.

This endpoint allows an application to retrieve information about a
shared web link when only given a shared link.

This operation is performed by calling function `get_shared_item_web_links`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shared-items-web-links/).

*Currently we don't have an example for calling `get_shared_item_web_links` in integration tests*

### Arguments

- query_params `Optional[GetSharedItemWebLinksQueryParamsArg]`
  - Used as queryParams for the API call
- headers `GetSharedItemWebLinksHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `WebLink`.

Returns a full file resource if the shared link is valid and
the user has access to it.


## Get shared link for web link

Gets the information for a shared link on a web link.

This operation is performed by calling function `get_web_link_get_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-web-links-id-get-shared-link/).

*Currently we don't have an example for calling `get_web_link_get_shared_link` in integration tests*

### Arguments

- web_link_id `str`
  - The ID of the web link.
  - Used as `web_link_id` in path `path` of the API call
- query_params `GetWebLinkGetSharedLinkQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `WebLink`.

Returns the base representation of a web link with the
additional shared link information.


## Add shared link to web link

Adds a shared link to a web link.

This operation is performed by calling function `update_web_link_add_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-web-links-id-add-shared-link/).

*Currently we don't have an example for calling `update_web_link_add_shared_link` in integration tests*

### Arguments

- web_link_id `str`
  - The ID of the web link.
  - Used as `web_link_id` in path `path` of the API call
- request_body `UpdateWebLinkAddSharedLinkRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateWebLinkAddSharedLinkQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `WebLink`.

Returns the base representation of a web link with a new shared
link attached.


## Update shared link on web link

Updates a shared link on a web link.

This operation is performed by calling function `update_web_link_update_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-web-links-id-update-shared-link/).

*Currently we don't have an example for calling `update_web_link_update_shared_link` in integration tests*

### Arguments

- web_link_id `str`
  - The ID of the web link.
  - Used as `web_link_id` in path `path` of the API call
- request_body `UpdateWebLinkUpdateSharedLinkRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateWebLinkUpdateSharedLinkQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `WebLink`.

Returns a basic representation of the web link, with the updated shared
link attached.


## Remove shared link from web link

Removes a shared link from a web link.

This operation is performed by calling function `update_web_link_remove_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-web-links-id-remove-shared-link/).

*Currently we don't have an example for calling `update_web_link_remove_shared_link` in integration tests*

### Arguments

- web_link_id `str`
  - The ID of the web link.
  - Used as `web_link_id` in path `path` of the API call
- request_body `UpdateWebLinkRemoveSharedLinkRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateWebLinkRemoveSharedLinkQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `WebLink`.

Returns a basic representation of a web link, with the
shared link removed.


