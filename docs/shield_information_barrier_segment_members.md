<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [ShieldInformationBarrierSegmentMembersManager](#shieldinformationbarriersegmentmembersmanager)
  - [Get shield information barrier segment member by ID](#get-shield-information-barrier-segment-member-by-id)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Delete shield information barrier segment member by ID](#delete-shield-information-barrier-segment-member-by-id)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [List shield information barrier segment members](#list-shield-information-barrier-segment-members)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Create shield information barrier segment member](#create-shield-information-barrier-segment-member)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ShieldInformationBarrierSegmentMembersManager

## Get shield information barrier segment member by ID

Retrieves a shield information barrier
segment member by its ID.

This operation is performed by calling function `get_shield_information_barrier_segment_member_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barrier-segment-members-id/).

*Currently we don't have an example for calling `get_shield_information_barrier_segment_member_by_id` in integration tests*

### Arguments

- shield_information_barrier_segment_member_id `str`
  - The ID of the shield information barrier segment Member.
  - Used as `shield_information_barrier_segment_member_id` in path `path` of the API call


### Returns

This function returns a value of type `ShieldInformationBarrierSegmentMember`.

Returns the shield information barrier segment member object.


## Delete shield information barrier segment member by ID

Deletes a shield information barrier
segment member based on provided ID.

This operation is performed by calling function `delete_shield_information_barrier_segment_member_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-shield-information-barrier-segment-members-id/).

*Currently we don't have an example for calling `delete_shield_information_barrier_segment_member_by_id` in integration tests*

### Arguments

- shield_information_barrier_segment_member_id `str`
  - The ID of the shield information barrier segment Member.
  - Used as `shield_information_barrier_segment_member_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Returns an empty response if the
segment member was deleted successfully.


## List shield information barrier segment members

Lists shield information barrier segment members
based on provided segment IDs.

This operation is performed by calling function `get_shield_information_barrier_segment_members`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barrier-segment-members/).

*Currently we don't have an example for calling `get_shield_information_barrier_segment_members` in integration tests*

### Arguments

- query_params `GetShieldInformationBarrierSegmentMembersQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `None`.

Returns a paginated list of
shield information barrier segment member objects.


## Create shield information barrier segment member

Creates a new shield information barrier segment member.

This operation is performed by calling function `create_shield_information_barrier_segment_member`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-shield-information-barrier-segment-members/).

*Currently we don't have an example for calling `create_shield_information_barrier_segment_member` in integration tests*

### Arguments

- request_body `CreateShieldInformationBarrierSegmentMemberRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `ShieldInformationBarrierSegmentMember`.

Returns a new shield information barrier segment Member object.


