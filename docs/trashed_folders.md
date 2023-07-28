# TrashedFoldersManager

## Restore folder

Restores a folder that has been moved to the trash.

An optional new parent ID can be provided to restore the folder to in case the
original folder has been deleted.

# Folder locking

During this operation, part of the file tree will be locked, mainly
the source folder and all of its descendants, as well as the destination
folder.

For the duration of the operation, no other move, copy, delete, or restore
operation can performed on any of the locked folders.

This operation is performed by calling function `restore_folder_from_trash`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-folders-id/).

*Currently we don't have an example for calling `restore_folder_from_trash` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call
- request_body `RestoreFolderFromTrashRequestBodyArg`
  - Used as requestBody for the API call
- query_params `RestoreFolderFromTrashQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `TrashFolderRestored`.

Returns a folder object when the folder has been restored.


## Get trashed folder

Retrieves a folder that has been moved to the trash.

Please note that only if the folder itself has been moved to the
trash can it be retrieved with this API call. If instead one of
its parent folders was moved to the trash, only that folder
can be inspected using the
[&#x60;GET /folders/:id/trash&#x60;](e://get_folders_id_trash) API.

To list all items that have been moved to the trash, please
use the [&#x60;GET /folders/trash/items&#x60;](e://get-folders-trash-items/)
API.

This operation is performed by calling function `get_folder_trash`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-folders-id-trash/).

*Currently we don't have an example for calling `get_folder_trash` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call
- query_params `GetFolderTrashQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `TrashFolder`.

Returns the folder that was trashed,
including information about when the it
was moved to the trash.


## Permanently remove folder

Permanently deletes a folder that is in the trash.
This action cannot be undone.

This operation is performed by calling function `delete_folder_trash`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-folders-id-trash/).

*Currently we don't have an example for calling `delete_folder_trash` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call


