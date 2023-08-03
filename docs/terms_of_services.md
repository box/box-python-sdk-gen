# TermsOfServicesManager


- [List terms of services](#list-terms-of-services)
- [Create terms of service](#create-terms-of-service)
- [Get terms of service](#get-terms-of-service)
- [Update terms of service](#update-terms-of-service)

## List terms of services

Returns the current terms of service text and settings
for the enterprise.

This operation is performed by calling function `get_term_of_services`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-terms-of-services/).

*Currently we don't have an example for calling `get_term_of_services` in integration tests*

### Arguments

- tos_type `Optional[GetTermOfServicesTosTypeArg]`
  - Limits the results to the terms of service of the given type.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


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

- status `CreateTermOfServiceStatusArg`
  - Whether this terms of service is active.
- tos_type `Optional[CreateTermOfServiceTosTypeArg]`
  - The type of user to set the terms of service for.
- text `str`
  - The terms of service text to display to users.  The text can be set to empty if the `status` is set to `disabled`.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


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
  - The ID of the terms of service. Example: "324234"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


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
  - The ID of the terms of service. Example: "324234"
- status `UpdateTermOfServiceByIdStatusArg`
  - Whether this terms of service is active.
- text `str`
  - The terms of service text to display to users.  The text can be set to empty if the `status` is set to `disabled`.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `TermsOfService`.

Returns an updated terms of service object.


