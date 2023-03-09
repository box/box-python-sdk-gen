from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import ShieldInformationBarrierReport

from box_sdk.schemas import ClientError

from box_sdk.schemas import ShieldInformationBarrierReference

class GetShieldInformationBarrierReportsOptionsArg(BaseObject):
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

class ShieldInformationBarrierReportsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getShieldInformationBarrierReports(self, shieldInformationBarrierId: str, options: GetShieldInformationBarrierReportsOptionsArg = None) -> None:
        """
        Lists shield information barrier reports with specific IDs.
        :param shieldInformationBarrierId: The ID of the shield information barrier.
            Example: "1910967"
        :type shieldInformationBarrierId: str
        """
        if options is None:
            options = GetShieldInformationBarrierReportsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_reports']), FetchOptions(method='GET', params={'shield_information_barrier_id': shieldInformationBarrierId, 'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return None
    def postShieldInformationBarrierReports(self, requestBody: ShieldInformationBarrierReference) -> ShieldInformationBarrierReport:
        """
        Creates a shield information barrier report for a given barrier.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_reports']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return ShieldInformationBarrierReport.from_dict(json.loads(response.text))
    def getShieldInformationBarrierReportsId(self, shieldInformationBarrierReportId: str) -> ShieldInformationBarrierReport:
        """
        Retrieves a shield information barrier report by its ID.
        :param shieldInformationBarrierReportId: The ID of the shield information barrier Report.
            Example: "3423"
        :type shieldInformationBarrierReportId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_reports/', shieldInformationBarrierReportId]), FetchOptions(method='GET', auth=self.auth))
        return ShieldInformationBarrierReport.from_dict(json.loads(response.text))