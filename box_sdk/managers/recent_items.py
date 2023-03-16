from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import RecentItems

from box_sdk.schemas import ClientError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetRecentItemsOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, limit: Union[None, int] = None, marker: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.limit = limit
        self.marker = marker

class RecentItemsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_recent_items(self, options: GetRecentItemsOptionsArg = None) -> RecentItems:
        """
        Returns information about the recent items accessed
        
        by a user, either in the last 90 days or up to the last

        
        1000 items accessed.

        """
        if options is None:
            options = GetRecentItemsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/recent_items']), FetchOptions(method='GET', params={'fields': options.fields, 'limit': options.limit, 'marker': options.marker}, auth=self.auth))
        return RecentItems.from_dict(json.loads(response.text))