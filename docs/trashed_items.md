<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [TrashedItemsManager](#trasheditemsmanager)
  - [List trashed items](#list-trashed-items)
    - [Arguments](#arguments)
    - [Returns](#returns)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# TrashedItemsManager

## List trashed items

Retrieves the files and folders that have been moved
to the trash.

Any attribute in the full files or folders objects can be passed
in with the &#x60;fields&#x60; parameter to retrieve those specific
attributes that are not returned by default.

This endpoint defaults to use offset-based pagination, yet also supports
marker-based pagination using the &#x60;marker&#x60; parameter.

This operation is performed by calling function `get_folder_trash_items`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-folders-trash-items/).

*Currently we don't have an example for calling `get_folder_trash_items` in integration tests*

### Arguments

- query_params `GetFolderTrashItemsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Items`.

Returns a list of items that have been deleted


