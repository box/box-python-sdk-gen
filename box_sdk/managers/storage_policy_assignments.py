from enum import Enum

from typing import Optional

from box_sdk.base_object import BaseObject

import json

from typing import Dict

from box_sdk.schemas import StoragePolicyAssignments

from box_sdk.schemas import ClientError

from box_sdk.schemas import StoragePolicyAssignment

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetStoragePolicyAssignmentsResolvedForTypeArg(str, Enum):
    USER = 'user'
    ENTERPRISE = 'enterprise'

class GetStoragePolicyAssignmentsOptionsArg(BaseObject):
    def __init__(self, marker: Optional[str] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.marker = marker

class CreateStoragePolicyAssignmentRequestBodyArgStoragePolicyFieldTypeField(str, Enum):
    STORAGE_POLICY = 'storage_policy'

class CreateStoragePolicyAssignmentRequestBodyArgStoragePolicyField(BaseObject):
    def __init__(self, type: CreateStoragePolicyAssignmentRequestBodyArgStoragePolicyFieldTypeField, id: str, **kwargs):
        """
        :param type: The type to assign.
        :type type: CreateStoragePolicyAssignmentRequestBodyArgStoragePolicyFieldTypeField
        :param id: The ID of the storage policy to assign.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class CreateStoragePolicyAssignmentRequestBodyArgAssignedToFieldTypeField(str, Enum):
    USER = 'user'
    ENTERPRISE = 'enterprise'

class CreateStoragePolicyAssignmentRequestBodyArgAssignedToField(BaseObject):
    def __init__(self, type: CreateStoragePolicyAssignmentRequestBodyArgAssignedToFieldTypeField, id: str, **kwargs):
        """
        :param type: The type to assign the policy to.
        :type type: CreateStoragePolicyAssignmentRequestBodyArgAssignedToFieldTypeField
        :param id: The ID of the user or enterprise
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class CreateStoragePolicyAssignmentRequestBodyArg(BaseObject):
    def __init__(self, storage_policy: CreateStoragePolicyAssignmentRequestBodyArgStoragePolicyField, assigned_to: CreateStoragePolicyAssignmentRequestBodyArgAssignedToField, **kwargs):
        """
        :param storage_policy: The storage policy to assign to the user or
            enterprise
        :type storage_policy: CreateStoragePolicyAssignmentRequestBodyArgStoragePolicyField
        :param assigned_to: The user or enterprise to assign the storage
            policy to.
        :type assigned_to: CreateStoragePolicyAssignmentRequestBodyArgAssignedToField
        """
        super().__init__(**kwargs)
        self.storage_policy = storage_policy
        self.assigned_to = assigned_to

class UpdateStoragePolicyAssignmentByIdRequestBodyArgStoragePolicyFieldTypeField(str, Enum):
    STORAGE_POLICY = 'storage_policy'

class UpdateStoragePolicyAssignmentByIdRequestBodyArgStoragePolicyField(BaseObject):
    def __init__(self, type: UpdateStoragePolicyAssignmentByIdRequestBodyArgStoragePolicyFieldTypeField, id: str, **kwargs):
        """
        :param type: The type to assign.
        :type type: UpdateStoragePolicyAssignmentByIdRequestBodyArgStoragePolicyFieldTypeField
        :param id: The ID of the storage policy to assign.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class UpdateStoragePolicyAssignmentByIdRequestBodyArg(BaseObject):
    def __init__(self, storage_policy: UpdateStoragePolicyAssignmentByIdRequestBodyArgStoragePolicyField, **kwargs):
        """
        :param storage_policy: The storage policy to assign to the user or
            enterprise
        :type storage_policy: UpdateStoragePolicyAssignmentByIdRequestBodyArgStoragePolicyField
        """
        super().__init__(**kwargs)
        self.storage_policy = storage_policy

class StoragePolicyAssignmentsManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def get_storage_policy_assignments(self, resolved_for_type: GetStoragePolicyAssignmentsResolvedForTypeArg, resolved_for_id: str, options: GetStoragePolicyAssignmentsOptionsArg = None) -> StoragePolicyAssignments:
        """
        Fetches all the storage policy assignment for an enterprise or user.
        :param resolved_for_type: The target type to return assignments for
            Example: "user"
        :type resolved_for_type: GetStoragePolicyAssignmentsResolvedForTypeArg
        :param resolved_for_id: The ID of the user or enterprise to return assignments for
            Example: "984322"
        :type resolved_for_id: str
        """
        if options is None:
            options = GetStoragePolicyAssignmentsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments']), FetchOptions(method='GET', params={'marker': options.marker, 'resolved_for_type': resolved_for_type, 'resolved_for_id': resolved_for_id}, auth=self.auth, network_session=self.network_session))
        return StoragePolicyAssignments.from_dict(json.loads(response.text))
    def create_storage_policy_assignment(self, request_body: CreateStoragePolicyAssignmentRequestBodyArg) -> StoragePolicyAssignment:
        """
        Creates a storage policy assignment for an enterprise or user.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return StoragePolicyAssignment.from_dict(json.loads(response.text))
    def get_storage_policy_assignment_by_id(self, storage_policy_assignment_id: str) -> StoragePolicyAssignment:
        """
        Fetches a specific storage policy assignment.
        :param storage_policy_assignment_id: The ID of the storage policy assignment.
            Example: "932483"
        :type storage_policy_assignment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments/', storage_policy_assignment_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return StoragePolicyAssignment.from_dict(json.loads(response.text))
    def update_storage_policy_assignment_by_id(self, storage_policy_assignment_id: str, request_body: UpdateStoragePolicyAssignmentByIdRequestBodyArg) -> StoragePolicyAssignment:
        """
        Updates a specific storage policy assignment.
        :param storage_policy_assignment_id: The ID of the storage policy assignment.
            Example: "932483"
        :type storage_policy_assignment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments/', storage_policy_assignment_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return StoragePolicyAssignment.from_dict(json.loads(response.text))
    def delete_storage_policy_assignment_by_id(self, storage_policy_assignment_id: str):
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
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments/', storage_policy_assignment_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content