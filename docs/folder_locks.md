# FolderLocksManager

## List folder locks

Retrieves folder lock details for a given folder.

You must be authenticated as the owner or co-owner of the folder to
use this endpoint.

This operation is performed by calling function `get_folder_locks`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-folder-locks/).

*Currently we don't have an example for calling `get_folder_locks` in integration tests*

### Arguments

- query_params `GetFolderLocksQueryParamsArg`
  - Used as queryParams for the API call
- headers `GetFolderLocksHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `FolderLocks`.

Returns details for all folder locks applied to the folder, including the
lock type and user that applied the lock.


## Create folder lock

Creates a folder lock on a folder, preventing it from being moved and/or
deleted.

You must be authenticated as the owner or co-owner of the folder to
use this endpoint.

This operation is performed by calling function `create_folder_lock`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-folder-locks/).

*Currently we don't have an example for calling `create_folder_lock` in integration tests*

### Arguments

- request_body `CreateFolderLockRequestBodyArg`
  - Used as requestBody for the API call
- headers `CreateFolderLockHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `FolderLock`.

Returns the instance of the folder lock that was applied to the folder,
including the user that applied the lock and the operations set.


## Delete folder lock

Deletes a folder lock on a given folder.

You must be authenticated as the owner or co-owner of the folder to
use this endpoint.

This operation is performed by calling function `delete_folder_lock_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-folder-locks-id/).

*Currently we don't have an example for calling `delete_folder_lock_by_id` in integration tests*

### Arguments

- folder_lock_id `str`
  - The ID of the folder lock.
  - Used as `folder_lock_id` in path `path` of the API call
- headers `DeleteFolderLockByIdHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `None`.

Returns an empty response when the folder lock is successfully deleted.


