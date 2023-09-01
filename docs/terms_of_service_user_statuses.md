# TermsOfServiceUserStatusesManager

- [List terms of service user statuses](#list-terms-of-service-user-statuses)
- [Create terms of service status for new user](#create-terms-of-service-status-for-new-user)
- [Update terms of service status for existing user](#update-terms-of-service-status-for-existing-user)

## List terms of service user statuses

Retrieves an overview of users and their status for a
terms of service, including Whether they have accepted
the terms and when.

This operation is performed by calling function `get_term_of_service_user_statuses`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-terms-of-service-user-statuses/).

_Currently we don't have an example for calling `get_term_of_service_user_statuses` in integration tests_

### Arguments

- tos_id `str`
  - The ID of the terms of service.
- user_id `Optional[str]`
  - Limits results to the given user ID.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `TermsOfServiceUserStatuses`.

Returns a list of terms of service statuses.

## Create terms of service status for new user

Sets the status for a terms of service for a user.

This operation is performed by calling function `create_term_of_service_user_status`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-terms-of-service-user-statuses/).

_Currently we don't have an example for calling `create_term_of_service_user_status` in integration tests_

### Arguments

- tos `CreateTermOfServiceUserStatusTosArg`
  - The terms of service to set the status for.
- user `CreateTermOfServiceUserStatusUserArg`
  - The user to set the status for.
- is_accepted `bool`
  - Whether the user has accepted the terms.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `TermsOfServiceUserStatus`.

Returns a terms of service status object.

## Update terms of service status for existing user

Updates the status for a terms of service for a user.

This operation is performed by calling function `update_term_of_service_user_status_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-terms-of-service-user-statuses-id/).

_Currently we don't have an example for calling `update_term_of_service_user_status_by_id` in integration tests_

### Arguments

- terms_of_service_user_status_id `str`
  - The ID of the terms of service status. Example: "324234"
- is_accepted `bool`
  - Whether the user has accepted the terms.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `TermsOfServiceUserStatus`.

Returns the updated terms of service status object.
