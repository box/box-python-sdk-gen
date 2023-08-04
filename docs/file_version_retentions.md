<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [FileVersionRetentionsManager](#fileversionretentionsmanager)
  - [List file version retentions](#list-file-version-retentions)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Get retention on file](#get-retention-on-file)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# FileVersionRetentionsManager

## List file version retentions

Retrieves all file version retentions for the given enterprise.

This operation is performed by calling function `get_file_version_retentions`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-file-version-retentions/).

*Currently we don't have an example for calling `get_file_version_retentions` in integration tests*

### Arguments

- query_params `GetFileVersionRetentionsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `FileVersionRetentions`.

Returns a list of all file version retentions for the enterprise.


## Get retention on file

Returns information about a file version retention.

This operation is performed by calling function `get_file_version_retention_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-file-version-retentions-id/).

*Currently we don't have an example for calling `get_file_version_retention_by_id` in integration tests*

### Arguments

- file_version_retention_id `str`
  - The ID of the file version retention
  - Used as `file_version_retention_id` in path `path` of the API call


### Returns

This function returns a value of type `FileVersionRetention`.

Returns a file version retention object.


