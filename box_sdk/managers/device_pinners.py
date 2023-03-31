from enum import Enum

from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import DevicePinner

from box_sdk.schemas import ClientError

from box_sdk.schemas import DevicePinners

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetEnterpriseDevicePinnersOptionsArgDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'

class GetEnterpriseDevicePinnersOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, limit: Union[None, int] = None, direction: Union[None, GetEnterpriseDevicePinnersOptionsArgDirectionField] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param direction: The direction to sort results in. This can be either in alphabetical ascending
            (`ASC`) or descending (`DESC`) order.
        :type direction: Union[None, GetEnterpriseDevicePinnersOptionsArgDirectionField], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit
        self.direction = direction

class DevicePinnersManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_device_pinner_by_id(self, device_pinner_id: str) -> DevicePinner:
        """
        Retrieves information about an individual device pin.
        :param device_pinner_id: The ID of the device pin
            Example: "2324234"
        :type device_pinner_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/device_pinners/', device_pinner_id]), FetchOptions(method='GET', auth=self.auth))
        return DevicePinner.from_dict(json.loads(response.text))
    def delete_device_pinner_by_id(self, device_pinner_id: str):
        """
        Deletes an individual device pin.
        :param device_pinner_id: The ID of the device pin
            Example: "2324234"
        :type device_pinner_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/device_pinners/', device_pinner_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def get_enterprise_device_pinners(self, enterprise_id: str, options: GetEnterpriseDevicePinnersOptionsArg = None) -> DevicePinners:
        """
        Retrieves all the device pins within an enterprise.
        
        The user must have admin privileges, and the application

        
        needs the "manage enterprise" scope to make this call.

        :param enterprise_id: The ID of the enterprise
            Example: "3442311"
        :type enterprise_id: str
        """
        if options is None:
            options = GetEnterpriseDevicePinnersOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/enterprises/', enterprise_id, '/device_pinners']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit, 'direction': options.direction}, auth=self.auth))
        return DevicePinners.from_dict(json.loads(response.text))