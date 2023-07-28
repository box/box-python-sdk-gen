# ChunkedUploadsManager

This is a manager for chunked uploads (allowed for files at least 20MB).

## Create upload session

Creates an upload session for a new file.

This operation is performed by calling function `create_file_upload_session`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-files-upload-sessions/).

*Currently we don't have an example for calling `create_file_upload_session` in integration tests*

### Arguments

- request_body `CreateFileUploadSessionRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `UploadSession`.

Returns a new upload session.


## Create upload session for existing file

Creates an upload session for an existing file.

This operation is performed by calling function `create_file_upload_session_for_existing_file`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-files-id-upload-sessions/).

*Currently we don't have an example for calling `create_file_upload_session_for_existing_file` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- request_body `CreateFileUploadSessionForExistingFileRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `UploadSession`.

Returns a new upload session.


## Get upload session

Return information about an upload session.

This operation is performed by calling function `get_file_upload_session_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-upload-sessions-id/).

*Currently we don't have an example for calling `get_file_upload_session_by_id` in integration tests*

### Arguments

- upload_session_id `str`
  - The ID of the upload session.
  - Used as `upload_session_id` in path `path` of the API call


### Returns

This function returns a value of type `UploadSession`.

Returns an upload session object.


## Upload part of file

Updates a chunk of an upload session for a file.

This operation is performed by calling function `upload_file_part`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-files-upload-sessions-id/).

*Currently we don't have an example for calling `upload_file_part` in integration tests*

### Arguments

- upload_session_id `str`
  - The ID of the upload session.
  - Used as `upload_session_id` in path `path` of the API call
- request_body `str`
  - Used as requestBody for the API call
- headers `UploadFilePartHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `UploadedPart`.

Chunk has been uploaded successfully.


## Remove upload session

Abort an upload session and discard all data uploaded.

This cannot be reversed.

This operation is performed by calling function `delete_file_upload_session_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-files-upload-sessions-id/).

*Currently we don't have an example for calling `delete_file_upload_session_by_id` in integration tests*

### Arguments

- upload_session_id `str`
  - The ID of the upload session.
  - Used as `upload_session_id` in path `path` of the API call


## List parts

Return a list of the chunks uploaded to the upload
session so far.

This operation is performed by calling function `get_file_upload_session_parts`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-upload-sessions-id-parts/).

*Currently we don't have an example for calling `get_file_upload_session_parts` in integration tests*

### Arguments

- upload_session_id `str`
  - The ID of the upload session.
  - Used as `upload_session_id` in path `path` of the API call
- query_params `GetFileUploadSessionPartsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `UploadParts`.

Returns a list of parts that have been uploaded.


## Commit upload session

Close an upload session and create a file from the
uploaded chunks.

This operation is performed by calling function `create_file_upload_session_commit`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-files-upload-sessions-id-commit/).

*Currently we don't have an example for calling `create_file_upload_session_commit` in integration tests*

### Arguments

- upload_session_id `str`
  - The ID of the upload session.
  - Used as `upload_session_id` in path `path` of the API call
- request_body `CreateFileUploadSessionCommitRequestBodyArg`
  - Used as requestBody for the API call
- headers `CreateFileUploadSessionCommitHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `Files`.

Returns the file object in a list.Returns when all chunks have been uploaded but not yet processed.

Inspect the upload session to get more information about the
progress of processing the chunks, then retry committing the file
when all chunks have processed.


