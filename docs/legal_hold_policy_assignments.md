# LegalHoldPolicyAssignmentsManager

## List legal hold policy assignments

Retrieves a list of items a legal hold policy has been assigned to.

This operation is performed by calling function `get_legal_hold_policy_assignments`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-legal-hold-policy-assignments/).

*Currently we don't have an example for calling `get_legal_hold_policy_assignments` in integration tests*

### Arguments

- query_params `GetLegalHoldPolicyAssignmentsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `LegalHoldPolicyAssignments`.

Returns a list of legal hold policy assignments.


## Assign legal hold policy

Assign a legal hold to a file, file version, folder, or user.

This operation is performed by calling function `create_legal_hold_policy_assignment`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-legal-hold-policy-assignments/).

*Currently we don't have an example for calling `create_legal_hold_policy_assignment` in integration tests*

### Arguments

- request_body `CreateLegalHoldPolicyAssignmentRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `LegalHoldPolicyAssignment`.

Returns a new legal hold policy assignment.


## Get legal hold policy assignment

Retrieve a legal hold policy assignment.

This operation is performed by calling function `get_legal_hold_policy_assignment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-legal-hold-policy-assignments-id/).

*Currently we don't have an example for calling `get_legal_hold_policy_assignment_by_id` in integration tests*

### Arguments

- legal_hold_policy_assignment_id `str`
  - The ID of the legal hold policy assignment
  - Used as `legal_hold_policy_assignment_id` in path `path` of the API call


### Returns

This function returns a value of type `LegalHoldPolicyAssignment`.

Returns a legal hold policy object.


## Unassign legal hold policy

Remove a legal hold from an item.

This is an asynchronous process. The policy will not be
fully removed yet when the response returns.

This operation is performed by calling function `delete_legal_hold_policy_assignment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-legal-hold-policy-assignments-id/).

*Currently we don't have an example for calling `delete_legal_hold_policy_assignment_by_id` in integration tests*

### Arguments

- legal_hold_policy_assignment_id `str`
  - The ID of the legal hold policy assignment
  - Used as `legal_hold_policy_assignment_id` in path `path` of the API call


## List current file versions for legal hold policy assignment

Get a list of current file versions for a legal hold
assignment.

In some cases you may want to get previous file versions instead. In these
cases, use the &#x60;GET  /legal_hold_policy_assignments/:id/file_versions_on_hold&#x60;
API instead to return any previous versions of a file for this legal hold
policy assignment.

Due to ongoing re-architecture efforts this API might not return all file
versions held for this policy ID. Instead, this API will only return the
latest file version held in the newly developed architecture. The &#x60;GET
/file_version_legal_holds&#x60; API can be used to fetch current and past versions
of files held within the legacy architecture.

The &#x60;GET /legal_hold_policy_assignments?policy_id&#x3D;{id}&#x60; API can be used to
find a list of policy assignments for a given policy ID.

This operation is performed by calling function `get_legal_hold_policy_assignment_file_on_hold`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-legal-hold-policy-assignments-id-files-on-hold/).

*Currently we don't have an example for calling `get_legal_hold_policy_assignment_file_on_hold` in integration tests*

### Arguments

- legal_hold_policy_assignment_id `str`
  - The ID of the legal hold policy assignment
  - Used as `legal_hold_policy_assignment_id` in path `path` of the API call
- query_params `Optional[GetLegalHoldPolicyAssignmentFileOnHoldQueryParamsArg]`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `FileVersionLegalHolds`.

Returns the list of current file versions held under legal hold for a
specific legal hold policy assignment.


## List previous file versions for legal hold policy assignment

Get a list of previous file versions for a legal hold
assignment.

In some cases you may only need the latest file versions instead. In these
cases, use the &#x60;GET  /legal_hold_policy_assignments/:id/files_on_hold&#x60; API
instead to return any current (latest) versions of a file for this legal hold
policy assignment.

Due to ongoing re-architecture efforts this API might not return all files
held for this policy ID. Instead, this API will only return past file versions
held in the newly developed architecture. The &#x60;GET /file_version_legal_holds&#x60;
API can be used to fetch current and past versions of files held within the
legacy architecture.

The &#x60;GET /legal_hold_policy_assignments?policy_id&#x3D;{id}&#x60; API can be used to
find a list of policy assignments for a given policy ID.

This operation is performed by calling function `get_legal_hold_policy_assignment_file_version_on_hold`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-legal-hold-policy-assignments-id-file-versions-on-hold/).

*Currently we don't have an example for calling `get_legal_hold_policy_assignment_file_version_on_hold` in integration tests*

### Arguments

- legal_hold_policy_assignment_id `str`
  - The ID of the legal hold policy assignment
  - Used as `legal_hold_policy_assignment_id` in path `path` of the API call
- query_params `Optional[GetLegalHoldPolicyAssignmentFileVersionOnHoldQueryParamsArg]`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `FileVersionLegalHolds`.

Returns the list of previous file versions held under legal hold for a
specific legal hold policy assignment.


