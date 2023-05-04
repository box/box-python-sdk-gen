from typing import Optional

from box_sdk.base_object import BaseObject

from enum import Enum

from typing import Union

import json

from box_sdk.schemas import CollaborationAllowlistEntries

from box_sdk.schemas import ClientError

from box_sdk.schemas import CollaborationAllowlistEntry

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetCollaborationWhitelistEntriesOptionsArg(BaseObject):
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

class CreateCollaborationWhitelistEntryRequestBodyArgDirectionField(str, Enum):
    INBOUND = 'inbound'
    OUTBOUND = 'outbound'
    BOTH = 'both'

class CreateCollaborationWhitelistEntryRequestBodyArg(BaseObject):
    def __init__(self, domain: str, direction: CreateCollaborationWhitelistEntryRequestBodyArgDirectionField, **kwargs):
        """
        :param domain: The domain to add to the list of allowed domains.
        :type domain: str
        :param direction: The direction in which to allow collaborations.
        :type direction: CreateCollaborationWhitelistEntryRequestBodyArgDirectionField
        """
        super().__init__(**kwargs)
        self.domain = domain
        self.direction = direction

class CollaborationAllowlistEntriesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_collaboration_whitelist_entries(self, options: GetCollaborationWhitelistEntriesOptionsArg = None) -> CollaborationAllowlistEntries:
        """
        Returns the list domains that have been deemed safe to create collaborations
        
        for within the current enterprise.

        """
        if options is None:
            options = GetCollaborationWhitelistEntriesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_entries']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return CollaborationAllowlistEntries.from_dict(json.loads(response.text))
    def create_collaboration_whitelist_entry(self, request_body: CreateCollaborationWhitelistEntryRequestBodyArg) -> CollaborationAllowlistEntry:
        """
        Creates a new entry in the list of allowed domains to allow
        
        collaboration for.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_entries']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return CollaborationAllowlistEntry.from_dict(json.loads(response.text))
    def get_collaboration_whitelist_entry_by_id(self, collaboration_whitelist_entry_id: str) -> CollaborationAllowlistEntry:
        """
        Returns a domain that has been deemed safe to create collaborations
        
        for within the current enterprise.

        :param collaboration_whitelist_entry_id: The ID of the entry in the list.
            Example: "213123"
        :type collaboration_whitelist_entry_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_entries/', collaboration_whitelist_entry_id]), FetchOptions(method='GET', auth=self.auth))
        return CollaborationAllowlistEntry.from_dict(json.loads(response.text))
    def delete_collaboration_whitelist_entry_by_id(self, collaboration_whitelist_entry_id: str):
        """
        Removes a domain from the list of domains that have been deemed safe to create
        
        collaborations for within the current enterprise.

        :param collaboration_whitelist_entry_id: The ID of the entry in the list.
            Example: "213123"
        :type collaboration_whitelist_entry_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_entries/', collaboration_whitelist_entry_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content