<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [TermsOfServiceUserStatusesManager](#termsofserviceuserstatusesmanager)
  - [List terms of service user statuses](#list-terms-of-service-user-statuses)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Create terms of service status for new user](#create-terms-of-service-status-for-new-user)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Update terms of service status for existing user](#update-terms-of-service-status-for-existing-user)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# TermsOfServiceUserStatusesManager

## List terms of service user statuses

Retrieves an overview of users and their status for a
terms of service, including Whether they have accepted
the terms and when.

This operation is performed by calling function `get_term_of_service_user_statuses`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-terms-of-service-user-statuses/).

*Currently we don't have an example for calling `get_term_of_service_user_statuses` in integration tests*

### Arguments

- query_params `GetTermOfServiceUserStatusesQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `TermsOfServiceUserStatuses`.

Returns a list of terms of service statuses.


## Create terms of service status for new user

Sets the status for a terms of service for a user.

This operation is performed by calling function `create_term_of_service_user_status`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-terms-of-service-user-statuses/).

*Currently we don't have an example for calling `create_term_of_service_user_status` in integration tests*

### Arguments

- request_body `CreateTermOfServiceUserStatusRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `TermsOfServiceUserStatus`.

Returns a terms of service status object.


## Update terms of service status for existing user

Updates the status for a terms of service for a user.

This operation is performed by calling function `update_term_of_service_user_status_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-terms-of-service-user-statuses-id/).

*Currently we don't have an example for calling `update_term_of_service_user_status_by_id` in integration tests*

### Arguments

- terms_of_service_user_status_id `str`
  - The ID of the terms of service status.
  - Used as `terms_of_service_user_status_id` in path `path` of the API call
- request_body `UpdateTermOfServiceUserStatusByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `TermsOfServiceUserStatus`.

Returns the updated terms of service status object.


