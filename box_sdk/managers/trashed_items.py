from enum import Enum

from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import Items

from box_sdk.schemas import ClientError

class GetFoldersTrashItemsOptionsArgDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'

class GetFoldersTrashItemsOptionsArgSortField(str, Enum):
    ID = 'id'
    NAME = 'name'
    DATE = 'date'
    SIZE = 'size'

class GetFoldersTrashItemsOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, limit: Union[None, int] = None, offset: Union[None, int] = None, usemarker: Union[None, bool] = None, marker: Union[None, str] = None, direction: Union[None, GetFoldersTrashItemsOptionsArgDirectionField] = None, sort: Union[None, GetFoldersTrashItemsOptionsArgSortField] = None, **kwargs):
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
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Union[None, int], optional
        :param usemarker: Specifies whether to use marker-based pagination instead of
            offset-based pagination. Only one pagination method can
            be used at a time.
            By setting this value to true, the API will return a `marker` field
            that can be passed as a parameter to this endpoint to get the next
            page of the response.
        :type usemarker: Union[None, bool], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param direction: The direction to sort results in. This can be either in alphabetical ascending
            (`ASC`) or descending (`DESC`) order.
        :type direction: Union[None, GetFoldersTrashItemsOptionsArgDirectionField], optional
        :param sort: Defines the **second** attribute by which items
            are sorted.
            Items are always sorted by their `type` first, with
            folders listed before files, and files listed
            before web links.
            This parameter is not supported when using marker-based pagination.
        :type sort: Union[None, GetFoldersTrashItemsOptionsArgSortField], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.limit = limit
        self.offset = offset
        self.usemarker = usemarker
        self.marker = marker
        self.direction = direction
        self.sort = sort

class TrashedItemsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFoldersTrashItems(self, options: GetFoldersTrashItemsOptionsArg = None) -> Items:
        """
        Retrieves the files and folders that have been moved
        
        to the trash.

        
        Any attribute in the full files or folders objects can be passed

        
        in with the `fields` parameter to retrieve those specific

        
        attributes that are not returned by default.

        
        This endpoint defaults to use offset-based pagination, yet also supports

        
        marker-based pagination using the `marker` parameter.

        """
        if options is None:
            options = GetFoldersTrashItemsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/trash/items']), FetchOptions(method='GET', params={'fields': options.fields, 'limit': options.limit, 'offset': options.offset, 'usemarker': options.usemarker, 'marker': options.marker, 'direction': options.direction, 'sort': options.sort}, auth=self.auth))
        return Items.from_dict(json.loads(response.text))