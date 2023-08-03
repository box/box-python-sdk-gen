# SharedLinksFoldersManager

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

- query_params `GetSharedItemFoldersQueryParamsArg`
  - Used as queryParams for the API call
- headers `GetSharedItemFoldersHeadersArg`
  - Used as headers for the API call


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
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call
- query_params `GetFolderGetSharedLinkQueryParamsArg`
  - Used as queryParams for the API call
- headers `GetFolderGetSharedLinkHeadersArg`
  - Used as headers for the API call


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
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call
- request_body `UpdateFolderAddSharedLinkRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateFolderAddSharedLinkQueryParamsArg`
  - Used as queryParams for the API call
- headers `UpdateFolderAddSharedLinkHeadersArg`
  - Used as headers for the API call


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
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call
- request_body `UpdateFolderUpdateSharedLinkRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateFolderUpdateSharedLinkQueryParamsArg`
  - Used as queryParams for the API call
- headers `UpdateFolderUpdateSharedLinkHeadersArg`
  - Used as headers for the API call


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
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call
- request_body `UpdateFolderRemoveSharedLinkRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateFolderRemoveSharedLinkQueryParamsArg`
  - Used as queryParams for the API call
- headers `UpdateFolderRemoveSharedLinkHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `FolderFull`.

Returns a basic representation of a folder, with the shared link removed.


