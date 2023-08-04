<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [RetentionPoliciesManager](#retentionpoliciesmanager)
  - [List retention policies](#list-retention-policies)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Create retention policy](#create-retention-policy)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Get retention policy](#get-retention-policy)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Update retention policy](#update-retention-policy)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)
  - [Delete retention policy](#delete-retention-policy)
    - [Arguments](#arguments-4)
    - [Returns](#returns-4)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# RetentionPoliciesManager

## List retention policies

Retrieves all of the retention policies for an enterprise.

This operation is performed by calling function `get_retention_policies`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-retention-policies/).

*Currently we don't have an example for calling `get_retention_policies` in integration tests*

### Arguments

- query_params `GetRetentionPoliciesQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `RetentionPolicies`.

Returns a list retention policies in the enterprise.


## Create retention policy

Creates a retention policy.

This operation is performed by calling function `create_retention_policy`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-retention-policies/).

*Currently we don't have an example for calling `create_retention_policy` in integration tests*

### Arguments

- request_body `CreateRetentionPolicyRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `RetentionPolicy`.

Returns a new retention policy object.


## Get retention policy

Retrieves a retention policy.

This operation is performed by calling function `get_retention_policy_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-retention-policies-id/).

*Currently we don't have an example for calling `get_retention_policy_by_id` in integration tests*

### Arguments

- retention_policy_id `str`
  - The ID of the retention policy.
  - Used as `retention_policy_id` in path `path` of the API call
- query_params `GetRetentionPolicyByIdQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `RetentionPolicy`.

Returns the retention policy object.


## Update retention policy

Updates a retention policy.

This operation is performed by calling function `update_retention_policy_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-retention-policies-id/).

*Currently we don't have an example for calling `update_retention_policy_by_id` in integration tests*

### Arguments

- retention_policy_id `str`
  - The ID of the retention policy.
  - Used as `retention_policy_id` in path `path` of the API call
- request_body `UpdateRetentionPolicyByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `RetentionPolicy`.

Returns the updated retention policy object.


## Delete retention policy

Permanently deletes a retention policy.

This operation is performed by calling function `delete_retention_policy_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-retention-policies-id/).

*Currently we don't have an example for calling `delete_retention_policy_by_id` in integration tests*

### Arguments

- retention_policy_id `str`
  - The ID of the retention policy.
  - Used as `retention_policy_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Returns an empty response when the policy has been deleted.


