from typing import Optional

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import SignTemplates

from box_sdk.schemas import ClientError

from box_sdk.schemas import SignTemplate

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetSignTemplatesOptionsArg(BaseObject):
    def __init__(self, marker: Optional[str] = None, limit: Optional[int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class SignTemplatesManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_sign_templates(self, options: GetSignTemplatesOptionsArg = None) -> SignTemplates:
        """
        Gets Box Sign templates created by a user.
        """
        if options is None:
            options = GetSignTemplatesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_templates']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth, network_session=self.network_session))
        return SignTemplates.from_dict(json.loads(response.text))
    def get_sign_template_by_id(self, template_id: str) -> SignTemplate:
        """
        Fetches details of a specific Box Sign template.
        :param template_id: The ID of a Box Sign template.
            Example: "123075213-7d117509-8f05-42e4-a5ef-5190a319d41d"
        :type template_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_templates/', template_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return SignTemplate.from_dict(json.loads(response.text))