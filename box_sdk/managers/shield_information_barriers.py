from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Union

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import ShieldInformationBarrier

from box_sdk.schemas import ClientError

class PostShieldInformationBarriersChangeStatusRequestBodyArgStatusField(str, Enum):
    PENDING = 'pending'
    DISABLED = 'disabled'

class PostShieldInformationBarriersChangeStatusRequestBodyArg(BaseObject):
    def __init__(self, id: str, status: PostShieldInformationBarriersChangeStatusRequestBodyArgStatusField, **kwargs):
        """
        :param id: The ID of the shield information barrier.
        :type id: str
        :param status: The desired status for the shield information barrier.
        :type status: PostShieldInformationBarriersChangeStatusRequestBodyArgStatusField
        """
        super().__init__(**kwargs)
        self.id = id
        self.status = status

class GetShieldInformationBarriersOptionsArg(BaseObject):
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

class ShieldInformationBarriersManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getShieldInformationBarriersId(self, shieldInformationBarrierId: str) -> ShieldInformationBarrier:
        """
        Get shield information barrier based on provided ID..
        :param shieldInformationBarrierId: The ID of the shield information barrier.
            Example: "1910967"
        :type shieldInformationBarrierId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barriers/', shieldInformationBarrierId]), FetchOptions(method='GET', auth=self.auth))
        return ShieldInformationBarrier.from_dict(json.loads(response.text))
    def postShieldInformationBarriersChangeStatus(self, requestBody: PostShieldInformationBarriersChangeStatusRequestBodyArg) -> ShieldInformationBarrier:
        """
        Change status of shield information barrier with the specified ID.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barriers/change_status']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return ShieldInformationBarrier.from_dict(json.loads(response.text))
    def getShieldInformationBarriers(self, options: GetShieldInformationBarriersOptionsArg = None) -> None:
        """
        Retrieves a list of shield information barrier objects
        
        for the enterprise of JWT.

        """
        if options is None:
            options = GetShieldInformationBarriersOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barriers']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return None
    def postShieldInformationBarriers(self, requestBody: ShieldInformationBarrier) -> ShieldInformationBarrier:
        """
        Creates a shield information barrier to
        
        separate individuals/groups within the same

        
        firm and prevents confidential information passing between them.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barriers']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return ShieldInformationBarrier.from_dict(json.loads(response.text))