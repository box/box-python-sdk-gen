from enum import Enum

from typing import Optional

from box_sdk.base_object import BaseObject

from typing import Dict

import json

from typing import List

from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.schemas import Workflows

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import prepare_params

from box_sdk.utils import to_string

from box_sdk.utils import ByteStream

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateWorkflowStartTypeArg(str, Enum):
    WORKFLOW_PARAMETERS = 'workflow_parameters'

class CreateWorkflowStartFlowArg(BaseObject):
    def __init__(self, type: Optional[str] = None, id: Optional[str] = None, **kwargs):
        """
        :param type: The type of the flow object
        :type type: Optional[str], optional
        :param id: The id of the flow
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class CreateWorkflowStartFolderArgTypeField(str, Enum):
    FOLDER = 'folder'

class CreateWorkflowStartFolderArg(BaseObject):
    def __init__(self, type: Optional[CreateWorkflowStartFolderArgTypeField] = None, id: Optional[str] = None, **kwargs):
        """
        :param type: The type of the folder object
        :type type: Optional[CreateWorkflowStartFolderArgTypeField], optional
        :param id: The id of the folder
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class WorkflowsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_workflows(self, folder_id: str, trigger_type: Optional[str] = None, limit: Optional[int] = None, marker: Optional[str] = None, extra_headers: Optional[Dict[str, Optional[str]]] = {}) -> Workflows:
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
        :type folder_id: str
        :param trigger_type: Type of trigger to search for.
        :type trigger_type: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to {}
        :type extra_headers: Optional[Dict[str, Optional[str]]]
        """
        query_params_map: Dict[str, str] = prepare_params({'folder_id': to_string(folder_id), 'trigger_type': to_string(trigger_type), 'limit': to_string(limit), 'marker': to_string(marker)})
        headers_map: Dict[str, str] = prepare_params({**{}, **extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/workflows']), FetchOptions(method='GET', params=query_params_map, headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return Workflows.from_dict(json.loads(response.text))
    def create_workflow_start(self, workflow_id: str, flow: CreateWorkflowStartFlowArg, files: List, folder: CreateWorkflowStartFolderArg, type: Optional[CreateWorkflowStartTypeArg] = None, outcomes: Optional[List] = None, extra_headers: Optional[Dict[str, Optional[str]]] = {}) -> None:
        """
        Initiates a flow with a trigger type of `WORKFLOW_MANUAL_START`.
        
        You application must be authorized to use the `Manage Box Relay` application

        
        scope within the developer console.

        :param workflow_id: The ID of the workflow.
            Example: "12345"
        :type workflow_id: str
        :param flow: The flow that will be triggered
        :type flow: CreateWorkflowStartFlowArg
        :param files: The array of files for which the workflow should start. All files
            must be in the workflow's configured folder.
        :type files: List
        :param folder: The folder object for which the workflow is configured.
        :type folder: CreateWorkflowStartFolderArg
        :param type: The type of the parameters object
        :type type: Optional[CreateWorkflowStartTypeArg], optional
        :param outcomes: A list of outcomes required to be configured at start time.
        :type outcomes: Optional[List], optional
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to {}
        :type extra_headers: Optional[Dict[str, Optional[str]]]
        """
        request_body: BaseObject = BaseObject(type=type, flow=flow, files=files, folder=folder, outcomes=outcomes)
        headers_map: Dict[str, str] = prepare_params({**{}, **extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/workflows/', workflow_id, '/start']), FetchOptions(method='POST', headers=headers_map, body=json.dumps(request_body.to_dict()), content_type='application/json', response_format=None, auth=self.auth, network_session=self.network_session))
        return None