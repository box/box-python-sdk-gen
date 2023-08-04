<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [FolderMetadataManager](#foldermetadatamanager)
  - [List metadata instances on folder](#list-metadata-instances-on-folder)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Get metadata instance on folder](#get-metadata-instance-on-folder)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Create metadata instance on folder](#create-metadata-instance-on-folder)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Remove metadata instance from folder](#remove-metadata-instance-from-folder)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# FolderMetadataManager

## List metadata instances on folder

Retrieves all metadata for a given folder. This can not be used on the root
folder with ID &#x60;0&#x60;.

This operation is performed by calling function `get_folder_metadata`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-folders-id-metadata/).

*Currently we don't have an example for calling `get_folder_metadata` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call


### Returns

This function returns a value of type `Metadatas`.

Returns all the metadata associated with a folder.

This API does not support pagination and will therefore always return
all of the metadata associated to the folder.


## Get metadata instance on folder

Retrieves the instance of a metadata template that has been applied to a
folder. This can not be used on the root folder with ID &#x60;0&#x60;.

This operation is performed by calling function `get_folder_metadata_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-folders-id-metadata-id-id/).

*Currently we don't have an example for calling `get_folder_metadata_by_id` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call
- scope `GetFolderMetadataByIdScopeArg`
  - The scope of the metadata template
  - Used as `scope` in path `path` of the API call
- template_key `str`
  - The name of the metadata template
  - Used as `template_key` in path `path` of the API call


### Returns

This function returns a value of type `Metadata`.

An instance of the metadata template that includes
additional &quot;key:value&quot; pairs defined by the user or
an application.


## Create metadata instance on folder

Applies an instance of a metadata template to a folder.

In most cases only values that are present in the metadata template
will be accepted, except for the &#x60;global.properties&#x60; template which accepts
any key-value pair.

To display the metadata template in the Box web app the enterprise needs to be
configured to enable **Cascading Folder Level Metadata** for the user in the
admin console.

This operation is performed by calling function `create_folder_metadata_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-folders-id-metadata-id-id/).

*Currently we don't have an example for calling `create_folder_metadata_by_id` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call
- scope `CreateFolderMetadataByIdScopeArg`
  - The scope of the metadata template
  - Used as `scope` in path `path` of the API call
- template_key `str`
  - The name of the metadata template
  - Used as `template_key` in path `path` of the API call
- request_body `CreateFolderMetadataByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `Metadata`.

Returns the instance of the template that was applied to the folder,
including the data that was applied to the template.


## Remove metadata instance from folder

Deletes a piece of folder metadata.

This operation is performed by calling function `delete_folder_metadata_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-folders-id-metadata-id-id/).

*Currently we don't have an example for calling `delete_folder_metadata_by_id` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.  The root folder of a Box account is always represented by the ID &#x60;0&#x60;.
  - Used as `folder_id` in path `path` of the API call
- scope `DeleteFolderMetadataByIdScopeArg`
  - The scope of the metadata template
  - Used as `scope` in path `path` of the API call
- template_key `str`
  - The name of the metadata template
  - Used as `template_key` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Returns an empty response when the metadata is
successfully deleted.


