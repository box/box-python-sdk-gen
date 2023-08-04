<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [CollaborationAllowlistExemptTargetsManager](#collaborationallowlistexempttargetsmanager)
  - [List users exempt from collaboration domain restrictions](#list-users-exempt-from-collaboration-domain-restrictions)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Create user exemption from collaboration domain restrictions](#create-user-exemption-from-collaboration-domain-restrictions)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Get user exempt from collaboration domain restrictions](#get-user-exempt-from-collaboration-domain-restrictions)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Remove user from list of users exempt from domain restrictions](#remove-user-from-list-of-users-exempt-from-domain-restrictions)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

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


### Returns

This function returns a value of type `None`.

A blank response is returned if the exemption was
successfully deleted.


