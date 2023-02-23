from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import TrashWebLink

from schemas import ClientError

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
    def getWebLinksIdTrash(self, webLinkId: str, options: GetWebLinksIdTrashOptionsArg = None) -> TrashWebLink:
        """
        Retrieves a web link that has been moved to the trash.
        :param webLinkId: The ID of the web link.
            Example: "12345"
        :type webLinkId: str
        """
        if options is None:
            options = GetWebLinksIdTrashOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', webLinkId, '/trash']), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return TrashWebLink.from_dict(json.loads(response.text))
    def deleteWebLinksIdTrash(self, webLinkId: str):
        """
        Permanently deletes a web link that is in the trash.
        
        This action cannot be undone.

        :param webLinkId: The ID of the web link.
            Example: "12345"
        :type webLinkId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', webLinkId, '/trash']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content