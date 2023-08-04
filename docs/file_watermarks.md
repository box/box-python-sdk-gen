<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [FileWatermarksManager](#filewatermarksmanager)
  - [Get watermark on file](#get-watermark-on-file)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Apply watermark to file](#apply-watermark-to-file)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Remove watermark from file](#remove-watermark-from-file)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# FileWatermarksManager

## Get watermark on file

Retrieve the watermark for a file.

This operation is performed by calling function `get_file_watermark`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-watermark/).

*Currently we don't have an example for calling `get_file_watermark` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call


### Returns

This function returns a value of type `Watermark`.

Returns an object containing information about the
watermark associated for to this file.


## Apply watermark to file

Applies or update a watermark on a file.

This operation is performed by calling function `update_file_watermark`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-files-id-watermark/).

*Currently we don't have an example for calling `update_file_watermark` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- request_body `UpdateFileWatermarkRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `Watermark`.

Returns an updated watermark if a watermark already
existed on this file.Returns a new watermark if no watermark existed on
this file yet.


## Remove watermark from file

Removes the watermark from a file.

This operation is performed by calling function `delete_file_watermark`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-files-id-watermark/).

*Currently we don't have an example for calling `delete_file_watermark` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Removes the watermark and returns an empty response.


