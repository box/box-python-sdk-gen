# RetentionPolicyAssignmentsManager

## List retention policy assignments

Returns a list of all retention policy assignments associated with a specified
retention policy.

This operation is performed by calling function `get_retention_policy_assignments`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-retention-policies-id-assignments/).

*Currently we don't have an example for calling `get_retention_policy_assignments` in integration tests*

### Arguments

- retention_policy_id `str`
  - The ID of the retention policy.
  - Used as `retention_policy_id` in path `path` of the API call
- query_params `GetRetentionPolicyAssignmentsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `RetentionPolicyAssignments`.

Returns a list of the retention policy assignments associated with the
specified retention policy.


## Assign retention policy

Assigns a retention policy to an item.

This operation is performed by calling function `create_retention_policy_assignment`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-retention-policy-assignments/).

*Currently we don't have an example for calling `create_retention_policy_assignment` in integration tests*

### Arguments

- request_body `CreateRetentionPolicyAssignmentRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `RetentionPolicyAssignment`.

Returns a new retention policy assignment object.


## Get retention policy assignment

Retrieves a retention policy assignment

This operation is performed by calling function `get_retention_policy_assignment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-retention-policy-assignments-id/).

*Currently we don't have an example for calling `get_retention_policy_assignment_by_id` in integration tests*

### Arguments

- retention_policy_assignment_id `str`
  - The ID of the retention policy assignment.
  - Used as `retention_policy_assignment_id` in path `path` of the API call
- query_params `GetRetentionPolicyAssignmentByIdQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `RetentionPolicyAssignment`.

Returns the retention policy assignment object.


## Remove retention policy assignment

Removes a retention policy assignment
applied to content.

This operation is performed by calling function `delete_retention_policy_assignment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-retention-policy-assignments-id/).

*Currently we don't have an example for calling `delete_retention_policy_assignment_by_id` in integration tests*

### Arguments

- retention_policy_assignment_id `str`
  - The ID of the retention policy assignment.
  - Used as `retention_policy_assignment_id` in path `path` of the API call


## Get files under retention

Returns a list of files under retention for a retention policy assignment.

This operation is performed by calling function `get_retention_policy_assignment_file_under_retention`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-retention-policy-assignments-id-files-under-retention/).

*Currently we don't have an example for calling `get_retention_policy_assignment_file_under_retention` in integration tests*

### Arguments

- retention_policy_assignment_id `str`
  - The ID of the retention policy assignment.
  - Used as `retention_policy_assignment_id` in path `path` of the API call
- query_params `GetRetentionPolicyAssignmentFileUnderRetentionQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `FilesUnderRetention`.

Returns a list of files under retention that are associated with the
specified retention policy assignment.


## Get file versions under retention

Returns a list of file versions under retention for a retention policy
assignment.

This operation is performed by calling function `get_retention_policy_assignment_file_version_under_retention`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-retention-policy-assignments-id-file-versions-under-retention/).

*Currently we don't have an example for calling `get_retention_policy_assignment_file_version_under_retention` in integration tests*

### Arguments

- retention_policy_assignment_id `str`
  - The ID of the retention policy assignment.
  - Used as `retention_policy_assignment_id` in path `path` of the API call
- query_params `GetRetentionPolicyAssignmentFileVersionUnderRetentionQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `FilesUnderRetention`.

Returns a list of file versions under retention that are associated with
the specified retention policy assignment.


