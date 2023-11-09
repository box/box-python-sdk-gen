from enum import Enum

from box_sdk_gen.base_object import BaseObject

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import StoragePolicyAssignments

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import StoragePolicyAssignment

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


class GetStoragePolicyAssignmentsResolvedForTypeArg(str, Enum):
    USER = 'user'
    ENTERPRISE = 'enterprise'


class CreateStoragePolicyAssignmentStoragePolicyArgTypeField(str, Enum):
    STORAGE_POLICY = 'storage_policy'


class CreateStoragePolicyAssignmentStoragePolicyArg(BaseObject):
    def __init__(
        self,
        type: CreateStoragePolicyAssignmentStoragePolicyArgTypeField,
        id: str,
        **kwargs
    ):
        """
        :param type: The type to assign.
        :type type: CreateStoragePolicyAssignmentStoragePolicyArgTypeField
        :param id: The ID of the storage policy to assign.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class CreateStoragePolicyAssignmentAssignedToArgTypeField(str, Enum):
    USER = 'user'
    ENTERPRISE = 'enterprise'


class CreateStoragePolicyAssignmentAssignedToArg(BaseObject):
    def __init__(
        self,
        type: CreateStoragePolicyAssignmentAssignedToArgTypeField,
        id: str,
        **kwargs
    ):
        """
        :param type: The type to assign the policy to.
        :type type: CreateStoragePolicyAssignmentAssignedToArgTypeField
        :param id: The ID of the user or enterprise
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class UpdateStoragePolicyAssignmentByIdStoragePolicyArgTypeField(str, Enum):
    STORAGE_POLICY = 'storage_policy'


class UpdateStoragePolicyAssignmentByIdStoragePolicyArg(BaseObject):
    def __init__(
        self,
        type: UpdateStoragePolicyAssignmentByIdStoragePolicyArgTypeField,
        id: str,
        **kwargs
    ):
        """
        :param type: The type to assign.
        :type type: UpdateStoragePolicyAssignmentByIdStoragePolicyArgTypeField
        :param id: The ID of the storage policy to assign.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class StoragePolicyAssignmentsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_storage_policy_assignments(
        self,
        resolved_for_type: GetStoragePolicyAssignmentsResolvedForTypeArg,
        resolved_for_id: str,
        marker: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> StoragePolicyAssignments:
        """
        Fetches all the storage policy assignment for an enterprise or user.
        :param resolved_for_type: The target type to return assignments for
        :type resolved_for_type: GetStoragePolicyAssignmentsResolvedForTypeArg
        :param resolved_for_id: The ID of the user or enterprise to return assignments for
        :type resolved_for_id: str
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({
            'marker': to_string(marker),
            'resolved_for_type': to_string(resolved_for_type),
            'resolved_for_id': to_string(resolved_for_id),
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/storage_policy_assignments']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, StoragePolicyAssignments)

    def create_storage_policy_assignment(
        self,
        storage_policy: CreateStoragePolicyAssignmentStoragePolicyArg,
        assigned_to: CreateStoragePolicyAssignmentAssignedToArg,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> StoragePolicyAssignment:
        """
        Creates a storage policy assignment for an enterprise or user.
        :param storage_policy: The storage policy to assign to the user or
            enterprise
        :type storage_policy: CreateStoragePolicyAssignmentStoragePolicyArg
        :param assigned_to: The user or enterprise to assign the storage
            policy to.
        :type assigned_to: CreateStoragePolicyAssignmentAssignedToArg
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'storage_policy': storage_policy,
            'assigned_to': assigned_to,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/storage_policy_assignments']),
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
        return deserialize(response.data, StoragePolicyAssignment)

    def get_storage_policy_assignment_by_id(
        self,
        storage_policy_assignment_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> StoragePolicyAssignment:
        """
        Fetches a specific storage policy assignment.
        :param storage_policy_assignment_id: The ID of the storage policy assignment.
            Example: "932483"
        :type storage_policy_assignment_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/storage_policy_assignments/',
                to_string(storage_policy_assignment_id),
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, StoragePolicyAssignment)

    def update_storage_policy_assignment_by_id(
        self,
        storage_policy_assignment_id: str,
        storage_policy: UpdateStoragePolicyAssignmentByIdStoragePolicyArg,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> StoragePolicyAssignment:
        """
        Updates a specific storage policy assignment.
        :param storage_policy_assignment_id: The ID of the storage policy assignment.
            Example: "932483"
        :type storage_policy_assignment_id: str
        :param storage_policy: The storage policy to assign to the user or
            enterprise
        :type storage_policy: UpdateStoragePolicyAssignmentByIdStoragePolicyArg
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'storage_policy': storage_policy}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/storage_policy_assignments/',
                to_string(storage_policy_assignment_id),
            ]),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, StoragePolicyAssignment)

    def delete_storage_policy_assignment_by_id(
        self,
        storage_policy_assignment_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Delete a storage policy assignment.

        Deleting a storage policy assignment on a user


        will have the user inherit the enterprise's default


        storage policy.


        There is a rate limit for calling this endpoint of only


        twice per user in a 24 hour time frame.

        :param storage_policy_assignment_id: The ID of the storage policy assignment.
            Example: "932483"
        :type storage_policy_assignment_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/storage_policy_assignments/',
                to_string(storage_policy_assignment_id),
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
