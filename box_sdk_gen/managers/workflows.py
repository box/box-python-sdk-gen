from enum import Enum

from typing import Optional

from box_sdk_gen.base_object import BaseObject

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from typing import List

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import Workflows

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json_data import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json_data import SerializedData


class StartWorkflowType(str, Enum):
    WORKFLOW_PARAMETERS = 'workflow_parameters'


class StartWorkflowFlow(BaseObject):
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


class StartWorkflowFilesTypeField(str, Enum):
    FILE = 'file'


class StartWorkflowFiles(BaseObject):
    _discriminator = 'type', {'file'}

    def __init__(
        self,
        type: Optional[StartWorkflowFilesTypeField] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: The type of the file object
        :type type: Optional[StartWorkflowFilesTypeField], optional
        :param id: The id of the file
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class StartWorkflowFolderTypeField(str, Enum):
    FOLDER = 'folder'


class StartWorkflowFolder(BaseObject):
    _discriminator = 'type', {'folder'}

    def __init__(
        self,
        type: Optional[StartWorkflowFolderTypeField] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: The type of the folder object
        :type type: Optional[StartWorkflowFolderTypeField], optional
        :param id: The id of the folder
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class StartWorkflowOutcomesTypeField(str, Enum):
    OUTCOME = 'outcome'


class StartWorkflowOutcomes(BaseObject):
    _discriminator = 'type', {'outcome'}

    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[StartWorkflowOutcomesTypeField] = None,
        parameter: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The id of the outcome
        :type id: Optional[str], optional
        :param type: The type of the outcome object
        :type type: Optional[StartWorkflowOutcomesTypeField], optional
        :param parameter: This is a placeholder example for various objects that
            can be passed in - refer to the guides section to find
            out more information.
        :type parameter: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.parameter = parameter


class WorkflowsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: NetworkSession = None,
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session

    def get_workflows(
        self,
        folder_id: str,
        trigger_type: Optional[str] = None,
        limit: Optional[int] = None,
        marker: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Workflows:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {
                'folder_id': to_string(folder_id),
                'trigger_type': to_string(trigger_type),
                'limit': to_string(limit),
                'marker': to_string(marker),
            }
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([self.network_session.base_urls.base_url, '/workflows']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Workflows)

    def start_workflow(
        self,
        workflow_id: str,
        flow: StartWorkflowFlow,
        files: List[StartWorkflowFiles],
        folder: StartWorkflowFolder,
        type: Optional[StartWorkflowType] = None,
        outcomes: Optional[List[StartWorkflowOutcomes]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Initiates a flow with a trigger type of `WORKFLOW_MANUAL_START`.

        You application must be authorized to use the `Manage Box Relay` application


        scope within the developer console.

        :param workflow_id: The ID of the workflow.
            Example: "12345"
        :type workflow_id: str
        :param flow: The flow that will be triggered
        :type flow: StartWorkflowFlow
        :param files: The array of files for which the workflow should start. All files
            must be in the workflow's configured folder.
        :type files: List[StartWorkflowFiles]
        :param folder: The folder object for which the workflow is configured.
        :type folder: StartWorkflowFolder
        :param type: The type of the parameters object
        :type type: Optional[StartWorkflowType], optional
        :param outcomes: A list of outcomes required to be configured at start time.
        :type outcomes: Optional[List[StartWorkflowOutcomes]], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'type': type,
            'flow': flow,
            'files': files,
            'folder': folder,
            'outcomes': outcomes,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/workflows/',
                    to_string(workflow_id),
                    '/start',
                ]
            ),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None
