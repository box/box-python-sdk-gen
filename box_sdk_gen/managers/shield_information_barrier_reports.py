from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import ShieldInformationBarrierBase

from box_sdk_gen.schemas import ShieldInformationBarrierReports

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import ShieldInformationBarrierReport

from box_sdk_gen.schemas import ShieldInformationBarrierReference

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json import SerializedData


class ShieldInformationBarrierReportsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_shield_information_barrier_reports(
        self,
        shield_information_barrier_id: str,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrierReports:
        """
        Lists shield information barrier reports.
        :param shield_information_barrier_id: The ID of the shield information barrier.
        :type shield_information_barrier_id: str
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({
            'shield_information_barrier_id': to_string(shield_information_barrier_id),
            'marker': to_string(marker),
            'limit': to_string(limit),
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/shield_information_barrier_reports']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, ShieldInformationBarrierReports)

    def create_shield_information_barrier_report(
        self,
        shield_information_barrier: Optional[ShieldInformationBarrierBase] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrierReport:
        """
        Creates a shield information barrier report for a given barrier.
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'shield_information_barrier': shield_information_barrier}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/shield_information_barrier_reports']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, ShieldInformationBarrierReport)

    def get_shield_information_barrier_report_by_id(
        self,
        shield_information_barrier_report_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrierReport:
        """
        Retrieves a shield information barrier report by its ID.
        :param shield_information_barrier_report_id: The ID of the shield information barrier Report.
            Example: "3423"
        :type shield_information_barrier_report_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/shield_information_barrier_reports/',
                to_string(shield_information_barrier_report_id),
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, ShieldInformationBarrierReport)
