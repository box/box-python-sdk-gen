from enum import Enum

from typing import Optional

from typing import List

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import RetentionPolicies

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import RetentionPolicy

from box_sdk_gen.schemas import UserMini

from box_sdk_gen.schemas import UserBase

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


class GetRetentionPoliciesPolicyTypeArg(str, Enum):
    FINITE = 'finite'
    INDEFINITE = 'indefinite'


class CreateRetentionPolicyPolicyTypeArg(str, Enum):
    FINITE = 'finite'
    INDEFINITE = 'indefinite'


class CreateRetentionPolicyDispositionActionArg(str, Enum):
    PERMANENTLY_DELETE = 'permanently_delete'
    REMOVE_RETENTION = 'remove_retention'


class CreateRetentionPolicyRetentionTypeArg(str, Enum):
    MODIFIABLE = 'modifiable'
    NON_MODIFIABLE = 'non_modifiable'


class RetentionPoliciesManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_retention_policies(
        self,
        policy_name: Optional[str] = None,
        policy_type: Optional[GetRetentionPoliciesPolicyTypeArg] = None,
        created_by_user_id: Optional[str] = None,
        fields: Optional[List[str]] = None,
        limit: Optional[int] = None,
        marker: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> RetentionPolicies:
        """
        Retrieves all of the retention policies for an enterprise.
        :param policy_name: Filters results by a case sensitive prefix of the name of
            retention policies.
        :type policy_name: Optional[str], optional
        :param policy_type: Filters results by the type of retention policy.
        :type policy_type: Optional[GetRetentionPoliciesPolicyTypeArg], optional
        :param created_by_user_id: Filters results by the ID of the user who created policy.
        :type created_by_user_id: Optional[str], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[List[str]], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
        :type marker: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({
            'policy_name': to_string(policy_name),
            'policy_type': to_string(policy_type),
            'created_by_user_id': to_string(created_by_user_id),
            'fields': to_string(fields),
            'limit': to_string(limit),
            'marker': to_string(marker),
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/retention_policies']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, RetentionPolicies)

    def create_retention_policy(
        self,
        policy_name: str,
        policy_type: CreateRetentionPolicyPolicyTypeArg,
        disposition_action: CreateRetentionPolicyDispositionActionArg,
        description: Optional[str] = None,
        retention_length: Optional[str] = None,
        retention_type: Optional[CreateRetentionPolicyRetentionTypeArg] = None,
        can_owner_extend_retention: Optional[bool] = None,
        are_owners_notified: Optional[bool] = None,
        custom_notification_recipients: Optional[List[UserMini]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> RetentionPolicy:
        """
        Creates a retention policy.
        :param policy_name: The name for the retention policy
        :type policy_name: str
        :param policy_type: The type of the retention policy. A retention
            policy type can either be `finite`, where a
            specific amount of time to retain the content is known
            upfront, or `indefinite`, where the amount of time
            to retain the content is still unknown.
        :type policy_type: CreateRetentionPolicyPolicyTypeArg
        :param disposition_action: The disposition action of the retention policy.
            `permanently_delete` deletes the content
            retained by the policy permanently.
            `remove_retention` lifts retention policy
            from the content, allowing it to be deleted
            by users once the retention policy has expired.
        :type disposition_action: CreateRetentionPolicyDispositionActionArg
        :param description: The additional text description of the retention policy.
        :type description: Optional[str], optional
        :param retention_length: The length of the retention policy. This value
            specifies the duration in days that the retention
            policy will be active for after being assigned to
            content.  If the policy has a `policy_type` of
            `indefinite`, the `retention_length` will also be
            `indefinite`.
        :type retention_length: Optional[str], optional
        :param retention_type: Specifies the retention type:
            * `modifiable`: You can modify the retention policy. For example,
            you can add or remove folders, shorten or lengthen
            the policy duration, or delete the assignment.
            Use this type if your retention policy
            is not related to any regulatory purposes.
            * `non_modifiable`: You can modify the retention policy
            only in a limited way: add a folder, lengthen the duration,
            retire the policy, change the disposition action
            or notification settings. You cannot perform other actions,
            such as deleting the assignment or shortening the
            policy duration. Use this type to ensure
            compliance with regulatory retention policies.
        :type retention_type: Optional[CreateRetentionPolicyRetentionTypeArg], optional
        :param can_owner_extend_retention: Whether the owner of a file will be allowed to
            extend the retention.
        :type can_owner_extend_retention: Optional[bool], optional
        :param are_owners_notified: Whether owner and co-owners of a file are notified
            when the policy nears expiration.
        :type are_owners_notified: Optional[bool], optional
        :param custom_notification_recipients: A list of users notified when
            the retention policy duration is about to end.
        :type custom_notification_recipients: Optional[List[UserMini]], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'policy_name': policy_name,
            'description': description,
            'policy_type': policy_type,
            'disposition_action': disposition_action,
            'retention_length': retention_length,
            'retention_type': retention_type,
            'can_owner_extend_retention': can_owner_extend_retention,
            'are_owners_notified': are_owners_notified,
            'custom_notification_recipients': custom_notification_recipients,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/retention_policies']),
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
        return deserialize(response.data, RetentionPolicy)

    def get_retention_policy_by_id(
        self,
        retention_policy_id: str,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> RetentionPolicy:
        """
        Retrieves a retention policy.
        :param retention_policy_id: The ID of the retention policy.
            Example: "982312"
        :type retention_policy_id: str
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
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/retention_policies/',
                to_string(retention_policy_id),
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
        return deserialize(response.data, RetentionPolicy)

    def update_retention_policy_by_id(
        self,
        retention_policy_id: str,
        policy_name: Optional[str] = None,
        description: Optional[str] = None,
        disposition_action: Optional[str] = None,
        retention_type: Optional[str] = None,
        retention_length: Optional[str] = None,
        status: Optional[str] = None,
        can_owner_extend_retention: Optional[bool] = None,
        are_owners_notified: Optional[bool] = None,
        custom_notification_recipients: Optional[List[UserBase]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> RetentionPolicy:
        """
        Updates a retention policy.
        :param retention_policy_id: The ID of the retention policy.
            Example: "982312"
        :type retention_policy_id: str
        :param policy_name: The name for the retention policy
        :type policy_name: Optional[str], optional
        :param description: The additional text description of the retention policy.
        :type description: Optional[str], optional
        :param disposition_action: The disposition action of the retention policy.
            This action can be `permanently_delete`, which
            will cause the content retained by the policy
            to be permanently deleted, or `remove_retention`,
            which will lift the retention policy from the content,
            allowing it to be deleted by users,
            once the retention policy has expired.
            You can use "null" if you don't want to change `disposition_action`.
        :type disposition_action: Optional[str], optional
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
        :type retention_type: Optional[str], optional
        :param retention_length: The length of the retention policy. This value
            specifies the duration in days that the retention
            policy will be active for after being assigned to
            content.  If the policy has a `policy_type` of
            `indefinite`, the `retention_length` will also be
            `indefinite`.
        :type retention_length: Optional[str], optional
        :param status: Used to retire a retention policy.
            If not retiring a policy, do not include this parameter
            or set it to `null`.
        :type status: Optional[str], optional
        :param can_owner_extend_retention: Determines if the owner of items under the policy
            can extend the retention when the original retention
            duration is about to end.
        :type can_owner_extend_retention: Optional[bool], optional
        :param are_owners_notified: Determines if owners and co-owners of items
            under the policy are notified when
            the retention duration is about to end.
        :type are_owners_notified: Optional[bool], optional
        :param custom_notification_recipients: A list of users notified when the retention duration is about to end.
        :type custom_notification_recipients: Optional[List[UserBase]], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'policy_name': policy_name,
            'description': description,
            'disposition_action': disposition_action,
            'retention_type': retention_type,
            'retention_length': retention_length,
            'status': status,
            'can_owner_extend_retention': can_owner_extend_retention,
            'are_owners_notified': are_owners_notified,
            'custom_notification_recipients': custom_notification_recipients,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/retention_policies/',
                to_string(retention_policy_id),
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
        return deserialize(response.data, RetentionPolicy)

    def delete_retention_policy_by_id(
        self,
        retention_policy_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Permanently deletes a retention policy.
        :param retention_policy_id: The ID of the retention policy.
            Example: "982312"
        :type retention_policy_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/retention_policies/',
                to_string(retention_policy_id),
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
