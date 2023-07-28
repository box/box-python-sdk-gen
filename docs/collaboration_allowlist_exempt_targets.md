# CollaborationAllowlistExemptTargetsManager

## List users exempt from collaboration domain restrictions

Returns a list of users who have been exempt from the collaboration
domain restrictions.

This operation is performed by calling function `get_collaboration_whitelist_exempt_targets`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-collaboration-whitelist-exempt-targets/).

*Currently we don't have an example for calling `get_collaboration_whitelist_exempt_targets` in integration tests*

### Arguments

- query_params `GetCollaborationWhitelistExemptTargetsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `CollaborationAllowlistExemptTargets`.

Returns a collection of user exemptions.


## Create user exemption from collaboration domain restrictions

Exempts a user from the restrictions set out by the allowed list of domains
for collaborations.

This operation is performed by calling function `create_collaboration_whitelist_exempt_target`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-collaboration-whitelist-exempt-targets/).

*Currently we don't have an example for calling `create_collaboration_whitelist_exempt_target` in integration tests*

### Arguments

- request_body `CreateCollaborationWhitelistExemptTargetRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `CollaborationAllowlistExemptTarget`.

Returns a new exemption entry.


## Get user exempt from collaboration domain restrictions

Returns a users who has been exempt from the collaboration
domain restrictions.

This operation is performed by calling function `get_collaboration_whitelist_exempt_target_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-collaboration-whitelist-exempt-targets-id/).

*Currently we don't have an example for calling `get_collaboration_whitelist_exempt_target_by_id` in integration tests*

### Arguments

- collaboration_whitelist_exempt_target_id `str`
  - The ID of the exemption to the list.
  - Used as `collaboration_whitelist_exempt_target_id` in path `path` of the API call


### Returns

This function returns a value of type `CollaborationAllowlistExemptTarget`.

Returns the user&#x27;s exempted from the list of collaboration domains.


## Remove user from list of users exempt from domain restrictions

Removes a user&#x27;s exemption from the restrictions set out by the allowed list
of domains for collaborations.

This operation is performed by calling function `delete_collaboration_whitelist_exempt_target_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-collaboration-whitelist-exempt-targets-id/).

*Currently we don't have an example for calling `delete_collaboration_whitelist_exempt_target_by_id` in integration tests*

### Arguments

- collaboration_whitelist_exempt_target_id `str`
  - The ID of the exemption to the list.
  - Used as `collaboration_whitelist_exempt_target_id` in path `path` of the API call


