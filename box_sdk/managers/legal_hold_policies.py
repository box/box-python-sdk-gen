from typing import Optional

from box_sdk.base_object import BaseObject

from typing import Union

import json

from box_sdk.schemas import LegalHoldPolicies

from box_sdk.schemas import ClientError

from box_sdk.schemas import LegalHoldPolicy

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetLegalHoldPoliciesOptionsArg(BaseObject):
    def __init__(self, policy_name: Optional[str] = None, fields: Optional[str] = None, marker: Optional[str] = None, limit: Optional[int] = None, **kwargs):
        """
        :param policy_name: Limits results to policies for which the names start with
            this search term. This is a case-insensitive prefix.
        :type policy_name: Optional[str], optional
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
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.policy_name = policy_name
        self.fields = fields
        self.marker = marker
        self.limit = limit

class CreateLegalHoldPolicyRequestBodyArg(BaseObject):
    def __init__(self, policy_name: str, description: Optional[str] = None, filter_started_at: Optional[str] = None, filter_ended_at: Optional[str] = None, is_ongoing: Optional[bool] = None, **kwargs):
        """
        :param policy_name: The name of the policy.
        :type policy_name: str
        :param description: A description for the policy.
        :type description: Optional[str], optional
        :param filter_started_at: The filter start date.
            When this policy is applied using a `custodian` legal
            hold assignments, it will only apply to file versions
            created or uploaded inside of the
            date range. Other assignment types, such as folders and
            files, will ignore the date filter.
            Required if `is_ongoing` is set to `false`.
        :type filter_started_at: Optional[str], optional
        :param filter_ended_at: The filter end date.
            When this policy is applied using a `custodian` legal
            hold assignments, it will only apply to file versions
            created or uploaded inside of the
            date range. Other assignment types, such as folders and
            files, will ignore the date filter.
            Required if `is_ongoing` is set to `false`.
        :type filter_ended_at: Optional[str], optional
        :param is_ongoing: Whether new assignments under this policy should
            continue applying to files even after initialization.
            When this policy is applied using a legal hold assignment,
            it will continue applying the policy to any new file versions
            even after it has been applied.
            For example, if a legal hold assignment is placed on a user
            today, and that user uploads a file tomorrow, that file will
            get held. This will continue until the policy is retired.
            Required if no filter dates are set.
        :type is_ongoing: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.policy_name = policy_name
        self.description = description
        self.filter_started_at = filter_started_at
        self.filter_ended_at = filter_ended_at
        self.is_ongoing = is_ongoing

class UpdateLegalHoldPolicyByIdRequestBodyArg(BaseObject):
    def __init__(self, policy_name: Optional[str] = None, description: Optional[str] = None, release_notes: Optional[str] = None, **kwargs):
        """
        :param policy_name: The name of the policy.
        :type policy_name: Optional[str], optional
        :param description: A description for the policy.
        :type description: Optional[str], optional
        :param release_notes: Notes around why the policy was released.
        :type release_notes: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.policy_name = policy_name
        self.description = description
        self.release_notes = release_notes

class LegalHoldPoliciesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_legal_hold_policies(self, options: GetLegalHoldPoliciesOptionsArg = None) -> LegalHoldPolicies:
        """
        Retrieves a list of legal hold policies that belong to
        
        an enterprise.

        """
        if options is None:
            options = GetLegalHoldPoliciesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policies']), FetchOptions(method='GET', params={'policy_name': options.policy_name, 'fields': options.fields, 'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return LegalHoldPolicies.from_dict(json.loads(response.text))
    def create_legal_hold_policy(self, request_body: CreateLegalHoldPolicyRequestBodyArg) -> LegalHoldPolicy:
        """
        Create a new legal hold policy.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policies']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return LegalHoldPolicy.from_dict(json.loads(response.text))
    def get_legal_hold_policy_by_id(self, legal_hold_policy_id: str) -> LegalHoldPolicy:
        """
        Retrieve a legal hold policy.
        :param legal_hold_policy_id: The ID of the legal hold policy
            Example: "324432"
        :type legal_hold_policy_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policies/', legal_hold_policy_id]), FetchOptions(method='GET', auth=self.auth))
        return LegalHoldPolicy.from_dict(json.loads(response.text))
    def update_legal_hold_policy_by_id(self, legal_hold_policy_id: str, request_body: UpdateLegalHoldPolicyByIdRequestBodyArg) -> LegalHoldPolicy:
        """
        Update legal hold policy.
        :param legal_hold_policy_id: The ID of the legal hold policy
            Example: "324432"
        :type legal_hold_policy_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policies/', legal_hold_policy_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return LegalHoldPolicy.from_dict(json.loads(response.text))
    def delete_legal_hold_policy_by_id(self, legal_hold_policy_id: str):
        """
        Delete an existing legal hold policy.
        
        This is an asynchronous process. The policy will not be

        
        fully deleted yet when the response returns.

        :param legal_hold_policy_id: The ID of the legal hold policy
            Example: "324432"
        :type legal_hold_policy_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policies/', legal_hold_policy_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content