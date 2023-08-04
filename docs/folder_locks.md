<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [FolderLocksManager](#folderlocksmanager)
  - [List folder locks](#list-folder-locks)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Create folder lock](#create-folder-lock)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Delete folder lock](#delete-folder-lock)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

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


### Returns

This function returns a value of type `None`.

Returns an empty response when the folder lock is successfully deleted.


