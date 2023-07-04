from typing import Optional

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import EmailAliases

from box_sdk.schemas import ClientError

from box_sdk.schemas import EmailAlias

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import to_map

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class EmailAliasesManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_user_email_aliases(self, user_id: str) -> EmailAliases:
        """
        Retrieves all email aliases for a user. The collection
        
        does not include the primary login for the user.

        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id, '/email_aliases']), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return EmailAliases.from_dict(json.loads(response.text))
    def create_user_email_alias(self, user_id: str, email: str) -> EmailAlias:
        """
        Adds a new email alias to a user account..
        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        :param email: The email address to add to the account as an alias.
            Note: The domain of the email alias needs to be registered
             to your enterprise.
            See the [domain verification guide](
              https://support.box.com/hc/en-us/articles/4408619650579-Domain-Verification
              ) for steps to add a new domain.
        :type email: str
        """
        request_body: BaseObject = BaseObject(email=email)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id, '/email_aliases']), FetchOptions(method='POST', body=json.dumps(to_map(request_body)), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return EmailAlias.from_dict(json.loads(response.text))
    def delete_user_email_alias_by_id(self, user_id: str, email_alias_id: str):
        """
        Removes an email alias from a user.
        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        :param email_alias_id: The ID of the email alias.
            Example: "23432"
        :type email_alias_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id, '/email_aliases/', email_alias_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content