from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import SignRequest

from schemas import ClientError

from schemas import SignRequests

from schemas import SignRequestCreateRequest

class GetSignRequestsOptionsArg(BaseObject):
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

class SignRequestsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def postSignRequestsIdCancel(self, signRequestId: str) -> SignRequest:
        """
        Cancels a sign request.
        :param signRequestId: The ID of the sign request
            Example: "33243242"
        :type signRequestId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_requests/', signRequestId, '/cancel']), FetchOptions(method='POST', auth=self.auth))
        return SignRequest.from_dict(json.loads(response.text))
    def postSignRequestsIdResend(self, signRequestId: str):
        """
        Resends a sign request email to all outstanding signers.
        :param signRequestId: The ID of the sign request
            Example: "33243242"
        :type signRequestId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_requests/', signRequestId, '/resend']), FetchOptions(method='POST', auth=self.auth))
        return response.content
    def getSignRequestsId(self, signRequestId: str) -> SignRequest:
        """
        Gets a sign request by ID.
        :param signRequestId: The ID of the sign request
            Example: "33243242"
        :type signRequestId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_requests/', signRequestId]), FetchOptions(method='GET', auth=self.auth))
        return SignRequest.from_dict(json.loads(response.text))
    def getSignRequests(self, options: GetSignRequestsOptionsArg = None) -> SignRequests:
        """
        Gets sign requests created by a user. If the `sign_files` and/or
        
        `parent_folder` are deleted, the sign request will not return in the list.

        """
        if options is None:
            options = GetSignRequestsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_requests']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return SignRequests.from_dict(json.loads(response.text))
    def postSignRequests(self, requestBody: SignRequestCreateRequest) -> SignRequest:
        """
        Creates a sign request. This involves preparing a document for signing and
        
        sending the sign request to signers.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_requests']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return SignRequest.from_dict(json.loads(response.text))