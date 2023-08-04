<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [FolderWatermarksManager](#folderwatermarksmanager)
  - [Get watermark for folder](#get-watermark-for-folder)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Apply watermark to folder](#apply-watermark-to-folder)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Remove watermark from folder](#remove-watermark-from-folder)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# FolderWatermarksManager

## Get watermark for folder

Retrieve the watermark for a folder.

This operation is performed by calling function `get_folder_watermark`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-folders-id-watermark/).

*Currently we don't have an example for calling `get_folder_watermark` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call


### Returns

This function returns a value of type `Watermark`.

Returns an object containing information about the
watermark associated for to this folder.


## Apply watermark to folder

Applies or update a watermark on a folder.

This operation is performed by calling function `update_folder_watermark`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-folders-id-watermark/).

*Currently we don't have an example for calling `update_folder_watermark` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call
- request_body `UpdateFolderWatermarkRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `Watermark`.

Returns an updated watermark if a watermark already
existed on this folder.Returns a new watermark if no watermark existed on
this folder yet.


## Remove watermark from folder

Removes the watermark from a folder.

This operation is performed by calling function `delete_folder_watermark`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-folders-id-watermark/).

*Currently we don't have an example for calling `delete_folder_watermark` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

An empty response will be returned when the watermark
was successfully deleted.


