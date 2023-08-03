# ShieldInformationBarriersManager


- [Get shield information barrier with specified ID](#get-shield-information-barrier-with-specified-id)
- [Add changed status of shield information barrier with specified ID](#add-changed-status-of-shield-information-barrier-with-specified-id)
- [List shield information barriers](#list-shield-information-barriers)
- [Create shield information barrier](#create-shield-information-barrier)

## Get shield information barrier with specified ID

Get shield information barrier based on provided ID..

This operation is performed by calling function `get_shield_information_barrier_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barriers-id/).

*Currently we don't have an example for calling `get_shield_information_barrier_by_id` in integration tests*

### Arguments

- shield_information_barrier_id `str`
  - The ID of the shield information barrier. Example: "1910967"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


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

- id `str`
  - The ID of the shield information barrier.
- status `CreateShieldInformationBarrierChangeStatusStatusArg`
  - The desired status for the shield information barrier.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


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

- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


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

- id `Optional[str]`
  - The unique identifier for the shield information barrier
- type `Optional[CreateShieldInformationBarrierTypeArg]`
  - The type of the shield information barrier
- enterprise `Optional[EnterpriseBase]`
  - 
- status `Optional[CreateShieldInformationBarrierStatusArg]`
  - Status of the shield information barrier
- created_at `Optional[str]`
  - ISO date time string when this shield information barrier object was created.
- created_by `Optional[UserBase]`
  - 
- updated_at `Optional[str]`
  - ISO date time string when this shield information barrier was updated.
- updated_by `Optional[UserBase]`
  - 
- enabled_at `Optional[str]`
  - ISO date time string when this shield information barrier was enabled.
- enabled_by `Optional[UserBase]`
  - 
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `ShieldInformationBarrier`.

Returns a new shield information barrier object.


