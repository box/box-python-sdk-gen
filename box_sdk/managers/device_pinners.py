from enum import Enum

from typing import Optional

import json

from typing import Dict

from box_sdk.schemas import DevicePinner

from box_sdk.schemas import ClientError

from box_sdk.schemas import DevicePinners

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import to_map

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetEnterpriseDevicePinnersDirectionArg(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'

class DevicePinnersManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_device_pinner_by_id(self, device_pinner_id: str) -> DevicePinner:
        """
        Retrieves information about an individual device pin.
        :param device_pinner_id: The ID of the device pin
            Example: "2324234"
        :type device_pinner_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/device_pinners/', device_pinner_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return DevicePinner.from_dict(json.loads(response.text))
    def delete_device_pinner_by_id(self, device_pinner_id: str):
        """
        Deletes an individual device pin.
        :param device_pinner_id: The ID of the device pin
            Example: "2324234"
        :type device_pinner_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/device_pinners/', device_pinner_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content
    def get_enterprise_device_pinners(self, enterprise_id: str, marker: Optional[str] = None, limit: Optional[int] = None, direction: Optional[GetEnterpriseDevicePinnersDirectionArg] = None) -> DevicePinners:
        """
        Retrieves all the device pins within an enterprise.
        
        The user must have admin privileges, and the application

        
        needs the "manage enterprise" scope to make this call.

        :param enterprise_id: The ID of the enterprise
            Example: "3442311"
        :type enterprise_id: str
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param direction: The direction to sort results in. This can be either in alphabetical ascending
            (`ASC`) or descending (`DESC`) order.
        :type direction: Optional[GetEnterpriseDevicePinnersDirectionArg], optional
        """
        query_params: Dict = {'marker': marker, 'limit': limit, 'direction': direction}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/enterprises/', enterprise_id, '/device_pinners']), FetchOptions(method='GET', params=to_map(query_params), auth=self.auth, network_session=self.network_session))
        return DevicePinners.from_dict(json.loads(response.text))