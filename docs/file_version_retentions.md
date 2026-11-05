# FileVersionRetentionsManager

<!-- box-python-sdk-gen deprecation banner -->
> [!CAUTION]
> **`box-python-sdk-gen` is deprecated and no longer maintained.** As of September 17, 2025, it receives no new features, bug fixes, or security patches. Do not use it for new projects.
>
> Use [`box-python-sdk`](https://github.com/box/box-python-sdk) v10+ instead: `pip install "boxsdk>=10"`.
> The equivalent of this page is [box-python-sdk/docs/file_version_retentions.md](https://github.com/box/box-python-sdk/blob/main/docs/file_version_retentions.md). To migrate existing code, see the [migration guide](https://github.com/box/box-python-sdk/blob/main/migration-guides/from-box-python-sdk-gen-v1-to-box-python-sdk.md).

- [List file version retentions](#list-file-version-retentions)
- [Get retention on file](#get-retention-on-file)

## List file version retentions

Retrieves all file version retentions for the given enterprise.

**Note**:
File retention API is now **deprecated**.
To get information about files and file versions under retention,
see [files under retention](e://get-retention-policy-assignments-id-files-under-retention) or [file versions under retention](e://get-retention-policy-assignments-id-file-versions-under-retention) endpoints.

This operation is performed by calling function `get_file_version_retentions`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-file-version-retentions/).

<!-- sample get_file_version_retentions -->

```python
client.file_version_retentions.get_file_version_retentions()
```

### Arguments

- file_id `Optional[str]`
  - Filters results by files with this ID.
- file_version_id `Optional[str]`
  - Filters results by file versions with this ID.
- policy_id `Optional[str]`
  - Filters results by the retention policy with this ID.
- disposition_action `Optional[GetFileVersionRetentionsDispositionAction]`
  - Filters results by the retention policy with this disposition action.
- disposition_before `Optional[str]`
  - Filters results by files that will have their disposition come into effect before this date.
- disposition_after `Optional[str]`
  - Filters results by files that will have their disposition come into effect after this date.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination. This requires `usemarker` to be set to `true`.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `FileVersionRetentions`.

Returns a list of all file version retentions for the enterprise.

## Get retention on file

Returns information about a file version retention.

**Note**:
File retention API is now **deprecated**.
To get information about files and file versions under retention,
see [files under retention](e://get-retention-policy-assignments-id-files-under-retention) or [file versions under retention](e://get-retention-policy-assignments-id-file-versions-under-retention) endpoints.

This operation is performed by calling function `get_file_version_retention_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-file-version-retentions-id/).

<!-- sample get_file_version_retentions_id -->

```python
client.file_version_retentions.get_file_version_retention_by_id(
    file_version_retention.id
)
```

### Arguments

- file_version_retention_id `str`
  - The ID of the file version retention. Example: "3424234"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `FileVersionRetention`.

Returns a file version retention object.
