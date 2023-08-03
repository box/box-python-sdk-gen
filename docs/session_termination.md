# SessionTerminationManager

## Create jobs to terminate users session

Validates the roles and permissions of the user,
and creates asynchronous jobs
to terminate the user&#x27;s sessions.
Returns the status for the POST request.

This operation is performed by calling function `create_user_terminate_session`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-users-terminate-sessions/).

*Currently we don't have an example for calling `create_user_terminate_session` in integration tests*

### Arguments

- request_body `CreateUserTerminateSessionRequestBodyArg`
  - Used as requestBody for the API call
- headers `CreateUserTerminateSessionHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `SessionTerminationMessage`.

Returns a message about the request status.


## Create jobs to terminate user group session

Validates the roles and permissions of the group,
and creates asynchronous jobs
to terminate the group&#x27;s sessions.
Returns the status for the POST request.

This operation is performed by calling function `create_group_terminate_session`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-groups-terminate-sessions/).

*Currently we don't have an example for calling `create_group_terminate_session` in integration tests*

### Arguments

- request_body `CreateGroupTerminateSessionRequestBodyArg`
  - Used as requestBody for the API call
- headers `CreateGroupTerminateSessionHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `SessionTerminationMessage`.

Returns a message about the request status.


