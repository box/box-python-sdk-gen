# ShieldInformationBarriersManager

## Get shield information barrier with specified ID

Get shield information barrier based on provided ID..

This operation is performed by calling function `get_shield_information_barrier_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barriers-id/).

*Currently we don't have an example for calling `get_shield_information_barrier_by_id` in integration tests*

### Arguments

- shield_information_barrier_id `str`
  - The ID of the shield information barrier.
  - Used as `shield_information_barrier_id` in path `path` of the API call


### Returns

This function returns a value of type `ShieldInformationBarrier`.

Returns the shield information barrier object.


## Add changed status of shield information barrier with specified ID

Change status of shield information barrier with the specified ID.

This operation is performed by calling function `create_shield_information_barrier_change_status`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-shield-information-barriers-change-status/).

*Currently we don't have an example for calling `create_shield_information_barrier_change_status` in integration tests*

### Arguments

- request_body `CreateShieldInformationBarrierChangeStatusRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `ShieldInformationBarrier`.

Returns the updated shield information barrier object.


## List shield information barriers

Retrieves a list of shield information barrier objects
for the enterprise of JWT.

This operation is performed by calling function `get_shield_information_barriers`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barriers/).

*Currently we don't have an example for calling `get_shield_information_barriers` in integration tests*

### Arguments

- query_params `Optional[GetShieldInformationBarriersQueryParamsArg]`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `None`.

Returns a paginated list of
shield information barrier objects,
empty list if currently no barrier.


## Create shield information barrier

Creates a shield information barrier to
separate individuals/groups within the same
firm and prevents confidential information passing between them.

This operation is performed by calling function `create_shield_information_barrier`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-shield-information-barriers/).

*Currently we don't have an example for calling `create_shield_information_barrier` in integration tests*

### Arguments

- request_body `ShieldInformationBarrier`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `ShieldInformationBarrier`.

Returns a new shield information barrier object.


