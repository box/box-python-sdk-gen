# ShieldInformationBarrierReportsManager

- [List shield information barrier reports](#list-shield-information-barrier-reports)
- [Create shield information barrier report](#create-shield-information-barrier-report)
- [Get shield information barrier report by ID](#get-shield-information-barrier-report-by-id)

## List shield information barrier reports

Lists shield information barrier reports.

This operation is performed by calling function `get_shield_information_barrier_reports`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barrier-reports/).

_Currently we don't have an example for calling `get_shield_information_barrier_reports` in integration tests_

### Arguments

- shield_information_barrier_id `str`
  - The ID of the shield information barrier.
- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination. This requires `usemarker` to be set to `true`.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `ShieldInformationBarrierReports`.

Returns a paginated list of shield information barrier report objects.

## Create shield information barrier report

Creates a shield information barrier report for a given barrier.

This operation is performed by calling function `create_shield_information_barrier_report`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-shield-information-barrier-reports/).

_Currently we don't have an example for calling `create_shield_information_barrier_report` in integration tests_

### Arguments

- shield_information_barrier `Optional[ShieldInformationBarrierBase]`
  -
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `ShieldInformationBarrierReport`.

Returns the shield information barrier report information object.

## Get shield information barrier report by ID

Retrieves a shield information barrier report by its ID.

This operation is performed by calling function `get_shield_information_barrier_report_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barrier-reports-id/).

_Currently we don't have an example for calling `get_shield_information_barrier_report_by_id` in integration tests_

### Arguments

- shield_information_barrier_report_id `str`
  - The ID of the shield information barrier Report. Example: "3423"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `ShieldInformationBarrierReport`.

Returns the shield information barrier report object.
