from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

from typing import List

import json

from box_sdk.schemas import Workflows

from box_sdk.schemas import ClientError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetWorkflowsOptionsArg(BaseObject):
    def __init__(self, trigger_type: Union[None, str] = None, limit: Union[None, int] = None, marker: Union[None, str] = None, **kwargs):
        """
        :param trigger_type: Type of trigger to search for.
        :type trigger_type: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.trigger_type = trigger_type
        self.limit = limit
        self.marker = marker

class CreateWorkflowStartRequestBodyArgTypeField(str, Enum):
    WORKFLOW_PARAMETERS = 'workflow_parameters'

class CreateWorkflowStartRequestBodyArgFlowField(BaseObject):
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

class CreateWorkflowStartRequestBodyArgFilesFieldTypeField(str, Enum):
    FILE = 'file'

class CreateWorkflowStartRequestBodyArgFilesField(BaseObject):
    def __init__(self, type: Union[None, CreateWorkflowStartRequestBodyArgFilesFieldTypeField] = None, id: Union[None, str] = None, **kwargs):
        """
        :param type: The type of the file object
        :type type: Union[None, CreateWorkflowStartRequestBodyArgFilesFieldTypeField], optional
        :param id: The id of the file
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class CreateWorkflowStartRequestBodyArgFolderFieldTypeField(str, Enum):
    FOLDER = 'folder'

class CreateWorkflowStartRequestBodyArgFolderField(BaseObject):
    def __init__(self, type: Union[None, CreateWorkflowStartRequestBodyArgFolderFieldTypeField] = None, id: Union[None, str] = None, **kwargs):
        """
        :param type: The type of the folder object
        :type type: Union[None, CreateWorkflowStartRequestBodyArgFolderFieldTypeField], optional
        :param id: The id of the folder
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class CreateWorkflowStartRequestBodyArgOutcomesFieldTypeField(str, Enum):
    OUTCOME = 'outcome'

class CreateWorkflowStartRequestBodyArgOutcomesField(BaseObject):
    def __init__(self, id: Union[None, str] = None, type: Union[None, CreateWorkflowStartRequestBodyArgOutcomesFieldTypeField] = None, parameter: Union[None, str] = None, **kwargs):
        """
        :param id: The id of the outcome
        :type id: Union[None, str], optional
        :param type: The type of the outcome object
        :type type: Union[None, CreateWorkflowStartRequestBodyArgOutcomesFieldTypeField], optional
        :param parameter: This is a placeholder example for various objects that
            can be passed in - refer to the guides section to find
            out more information.
        :type parameter: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.parameter = parameter

class CreateWorkflowStartRequestBodyArg(BaseObject):
    def __init__(self, flow: CreateWorkflowStartRequestBodyArgFlowField, files: List[CreateWorkflowStartRequestBodyArgFilesField], folder: CreateWorkflowStartRequestBodyArgFolderField, type: Union[None, CreateWorkflowStartRequestBodyArgTypeField] = None, outcomes: Union[None, List[CreateWorkflowStartRequestBodyArgOutcomesField]] = None, **kwargs):
        """
        :param flow: The flow that will be triggered
        :type flow: CreateWorkflowStartRequestBodyArgFlowField
        :param files: The array of files for which the workflow should start. All files
            must be in the workflow's configured folder.
        :type files: List[CreateWorkflowStartRequestBodyArgFilesField]
        :param folder: The folder object for which the workflow is configured.
        :type folder: CreateWorkflowStartRequestBodyArgFolderField
        :param type: The type of the parameters object
        :type type: Union[None, CreateWorkflowStartRequestBodyArgTypeField], optional
        :param outcomes: A list of outcomes required to be configured at start time.
        :type outcomes: Union[None, List[CreateWorkflowStartRequestBodyArgOutcomesField]], optional
        """
        super().__init__(**kwargs)
        self.flow = flow
        self.files = files
        self.folder = folder
        self.type = type
        self.outcomes = outcomes

class WorkflowsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_workflows(self, folder_id: str, options: GetWorkflowsOptionsArg = None) -> Workflows:
        """
        Returns list of workflows that act on a given `folder ID`, and
        
        have a flow with a trigger type of `WORKFLOW_MANUAL_START`.

        
        You application must be authorized to use the `Manage Box Relay` application

        
        scope within the developer console in to use this endpoint.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        """
        if options is None:
            options = GetWorkflowsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/workflows']), FetchOptions(method='GET', params={'folder_id': folder_id, 'trigger_type': options.triggerType, 'limit': options.limit, 'marker': options.marker}, auth=self.auth))
        return Workflows.from_dict(json.loads(response.text))
    def create_workflow_start(self, workflow_id: str, request_body: CreateWorkflowStartRequestBodyArg):
        """
        Initiates a flow with a trigger type of `WORKFLOW_MANUAL_START`.
        
        You application must be authorized to use the `Manage Box Relay` application

        
        scope within the developer console.

        :param workflow_id: The ID of the workflow.
            Example: "12345"
        :type workflow_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/workflows/', workflow_id, '/start']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return response.content