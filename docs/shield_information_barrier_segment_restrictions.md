# ShieldInformationBarrierSegmentRestrictionsManager


- [Get shield information barrier segment restriction by ID](#get-shield-information-barrier-segment-restriction-by-id)
- [Delete shield information barrier segment restriction by ID](#delete-shield-information-barrier-segment-restriction-by-id)
- [List shield information barrier segment restrictions](#list-shield-information-barrier-segment-restrictions)
- [Create shield information barrier segment restriction](#create-shield-information-barrier-segment-restriction)

## Get shield information barrier segment restriction by ID

Retrieves a shield information barrier segment
restriction based on provided ID.

This operation is performed by calling function `get_shield_information_barrier_segment_restriction_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barrier-segment-restrictions-id/).

*Currently we don't have an example for calling `get_shield_information_barrier_segment_restriction_by_id` in integration tests*

### Arguments

- shield_information_barrier_segment_restriction_id `str`
  - The ID of the shield information barrier segment Restriction. Example: "4563"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


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
  - The ID of the shield information barrier segment Restriction. Example: "4563"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


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

- shield_information_barrier_segment_id `str`
  - The ID of the shield information barrier segment.
- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


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

- type `CreateShieldInformationBarrierSegmentRestrictionTypeArg`
  - The type of the shield barrier segment restriction for this member.
- shield_information_barrier `Optional[ShieldInformationBarrierBase]`
  - 
- shield_information_barrier_segment `CreateShieldInformationBarrierSegmentRestrictionShieldInformationBarrierSegmentArg`
  - The `type` and `id` of the requested shield information barrier segment.
- restricted_segment `CreateShieldInformationBarrierSegmentRestrictionRestrictedSegmentArg`
  - The `type` and `id` of the restricted shield information barrier segment.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `ShieldInformationBarrierSegmentRestriction`.

Returns the newly created Shield
Information Barrier Segment Restriction object.


