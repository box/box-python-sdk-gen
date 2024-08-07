# ChunkedUploadsManager

This is a manager for chunked uploads (allowed for files at least 20MB).

- [Create upload session](#create-upload-session)
- [Create upload session for existing file](#create-upload-session-for-existing-file)
- [Get upload session](#get-upload-session)
- [Upload part of file](#upload-part-of-file)
- [Remove upload session](#remove-upload-session)
- [List parts](#list-parts)
- [Commit upload session](#commit-upload-session)
- [Upload_big_file](#upload-big-file)

## Create upload session

Creates an upload session for a new file.

This operation is performed by calling function `create_file_upload_session`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-files-upload-sessions/).

<!-- sample post_files_upload_sessions -->

```python
self.create_file_upload_session(parent_folder_id, file_size, file_name)
```

### Arguments

- folder_id `str`
  - The ID of the folder to upload the new file to.
- file_size `int`
  - The total number of bytes of the file to be uploaded
- file_name `str`
  - The name of new file
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `UploadSession`.

Returns a new upload session.

## Create upload session for existing file

Creates an upload session for an existing file.

This operation is performed by calling function `create_file_upload_session_for_existing_file`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-files-id-upload-sessions/).

_Currently we don't have an example for calling `create_file_upload_session_for_existing_file` in integration tests_

### Arguments

- file_id `str`
  - The unique identifier that represents a file. The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`. Example: "12345"
- file_size `int`
  - The total number of bytes of the file to be uploaded
- file_name `Optional[str]`
  - The optional new name of new file
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `UploadSession`.

Returns a new upload session.

## Get upload session

Return information about an upload session.

The actual endpoint URL is returned by the [`Create upload session`](e://post-files-upload-sessions) endpoint.

This operation is performed by calling function `get_file_upload_session_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-upload-sessions-id/).

_Currently we don't have an example for calling `get_file_upload_session_by_id` in integration tests_

### Arguments

- upload_session_id `str`
  - The ID of the upload session. Example: "D5E3F7A"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `UploadSession`.

Returns an upload session object.

## Upload part of file

Uploads a chunk of a file for an upload session.

The actual endpoint URL is returned by the [`Create upload session`](e://post-files-upload-sessions)
and [`Get upload session`](e://get-files-upload-sessions-id) endpoints.

This operation is performed by calling function `upload_file_part`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-files-upload-sessions-id/).

<!-- sample put_files_upload_sessions_id -->

```python
self.upload_file_part(
    acc.upload_session_id,
    generate_byte_stream_from_buffer(chunk_buffer),
    digest,
    content_range,
)
```

### Arguments

- upload_session_id `str`
  - The ID of the upload session. Example: "D5E3F7A"
- request_body `ByteStream`
  - Request body of uploadFilePart method
- digest `str`
  - The [RFC3230][1] message digest of the chunk uploaded. Only SHA1 is supported. The SHA1 digest must be base64 encoded. The format of this header is as `sha=BASE64_ENCODED_DIGEST`. To get the value for the `SHA` digest, use the openSSL command to encode the file part: `openssl sha1 -binary <FILE_PART_NAME> | base64` [1]: https://tools.ietf.org/html/rfc3230
- content_range `str`
  - The byte range of the chunk. Must not overlap with the range of a part already uploaded this session. Each part’s size must be exactly equal in size to the part size specified in the upload session that you created. One exception is the last part of the file, as this can be smaller. When providing the value for `content-range`, remember that: _ The lower bound of each part's byte range must be a multiple of the part size. _ The higher bound must be a multiple of the part size - 1.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `UploadedPart`.

Chunk has been uploaded successfully.

## Remove upload session

Abort an upload session and discard all data uploaded.

This cannot be reversed.

The actual endpoint URL is returned by the [`Create upload session`](e://post-files-upload-sessions)
and [`Get upload session`](e://get-files-upload-sessions-id) endpoints.

This operation is performed by calling function `delete_file_upload_session_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-files-upload-sessions-id/).

_Currently we don't have an example for calling `delete_file_upload_session_by_id` in integration tests_

### Arguments

- upload_session_id `str`
  - The ID of the upload session. Example: "D5E3F7A"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `None`.

A blank response is returned if the session was
successfully aborted.

## List parts

Return a list of the chunks uploaded to the upload session so far.

The actual endpoint URL is returned by the [`Create upload session`](e://post-files-upload-sessions)
and [`Get upload session`](e://get-files-upload-sessions-id) endpoints.

This operation is performed by calling function `get_file_upload_session_parts`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-upload-sessions-id-parts/).

<!-- sample get_files_upload_sessions_id_parts -->

```python
self.get_file_upload_session_parts(upload_session_id)
```

### Arguments

- upload_session_id `str`
  - The ID of the upload session. Example: "D5E3F7A"
- offset `Optional[int]`
  - The offset of the item at which to begin the response. Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `UploadParts`.

Returns a list of parts that have been uploaded.

## Commit upload session

Close an upload session and create a file from the uploaded chunks.

The actual endpoint URL is returned by the [`Create upload session`](e://post-files-upload-sessions)
and [`Get upload session`](e://get-files-upload-sessions-id) endpoints.

This operation is performed by calling function `create_file_upload_session_commit`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-files-upload-sessions-id-commit/).

<!-- sample post_files_upload_sessions_id_commit -->

```python
self.create_file_upload_session_commit(upload_session_id, parts, digest)
```

### Arguments

- upload_session_id `str`
  - The ID of the upload session. Example: "D5E3F7A"
- parts `List[UploadPart]`
  - The list details for the uploaded parts
- digest `str`
  - The [RFC3230][1] message digest of the whole file. Only SHA1 is supported. The SHA1 digest must be Base64 encoded. The format of this header is as `sha=BASE64_ENCODED_DIGEST`. [1]: https://tools.ietf.org/html/rfc3230
- if_match `Optional[str]`
  - Ensures this item hasn't recently changed before making changes. Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `412 Precondition Failed` if it has changed since.
- if_none_match `Optional[str]`
  - Ensures an item is only returned if it has changed. Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `304 Not Modified` if the item has not changed since.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `Files`.

Returns the file object in a list.Returns when all chunks have been uploaded but not yet processed.

Inspect the upload session to get more information about the
progress of processing the chunks, then retry committing the file
when all chunks have processed.

## Upload_big_file

Starts the process of chunk uploading a big file. Should return a File object representing uploaded file.

This operation is performed by calling function `upload_big_file`.

```python
client.chunked_uploads.upload_big_file(
    file_byte_stream, file_name, file_size, parent_folder_id
)
```

### Arguments

- file `ByteStream`
  - The stream of the file to upload.
- file_name `str`
  - The name of the file, which will be used for storage in Box.
- file_size `int`
  - The total size of the file for the chunked upload in bytes.
- parent_folder_id `str`
  - The ID of the folder where the file should be uploaded.

### Returns

This function returns a value of type `FileFull`.
