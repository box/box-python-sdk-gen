<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [TrashedWebLinksManager](#trashedweblinksmanager)
  - [Restore web link](#restore-web-link)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Get trashed web link](#get-trashed-web-link)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Permanently remove web link](#permanently-remove-web-link)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# TrashedWebLinksManager

## Restore web link

Restores a web link that has been moved to the trash.

An optional new parent ID can be provided to restore the  web link to in case
the original folder has been deleted.

This operation is performed by calling function `create_web_link_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-web-links-id/).

*Currently we don't have an example for calling `create_web_link_by_id` in integration tests*

### Arguments

- web_link_id `str`
  - The ID of the web link.
  - Used as `web_link_id` in path `path` of the API call
- request_body `CreateWebLinkByIdRequestBodyArg`
  - Used as requestBody for the API call
- query_params `CreateWebLinkByIdQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `TrashWebLinkRestored`.

Returns a web link object when it has been restored.


## Get trashed web link

Retrieves a web link that has been moved to the trash.

This operation is performed by calling function `get_web_link_trash`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-web-links-id-trash/).

*Currently we don't have an example for calling `get_web_link_trash` in integration tests*

### Arguments

- web_link_id `str`
  - The ID of the web link.
  - Used as `web_link_id` in path `path` of the API call
- query_params `GetWebLinkTrashQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `TrashWebLink`.

Returns the web link that was trashed,
including information about when the it
was moved to the trash.


## Permanently remove web link

Permanently deletes a web link that is in the trash.
This action cannot be undone.

This operation is performed by calling function `delete_web_link_trash`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-web-links-id-trash/).

*Currently we don't have an example for calling `delete_web_link_trash` in integration tests*

### Arguments

- web_link_id `str`
  - The ID of the web link.
  - Used as `web_link_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Returns an empty response when the web link was
permanently deleted.


