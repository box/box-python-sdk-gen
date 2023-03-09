from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import LegalHoldPolicies

from box_sdk.schemas import ClientError

from box_sdk.schemas import LegalHoldPolicy

class GetLegalHoldPoliciesOptionsArg(BaseObject):
    def __init__(self, policyName: Union[None, str] = None, fields: Union[None, str] = None, marker: Union[None, str] = None, limit: Union[None, int] = None, **kwargs):
        """
        :param policyName: Limits results to policies for which the names start with
            this search term. This is a case-insensitive prefix.
        :type policyName: Union[None, str], optional
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
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.policyName = policyName
        self.fields = fields
        self.marker = marker
        self.limit = limit

class PostLegalHoldPoliciesRequestBodyArg(BaseObject):
    def __init__(self, policy_name: str, description: Union[None, str] = None, filter_started_at: Union[None, str] = None, filter_ended_at: Union[None, str] = None, is_ongoing: Union[None, bool] = None, **kwargs):
        """
        :param policy_name: The name of the policy.
        :type policy_name: str
        :param description: A description for the policy.
        :type description: Union[None, str], optional
        :param filter_started_at: The filter start date.
            When this policy is applied using a `custodian` legal
            hold assignments, it will only apply to file versions
            created or uploaded inside of the
            date range. Other assignment types, such as folders and
            files, will ignore the date filter.
            Required if `is_ongoing` is set to `false`.
        :type filter_started_at: Union[None, str], optional
        :param filter_ended_at: The filter end date.
            When this policy is applied using a `custodian` legal
            hold assignments, it will only apply to file versions
            created or uploaded inside of the
            date range. Other assignment types, such as folders and
            files, will ignore the date filter.
            Required if `is_ongoing` is set to `false`.
        :type filter_ended_at: Union[None, str], optional
        :param is_ongoing: Whether new assignments under this policy should
            continue applying to files even after initialization.
            When this policy is applied using a legal hold assignment,
            it will continue applying the policy to any new file versions
            even after it has been applied.
            For example, if a legal hold assignment is placed on a user
            today, and that user uploads a file tomorrow, that file will
            get held. This will continue until the policy is retired.
            Required if no filter dates are set.
        :type is_ongoing: Union[None, bool], optional
        """
        super().__init__(**kwargs)
        self.policy_name = policy_name
        self.description = description
        self.filter_started_at = filter_started_at
        self.filter_ended_at = filter_ended_at
        self.is_ongoing = is_ongoing

class PutLegalHoldPoliciesIdRequestBodyArg(BaseObject):
    def __init__(self, policy_name: Union[None, str] = None, description: Union[None, str] = None, release_notes: Union[None, str] = None, **kwargs):
        """
        :param policy_name: The name of the policy.
        :type policy_name: Union[None, str], optional
        :param description: A description for the policy.
        :type description: Union[None, str], optional
        :param release_notes: Notes around why the policy was released.
        :type release_notes: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.policy_name = policy_name
        self.description = description
        self.release_notes = release_notes

class LegalHoldPoliciesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getLegalHoldPolicies(self, options: GetLegalHoldPoliciesOptionsArg = None) -> LegalHoldPolicies:
        """
        Retrieves a list of legal hold policies that belong to
        
        an enterprise.

        """
        if options is None:
            options = GetLegalHoldPoliciesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policies']), FetchOptions(method='GET', params={'policy_name': options.policyName, 'fields': options.fields, 'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return LegalHoldPolicies.from_dict(json.loads(response.text))
    def postLegalHoldPolicies(self, requestBody: PostLegalHoldPoliciesRequestBodyArg) -> LegalHoldPolicy:
        """
        Create a new legal hold policy.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policies']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return LegalHoldPolicy.from_dict(json.loads(response.text))
    def getLegalHoldPoliciesId(self, legalHoldPolicyId: str) -> LegalHoldPolicy:
        """
        Retrieve a legal hold policy.
        :param legalHoldPolicyId: The ID of the legal hold policy
            Example: "324432"
        :type legalHoldPolicyId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policies/', legalHoldPolicyId]), FetchOptions(method='GET', auth=self.auth))
        return LegalHoldPolicy.from_dict(json.loads(response.text))
    def putLegalHoldPoliciesId(self, legalHoldPolicyId: str, requestBody: PutLegalHoldPoliciesIdRequestBodyArg) -> LegalHoldPolicy:
        """
        Update legal hold policy.
        :param legalHoldPolicyId: The ID of the legal hold policy
            Example: "324432"
        :type legalHoldPolicyId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policies/', legalHoldPolicyId]), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return LegalHoldPolicy.from_dict(json.loads(response.text))
    def deleteLegalHoldPoliciesId(self, legalHoldPolicyId: str):
        """
        Delete an existing legal hold policy.
        
        This is an asynchronous process. The policy will not be

        
        fully deleted yet when the response returns.

        :param legalHoldPolicyId: The ID of the legal hold policy
            Example: "324432"
        :type legalHoldPolicyId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/legal_hold_policies/', legalHoldPolicyId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content