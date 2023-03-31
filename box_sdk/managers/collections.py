from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import Collections

from box_sdk.schemas import ClientError

from box_sdk.schemas import Items

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetCollectionsOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, offset: Union[None, int] = None, limit: Union[None, int] = None, **kwargs):
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
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Union[None, int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.offset = offset
        self.limit = limit

class GetCollectionItemsOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, offset: Union[None, int] = None, limit: Union[None, int] = None, **kwargs):
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
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Union[None, int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.offset = offset
        self.limit = limit

class CollectionsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_collections(self, options: GetCollectionsOptionsArg = None) -> Collections:
        """
        Retrieves all collections for a given user.
        
        Currently, only the `favorites` collection

        
        is supported.

        """
        if options is None:
            options = GetCollectionsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collections']), FetchOptions(method='GET', params={'fields': options.fields, 'offset': options.offset, 'limit': options.limit}, auth=self.auth))
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collections/', collection_id, '/items']), FetchOptions(method='GET', params={'fields': options.fields, 'offset': options.offset, 'limit': options.limit}, auth=self.auth))
        return Items.from_dict(json.loads(response.text))