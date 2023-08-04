<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ShieldInformationBarrierSegmentsManager](#shieldinformationbarriersegmentsmanager)
  - [Get shield information barrier segment with specified ID](#get-shield-information-barrier-segment-with-specified-id)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Update shield information barrier segment with specified ID](#update-shield-information-barrier-segment-with-specified-id)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Delete shield information barrier segment](#delete-shield-information-barrier-segment)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [List shield information barrier segments](#list-shield-information-barrier-segments)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)
  - [Create shield information barrier segment](#create-shield-information-barrier-segment)
    - [Arguments](#arguments-4)
    - [Returns](#returns-4)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ShieldInformationBarrierSegmentsManager

## Get shield information barrier segment with specified ID

Retrieves shield information barrier segment based on provided ID..

This operation is performed by calling function `get_shield_information_barrier_segment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barrier-segments-id/).

*Currently we don't have an example for calling `get_shield_information_barrier_segment_by_id` in integration tests*

### Arguments

- shield_information_barrier_segment_id `str`
  - The ID of the shield information barrier segment.
  - Used as `shield_information_barrier_segment_id` in path `path` of the API call


### Returns

This function returns a value of type `ShieldInformationBarrierSegment`.

Returns the shield information barrier segment object.


## Update shield information barrier segment with specified ID

Updates the shield information barrier segment based on provided ID..

This operation is performed by calling function `update_shield_information_barrier_segment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-shield-information-barrier-segments-id/).

*Currently we don't have an example for calling `update_shield_information_barrier_segment_by_id` in integration tests*

### Arguments

- shield_information_barrier_segment_id `str`
  - The ID of the shield information barrier segment.
  - Used as `shield_information_barrier_segment_id` in path `path` of the API call
- request_body `UpdateShieldInformationBarrierSegmentByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `ShieldInformationBarrierSegment`.

Returns the updated shield information barrier segment object.


## Delete shield information barrier segment

Deletes the shield information barrier segment
based on provided ID.

This operation is performed by calling function `delete_shield_information_barrier_segment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-shield-information-barrier-segments-id/).

*Currently we don't have an example for calling `delete_shield_information_barrier_segment_by_id` in integration tests*

### Arguments

- shield_information_barrier_segment_id `str`
  - The ID of the shield information barrier segment.
  - Used as `shield_information_barrier_segment_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Empty body in response


## List shield information barrier segments

Retrieves a list of shield information barrier segment objects
for the specified Information Barrier ID.

This operation is performed by calling function `get_shield_information_barrier_segments`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barrier-segments/).

*Currently we don't have an example for calling `get_shield_information_barrier_segments` in integration tests*

### Arguments

- query_params `GetShieldInformationBarrierSegmentsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `None`.

Returns a paginated list of shield information barrier segment objects.


## Create shield information barrier segment

Creates a shield information barrier segment.

This operation is performed by calling function `create_shield_information_barrier_segment`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-shield-information-barrier-segments/).

*Currently we don't have an example for calling `create_shield_information_barrier_segment` in integration tests*

### Arguments

- request_body `CreateShieldInformationBarrierSegmentRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `ShieldInformationBarrierSegment`.

Returns a new shield information barrier segment object.


