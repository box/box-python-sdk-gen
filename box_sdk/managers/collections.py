from typing import Optional

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import Collections

from box_sdk.schemas import ClientError

from box_sdk.schemas import Items

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetCollectionsOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.offset = offset
        self.limit = limit

class GetCollectionItemsOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.offset = offset
        self.limit = limit

class CollectionsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_collections(self, options: GetCollectionsOptionsArg = None) -> Collections:
        """
        Retrieves all collections for a given user.
        
        Currently, only the `favorites` collection

        
        is supported.

        """
        if options is None:
            options = GetCollectionsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collections']), FetchOptions(method='GET', params={'fields': options.fields, 'offset': options.offset, 'limit': options.limit}, auth=self.auth, network_session=self.network_session))
        return Collections.from_dict(json.loads(response.text))
    def get_collection_items(self, collection_id: str, options: GetCollectionItemsOptionsArg = None) -> Items:
        """
        Retrieves the files and/or folders contained within
        
        this collection.

        :param collection_id: The ID of the collection.
            Example: "926489"
        :type collection_id: str
        """
        if options is None:
            options = GetCollectionItemsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collections/', collection_id, '/items']), FetchOptions(method='GET', params={'fields': options.fields, 'offset': options.offset, 'limit': options.limit}, auth=self.auth, network_session=self.network_session))
        return Items.from_dict(json.loads(response.text))