# FileWatermarksManager

- [Get watermark on file](#get-watermark-on-file)
- [Apply watermark to file](#apply-watermark-to-file)
- [Remove watermark from file](#remove-watermark-from-file)

## Get watermark on file

Retrieve the watermark for a file.

This operation is performed by calling function `get_file_watermark`.

```python
client.file_watermarks.get_file_watermark(file.id)
```

### Arguments

- file_id `str`
  - The unique identifier that represents a file. The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`. Example: "12345"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `Watermark`.

Returns an object containing information about the
watermark associated for to this file.

## Apply watermark to file

Applies or update a watermark on a file.

This operation is performed by calling function `update_file_watermark`.

```python
client.file_watermarks.update_file_watermark(
    file.id,
    UpdateFileWatermarkWatermark(
        imprint=UpdateFileWatermarkWatermarkImprintField.DEFAULT.value
    ),
)
```

### Arguments

- file_id `str`
  - The unique identifier that represents a file. The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`. Example: "12345"
- watermark `UpdateFileWatermarkWatermark`
  - The watermark to imprint on the file
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `Watermark`.

Returns an updated watermark if a watermark already
existed on this file.Returns a new watermark if no watermark existed on
this file yet.

## Remove watermark from file

Removes the watermark from a file.

This operation is performed by calling function `delete_file_watermark`.

```python
client.file_watermarks.delete_file_watermark(file.id)
```

### Arguments

- file_id `str`
  - The unique identifier that represents a file. The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`. Example: "12345"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `None`.

Removes the watermark and returns an empty response.
