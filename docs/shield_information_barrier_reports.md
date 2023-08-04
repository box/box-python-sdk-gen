<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ShieldInformationBarrierReportsManager](#shieldinformationbarrierreportsmanager)
  - [List shield information barrier reports](#list-shield-information-barrier-reports)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Create shield information barrier report](#create-shield-information-barrier-report)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Get shield information barrier report by ID](#get-shield-information-barrier-report-by-id)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ShieldInformationBarrierReportsManager

## List shield information barrier reports

Lists shield information barrier reports with specific IDs.

This operation is performed by calling function `get_shield_information_barrier_reports`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barrier-reports/).

*Currently we don't have an example for calling `get_shield_information_barrier_reports` in integration tests*

### Arguments

- query_params `GetShieldInformationBarrierReportsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `None`.

Returns a paginated list of shield information barrier report objects.


## Create shield information barrier report

Creates a shield information barrier report for a given barrier.

This operation is performed by calling function `create_shield_information_barrier_report`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-shield-information-barrier-reports/).

*Currently we don't have an example for calling `create_shield_information_barrier_report` in integration tests*

### Arguments

- request_body `ShieldInformationBarrierReference`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `ShieldInformationBarrierReport`.

Returns the shield information barrier report information object.


## Get shield information barrier report by ID

Retrieves a shield information barrier report by its ID.

This operation is performed by calling function `get_shield_information_barrier_report_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shield-information-barrier-reports-id/).

*Currently we don't have an example for calling `get_shield_information_barrier_report_by_id` in integration tests*

### Arguments

- shield_information_barrier_report_id `str`
  - The ID of the shield information barrier Report.
  - Used as `shield_information_barrier_report_id` in path `path` of the API call


### Returns

This function returns a value of type `ShieldInformationBarrierReport`.

Returns the  shield information barrier report object.


