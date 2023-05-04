from typing import Optional

from box_sdk.base_object import BaseObject

from typing import Union

import json

from box_sdk.schemas import SignRequest

from box_sdk.schemas import ClientError

from box_sdk.schemas import SignRequests

from box_sdk.schemas import SignRequestCreateRequest

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetSignRequestsOptionsArg(BaseObject):
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

class SignRequestsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def cancel_sign_request(self, sign_request_id: str) -> SignRequest:
        """
        Cancels a sign request.
        :param sign_request_id: The ID of the sign request
            Example: "33243242"
        :type sign_request_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_requests/', sign_request_id, '/cancel']), FetchOptions(method='POST', auth=self.auth))
        return SignRequest.from_dict(json.loads(response.text))
    def resend_sign_request(self, sign_request_id: str):
        """
        Resends a sign request email to all outstanding signers.
        :param sign_request_id: The ID of the sign request
            Example: "33243242"
        :type sign_request_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_requests/', sign_request_id, '/resend']), FetchOptions(method='POST', auth=self.auth))
        return response.content
    def get_sign_request_by_id(self, sign_request_id: str) -> SignRequest:
        """
        Gets a sign request by ID.
        :param sign_request_id: The ID of the sign request
            Example: "33243242"
        :type sign_request_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_requests/', sign_request_id]), FetchOptions(method='GET', auth=self.auth))
        return SignRequest.from_dict(json.loads(response.text))
    def get_sign_requests(self, options: GetSignRequestsOptionsArg = None) -> SignRequests:
        """
        Gets sign requests created by a user. If the `sign_files` and/or
        
        `parent_folder` are deleted, the sign request will not return in the list.

        """
        if options is None:
            options = GetSignRequestsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_requests']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return SignRequests.from_dict(json.loads(response.text))
    def create_sign_request(self, request_body: SignRequestCreateRequest) -> SignRequest:
        """
        Creates a sign request. This involves preparing a document for signing and
        
        sending the sign request to signers.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_requests']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return SignRequest.from_dict(json.loads(response.text))