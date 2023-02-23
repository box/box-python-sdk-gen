from base_object import BaseObject

from typing import Union

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import EmailAliases

from schemas import ClientError

from schemas import EmailAlias

class PostUsersIdEmailAliasesRequestBodyArg(BaseObject):
    def __init__(self, email: str, **kwargs):
        """
        :param email: The email address to add to the account as an alias.
            Note: The domain of the email alias needs to be registered
             to your enterprise.
            See the [domain verification guide](
              https://support.box.com/hc/en-us/articles/4408619650579-Domain-Verification
              ) for steps to add a new domain.
        :type email: str
        """
        super().__init__(**kwargs)
        self.email = email

class EmailAliasesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getUsersIdEmailAliases(self, userId: str) -> EmailAliases:
        """
        Retrieves all email aliases for a user. The collection
        
        does not include the primary login for the user.

        :param userId: The ID of the user.
            Example: "12345"
        :type userId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', userId, '/email_aliases']), FetchOptions(method='GET', auth=self.auth))
        return EmailAliases.from_dict(json.loads(response.text))
    def postUsersIdEmailAliases(self, userId: str, requestBody: PostUsersIdEmailAliasesRequestBodyArg) -> EmailAlias:
        """
        Adds a new email alias to a user account..
        :param userId: The ID of the user.
            Example: "12345"
        :type userId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', userId, '/email_aliases']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return EmailAlias.from_dict(json.loads(response.text))
    def deleteUsersIdEmailAliasesId(self, userId: str, emailAliasId: str):
        """
        Removes an email alias from a user.
        :param userId: The ID of the user.
            Example: "12345"
        :type userId: str
        :param emailAliasId: The ID of the email alias.
            Example: "23432"
        :type emailAliasId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', userId, '/email_aliases/', emailAliasId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content