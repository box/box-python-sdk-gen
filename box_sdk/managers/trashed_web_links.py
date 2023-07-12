from typing import Optional

from box_sdk.base_object import BaseObject

from typing import Dict

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import TrashWebLinkRestored

from box_sdk.schemas import ClientError

from box_sdk.schemas import TrashWebLink

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import prepare_params

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateWebLinkByIdParentArg(BaseObject):
    def __init__(self, id: Optional[str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class TrashedWebLinksManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def create_web_link_by_id(self, web_link_id: str, name: Optional[str] = None, parent: Optional[CreateWebLinkByIdParentArg] = None, fields: Optional[str] = None) -> TrashWebLinkRestored:
        """
        Restores a web link that has been moved to the trash.
        
        An optional new parent ID can be provided to restore the  web link to in case

        
        the original folder has been deleted.

        :param web_link_id: The ID of the web link.
            Example: "12345"
        :type web_link_id: str
        :param name: An optional new name for the web link.
        :type name: Optional[str], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        """
        request_body: BaseObject = BaseObject(name=name, parent=parent)
        query_params: Dict = {'fields': fields}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', web_link_id]), FetchOptions(method='POST', params=prepare_params(query_params), body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return TrashWebLinkRestored.from_dict(json.loads(response.text))
    def get_web_link_trash(self, web_link_id: str, fields: Optional[str] = None) -> TrashWebLink:
        """
        Retrieves a web link that has been moved to the trash.
        :param web_link_id: The ID of the web link.
            Example: "12345"
        :type web_link_id: str
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        """
        query_params: Dict = {'fields': fields}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', web_link_id, '/trash']), FetchOptions(method='GET', params=prepare_params(query_params), auth=self.auth, network_session=self.network_session))
        return TrashWebLink.from_dict(json.loads(response.text))
    def delete_web_link_trash(self, web_link_id: str):
        """
        Permanently deletes a web link that is in the trash.
        
        This action cannot be undone.

        :param web_link_id: The ID of the web link.
            Example: "12345"
        :type web_link_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', web_link_id, '/trash']), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content