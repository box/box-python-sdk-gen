from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.schemas import DevicePinner

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import DevicePinners

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json import sd_to_json

from box_sdk_gen.json import SerializedData


class GetEnterpriseDevicePinnersDirectionArg(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class DevicePinnersManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_device_pinner_by_id(
        self,
        device_pinner_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> DevicePinner:
        """
        Retrieves information about an individual device pin.
        :param device_pinner_id: The ID of the device pin
            Example: "2324234"
        :type device_pinner_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/device_pinners/', to_string(device_pinner_id)
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, DevicePinner)

    def delete_device_pinner_by_id(
        self,
        device_pinner_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Deletes an individual device pin.
        :param device_pinner_id: The ID of the device pin
            Example: "2324234"
        :type device_pinner_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/device_pinners/', to_string(device_pinner_id)
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

    def get_enterprise_device_pinners(
        self,
        enterprise_id: str,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        direction: Optional[GetEnterpriseDevicePinnersDirectionArg] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> DevicePinners:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({
            'marker': to_string(marker),
            'limit': to_string(limit),
            'direction': to_string(direction),
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/enterprises/',
                to_string(enterprise_id),
                '/device_pinners',
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
        return deserialize(response.data, DevicePinners)
