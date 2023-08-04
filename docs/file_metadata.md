<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [FileMetadataManager](#filemetadatamanager)
  - [List metadata instances on file](#list-metadata-instances-on-file)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Get metadata instance on file](#get-metadata-instance-on-file)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Create metadata instance on file](#create-metadata-instance-on-file)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Remove metadata instance from file](#remove-metadata-instance-from-file)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# FileMetadataManager

## List metadata instances on file

Retrieves all metadata for a given file.

This operation is performed by calling function `get_file_metadata`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-metadata/).

*Currently we don't have an example for calling `get_file_metadata` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call


### Returns

This function returns a value of type `Metadatas`.

Returns all the metadata associated with a file.

This API does not support pagination and will therefore always return
all of the metadata associated to the file.


## Get metadata instance on file

Retrieves the instance of a metadata template that has been applied to a
file.

This operation is performed by calling function `get_file_metadata_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-metadata-id-id/).

*Currently we don't have an example for calling `get_file_metadata_by_id` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- scope `GetFileMetadataByIdScopeArg`
  - The scope of the metadata template
  - Used as `scope` in path `path` of the API call
- template_key `str`
  - The name of the metadata template
  - Used as `template_key` in path `path` of the API call


### Returns

This function returns a value of type `MetadataFull`.

An instance of the metadata template that includes
additional &quot;key:value&quot; pairs defined by the user or
an application.


## Create metadata instance on file

Applies an instance of a metadata template to a file.

In most cases only values that are present in the metadata template
will be accepted, except for the &#x60;global.properties&#x60; template which accepts
any key-value pair.

This operation is performed by calling function `create_file_metadata_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-files-id-metadata-id-id/).

*Currently we don't have an example for calling `create_file_metadata_by_id` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- scope `CreateFileMetadataByIdScopeArg`
  - The scope of the metadata template
  - Used as `scope` in path `path` of the API call
- template_key `str`
  - The name of the metadata template
  - Used as `template_key` in path `path` of the API call
- request_body `CreateFileMetadataByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `Metadata`.

Returns the instance of the template that was applied to the file,
including the data that was applied to the template.


## Remove metadata instance from file

Deletes a piece of file metadata.

This operation is performed by calling function `delete_file_metadata_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-files-id-metadata-id-id/).

*Currently we don't have an example for calling `delete_file_metadata_by_id` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- scope `DeleteFileMetadataByIdScopeArg`
  - The scope of the metadata template
  - Used as `scope` in path `path` of the API call
- template_key `str`
  - The name of the metadata template
  - Used as `template_key` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Returns an empty response when the metadata is
successfully deleted.


