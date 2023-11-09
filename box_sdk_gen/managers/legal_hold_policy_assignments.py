from enum import Enum

from box_sdk_gen.base_object import BaseObject

from typing import Optional

from typing import List

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import LegalHoldPolicyAssignments

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import LegalHoldPolicyAssignment

from box_sdk_gen.schemas import FileVersionLegalHolds

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json import SerializedData


class GetLegalHoldPolicyAssignmentsAssignToTypeArg(str, Enum):
    FILE = 'file'
    FILE_VERSION = 'file_version'
    FOLDER = 'folder'
    USER = 'user'


class CreateLegalHoldPolicyAssignmentAssignToArgTypeField(str, Enum):
    FILE = 'file'
    FILE_VERSION = 'file_version'
    FOLDER = 'folder'
    USER = 'user'


class CreateLegalHoldPolicyAssignmentAssignToArg(BaseObject):
    def __init__(
        self,
        type: CreateLegalHoldPolicyAssignmentAssignToArgTypeField,
        id: str,
        **kwargs
    ):
        """
        :param type: The type of item to assign the policy to
        :type type: CreateLegalHoldPolicyAssignmentAssignToArgTypeField
        :param id: The ID of item to assign the policy to
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class LegalHoldPolicyAssignmentsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_legal_hold_policy_assignments(
        self,
        policy_id: str,
        assign_to_type: Optional[GetLegalHoldPolicyAssignmentsAssignToTypeArg] = None,
        assign_to_id: Optional[str] = None,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> LegalHoldPolicyAssignments:
        """
        Retrieves a list of items a legal hold policy has been assigned to.
        :param policy_id: The ID of the legal hold policy
        :type policy_id: str
        :param assign_to_type: Filters the results by the type of item the
            policy was applied to.
        :type assign_to_type: Optional[GetLegalHoldPolicyAssignmentsAssignToTypeArg], optional
        :param assign_to_id: Filters the results by the ID of item the
            policy was applied to.
        :type assign_to_id: Optional[str], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[List[str]], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({
            'policy_id': to_string(policy_id),
            'assign_to_type': to_string(assign_to_type),
            'assign_to_id': to_string(assign_to_id),
            'marker': to_string(marker),
            'limit': to_string(limit),
            'fields': to_string(fields),
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/legal_hold_policy_assignments']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, LegalHoldPolicyAssignments)

    def create_legal_hold_policy_assignment(
        self,
        policy_id: str,
        assign_to: CreateLegalHoldPolicyAssignmentAssignToArg,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> LegalHoldPolicyAssignment:
        """
        Assign a legal hold to a file, file version, folder, or user.
        :param policy_id: The ID of the policy to assign.
        :type policy_id: str
        :param assign_to: The item to assign the policy to
        :type assign_to: CreateLegalHoldPolicyAssignmentAssignToArg
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'policy_id': policy_id, 'assign_to': assign_to}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/legal_hold_policy_assignments']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, LegalHoldPolicyAssignment)

    def get_legal_hold_policy_assignment_by_id(
        self,
        legal_hold_policy_assignment_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> LegalHoldPolicyAssignment:
        """
        Retrieve a legal hold policy assignment.
        :param legal_hold_policy_assignment_id: The ID of the legal hold policy assignment
            Example: "753465"
        :type legal_hold_policy_assignment_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/legal_hold_policy_assignments/',
                to_string(legal_hold_policy_assignment_id),
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, LegalHoldPolicyAssignment)

    def delete_legal_hold_policy_assignment_by_id(
        self,
        legal_hold_policy_assignment_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Remove a legal hold from an item.

        This is an asynchronous process. The policy will not be


        fully removed yet when the response returns.

        :param legal_hold_policy_assignment_id: The ID of the legal hold policy assignment
            Example: "753465"
        :type legal_hold_policy_assignment_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/legal_hold_policy_assignments/',
                to_string(legal_hold_policy_assignment_id),
            ]),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def get_legal_hold_policy_assignment_file_on_hold(
        self,
        legal_hold_policy_assignment_id: str,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FileVersionLegalHolds:
        """
        Get a list of current file versions for a legal hold

        assignment.


        In some cases you may want to get previous file versions instead. In these


        cases, use the `GET  /legal_hold_policy_assignments/:id/file_versions_on_hold`


        API instead to return any previous versions of a file for this legal hold


        policy assignment.


        Due to ongoing re-architecture efforts this API might not return all file


        versions held for this policy ID. Instead, this API will only return the


        latest file version held in the newly developed architecture. The `GET


        /file_version_legal_holds` API can be used to fetch current and past versions


        of files held within the legacy architecture.


        The `GET /legal_hold_policy_assignments?policy_id={id}` API can be used to


        find a list of policy assignments for a given policy ID.

        :param legal_hold_policy_assignment_id: The ID of the legal hold policy assignment
            Example: "753465"
        :type legal_hold_policy_assignment_id: str
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[List[str]], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({
            'marker': to_string(marker),
            'limit': to_string(limit),
            'fields': to_string(fields),
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/legal_hold_policy_assignments/',
                to_string(legal_hold_policy_assignment_id),
                '/files_on_hold',
            ]),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, FileVersionLegalHolds)

    def get_legal_hold_policy_assignment_file_version_on_hold(
        self,
        legal_hold_policy_assignment_id: str,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FileVersionLegalHolds:
        """
        Get a list of previous file versions for a legal hold

        assignment.


        In some cases you may only need the latest file versions instead. In these


        cases, use the `GET  /legal_hold_policy_assignments/:id/files_on_hold` API


        instead to return any current (latest) versions of a file for this legal hold


        policy assignment.


        Due to ongoing re-architecture efforts this API might not return all files


        held for this policy ID. Instead, this API will only return past file versions


        held in the newly developed architecture. The `GET /file_version_legal_holds`


        API can be used to fetch current and past versions of files held within the


        legacy architecture.


        The `GET /legal_hold_policy_assignments?policy_id={id}` API can be used to


        find a list of policy assignments for a given policy ID.

        :param legal_hold_policy_assignment_id: The ID of the legal hold policy assignment
            Example: "753465"
        :type legal_hold_policy_assignment_id: str
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[List[str]], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({
            'marker': to_string(marker),
            'limit': to_string(limit),
            'fields': to_string(fields),
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/legal_hold_policy_assignments/',
                to_string(legal_hold_policy_assignment_id),
                '/file_versions_on_hold',
            ]),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, FileVersionLegalHolds)
