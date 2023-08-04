<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [TermsOfServicesManager](#termsofservicesmanager)
  - [List terms of services](#list-terms-of-services)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Create terms of service](#create-terms-of-service)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Get terms of service](#get-terms-of-service)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Update terms of service](#update-terms-of-service)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# TermsOfServicesManager

## List terms of services

Returns the current terms of service text and settings
for the enterprise.

This operation is performed by calling function `get_term_of_services`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-terms-of-services/).

*Currently we don't have an example for calling `get_term_of_services` in integration tests*

### Arguments

- query_params `GetTermOfServicesQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `TermsOfServices`.

Returns a collection of terms of service text and settings for the
enterprise.


## Create terms of service

Creates a terms of service for a given enterprise
and type of user.

This operation is performed by calling function `create_term_of_service`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-terms-of-services/).

*Currently we don't have an example for calling `create_term_of_service` in integration tests*

### Arguments

- request_body `CreateTermOfServiceRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `Task`.

Returns a new task object


## Get terms of service

Fetches a specific terms of service.

This operation is performed by calling function `get_term_of_service_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-terms-of-services-id/).

*Currently we don't have an example for calling `get_term_of_service_by_id` in integration tests*

### Arguments

- terms_of_service_id `str`
  - The ID of the terms of service.
  - Used as `terms_of_service_id` in path `path` of the API call


### Returns

This function returns a value of type `TermsOfService`.

Returns a terms of service object.


## Update terms of service

Updates a specific terms of service.

This operation is performed by calling function `update_term_of_service_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-terms-of-services-id/).

*Currently we don't have an example for calling `update_term_of_service_by_id` in integration tests*

### Arguments

- terms_of_service_id `str`
  - The ID of the terms of service.
  - Used as `terms_of_service_id` in path `path` of the API call
- request_body `UpdateTermOfServiceByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `TermsOfService`.

Returns an updated terms of service object.


