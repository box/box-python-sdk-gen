from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import StoragePolicies

from schemas import ClientError

from schemas import StoragePolicy

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
    def getStoragePolicies(self, options: GetStoragePoliciesOptionsArg = None) -> StoragePolicies:
        """
        Fetches all the storage policies in the enterprise.
        """
        if options is None:
            options = GetStoragePoliciesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policies']), FetchOptions(method='GET', params={'fields': options.fields, 'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return StoragePolicies.from_dict(json.loads(response.text))
    def getStoragePoliciesId(self, storagePolicyId: str) -> StoragePolicy:
        """
        Fetches a specific storage policy.
        :param storagePolicyId: The ID of the storage policy.
            Example: "34342"
        :type storagePolicyId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/storage_policies/', storagePolicyId]), FetchOptions(method='GET', auth=self.auth))
        return StoragePolicy.from_dict(json.loads(response.text))