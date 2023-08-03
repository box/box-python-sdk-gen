# SharedLinksFilesManager

## Find file for shared link

Returns the file represented by a shared link.

A shared file can be represented by a shared link,
which can originate within the current enterprise or within another.

This endpoint allows an application to retrieve information about a
shared file when only given a shared link.

The &#x60;shared_link_permission_options&#x60; array field can be returned
by requesting it in the &#x60;fields&#x60; query parameter.

This operation is performed by calling function `get_shared_items`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shared-items/).

*Currently we don't have an example for calling `get_shared_items` in integration tests*

### Arguments

- query_params `GetSharedItemsQueryParamsArg`
  - Used as queryParams for the API call
- headers `GetSharedItemsHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `FileFull`.

Returns a full file resource if the shared link is valid and
the user has access to it.


## Get shared link for file

Gets the information for a shared link on a file.

This operation is performed by calling function `get_file_get_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-get-shared-link/).

*Currently we don't have an example for calling `get_file_get_shared_link` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- query_params `GetFileGetSharedLinkQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `FileFull`.

Returns the base representation of a file with the
additional shared link information.


## Add shared link to file

Adds a shared link to a file.

This operation is performed by calling function `update_file_add_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-files-id-add-shared-link/).

*Currently we don't have an example for calling `update_file_add_shared_link` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- request_body `UpdateFileAddSharedLinkRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateFileAddSharedLinkQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `FileFull`.

Returns the base representation of a file with a new shared
link attached.


## Update shared link on file

Updates a shared link on a file.

This operation is performed by calling function `update_file_update_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-files-id-update-shared-link/).

*Currently we don't have an example for calling `update_file_update_shared_link` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- request_body `UpdateFileUpdateSharedLinkRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateFileUpdateSharedLinkQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `FileFull`.

Returns a basic representation of the file, with the updated shared
link attached.


## Remove shared link from file

Removes a shared link from a file.

This operation is performed by calling function `update_file_remove_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-files-id-remove-shared-link/).

*Currently we don't have an example for calling `update_file_remove_shared_link` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- request_body `UpdateFileRemoveSharedLinkRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateFileRemoveSharedLinkQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `FileFull`.

Returns a basic representation of a file, with the shared link removed.


