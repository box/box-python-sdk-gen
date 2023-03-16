from enum import Enum

from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import StoragePolicyAssignments

from box_sdk.schemas import ClientError

from box_sdk.schemas import StoragePolicyAssignment

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetStoragePolicyAssignmentsResolvedForTypeArg(str, Enum):
    USER = 'user'
    ENTERPRISE = 'enterprise'

class GetStoragePolicyAssignmentsOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.marker = marker

class PostStoragePolicyAssignmentsRequestBodyArgStoragePolicyFieldTypeField:
    pass

class PostStoragePolicyAssignmentsRequestBodyArgStoragePolicyField(BaseObject):
    def __init__(self, type: PostStoragePolicyAssignmentsRequestBodyArgStoragePolicyFieldTypeField, id: str, **kwargs):
        """
        :param type: The type to assign.
        :type type: PostStoragePolicyAssignmentsRequestBodyArgStoragePolicyFieldTypeField
        :param id: The ID of the storage policy to assign.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PostStoragePolicyAssignmentsRequestBodyArgAssignedToFieldTypeField(str, Enum):
    USER = 'user'
    ENTERPRISE = 'enterprise'

class PostStoragePolicyAssignmentsRequestBodyArgAssignedToField(BaseObject):
    def __init__(self, type: PostStoragePolicyAssignmentsRequestBodyArgAssignedToFieldTypeField, id: str, **kwargs):
        """
        :param type: The type to assign the policy to.
        :type type: PostStoragePolicyAssignmentsRequestBodyArgAssignedToFieldTypeField
        :param id: The ID of the user or enterprise
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PostStoragePolicyAssignmentsRequestBodyArg(BaseObject):
    def __init__(self, storage_policy: PostStoragePolicyAssignmentsRequestBodyArgStoragePolicyField, assigned_to: PostStoragePolicyAssignmentsRequestBodyArgAssignedToField, **kwargs):
        """
        :param storage_policy: The storage policy to assign to the user or
            enterprise
        :type storage_policy: PostStoragePolicyAssignmentsRequestBodyArgStoragePolicyField
        :param assigned_to: The user or enterprise to assign the storage
            policy to.
        :type assigned_to: PostStoragePolicyAssignmentsRequestBodyArgAssignedToField
        """
        super().__init__(**kwargs)
        self.storage_policy = storage_policy
        self.assigned_to = assigned_to

class PutStoragePolicyAssignmentsIdRequestBodyArgStoragePolicyFieldTypeField:
    pass

class PutStoragePolicyAssignmentsIdRequestBodyArgStoragePolicyField(BaseObject):
    def __init__(self, type: PutStoragePolicyAssignmentsIdRequestBodyArgStoragePolicyFieldTypeField, id: str, **kwargs):
        """
        :param type: The type to assign.
        :type type: PutStoragePolicyAssignmentsIdRequestBodyArgStoragePolicyFieldTypeField
        :param id: The ID of the storage policy to assign.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PutStoragePolicyAssignmentsIdRequestBodyArg(BaseObject):
    def __init__(self, storage_policy: PutStoragePolicyAssignmentsIdRequestBodyArgStoragePolicyField, **kwargs):
        """
        :param storage_policy: The storage policy to assign to the user or
            enterprise
        :type storage_policy: PutStoragePolicyAssignmentsIdRequestBodyArgStoragePolicyField
        """
        super().__init__(**kwargs)
        self.storage_policy = storage_policy

class StoragePolicyAssignmentsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments']), FetchOptions(method='GET', params={'marker': options.marker, 'resolved_for_type': resolved_for_type, 'resolved_for_id': resolved_for_id}, auth=self.auth))
        return StoragePolicyAssignments.from_dict(json.loads(response.text))
    def post_storage_policy_assignments(self, request_body: PostStoragePolicyAssignmentsRequestBodyArg) -> StoragePolicyAssignment:
        """
        Creates a storage policy assignment for an enterprise or user.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return StoragePolicyAssignment.from_dict(json.loads(response.text))
    def get_storage_policy_assignments_id(self, storage_policy_assignment_id: str) -> StoragePolicyAssignment:
        """
        Fetches a specific storage policy assignment.
        :param storage_policy_assignment_id: The ID of the storage policy assignment.
            Example: "932483"
        :type storage_policy_assignment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments/', storage_policy_assignment_id]), FetchOptions(method='GET', auth=self.auth))
        return StoragePolicyAssignment.from_dict(json.loads(response.text))
    def put_storage_policy_assignments_id(self, storage_policy_assignment_id: str, request_body: PutStoragePolicyAssignmentsIdRequestBodyArg) -> StoragePolicyAssignment:
        """
        Updates a specific storage policy assignment.
        :param storage_policy_assignment_id: The ID of the storage policy assignment.
            Example: "932483"
        :type storage_policy_assignment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments/', storage_policy_assignment_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return StoragePolicyAssignment.from_dict(json.loads(response.text))
    def delete_storage_policy_assignments_id(self, storage_policy_assignment_id: str):
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments/', storage_policy_assignment_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content