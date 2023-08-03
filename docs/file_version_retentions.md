# FileVersionRetentionsManager


- [List file version retentions](#list-file-version-retentions)
- [Get retention on file](#get-retention-on-file)

## List file version retentions

Retrieves all file version retentions for the given enterprise.

This operation is performed by calling function `get_file_version_retentions`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-file-version-retentions/).

*Currently we don't have an example for calling `get_file_version_retentions` in integration tests*

### Arguments

- file_id `Optional[str]`
  - Filters results by files with this ID.
- file_version_id `Optional[str]`
  - Filters results by file versions with this ID.
- policy_id `Optional[str]`
  - Filters results by the retention policy with this ID.
- disposition_action `Optional[GetFileVersionRetentionsDispositionActionArg]`
  - Filters results by the retention policy with this disposition action.
- disposition_before `Optional[str]`
  - Filters results by files that will have their disposition come into effect before this date.
- disposition_after `Optional[str]`
  - Filters results by files that will have their disposition come into effect after this date.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


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
  - The ID of the file version retention Example: "3424234"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `FileVersionRetention`.

Returns a file version retention object.


