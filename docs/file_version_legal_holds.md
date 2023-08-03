# FileVersionLegalHoldsManager

## Get file version legal hold

Retrieves information about the legal hold policies
assigned to a file version.

This operation is performed by calling function `get_file_version_legal_hold_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-file-version-legal-holds-id/).

*Currently we don't have an example for calling `get_file_version_legal_hold_by_id` in integration tests*

### Arguments

- file_version_legal_hold_id `str`
  - The ID of the file version legal hold
  - Used as `file_version_legal_hold_id` in path `path` of the API call
- headers `GetFileVersionLegalHoldByIdHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `FileVersionLegalHold`.

Returns the legal hold policy assignments for the file version.


## List file version legal holds

Get a list of file versions on legal hold for a legal hold
assignment.

Due to ongoing re-architecture efforts this API might not return all file
versions for this policy ID.

Instead, this API will only return file versions held in the legacy
architecture. Two new endpoints will available to request any file versions
held in the new architecture.

For file versions held in the new architecture, the &#x60;GET
/legal_hold_policy_assignments/:id/file_versions_on_hold&#x60; API can be used to
return all past file versions available for this policy assignment, and the
&#x60;GET /legal_hold_policy_assignments/:id/files_on_hold&#x60; API can be used to
return any current (latest) versions of a file under legal hold.

The &#x60;GET /legal_hold_policy_assignments?policy_id&#x3D;{id}&#x60; API can be used to
find a list of policy assignments for a given policy ID.

Once the re-architecture is completed this API will be deprecated.

This operation is performed by calling function `get_file_version_legal_holds`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-file-version-legal-holds/).

*Currently we don't have an example for calling `get_file_version_legal_holds` in integration tests*

### Arguments

- query_params `GetFileVersionLegalHoldsQueryParamsArg`
  - Used as queryParams for the API call
- headers `GetFileVersionLegalHoldsHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `FileVersionLegalHolds`.

Returns the list of file version legal holds for a specific legal
hold policy.


