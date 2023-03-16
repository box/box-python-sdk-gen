from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import StoragePolicies

from box_sdk.schemas import ClientError

from box_sdk.schemas import StoragePolicy

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetStoragePoliciesOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, marker: Union[None, str] = None, limit: Union[None, int] = None, **kwargs):
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
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.marker = marker
        self.limit = limit

class StoragePoliciesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_storage_policies(self, options: GetStoragePoliciesOptionsArg = None) -> StoragePolicies:
        """
        Fetches all the storage policies in the enterprise.
        """
        if options is None:
            options = GetStoragePoliciesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policies']), FetchOptions(method='GET', params={'fields': options.fields, 'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return StoragePolicies.from_dict(json.loads(response.text))
    def get_storage_policies_id(self, storage_policy_id: str) -> StoragePolicy:
        """
        Fetches a specific storage policy.
        :param storage_policy_id: The ID of the storage policy.
            Example: "34342"
        :type storage_policy_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policies/', storage_policy_id]), FetchOptions(method='GET', auth=self.auth))
        return StoragePolicy.from_dict(json.loads(response.text))