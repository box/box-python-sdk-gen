from enum import Enum

from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import LegalHoldPolicyAssignments

from schemas import ClientError

from schemas import LegalHoldPolicyAssignment

from schemas import FileVersionLegalHolds

class GetLegalHoldPolicyAssignmentsOptionsArgAssignToTypeField(str, Enum):
    FILE = 'file'
    FILE_VERSION = 'file_version'
    FOLDER = 'folder'
    USER = 'user'

class GetLegalHoldPolicyAssignmentsOptionsArg(BaseObject):
    def __init__(self, assignToType: Union[None, GetLegalHoldPolicyAssignmentsOptionsArgAssignToTypeField] = None, assignToId: Union[None, str] = None, marker: Union[None, str] = None, limit: Union[None, int] = None, fields: Union[None, str] = None, **kwargs):
        """
        :param assignToType: Filters the results by the type of item the
            policy was applied to.
        :type assignToType: Union[None, GetLegalHoldPolicyAssignmentsOptionsArgAssignToTypeField], optional
        :param assignToId: Filters the results by the ID of item the
            policy was applied to.
        :type assignToId: Union[None, str], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.assignToType = assignToType
        self.assignToId = assignToId
        self.marker = marker
        self.limit = limit
        self.fields = fields

class PostLegalHoldPolicyAssignmentsRequestBodyArgAssignToFieldTypeField(str, Enum):
    FILE = 'file'
    FILE_VERSION = 'file_version'
    FOLDER = 'folder'
    USER = 'user'

class PostLegalHoldPolicyAssignmentsRequestBodyArgAssignToField(BaseObject):
    def __init__(self, type: PostLegalHoldPolicyAssignmentsRequestBodyArgAssignToFieldTypeField, id: str, **kwargs):
        """
        :param type: The type of item to assign the policy to
        :type type: PostLegalHoldPolicyAssignmentsRequestBodyArgAssignToFieldTypeField
        :param id: The ID of item to assign the policy to
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PostLegalHoldPolicyAssignmentsRequestBodyArg(BaseObject):
    def __init__(self, policy_id: str, assign_to: PostLegalHoldPolicyAssignmentsRequestBodyArgAssignToField, **kwargs):
        """
        :param policy_id: The ID of the policy to assign.
        :type policy_id: str
        :param assign_to: The item to assign the policy to
        :type assign_to: PostLegalHoldPolicyAssignmentsRequestBodyArgAssignToField
        """
        super().__init__(**kwargs)
        self.policy_id = policy_id
        self.assign_to = assign_to

class GetLegalHoldPolicyAssignmentsIdFilesOnHoldOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, limit: Union[None, int] = None, fields: Union[None, str] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit
        self.fields = fields

class GetLegalHoldPolicyAssignmentsIdFileVersionsOnHoldOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, limit: Union[None, int] = None, fields: Union[None, str] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit
        self.fields = fields

class LegalHoldPolicyAssignmentsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getLegalHoldPolicyAssignments(self, policyId: str, options: GetLegalHoldPolicyAssignmentsOptionsArg = None) -> LegalHoldPolicyAssignments:
        """
        Retrieves a list of items a legal hold policy has been assigned to.
        :param policyId: The ID of the legal hold policy
            Example: "324432"
        :type policyId: str
        """
        if options is None:
            options = GetLegalHoldPolicyAssignmentsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policy_assignments']), FetchOptions(method='GET', params={'policy_id': policyId, 'assign_to_type': options.assignToType, 'assign_to_id': options.assignToId, 'marker': options.marker, 'limit': options.limit, 'fields': options.fields}, auth=self.auth))
        return LegalHoldPolicyAssignments.from_dict(json.loads(response.text))
    def postLegalHoldPolicyAssignments(self, requestBody: PostLegalHoldPolicyAssignmentsRequestBodyArg) -> LegalHoldPolicyAssignment:
        """
        Assign a legal hold to a file, file version, folder, or user.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policy_assignments']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return LegalHoldPolicyAssignment.from_dict(json.loads(response.text))
    def getLegalHoldPolicyAssignmentsId(self, legalHoldPolicyAssignmentId: str) -> LegalHoldPolicyAssignment:
        """
        Retrieve a legal hold policy assignment.
        :param legalHoldPolicyAssignmentId: The ID of the legal hold policy assignment
            Example: "753465"
        :type legalHoldPolicyAssignmentId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policy_assignments/', legalHoldPolicyAssignmentId]), FetchOptions(method='GET', auth=self.auth))
        return LegalHoldPolicyAssignment.from_dict(json.loads(response.text))
    def deleteLegalHoldPolicyAssignmentsId(self, legalHoldPolicyAssignmentId: str):
        """
        Remove a legal hold from an item.
        
        This is an asynchronous process. The policy will not be

        
        fully removed yet when the response returns.

        :param legalHoldPolicyAssignmentId: The ID of the legal hold policy assignment
            Example: "753465"
        :type legalHoldPolicyAssignmentId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policy_assignments/', legalHoldPolicyAssignmentId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def getLegalHoldPolicyAssignmentsIdFilesOnHold(self, legalHoldPolicyAssignmentId: str, options: GetLegalHoldPolicyAssignmentsIdFilesOnHoldOptionsArg = None) -> FileVersionLegalHolds:
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

        :param legalHoldPolicyAssignmentId: The ID of the legal hold policy assignment
            Example: "753465"
        :type legalHoldPolicyAssignmentId: str
        """
        if options is None:
            options = GetLegalHoldPolicyAssignmentsIdFilesOnHoldOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policy_assignments/', legalHoldPolicyAssignmentId, '/files_on_hold']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit, 'fields': options.fields}, auth=self.auth))
        return FileVersionLegalHolds.from_dict(json.loads(response.text))
    def getLegalHoldPolicyAssignmentsIdFileVersionsOnHold(self, legalHoldPolicyAssignmentId: str, options: GetLegalHoldPolicyAssignmentsIdFileVersionsOnHoldOptionsArg = None) -> FileVersionLegalHolds:
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

        :param legalHoldPolicyAssignmentId: The ID of the legal hold policy assignment
            Example: "753465"
        :type legalHoldPolicyAssignmentId: str
        """
        if options is None:
            options = GetLegalHoldPolicyAssignmentsIdFileVersionsOnHoldOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policy_assignments/', legalHoldPolicyAssignmentId, '/file_versions_on_hold']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit, 'fields': options.fields}, auth=self.auth))
        return FileVersionLegalHolds.from_dict(json.loads(response.text))