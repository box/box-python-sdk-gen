# WorkflowsManager

- [List workflows](#list-workflows)
- [Starts workflow based on request body](#starts-workflow-based-on-request-body)

## List workflows

Returns list of workflows that act on a given `folder ID`, and
have a flow with a trigger type of `WORKFLOW_MANUAL_START`.

You application must be authorized to use the `Manage Box Relay` application
scope within the developer console in to use this endpoint.

This operation is performed by calling function `get_workflows`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-workflows/).

_Currently we don't have an example for calling `get_workflows` in integration tests_

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder. The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`. The root folder of a Box account is always represented by the ID `0`.
- trigger_type `Optional[str]`
  - Type of trigger to search for.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination. This requires `usemarker` to be set to `true`.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `Workflows`.

Returns the workflow.

## Starts workflow based on request body

Initiates a flow with a trigger type of `WORKFLOW_MANUAL_START`.

You application must be authorized to use the `Manage Box Relay` application
scope within the developer console.

This operation is performed by calling function `create_workflow_start`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-workflows-id-start/).

_Currently we don't have an example for calling `create_workflow_start` in integration tests_

### Arguments

- workflow_id `str`
  - The ID of the workflow. Example: "12345"
- type `Optional[CreateWorkflowStartTypeArg]`
  - The type of the parameters object
- flow `CreateWorkflowStartFlowArg`
  - The flow that will be triggered
- files `List[CreateWorkflowStartFilesArg]`
  - The array of files for which the workflow should start. All files must be in the workflow's configured folder.
- folder `CreateWorkflowStartFolderArg`
  - The folder object for which the workflow is configured.
- outcomes `Optional[List[CreateWorkflowStartOutcomesArg]]`
  - A list of outcomes required to be configured at start time.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `None`.

Starts the workflow.
