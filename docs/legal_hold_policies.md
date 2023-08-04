<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [LegalHoldPoliciesManager](#legalholdpoliciesmanager)
  - [List all legal hold policies](#list-all-legal-hold-policies)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Create legal hold policy](#create-legal-hold-policy)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Get legal hold policy](#get-legal-hold-policy)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Update legal hold policy](#update-legal-hold-policy)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)
  - [Remove legal hold policy](#remove-legal-hold-policy)
    - [Arguments](#arguments-4)
    - [Returns](#returns-4)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# LegalHoldPoliciesManager

## List all legal hold policies

Retrieves a list of legal hold policies that belong to
an enterprise.

This operation is performed by calling function `get_legal_hold_policies`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-legal-hold-policies/).

*Currently we don't have an example for calling `get_legal_hold_policies` in integration tests*

### Arguments

- query_params `GetLegalHoldPoliciesQueryParamsArg`
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


### Returns

This function returns a value of type `None`.

A blank response is returned if the policy was
successfully deleted.


