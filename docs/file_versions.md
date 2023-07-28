# FileVersionsManager

## List all file versions

Retrieve a list of the past versions for a file.

Versions are only tracked by Box users with premium accounts. To fetch the ID
of the current version of a file, use the &#x60;GET /file/:id&#x60; API.

This operation is performed by calling function `get_file_versions`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-versions/).

*Currently we don't have an example for calling `get_file_versions` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- query_params `GetFileVersionsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `FileVersions`.

Returns an array of past versions for this file.


## Get file version

Retrieve a specific version of a file.

Versions are only tracked for Box users with premium accounts.

This operation is performed by calling function `get_file_version_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-versions-id/).

*Currently we don't have an example for calling `get_file_version_by_id` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- file_version_id `str`
  - The ID of the file version
  - Used as `file_version_id` in path `path` of the API call
- query_params `GetFileVersionByIdQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `FileVersionFull`.

Returns a specific version of a file.

Not all available fields are returned by default. Use the
[fields](#param-fields) query parameter to explicitly request
any specific fields.


## Restore file version

Restores a specific version of a file after it was deleted.
Don&#x27;t use this endpoint to restore Box Notes,
as it works with file formats such as PDF, DOC,
PPTX or similar.

This operation is performed by calling function `update_file_version_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-files-id-versions-id/).

*Currently we don't have an example for calling `update_file_version_by_id` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- file_version_id `str`
  - The ID of the file version
  - Used as `file_version_id` in path `path` of the API call
- request_body `UpdateFileVersionByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `FileVersionFull`.

Returns a restored file version object.


## Remove file version

Move a file version to the trash.

Versions are only tracked for Box users with premium accounts.

This operation is performed by calling function `delete_file_version_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-files-id-versions-id/).

*Currently we don't have an example for calling `delete_file_version_by_id` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- file_version_id `str`
  - The ID of the file version
  - Used as `file_version_id` in path `path` of the API call
- headers `DeleteFileVersionByIdHeadersArg`
  - Used as headers for the API call


## Promote file version

Promote a specific version of a file.

If previous versions exist, this method can be used to
promote one of the older versions to the top of the version history.

This creates a new copy of the old version and puts it at the
top of the versions history. The file will have the exact same contents
as the older version, with the the same hash digest, &#x60;etag&#x60;, and
name as the original.

Other properties such as comments do not get updated to their
former values.

Don&#x27;t use this endpoint to restore Box Notes,
as it works with file formats such as PDF, DOC,
PPTX or similar.

This operation is performed by calling function `promote_file_version`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-files-id-versions-current/).

*Currently we don't have an example for calling `promote_file_version` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- request_body `PromoteFileVersionRequestBodyArg`
  - Used as requestBody for the API call
- query_params `PromoteFileVersionQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `FileVersionFull`.

Returns a newly created file version object.


