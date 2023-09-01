# InvitesManager

- [Create user invite](#create-user-invite)
- [Get user invite status](#get-user-invite-status)

## Create user invite

Invites an existing external user to join an enterprise.

The existing user can not be part of another enterprise and
must already have a Box account. Once invited, the user will receive an
email and are prompted to accept the invitation within the
Box web application.

This method requires the "Manage An Enterprise" scope enabled for
the application, which can be enabled within the developer console.

This operation is performed by calling function `create_invite`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-invites/).

_Currently we don't have an example for calling `create_invite` in integration tests_

### Arguments

- enterprise `CreateInviteEnterpriseArg`
  - The enterprise to invite the user to
- actionable_by `CreateInviteActionableByArg`
  - The user to invite
- fields `Optional[str]`
  - A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `Invite`.

Returns a new invite object.

## Get user invite status

Returns the status of a user invite.

This operation is performed by calling function `get_invite_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-invites-id/).

_Currently we don't have an example for calling `get_invite_by_id` in integration tests_

### Arguments

- invite_id `str`
  - The ID of an invite. Example: "213723"
- fields `Optional[str]`
  - A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `Invite`.

Returns an invite object
