# LegalHoldPoliciesManager

## List all legal hold policies

Retrieves a list of legal hold policies that belong to
an enterprise.

This operation is performed by calling function `get_legal_hold_policies`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-legal-hold-policies/).

*Currently we don't have an example for calling `get_legal_hold_policies` in integration tests*

### Arguments

- query_params `Optional[GetLegalHoldPoliciesQueryParamsArg]`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `LegalHoldPolicies`.

Returns a list of legal hold policies.


## Create legal hold policy

Create a new legal hold policy.

This operation is performed by calling function `create_legal_hold_policy`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-legal-hold-policies/).

*Currently we don't have an example for calling `create_legal_hold_policy` in integration tests*

### Arguments

- request_body `CreateLegalHoldPolicyRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `LegalHoldPolicy`.

Returns a new legal hold policy object.


## Get legal hold policy

Retrieve a legal hold policy.

This operation is performed by calling function `get_legal_hold_policy_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-legal-hold-policies-id/).

*Currently we don't have an example for calling `get_legal_hold_policy_by_id` in integration tests*

### Arguments

- legal_hold_policy_id `str`
  - The ID of the legal hold policy
  - Used as `legal_hold_policy_id` in path `path` of the API call


### Returns

This function returns a value of type `LegalHoldPolicy`.

Returns a legal hold policy object.


## Update legal hold policy

Update legal hold policy.

This operation is performed by calling function `update_legal_hold_policy_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-legal-hold-policies-id/).

*Currently we don't have an example for calling `update_legal_hold_policy_by_id` in integration tests*

### Arguments

- legal_hold_policy_id `str`
  - The ID of the legal hold policy
  - Used as `legal_hold_policy_id` in path `path` of the API call
- request_body `UpdateLegalHoldPolicyByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `LegalHoldPolicy`.

Returns a new legal hold policy object.


## Remove legal hold policy

Delete an existing legal hold policy.

This is an asynchronous process. The policy will not be
fully deleted yet when the response returns.

This operation is performed by calling function `delete_legal_hold_policy_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-legal-hold-policies-id/).

*Currently we don't have an example for calling `delete_legal_hold_policy_by_id` in integration tests*

### Arguments

- legal_hold_policy_id `str`
  - The ID of the legal hold policy
  - Used as `legal_hold_policy_id` in path `path` of the API call


