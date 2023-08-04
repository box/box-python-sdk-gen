<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [ShieldInformationBarrierSegmentRestrictionsManager](#shieldinformationbarriersegmentrestrictionsmanager)
  - [Get shield information barrier segment restriction by ID](#get-shield-information-barrier-segment-restriction-by-id)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Delete shield information barrier segment restriction by ID](#delete-shield-information-barrier-segment-restriction-by-id)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [List shield information barrier segment restrictions](#list-shield-information-barrier-segment-restrictions)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Create shield information barrier segment restriction](#create-shield-information-barrier-segment-restriction)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ShieldInformationBarrierSegmentRestrictionsManager

## Get shield information barrier segment restriction by ID

Retrieves a shield information barrier segment
restriction based on provided ID.

This operation is performed by calling function `get_shield_information_barrier_segment_restriction_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barrier-segment-restrictions-id/).

*Currently we don't have an example for calling `get_shield_information_barrier_segment_restriction_by_id` in integration tests*

### Arguments

- shield_information_barrier_segment_restriction_id `str`
  - The ID of the shield information barrier segment Restriction.
  - Used as `shield_information_barrier_segment_restriction_id` in path `path` of the API call


### Returns

This function returns a value of type `ShieldInformationBarrierSegmentRestriction`.

Returns the shield information barrier segment
restriction object.


## Delete shield information barrier segment restriction by ID

Delete shield information barrier segment restriction
based on provided ID.

This operation is performed by calling function `delete_shield_information_barrier_segment_restriction_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-shield-information-barrier-segment-restrictions-id/).

*Currently we don't have an example for calling `delete_shield_information_barrier_segment_restriction_by_id` in integration tests*

### Arguments

- shield_information_barrier_segment_restriction_id `str`
  - The ID of the shield information barrier segment Restriction.
  - Used as `shield_information_barrier_segment_restriction_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Empty body in response


## List shield information barrier segment restrictions

Lists shield information barrier segment restrictions
based on provided segment ID.

This operation is performed by calling function `get_shield_information_barrier_segment_restrictions`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barrier-segment-restrictions/).

*Currently we don't have an example for calling `get_shield_information_barrier_segment_restrictions` in integration tests*

### Arguments

- query_params `GetShieldInformationBarrierSegmentRestrictionsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `None`.

Returns a paginated list of
shield information barrier segment restriction objects.


## Create shield information barrier segment restriction

Creates a shield information barrier
segment restriction object.

This operation is performed by calling function `create_shield_information_barrier_segment_restriction`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-shield-information-barrier-segment-restrictions/).

*Currently we don't have an example for calling `create_shield_information_barrier_segment_restriction` in integration tests*

### Arguments

- request_body `CreateShieldInformationBarrierSegmentRestrictionRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `ShieldInformationBarrierSegmentRestriction`.

Returns the newly created Shield
Information Barrier Segment Restriction object.


