from typing import Optional

from typing import Dict

import json

from box_sdk.schemas import StoragePolicies

from box_sdk.schemas import ClientError

from box_sdk.schemas import StoragePolicy

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import prepare_params

from box_sdk.utils import to_string

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class StoragePoliciesManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_storage_policies(self, fields: Optional[str] = None, marker: Optional[str] = None, limit: Optional[int] = None) -> StoragePolicies:
        """
        Fetches all the storage policies in the enterprise.
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields), 'marker': to_string(marker), 'limit': to_string(limit)})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policies']), FetchOptions(method='GET', params=query_params_map, auth=self.auth, network_session=self.network_session))
        return StoragePolicies.from_dict(json.loads(response.text))
    def get_storage_policy_by_id(self, storage_policy_id: str) -> StoragePolicy:
        """
        Fetches a specific storage policy.
        :param storage_policy_id: The ID of the storage policy.
            Example: "34342"
        :type storage_policy_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policies/', storage_policy_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return StoragePolicy.from_dict(json.loads(response.text))