from enum import Enum

from typing import Optional

from box_sdk.base_object import BaseObject

from typing import List

from typing import Union

import json

from box_sdk.schemas import RetentionPolicyAssignments

from box_sdk.schemas import ClientError

from box_sdk.schemas import RetentionPolicyAssignment

from box_sdk.schemas import FilesUnderRetention

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetRetentionPolicyAssignmentsOptionsArgTypeField(str, Enum):
    FOLDER = 'folder'
    ENTERPRISE = 'enterprise'
    METADATA_TEMPLATE = 'metadata_template'

class GetRetentionPolicyAssignmentsOptionsArg(BaseObject):
    def __init__(self, type: Optional[GetRetentionPolicyAssignmentsOptionsArgTypeField] = None, fields: Optional[str] = None, marker: Optional[str] = None, limit: Optional[int] = None, **kwargs):
        """
        :param type: The type of the retention policy assignment to retrieve.
        :type type: Optional[GetRetentionPolicyAssignmentsOptionsArgTypeField], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.fields = fields
        self.marker = marker
        self.limit = limit

class CreateRetentionPolicyAssignmentRequestBodyArgAssignToFieldTypeField(str, Enum):
    ENTERPRISE = 'enterprise'
    FOLDER = 'folder'
    METADATA_TEMPLATE = 'metadata_template'

class CreateRetentionPolicyAssignmentRequestBodyArgAssignToField(BaseObject):
    def __init__(self, type: CreateRetentionPolicyAssignmentRequestBodyArgAssignToFieldTypeField, id: str, **kwargs):
        """
        :param type: The type of item to assign the policy to.
        :type type: CreateRetentionPolicyAssignmentRequestBodyArgAssignToFieldTypeField
        :param id: The ID of item to assign the policy to.
            Set to `null` or omit when `type` is set to
            `enterprise`.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class CreateRetentionPolicyAssignmentRequestBodyArgFilterFieldsField(BaseObject):
    def __init__(self, field: Optional[str] = None, value: Optional[str] = None, **kwargs):
        """
        :param field: The metadata attribute key id.
        :type field: Optional[str], optional
        :param value: The metadata attribute field id. For value, only
            enum and multiselect types are supported.
        :type value: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.field = field
        self.value = value

class CreateRetentionPolicyAssignmentRequestBodyArg(BaseObject):
    def __init__(self, policy_id: str, assign_to: CreateRetentionPolicyAssignmentRequestBodyArgAssignToField, filter_fields: Optional[List[CreateRetentionPolicyAssignmentRequestBodyArgFilterFieldsField]] = None, start_date_field: Optional[str] = None, **kwargs):
        """
        :param policy_id: The ID of the retention policy to assign
        :type policy_id: str
        :param assign_to: The item to assign the policy to
        :type assign_to: CreateRetentionPolicyAssignmentRequestBodyArgAssignToField
        :param filter_fields: If the `assign_to` type is `metadata_template`,
            then optionally add the `filter_fields` parameter which will
            require an array of objects with a field entry and a value entry.
            Currently only one object of `field` and `value` is supported.
        :type filter_fields: Optional[List[CreateRetentionPolicyAssignmentRequestBodyArgFilterFieldsField]], optional
        :param start_date_field: The date the retention policy assignment begins.
            If the `assigned_to` type is `metadata_template`,
            this field can be a date field's metadata attribute key id.
        :type start_date_field: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.policy_id = policy_id
        self.assign_to = assign_to
        self.filter_fields = filter_fields
        self.start_date_field = start_date_field

class GetRetentionPolicyAssignmentByIdOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class GetRetentionPolicyAssignmentFileUnderRetentionOptionsArg(BaseObject):
    def __init__(self, marker: Optional[str] = None, limit: Optional[int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class GetRetentionPolicyAssignmentFileVersionUnderRetentionOptionsArg(BaseObject):
    def __init__(self, marker: Optional[str] = None, limit: Optional[int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class RetentionPolicyAssignmentsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_retention_policy_assignments(self, retention_policy_id: str, options: GetRetentionPolicyAssignmentsOptionsArg = None) -> RetentionPolicyAssignments:
        """
        Returns a list of all retention policy assignments associated with a specified
        
        retention policy.

        :param retention_policy_id: The ID of the retention policy.
            Example: "982312"
        :type retention_policy_id: str
        """
        if options is None:
            options = GetRetentionPolicyAssignmentsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policies/', retention_policy_id, '/assignments']), FetchOptions(method='GET', params={'type': options.type, 'fields': options.fields, 'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return RetentionPolicyAssignments.from_dict(json.loads(response.text))
    def create_retention_policy_assignment(self, request_body: CreateRetentionPolicyAssignmentRequestBodyArg) -> RetentionPolicyAssignment:
        """
        Assigns a retention policy to an item.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policy_assignments']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return RetentionPolicyAssignment.from_dict(json.loads(response.text))
    def get_retention_policy_assignment_by_id(self, retention_policy_assignment_id: str, options: GetRetentionPolicyAssignmentByIdOptionsArg = None) -> RetentionPolicyAssignment:
        """
        Retrieves a retention policy assignment
        :param retention_policy_assignment_id: The ID of the retention policy assignment.
            Example: "1233123"
        :type retention_policy_assignment_id: str
        """
        if options is None:
            options = GetRetentionPolicyAssignmentByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policy_assignments/', retention_policy_assignment_id]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return RetentionPolicyAssignment.from_dict(json.loads(response.text))
    def delete_retention_policy_assignment_by_id(self, retention_policy_assignment_id: str):
        """
        Removes a retention policy assignment
        
        applied to content.

        :param retention_policy_assignment_id: The ID of the retention policy assignment.
            Example: "1233123"
        :type retention_policy_assignment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policy_assignments/', retention_policy_assignment_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def get_retention_policy_assignment_file_under_retention(self, retention_policy_assignment_id: str, options: GetRetentionPolicyAssignmentFileUnderRetentionOptionsArg = None) -> FilesUnderRetention:
        """
        Returns a list of files under retention for a retention policy assignment.
        :param retention_policy_assignment_id: The ID of the retention policy assignment.
            Example: "1233123"
        :type retention_policy_assignment_id: str
        """
        if options is None:
            options = GetRetentionPolicyAssignmentFileUnderRetentionOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policy_assignments/', retention_policy_assignment_id, '/files_under_retention']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return FilesUnderRetention.from_dict(json.loads(response.text))
    def get_retention_policy_assignment_file_version_under_retention(self, retention_policy_assignment_id: str, options: GetRetentionPolicyAssignmentFileVersionUnderRetentionOptionsArg = None) -> FilesUnderRetention:
        """
        Returns a list of file versions under retention for a retention policy
        
        assignment.

        :param retention_policy_assignment_id: The ID of the retention policy assignment.
            Example: "1233123"
        :type retention_policy_assignment_id: str
        """
        if options is None:
            options = GetRetentionPolicyAssignmentFileVersionUnderRetentionOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policy_assignments/', retention_policy_assignment_id, '/file_versions_under_retention']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return FilesUnderRetention.from_dict(json.loads(response.text))