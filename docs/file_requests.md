# FileRequestsManager

## Get file request

Retrieves the information about a file request.

This operation is performed by calling function `get_file_request_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-file-requests-id/).

*Currently we don't have an example for calling `get_file_request_by_id` in integration tests*

### Arguments

- file_request_id `str`
  - The unique identifier that represent a file request.  The ID for any file request can be determined by visiting a file request builder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/filerequest/123&#x60; the &#x60;file_request_id&#x60; is &#x60;123&#x60;.
  - Used as `file_request_id` in path `path` of the API call


### Returns

This function returns a value of type `FileRequest`.

Returns a file request object.


## Update file request

Updates a file request. This can be used to activate or
deactivate a file request.

This operation is performed by calling function `update_file_request_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-file-requests-id/).

*Currently we don't have an example for calling `update_file_request_by_id` in integration tests*

### Arguments

- file_request_id `str`
  - The unique identifier that represent a file request.  The ID for any file request can be determined by visiting a file request builder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/filerequest/123&#x60; the &#x60;file_request_id&#x60; is &#x60;123&#x60;.
  - Used as `file_request_id` in path `path` of the API call
- request_body `FileRequestUpdateRequest`
  - Used as requestBody for the API call
- headers `Optional[UpdateFileRequestByIdHeadersArg]`
  - Used as headers for the API call


### Returns

This function returns a value of type `FileRequest`.

Returns the updated file request object.


## Delete file request

Deletes a file request permanently.

This operation is performed by calling function `delete_file_request_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-file-requests-id/).

*Currently we don't have an example for calling `delete_file_request_by_id` in integration tests*

### Arguments

- file_request_id `str`
  - The unique identifier that represent a file request.  The ID for any file request can be determined by visiting a file request builder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/filerequest/123&#x60; the &#x60;file_request_id&#x60; is &#x60;123&#x60;.
  - Used as `file_request_id` in path `path` of the API call


## Copy file request

Copies an existing file request that is already present on one folder,
and applies it to another folder.

This operation is performed by calling function `create_file_request_copy`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-file-requests-id-copy/).

*Currently we don't have an example for calling `create_file_request_copy` in integration tests*

### Arguments

- file_request_id `str`
  - The unique identifier that represent a file request.  The ID for any file request can be determined by visiting a file request builder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/filerequest/123&#x60; the &#x60;file_request_id&#x60; is &#x60;123&#x60;.
  - Used as `file_request_id` in path `path` of the API call
- request_body `FileRequestCopyRequest`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `FileRequest`.

Returns updated file request object.


