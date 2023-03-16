from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import TrashWebLink

from box_sdk.schemas import ClientError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetWebLinksIdTrashOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, **kwargs):
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
        """
        super().__init__(**kwargs)
        self.fields = fields

class TrashedWebLinksManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_web_links_id_trash(self, web_link_id: str, options: GetWebLinksIdTrashOptionsArg = None) -> TrashWebLink:
        """
        Retrieves a web link that has been moved to the trash.
        :param web_link_id: The ID of the web link.
            Example: "12345"
        :type web_link_id: str
        """
        if options is None:
            options = GetWebLinksIdTrashOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', web_link_id, '/trash']), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return TrashWebLink.from_dict(json.loads(response.text))
    def delete_web_links_id_trash(self, web_link_id: str):
        """
        Permanently deletes a web link that is in the trash.
        
        This action cannot be undone.

        :param web_link_id: The ID of the web link.
            Example: "12345"
        :type web_link_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', web_link_id, '/trash']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content