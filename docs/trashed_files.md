<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [TrashedFilesManager](#trashedfilesmanager)
  - [Restore file](#restore-file)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Get trashed file](#get-trashed-file)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Permanently remove file](#permanently-remove-file)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# TrashedFilesManager

## Restore file

Restores a file that has been moved to the trash.

An optional new parent ID can be provided to restore the file to in case the
original folder has been deleted.

This operation is performed by calling function `restore_file_from_trash`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-files-id/).

*Currently we don't have an example for calling `restore_file_from_trash` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- request_body `RestoreFileFromTrashRequestBodyArg`
  - Used as requestBody for the API call
- query_params `RestoreFileFromTrashQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `TrashFileRestored`.

Returns a file object when the file has been restored.


## Get trashed file

Retrieves a file that has been moved to the trash.

Please note that only if the file itself has been moved to the
trash can it be retrieved with this API call. If instead one of
its parent folders was moved to the trash, only that folder
can be inspected using the
[&#x60;GET /folders/:id/trash&#x60;](e://get_folders_id_trash) API.

To list all items that have been moved to the trash, please
use the [&#x60;GET /folders/trash/items&#x60;](e://get-folders-trash-items/)
API.

This operation is performed by calling function `get_file_trash`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-trash/).

<!-- sample get_files_id_trash -->
```python
client.trashed_files.get_file_trash(uploaded_file.id)
```

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- query_params `GetFileTrashQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `TrashFile`.

Returns the file that was trashed,
including information about when the it
was moved to the trash.


## Permanently remove file

Permanently deletes a file that is in the trash.
This action cannot be undone.

This operation is performed by calling function `delete_file_trash`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-files-id-trash/).

*Currently we don't have an example for calling `delete_file_trash` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Returns an empty response when the file was
permanently deleted.


