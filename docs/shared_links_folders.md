# SharedLinksFoldersManager


- [Find folder for shared link](#find-folder-for-shared-link)
- [Get shared link for folder](#get-shared-link-for-folder)
- [Add shared link to folder](#add-shared-link-to-folder)
- [Update shared link on folder](#update-shared-link-on-folder)
- [Remove shared link from folder](#remove-shared-link-from-folder)

## Find folder for shared link

Return the folder represented by a shared link.

A shared folder can be represented by a shared link,
which can originate within the current enterprise or within another.

This endpoint allows an application to retrieve information about a
shared folder when only given a shared link.

This operation is performed by calling function `get_shared_item_folders`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shared-items-folders/).

*Currently we don't have an example for calling `get_shared_item_folders` in integration tests*

### Arguments

- fields `Optional[str]`
  - A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.
- if_none_match `Optional[str]`
  - Ensures an item is only returned if it has changed.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `304 Not Modified` if the item has not changed since.
- boxapi `str`
  - A header containing the shared link and optional password for the shared link.  The format for this header is as follows.  `shared_link=[link]&shared_link_password=[password]`
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `FolderFull`.

Returns a full folder resource if the shared link is valid and
the user has access to it.


## Get shared link for folder

Gets the information for a shared link on a folder.

This operation is performed by calling function `get_folder_get_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-folders-id-get-shared-link/).

*Currently we don't have an example for calling `get_folder_get_shared_link` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`. Example: "12345"
- fields `str`
  - Explicitly request the `shared_link` fields to be returned for this item.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `FolderFull`.

Returns the base representation of a folder with the
additional shared link information.


## Add shared link to folder

Adds a shared link to a folder.

This operation is performed by calling function `update_folder_add_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-folders-id-add-shared-link/).

*Currently we don't have an example for calling `update_folder_add_shared_link` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`. Example: "12345"
- shared_link `Optional[UpdateFolderAddSharedLinkSharedLinkArg]`
  - The settings for the shared link to create on the folder.  Use an empty object (`{}`) to use the default settings for shared links.
- fields `str`
  - Explicitly request the `shared_link` fields to be returned for this item.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `FolderFull`.

Returns the base representation of a folder with a new shared
link attached.


## Update shared link on folder

Updates a shared link on a folder.

This operation is performed by calling function `update_folder_update_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-folders-id-update-shared-link/).

*Currently we don't have an example for calling `update_folder_update_shared_link` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`. Example: "12345"
- shared_link `Optional[UpdateFolderUpdateSharedLinkSharedLinkArg]`
  - The settings for the shared link to update.
- fields `str`
  - Explicitly request the `shared_link` fields to be returned for this item.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `FolderFull`.

Returns a basic representation of the folder, with the updated shared
link attached.


## Remove shared link from folder

Removes a shared link from a folder.

This operation is performed by calling function `update_folder_remove_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-folders-id-remove-shared-link/).

*Currently we don't have an example for calling `update_folder_remove_shared_link` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`. Example: "12345"
- shared_link `Optional[UpdateFolderRemoveSharedLinkSharedLinkArg]`
  - By setting this value to `null`, the shared link is removed from the folder.
- fields `str`
  - Explicitly request the `shared_link` fields to be returned for this item.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `FolderFull`.

Returns a basic representation of a folder, with the shared link removed.


