# TransferManager

## Transfer owned folders

Move all of the items (files, folders and workflows) owned by a user into
another user&#x27;s account

Only the root folder (&#x60;0&#x60;) can be transferred.

Folders can only be moved across users by users with administrative
permissions.

All existing shared links and folder-level collaborations are transferred
during the operation. Please note that while collaborations at the individual
file-level are transferred during the operation, the collaborations are
deleted when the original user is deleted.

This call will be performed synchronously which might lead to a slow response
when the source user has a large number of items in all of its folders.

If the destination path has a metadata cascade policy attached to any of
the parent folders, a metadata cascade operation will be kicked off
asynchronously.

There is currently no way to check for when this operation is finished.

The destination folder&#x27;s name will be in the format &#x60;{User}&#x27;s Files and
Folders&#x60;, where &#x60;{User}&#x60; is the display name of the user.

To make this API call your application will need to have the &quot;Read and write
all files and folders stored in Box&quot; scope enabled.

Please make sure the destination user has access to &#x60;Relay&#x60; or &#x60;Relay Lite&#x60;,
and has access to the files and folders involved in the workflows being
transferred.

Admins will receive an email when the operation is completed.

This operation is performed by calling function `transfer_owned_folder`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-users-id-folders-0/).

*Currently we don't have an example for calling `transfer_owned_folder` in integration tests*

### Arguments

- user_id `str`
  - The ID of the user.
  - Used as `user_id` in path `path` of the API call
- request_body `TransferOwnedFolderRequestBodyArg`
  - Used as requestBody for the API call
- query_params `TransferOwnedFolderQueryParamsArg`
  - Used as queryParams for the API call
- headers `TransferOwnedFolderHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `FolderFull`.

Returns the information for the newly created
destination folder.


