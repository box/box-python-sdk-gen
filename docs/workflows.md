<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [WorkflowsManager](#workflowsmanager)
  - [List workflows](#list-workflows)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Starts workflow based on request body](#starts-workflow-based-on-request-body)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# WorkflowsManager

## List workflows

Returns list of workflows that act on a given &#x60;folder ID&#x60;, and
have a flow with a trigger type of &#x60;WORKFLOW_MANUAL_START&#x60;.

You application must be authorized to use the &#x60;Manage Box Relay&#x60; application
scope within the developer console in to use this endpoint.

This operation is performed by calling function `get_workflows`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-workflows/).

*Currently we don't have an example for calling `get_workflows` in integration tests*

### Arguments

- query_params `GetWorkflowsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Workflows`.

Returns the workflow.


## Starts workflow based on request body

Initiates a flow with a trigger type of &#x60;WORKFLOW_MANUAL_START&#x60;.

You application must be authorized to use the &#x60;Manage Box Relay&#x60; application
scope within the developer console.

This operation is performed by calling function `create_workflow_start`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-workflows-id-start/).

*Currently we don't have an example for calling `create_workflow_start` in integration tests*

### Arguments

- workflow_id `str`
  - The ID of the workflow.
  - Used as `workflow_id` in path `path` of the API call
- request_body `CreateWorkflowStartRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `None`.

Starts the workflow.


