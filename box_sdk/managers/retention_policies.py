from enum import Enum

from typing import Union

from box_sdk.base_object import BaseObject

from typing import List

import json

from box_sdk.schemas import RetentionPolicies

from box_sdk.schemas import ClientError

from box_sdk.schemas import RetentionPolicy

from box_sdk.schemas import UserMini

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetRetentionPoliciesOptionsArgPolicyTypeField(str, Enum):
    FINITE = 'finite'
    INDEFINITE = 'indefinite'

class GetRetentionPoliciesOptionsArg(BaseObject):
    def __init__(self, policy_name: Union[None, str] = None, policy_type: Union[None, GetRetentionPoliciesOptionsArgPolicyTypeField] = None, created_by_user_id: Union[None, str] = None, fields: Union[None, str] = None, limit: Union[None, int] = None, marker: Union[None, str] = None, **kwargs):
        """
        :param policy_name: Filters results by a case sensitive prefix of the name of
            retention policies.
        :type policy_name: Union[None, str], optional
        :param policy_type: Filters results by the type of retention policy.
        :type policy_type: Union[None, GetRetentionPoliciesOptionsArgPolicyTypeField], optional
        :param created_by_user_id: Filters results by the ID of the user who created policy.
        :type created_by_user_id: Union[None, str], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
        :type marker: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.created_by_user_id = created_by_user_id
        self.fields = fields
        self.limit = limit
        self.marker = marker

class PostRetentionPoliciesRequestBodyArgPolicyTypeField(str, Enum):
    FINITE = 'finite'
    INDEFINITE = 'indefinite'

class PostRetentionPoliciesRequestBodyArgDispositionActionField(str, Enum):
    PERMANENTLY_DELETE = 'permanently_delete'
    REMOVE_RETENTION = 'remove_retention'

class PostRetentionPoliciesRequestBodyArgRetentionTypeField(str, Enum):
    MODIFIABLE = 'modifiable'
    NON_MODIFIABLE = 'non-modifiable'

class PostRetentionPoliciesRequestBodyArg(BaseObject):
    def __init__(self, policy_name: str, policy_type: PostRetentionPoliciesRequestBodyArgPolicyTypeField, disposition_action: PostRetentionPoliciesRequestBodyArgDispositionActionField, description: Union[None, str] = None, retention_length: Union[None, str] = None, retention_type: Union[None, PostRetentionPoliciesRequestBodyArgRetentionTypeField] = None, can_owner_extend_retention: Union[None, bool] = None, are_owners_notified: Union[None, bool] = None, custom_notification_recipients: Union[None, List[UserMini]] = None, **kwargs):
        """
        :param policy_name: The name for the retention policy
        :type policy_name: str
        :param policy_type: The type of the retention policy. A retention
            policy type can either be `finite`, where a
            specific amount of time to retain the content is known
            upfront, or `indefinite`, where the amount of time
            to retain the content is still unknown.
        :type policy_type: PostRetentionPoliciesRequestBodyArgPolicyTypeField
        :param disposition_action: The disposition action of the retention policy.
            `permanently_delete` deletes the content
            retained by the policy permanently.
            `remove_retention` lifts retention policy
            from the content, allowing it to be deleted
            by users once the retention policy has expired.
        :type disposition_action: PostRetentionPoliciesRequestBodyArgDispositionActionField
        :param description: The additional text description of the retention policy.
        :type description: Union[None, str], optional
        :param retention_length: The length of the retention policy. This value
            specifies the duration in days that the retention
            policy will be active for after being assigned to
            content.  If the policy has a `policy_type` of
            `indefinite`, the `retention_length` will also be
            `indefinite`.
        :type retention_length: Union[None, str], optional
        :param retention_type: Specifies the retention type:
            * `modifiable`: You can modify the retention policy. For example,
            you can add or remove folders, shorten or lengthen
            the policy duration, or delete the assignment.
            Use this type if your retention policy
            is not related to any regulatory purposes.
            * `non-modifiable`: You can modify the retention policy
            only in a limited way: add a folder, lengthen the duration,
            retire the policy, change the disposition action
            or notification settings. You cannot perform other actions,
            such as deleting the assignment or shortening the
            policy duration. Use this type to ensure
            compliance with regulatory retention policies.
        :type retention_type: Union[None, PostRetentionPoliciesRequestBodyArgRetentionTypeField], optional
        :param can_owner_extend_retention: Whether the owner of a file will be allowed to
            extend the retention.
        :type can_owner_extend_retention: Union[None, bool], optional
        :param are_owners_notified: Whether owner and co-owners of a file are notified
            when the policy nears expiration.
        :type are_owners_notified: Union[None, bool], optional
        :param custom_notification_recipients: A list of users notified when
            the retention policy duration is about to end.
        :type custom_notification_recipients: Union[None, List[UserMini]], optional
        """
        super().__init__(**kwargs)
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.disposition_action = disposition_action
        self.description = description
        self.retention_length = retention_length
        self.retention_type = retention_type
        self.can_owner_extend_retention = can_owner_extend_retention
        self.are_owners_notified = are_owners_notified
        self.custom_notification_recipients = custom_notification_recipients

class GetRetentionPoliciesIdOptionsArg(BaseObject):
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

class PutRetentionPoliciesIdRequestBodyArgDispositionActionField(str, Enum):
    PERMANENTLY_DELETE = 'permanently_delete'
    REMOVE_RETENTION = 'remove_retention'

class PutRetentionPoliciesIdRequestBodyArg(BaseObject):
    def __init__(self, policy_name: Union[None, str] = None, description: Union[None, str] = None, disposition_action: Union[None, PutRetentionPoliciesIdRequestBodyArgDispositionActionField] = None, retention_type: Union[None, str] = None, retention_length: Union[None, str] = None, status: Union[None, str] = None, can_owner_extend_retention: Union[None, bool] = None, are_owners_notified: Union[None, bool] = None, custom_notification_recipients: Union[None, List[UserMini]] = None, **kwargs):
        """
        :param policy_name: The name for the retention policy
        :type policy_name: Union[None, str], optional
        :param description: The additional text description of the retention policy.
        :type description: Union[None, str], optional
        :param disposition_action: The disposition action of the retention policy.
            `permanently_delete` deletes the content
            retained by the policy permanently.
            `remove_retention` lifts retention policy
            from the content, allowing it to be deleted
            by users once the retention policy has expired.
        :type disposition_action: Union[None, PutRetentionPoliciesIdRequestBodyArgDispositionActionField], optional
        :param retention_type: Specifies the retention type:
            * `modifiable`: You can modify the retention policy. For example,
            you can add or remove folders, shorten or lengthen
            the policy duration, or delete the assignment.
            Use this type if your retention policy
            is not related to any regulatory purposes.
            * `non-modifiable`: You can modify the retention policy
            only in a limited way: add a folder, lengthen the duration,
            retire the policy, change the disposition action
            or notification settings. You cannot perform other actions,
            such as deleting the assignment or shortening the
            policy duration. Use this type to ensure
            compliance with regulatory retention policies.
            When updating a retention policy, you can use
            `non-modifiable` type only. You can convert a
            `modifiable` policy to `non-modifiable`, but
            not the other way around.
        :type retention_type: Union[None, str], optional
        :param retention_length: The length of the retention policy. This value
            specifies the duration in days that the retention
            policy will be active for after being assigned to
            content.  If the policy has a `policy_type` of
            `indefinite`, the `retention_length` will also be
            `indefinite`.
        :type retention_length: Union[None, str], optional
        :param status: Used to retire a retention policy.
            If not retiring a policy, do not include this parameter
            or set it to `null`.
        :type status: Union[None, str], optional
        :param can_owner_extend_retention: Determines if the owner of items under the policy
            can extend the retention when the original retention
            duration is about to end.
        :type can_owner_extend_retention: Union[None, bool], optional
        :param are_owners_notified: Determines if owners and co-owners of items
            under the policy are notified when
            the retention duration is about to end.
        :type are_owners_notified: Union[None, bool], optional
        :param custom_notification_recipients: A list of users notified when the retention duration is about to end.
        :type custom_notification_recipients: Union[None, List[UserMini]], optional
        """
        super().__init__(**kwargs)
        self.policy_name = policy_name
        self.description = description
        self.disposition_action = disposition_action
        self.retention_type = retention_type
        self.retention_length = retention_length
        self.status = status
        self.can_owner_extend_retention = can_owner_extend_retention
        self.are_owners_notified = are_owners_notified
        self.custom_notification_recipients = custom_notification_recipients

class RetentionPoliciesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_retention_policies(self, options: GetRetentionPoliciesOptionsArg = None) -> RetentionPolicies:
        """
        Retrieves all of the retention policies for an enterprise.
        """
        if options is None:
            options = GetRetentionPoliciesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policies']), FetchOptions(method='GET', params={'policy_name': options.policyName, 'policy_type': options.policyType, 'created_by_user_id': options.createdByUserId, 'fields': options.fields, 'limit': options.limit, 'marker': options.marker}, auth=self.auth))
        return RetentionPolicies.from_dict(json.loads(response.text))
    def post_retention_policies(self, request_body: PostRetentionPoliciesRequestBodyArg) -> RetentionPolicy:
        """
        Creates a retention policy.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policies']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return RetentionPolicy.from_dict(json.loads(response.text))
    def get_retention_policies_id(self, retention_policy_id: str, options: GetRetentionPoliciesIdOptionsArg = None) -> RetentionPolicy:
        """
        Retrieves a retention policy.
        :param retention_policy_id: The ID of the retention policy.
            Example: "982312"
        :type retention_policy_id: str
        """
        if options is None:
            options = GetRetentionPoliciesIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policies/', retention_policy_id]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return RetentionPolicy.from_dict(json.loads(response.text))
    def put_retention_policies_id(self, retention_policy_id: str, request_body: PutRetentionPoliciesIdRequestBodyArg) -> RetentionPolicy:
        """
        Updates a retention policy.
        :param retention_policy_id: The ID of the retention policy.
            Example: "982312"
        :type retention_policy_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policies/', retention_policy_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return RetentionPolicy.from_dict(json.loads(response.text))
    def delete_retention_policies_id(self, retention_policy_id: str):
        """
        Permanently deletes a retention policy.
        :param retention_policy_id: The ID of the retention policy.
            Example: "982312"
        :type retention_policy_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/retention_policies/', retention_policy_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content