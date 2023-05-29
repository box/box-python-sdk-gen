from typing import Optional

from box_sdk.base_object import BaseObject

import json

from typing import Dict

from box_sdk.schemas import ShieldInformationBarrierReport

from box_sdk.schemas import ClientError

from box_sdk.schemas import ShieldInformationBarrierReference

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetShieldInformationBarrierReportsOptionsArg(BaseObject):
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

class ShieldInformationBarrierReportsManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def get_shield_information_barrier_reports(self, shield_information_barrier_id: str, options: GetShieldInformationBarrierReportsOptionsArg = None) -> None:
        """
        Lists shield information barrier reports with specific IDs.
        :param shield_information_barrier_id: The ID of the shield information barrier.
            Example: "1910967"
        :type shield_information_barrier_id: str
        """
        if options is None:
            options = GetShieldInformationBarrierReportsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_reports']), FetchOptions(method='GET', params={'shield_information_barrier_id': shield_information_barrier_id, 'marker': options.marker, 'limit': options.limit}, auth=self.auth, network_session=self.network_session))
        return None
    def create_shield_information_barrier_report(self, request_body: ShieldInformationBarrierReference) -> ShieldInformationBarrierReport:
        """
        Creates a shield information barrier report for a given barrier.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_reports']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return ShieldInformationBarrierReport.from_dict(json.loads(response.text))
    def get_shield_information_barrier_report_by_id(self, shield_information_barrier_report_id: str) -> ShieldInformationBarrierReport:
        """
        Retrieves a shield information barrier report by its ID.
        :param shield_information_barrier_report_id: The ID of the shield information barrier Report.
            Example: "3423"
        :type shield_information_barrier_report_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_reports/', shield_information_barrier_report_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return ShieldInformationBarrierReport.from_dict(json.loads(response.text))