from enum import Enum

from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import StoragePolicyAssignments

from schemas import ClientError

from schemas import StoragePolicyAssignment

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
    def getStoragePolicyAssignments(self, resolvedForType: GetStoragePolicyAssignmentsResolvedForTypeArg, resolvedForId: str, options: GetStoragePolicyAssignmentsOptionsArg = None) -> StoragePolicyAssignments:
        """
        Fetches all the storage policy assignment for an enterprise or user.
        :param resolvedForType: The target type to return assignments for
            Example: "user"
        :type resolvedForType: GetStoragePolicyAssignmentsResolvedForTypeArg
        :param resolvedForId: The ID of the user or enterprise to return assignments for
            Example: "984322"
        :type resolvedForId: str
        """
        if options is None:
            options = GetStoragePolicyAssignmentsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments']), FetchOptions(method='GET', params={'marker': options.marker, 'resolved_for_type': resolvedForType, 'resolved_for_id': resolvedForId}, auth=self.auth))
        return StoragePolicyAssignments.from_dict(json.loads(response.text))
    def postStoragePolicyAssignments(self, requestBody: PostStoragePolicyAssignmentsRequestBodyArg) -> StoragePolicyAssignment:
        """
        Creates a storage policy assignment for an enterprise or user.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return StoragePolicyAssignment.from_dict(json.loads(response.text))
    def getStoragePolicyAssignmentsId(self, storagePolicyAssignmentId: str) -> StoragePolicyAssignment:
        """
        Fetches a specific storage policy assignment.
        :param storagePolicyAssignmentId: The ID of the storage policy assignment.
            Example: "932483"
        :type storagePolicyAssignmentId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments/', storagePolicyAssignmentId]), FetchOptions(method='GET', auth=self.auth))
        return StoragePolicyAssignment.from_dict(json.loads(response.text))
    def putStoragePolicyAssignmentsId(self, storagePolicyAssignmentId: str, requestBody: PutStoragePolicyAssignmentsIdRequestBodyArg) -> StoragePolicyAssignment:
        """
        Updates a specific storage policy assignment.
        :param storagePolicyAssignmentId: The ID of the storage policy assignment.
            Example: "932483"
        :type storagePolicyAssignmentId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments/', storagePolicyAssignmentId]), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return StoragePolicyAssignment.from_dict(json.loads(response.text))
    def deleteStoragePolicyAssignmentsId(self, storagePolicyAssignmentId: str):
        """
        Delete a storage policy assignment.
        
        Deleting a storage policy assignment on a user

        
        will have the user inherit the enterprise's default

        
        storage policy.

        
        There is a rate limit for calling this endpoint of only

        
        twice per user in a 24 hour time frame.

        :param storagePolicyAssignmentId: The ID of the storage policy assignment.
            Example: "932483"
        :type storagePolicyAssignmentId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policy_assignments/', storagePolicyAssignmentId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content