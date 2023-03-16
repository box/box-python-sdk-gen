from enum import Enum

from typing import Union

from box_sdk.base_object import BaseObject

from typing import List

import json

from box_sdk.schemas import RetentionPolicyAssignments

from box_sdk.schemas import ClientError

from box_sdk.schemas import RetentionPolicyAssignment

from box_sdk.schemas import FilesUnderRetention

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetRetentionPoliciesIdAssignmentsOptionsArgTypeField(str, Enum):
    FOLDER = 'folder'
    ENTERPRISE = 'enterprise'
    METADATA_TEMPLATE = 'metadata_template'

class GetRetentionPoliciesIdAssignmentsOptionsArg(BaseObject):
    def __init__(self, type: Union[None, GetRetentionPoliciesIdAssignmentsOptionsArgTypeField] = None, fields: Union[None, str] = None, marker: Union[None, str] = None, limit: Union[None, int] = None, **kwargs):
        """
        :param type: The type of the retention policy assignment to retrieve.
        :type type: Union[None, GetRetentionPoliciesIdAssignmentsOptionsArgTypeField], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.fields = fields
        self.marker = marker
        self.limit = limit

class PostRetentionPolicyAssignmentsRequestBodyArgAssignToFieldTypeField(str, Enum):
    ENTERPRISE = 'enterprise'
    FOLDER = 'folder'
    METADATA_TEMPLATE = 'metadata_template'

class PostRetentionPolicyAssignmentsRequestBodyArgAssignToField(BaseObject):
    def __init__(self, type: PostRetentionPolicyAssignmentsRequestBodyArgAssignToFieldTypeField, id: str, **kwargs):
        """
        :param type: The type of item to assign the policy to.
        :type type: PostRetentionPolicyAssignmentsRequestBodyArgAssignToFieldTypeField
        :param id: The ID of item to assign the policy to.
            Set to `null` or omit when `type` is set to
            `enterprise`.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PostRetentionPolicyAssignmentsRequestBodyArgFilterFieldsField(BaseObject):
    def __init__(self, field: Union[None, str] = None, value: Union[None, str] = None, **kwargs):
        """
        :param field: The metadata attribute key id.
        :type field: Union[None, str], optional
        :param value: The metadata attribute field id. For value, only
            enum and multiselect types are supported.
        :type value: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.field = field
        self.value = value

class PostRetentionPolicyAssignmentsRequestBodyArg(BaseObject):
    def __init__(self, policy_id: str, assign_to: PostRetentionPolicyAssignmentsRequestBodyArgAssignToField, filter_fields: Union[None, List[PostRetentionPolicyAssignmentsRequestBodyArgFilterFieldsField]] = None, start_date_field: Union[None, str] = None, **kwargs):
        """
        :param policy_id: The ID of the retention policy to assign
        :type policy_id: str
        :param assign_to: The item to assign the policy to
        :type assign_to: PostRetentionPolicyAssignmentsRequestBodyArgAssignToField
        :param filter_fields: If the `assign_to` type is `metadata_template`,
            then optionally add the `filter_fields` parameter which will
            require an array of objects with a field entry and a value entry.
            Currently only one object of `field` and `value` is supported.
        :type filter_fields: Union[None, List[PostRetentionPolicyAssignmentsRequestBodyArgFilterFieldsField]], optional
        :param start_date_field: The date the retention policy assignment begins.
            If the `assigned_to` type is `metadata_template`,
            this field can be a date field's metadata attribute key id.
        :type start_date_field: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.policy_id = policy_id
        self.assign_to = assign_to
        self.filter_fields = filter_fields
        self.start_date_field = start_date_field

class GetRetentionPolicyAssignmentsIdOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, **kwargs):
        """
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
        self.fields = fields

class GetRetentionPolicyAssignmentsIdFilesUnderRetentionOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, limit: Union[None, int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class GetRetentionPolicyAssignmentsIdFileVersionsUnderRetentionOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, limit: Union[None, int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class RetentionPolicyAssignmentsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_retention_policies_id_assignments(self, retention_policy_id: str, options: GetRetentionPoliciesIdAssignmentsOptionsArg = None) -> RetentionPolicyAssignments:
        """
        Returns a list of all retention policy assignments associated with a specified
        
        retention policy.

        :param retention_policy_id: The ID of the retention policy.
            Example: "982312"
        :type retention_policy_id: str
        """
        if options is None:
            options = GetRetentionPoliciesIdAssignmentsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policies/', retention_policy_id, '/assignments']), FetchOptions(method='GET', params={'type': options.type, 'fields': options.fields, 'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return RetentionPolicyAssignments.from_dict(json.loads(response.text))
    def post_retention_policy_assignments(self, request_body: PostRetentionPolicyAssignmentsRequestBodyArg) -> RetentionPolicyAssignment:
        """
        Assigns a retention policy to an item.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policy_assignments']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return RetentionPolicyAssignment.from_dict(json.loads(response.text))
    def get_retention_policy_assignments_id(self, retention_policy_assignment_id: str, options: GetRetentionPolicyAssignmentsIdOptionsArg = None) -> RetentionPolicyAssignment:
        """
        Retrieves a retention policy assignment
        :param retention_policy_assignment_id: The ID of the retention policy assignment.
            Example: "1233123"
        :type retention_policy_assignment_id: str
        """
        if options is None:
            options = GetRetentionPolicyAssignmentsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policy_assignments/', retention_policy_assignment_id]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return RetentionPolicyAssignment.from_dict(json.loads(response.text))
    def delete_retention_policy_assignments_id(self, retention_policy_assignment_id: str):
        """
        Removes a retention policy assignment
        
        applied to content.

        :param retention_policy_assignment_id: The ID of the retention policy assignment.
            Example: "1233123"
        :type retention_policy_assignment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policy_assignments/', retention_policy_assignment_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def get_retention_policy_assignments_id_files_under_retention(self, retention_policy_assignment_id: str, options: GetRetentionPolicyAssignmentsIdFilesUnderRetentionOptionsArg = None) -> FilesUnderRetention:
        """
        Returns a list of files under retention for a retention policy assignment.
        :param retention_policy_assignment_id: The ID of the retention policy assignment.
            Example: "1233123"
        :type retention_policy_assignment_id: str
        """
        if options is None:
            options = GetRetentionPolicyAssignmentsIdFilesUnderRetentionOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policy_assignments/', retention_policy_assignment_id, '/files_under_retention']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return FilesUnderRetention.from_dict(json.loads(response.text))
    def get_retention_policy_assignments_id_file_versions_under_retention(self, retention_policy_assignment_id: str, options: GetRetentionPolicyAssignmentsIdFileVersionsUnderRetentionOptionsArg = None) -> FilesUnderRetention:
        """
        Returns a list of file versions under retention for a retention policy
        
        assignment.

        :param retention_policy_assignment_id: The ID of the retention policy assignment.
            Example: "1233123"
        :type retention_policy_assignment_id: str
        """
        if options is None:
            options = GetRetentionPolicyAssignmentsIdFileVersionsUnderRetentionOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policy_assignments/', retention_policy_assignment_id, '/file_versions_under_retention']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return FilesUnderRetention.from_dict(json.loads(response.text))