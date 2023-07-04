from typing import Optional

from typing import Dict

import json

from box_sdk.schemas import RecentItems

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import to_map

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class RecentItemsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_recent_items(self, fields: Optional[str] = None, limit: Optional[int] = None, marker: Optional[str] = None) -> RecentItems:
        """
        Returns information about the recent items accessed
        
        by a user, either in the last 90 days or up to the last

        
        1000 items accessed.

        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        """
        query_params: Dict = {'fields': fields, 'limit': limit, 'marker': marker}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/recent_items']), FetchOptions(method='GET', params=to_map(query_params), auth=self.auth, network_session=self.network_session))
        return RecentItems.from_dict(json.loads(response.text))