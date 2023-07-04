from typing import Optional

from typing import Dict

import json

from box_sdk.schemas import SignTemplates

from box_sdk.schemas import ClientError

from box_sdk.schemas import SignTemplate

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import to_map

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class SignTemplatesManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_sign_templates(self, marker: Optional[str] = None, limit: Optional[int] = None) -> SignTemplates:
        """
        Gets Box Sign templates created by a user.
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        query_params: Dict = {'marker': marker, 'limit': limit}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/sign_templates']), FetchOptions(method='GET', params=to_map(query_params), auth=self.auth, network_session=self.network_session))
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