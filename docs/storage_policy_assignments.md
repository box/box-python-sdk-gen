<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [StoragePolicyAssignmentsManager](#storagepolicyassignmentsmanager)
  - [List storage policy assignments](#list-storage-policy-assignments)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Assign storage policy](#assign-storage-policy)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Get storage policy assignment](#get-storage-policy-assignment)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Update storage policy assignment](#update-storage-policy-assignment)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)
  - [Unassign storage policy](#unassign-storage-policy)
    - [Arguments](#arguments-4)
    - [Returns](#returns-4)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# StoragePolicyAssignmentsManager

## List storage policy assignments

Fetches all the storage policy assignment for an enterprise or user.

This operation is performed by calling function `get_storage_policy_assignments`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-storage-policy-assignments/).

*Currently we don't have an example for calling `get_storage_policy_assignments` in integration tests*

### Arguments

- query_params `GetStoragePolicyAssignmentsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `StoragePolicyAssignments`.

Returns a collection of storage policies for
the enterprise or user.


## Assign storage policy

Creates a storage policy assignment for an enterprise or user.

This operation is performed by calling function `create_storage_policy_assignment`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-storage-policy-assignments/).

*Currently we don't have an example for calling `create_storage_policy_assignment` in integration tests*

### Arguments

- request_body `CreateStoragePolicyAssignmentRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `StoragePolicyAssignment`.

Returns the new storage policy assignment created.


## Get storage policy assignment

Fetches a specific storage policy assignment.

This operation is performed by calling function `get_storage_policy_assignment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-storage-policy-assignments-id/).

*Currently we don't have an example for calling `get_storage_policy_assignment_by_id` in integration tests*

### Arguments

- storage_policy_assignment_id `str`
  - The ID of the storage policy assignment.
  - Used as `storage_policy_assignment_id` in path `path` of the API call


### Returns

This function returns a value of type `StoragePolicyAssignment`.

Returns a storage policy assignment object.


## Update storage policy assignment

Updates a specific storage policy assignment.

This operation is performed by calling function `update_storage_policy_assignment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-storage-policy-assignments-id/).

*Currently we don't have an example for calling `update_storage_policy_assignment_by_id` in integration tests*

### Arguments

- storage_policy_assignment_id `str`
  - The ID of the storage policy assignment.
  - Used as `storage_policy_assignment_id` in path `path` of the API call
- request_body `UpdateStoragePolicyAssignmentByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `StoragePolicyAssignment`.

Returns an updated storage policy assignment object.


## Unassign storage policy

Delete a storage policy assignment.

Deleting a storage policy assignment on a user
will have the user inherit the enterprise&#x27;s default
storage policy.

There is a rate limit for calling this endpoint of only
twice per user in a 24 hour time frame.

This operation is performed by calling function `delete_storage_policy_assignment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-storage-policy-assignments-id/).

*Currently we don't have an example for calling `delete_storage_policy_assignment_by_id` in integration tests*

### Arguments

- storage_policy_assignment_id `str`
  - The ID of the storage policy assignment.
  - Used as `storage_policy_assignment_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Returns an empty response when the storage policy
assignment is successfully deleted.


