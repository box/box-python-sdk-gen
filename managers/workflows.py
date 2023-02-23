from typing import Union

from base_object import BaseObject

from typing import List

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import Workflows

from schemas import ClientError

class GetWorkflowsOptionsArg(BaseObject):
    def __init__(self, triggerType: Union[None, str] = None, limit: Union[None, int] = None, marker: Union[None, str] = None, **kwargs):
        """
        :param triggerType: Type of trigger to search for.
        :type triggerType: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.triggerType = triggerType
        self.limit = limit
        self.marker = marker

class PostWorkflowsIdStartRequestBodyArgTypeField:
    pass

class PostWorkflowsIdStartRequestBodyArgFlowField(BaseObject):
    def __init__(self, type: Union[None, str] = None, id: Union[None, str] = None, **kwargs):
        """
        :param type: The type of the flow object
        :type type: Union[None, str], optional
        :param id: The id of the flow
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PostWorkflowsIdStartRequestBodyArgFilesFieldTypeField:
    pass

class PostWorkflowsIdStartRequestBodyArgFilesField(BaseObject):
    def __init__(self, type: Union[None, PostWorkflowsIdStartRequestBodyArgFilesFieldTypeField] = None, id: Union[None, str] = None, **kwargs):
        """
        :param type: The type of the file object
        :type type: Union[None, PostWorkflowsIdStartRequestBodyArgFilesFieldTypeField], optional
        :param id: The id of the file
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PostWorkflowsIdStartRequestBodyArgFolderFieldTypeField:
    pass

class PostWorkflowsIdStartRequestBodyArgFolderField(BaseObject):
    def __init__(self, type: Union[None, PostWorkflowsIdStartRequestBodyArgFolderFieldTypeField] = None, id: Union[None, str] = None, **kwargs):
        """
        :param type: The type of the folder object
        :type type: Union[None, PostWorkflowsIdStartRequestBodyArgFolderFieldTypeField], optional
        :param id: The id of the folder
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PostWorkflowsIdStartRequestBodyArgOutcomesFieldTypeField:
    pass

class PostWorkflowsIdStartRequestBodyArgOutcomesField(BaseObject):
    def __init__(self, id: Union[None, str] = None, type: Union[None, PostWorkflowsIdStartRequestBodyArgOutcomesFieldTypeField] = None, parameter: Union[None, str] = None, **kwargs):
        """
        :param id: The id of the outcome
        :type id: Union[None, str], optional
        :param type: The type of the outcome object
        :type type: Union[None, PostWorkflowsIdStartRequestBodyArgOutcomesFieldTypeField], optional
        :param parameter: This is a placeholder example for various objects that
            can be passed in - refer to the guides section to find
            out more information.
        :type parameter: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.parameter = parameter

class PostWorkflowsIdStartRequestBodyArg(BaseObject):
    def __init__(self, flow: PostWorkflowsIdStartRequestBodyArgFlowField, files: List[PostWorkflowsIdStartRequestBodyArgFilesField], folder: PostWorkflowsIdStartRequestBodyArgFolderField, type: Union[None, PostWorkflowsIdStartRequestBodyArgTypeField] = None, outcomes: Union[None, List[PostWorkflowsIdStartRequestBodyArgOutcomesField]] = None, **kwargs):
        """
        :param flow: The flow that will be triggered
        :type flow: PostWorkflowsIdStartRequestBodyArgFlowField
        :param files: The array of files for which the workflow should start. All files
            must be in the workflow's configured folder.
        :type files: List[PostWorkflowsIdStartRequestBodyArgFilesField]
        :param folder: The folder object for which the workflow is configured.
        :type folder: PostWorkflowsIdStartRequestBodyArgFolderField
        :param type: The type of the parameters object
        :type type: Union[None, PostWorkflowsIdStartRequestBodyArgTypeField], optional
        :param outcomes: A list of outcomes required to be configured at start time.
        :type outcomes: Union[None, List[PostWorkflowsIdStartRequestBodyArgOutcomesField]], optional
        """
        super().__init__(**kwargs)
        self.flow = flow
        self.files = files
        self.folder = folder
        self.type = type
        self.outcomes = outcomes

class WorkflowsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getWorkflows(self, folderId: str, options: GetWorkflowsOptionsArg = None) -> Workflows:
        """
        Returns list of workflows that act on a given `folder ID`, and
        
        have a flow with a trigger type of `WORKFLOW_MANUAL_START`.

        
        You application must be authorized to use the `Manage Box Relay` application

        
        scope within the developer console in to use this endpoint.

        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        """
        if options is None:
            options = GetWorkflowsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/workflows']), FetchOptions(method='GET', params={'folder_id': folderId, 'trigger_type': options.triggerType, 'limit': options.limit, 'marker': options.marker}, auth=self.auth))
        return Workflows.from_dict(json.loads(response.text))
    def postWorkflowsIdStart(self, workflowId: str, requestBody: PostWorkflowsIdStartRequestBodyArg):
        """
        Initiates a flow with a trigger type of `WORKFLOW_MANUAL_START`.
        
        You application must be authorized to use the `Manage Box Relay` application

        
        scope within the developer console.

        :param workflowId: The ID of the workflow.
            Example: "12345"
        :type workflowId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/workflows/', workflowId, '/start']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return response.content