from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import CollaborationAllowlistEntries

from box_sdk.schemas import ClientError

from box_sdk.schemas import CollaborationAllowlistEntry

class GetCollaborationWhitelistEntriesOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, limit: Union[None, int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class PostCollaborationWhitelistEntriesRequestBodyArgDirectionField(str, Enum):
    INBOUND = 'inbound'
    OUTBOUND = 'outbound'
    BOTH = 'both'

class PostCollaborationWhitelistEntriesRequestBodyArg(BaseObject):
    def __init__(self, domain: str, direction: PostCollaborationWhitelistEntriesRequestBodyArgDirectionField, **kwargs):
        """
        :param domain: The domain to add to the list of allowed domains.
        :type domain: str
        :param direction: The direction in which to allow collaborations.
        :type direction: PostCollaborationWhitelistEntriesRequestBodyArgDirectionField
        """
        super().__init__(**kwargs)
        self.domain = domain
        self.direction = direction

class CollaborationAllowlistEntriesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getCollaborationWhitelistEntries(self, options: GetCollaborationWhitelistEntriesOptionsArg = None) -> CollaborationAllowlistEntries:
        """
        Returns the list domains that have been deemed safe to create collaborations
        
        for within the current enterprise.

        """
        if options is None:
            options = GetCollaborationWhitelistEntriesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_entries']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return CollaborationAllowlistEntries.from_dict(json.loads(response.text))
    def postCollaborationWhitelistEntries(self, requestBody: PostCollaborationWhitelistEntriesRequestBodyArg) -> CollaborationAllowlistEntry:
        """
        Creates a new entry in the list of allowed domains to allow
        
        collaboration for.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_entries']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return CollaborationAllowlistEntry.from_dict(json.loads(response.text))
    def getCollaborationWhitelistEntriesId(self, collaborationWhitelistEntryId: str) -> CollaborationAllowlistEntry:
        """
        Returns a domain that has been deemed safe to create collaborations
        
        for within the current enterprise.

        :param collaborationWhitelistEntryId: The ID of the entry in the list.
            Example: "213123"
        :type collaborationWhitelistEntryId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_entries/', collaborationWhitelistEntryId]), FetchOptions(method='GET', auth=self.auth))
        return CollaborationAllowlistEntry.from_dict(json.loads(response.text))
    def deleteCollaborationWhitelistEntriesId(self, collaborationWhitelistEntryId: str):
        """
        Removes a domain from the list of domains that have been deemed safe to create
        
        collaborations for within the current enterprise.

        :param collaborationWhitelistEntryId: The ID of the entry in the list.
            Example: "213123"
        :type collaborationWhitelistEntryId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_entries/', collaborationWhitelistEntryId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content