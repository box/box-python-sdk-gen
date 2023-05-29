from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Optional

import json

from typing import Dict

from box_sdk.schemas import ShieldInformationBarrier

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateShieldInformationBarrierChangeStatusRequestBodyArgStatusField(str, Enum):
    PENDING = 'pending'
    DISABLED = 'disabled'

class CreateShieldInformationBarrierChangeStatusRequestBodyArg(BaseObject):
    def __init__(self, id: str, status: CreateShieldInformationBarrierChangeStatusRequestBodyArgStatusField, **kwargs):
        """
        :param id: The ID of the shield information barrier.
        :type id: str
        :param status: The desired status for the shield information barrier.
        :type status: CreateShieldInformationBarrierChangeStatusRequestBodyArgStatusField
        """
        super().__init__(**kwargs)
        self.id = id
        self.status = status

class GetShieldInformationBarriersOptionsArg(BaseObject):
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

class ShieldInformationBarriersManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def get_shield_information_barrier_by_id(self, shield_information_barrier_id: str) -> ShieldInformationBarrier:
        """
        Get shield information barrier based on provided ID..
        :param shield_information_barrier_id: The ID of the shield information barrier.
            Example: "1910967"
        :type shield_information_barrier_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barriers/', shield_information_barrier_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return ShieldInformationBarrier.from_dict(json.loads(response.text))
    def create_shield_information_barrier_change_status(self, request_body: CreateShieldInformationBarrierChangeStatusRequestBodyArg) -> ShieldInformationBarrier:
        """
        Change status of shield information barrier with the specified ID.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barriers/change_status']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return ShieldInformationBarrier.from_dict(json.loads(response.text))
    def get_shield_information_barriers(self, options: GetShieldInformationBarriersOptionsArg = None) -> None:
        """
        Retrieves a list of shield information barrier objects
        
        for the enterprise of JWT.

        """
        if options is None:
            options = GetShieldInformationBarriersOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barriers']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth, network_session=self.network_session))
        return None
    def create_shield_information_barrier(self, request_body: ShieldInformationBarrier) -> ShieldInformationBarrier:
        """
        Creates a shield information barrier to
        
        separate individuals/groups within the same

        
        firm and prevents confidential information passing between them.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barriers']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return ShieldInformationBarrier.from_dict(json.loads(response.text))