from enum import Enum

from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import DevicePinner

from box_sdk.schemas import ClientError

from box_sdk.schemas import DevicePinners

class GetEnterprisesIdDevicePinnersOptionsArgDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'

class GetEnterprisesIdDevicePinnersOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, limit: Union[None, int] = None, direction: Union[None, GetEnterprisesIdDevicePinnersOptionsArgDirectionField] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param direction: The direction to sort results in. This can be either in alphabetical ascending
            (`ASC`) or descending (`DESC`) order.
        :type direction: Union[None, GetEnterprisesIdDevicePinnersOptionsArgDirectionField], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit
        self.direction = direction

class DevicePinnersManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getDevicePinnersId(self, devicePinnerId: str) -> DevicePinner:
        """
        Retrieves information about an individual device pin.
        :param devicePinnerId: The ID of the device pin
            Example: "2324234"
        :type devicePinnerId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/device_pinners/', devicePinnerId]), FetchOptions(method='GET', auth=self.auth))
        return DevicePinner.from_dict(json.loads(response.text))
    def deleteDevicePinnersId(self, devicePinnerId: str):
        """
        Deletes an individual device pin.
        :param devicePinnerId: The ID of the device pin
            Example: "2324234"
        :type devicePinnerId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/device_pinners/', devicePinnerId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def getEnterprisesIdDevicePinners(self, enterpriseId: str, options: GetEnterprisesIdDevicePinnersOptionsArg = None) -> DevicePinners:
        """
        Retrieves all the device pins within an enterprise.
        
        The user must have admin privileges, and the application

        
        needs the "manage enterprise" scope to make this call.

        :param enterpriseId: The ID of the enterprise
            Example: "3442311"
        :type enterpriseId: str
        """
        if options is None:
            options = GetEnterprisesIdDevicePinnersOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/enterprises/', enterpriseId, '/device_pinners']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit, 'direction': options.direction}, auth=self.auth))
        return DevicePinners.from_dict(json.loads(response.text))