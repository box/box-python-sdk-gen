<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [InvitesManager](#invitesmanager)
  - [Create user invite](#create-user-invite)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Get user invite status](#get-user-invite-status)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# InvitesManager

## Create user invite

Invites an existing external user to join an enterprise.

The existing user can not be part of another enterprise and
must already have a Box account. Once invited, the user will receive an
email and are prompted to accept the invitation within the
Box web application.

This method requires the &quot;Manage An Enterprise&quot; scope enabled for
the application, which can be enabled within the developer console.

This operation is performed by calling function `create_invite`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-invites/).

*Currently we don't have an example for calling `create_invite` in integration tests*

### Arguments

- request_body `CreateInviteRequestBodyArg`
  - Used as requestBody for the API call
- query_params `CreateInviteQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Invite`.

Returns a new invite object.


## Get user invite status

Returns the status of a user invite.

This operation is performed by calling function `get_invite_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-invites-id/).

*Currently we don't have an example for calling `get_invite_by_id` in integration tests*

### Arguments

- invite_id `str`
  - The ID of an invite.
  - Used as `invite_id` in path `path` of the API call
- query_params `GetInviteByIdQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Invite`.

Returns an invite object


