from enum import Enum

from typing import Optional

from typing import Dict

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import CollaborationAllowlistEntries

from box_sdk.schemas import ClientError

from box_sdk.schemas import CollaborationAllowlistEntry

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import prepare_params

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateCollaborationWhitelistEntryDirectionArg(str, Enum):
    INBOUND = 'inbound'
    OUTBOUND = 'outbound'
    BOTH = 'both'

class CollaborationAllowlistEntriesManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_collaboration_whitelist_entries(self, marker: Optional[str] = None, limit: Optional[int] = None) -> CollaborationAllowlistEntries:
        """
        Returns the list domains that have been deemed safe to create collaborations
        
        for within the current enterprise.

        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        query_params: Dict = {'marker': marker, 'limit': limit}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_entries']), FetchOptions(method='GET', params=prepare_params(query_params), auth=self.auth, network_session=self.network_session))
        return CollaborationAllowlistEntries.from_dict(json.loads(response.text))
    def create_collaboration_whitelist_entry(self, domain: str, direction: CreateCollaborationWhitelistEntryDirectionArg) -> CollaborationAllowlistEntry:
        """
        Creates a new entry in the list of allowed domains to allow
        
        collaboration for.

        :param domain: The domain to add to the list of allowed domains.
        :type domain: str
        :param direction: The direction in which to allow collaborations.
        :type direction: CreateCollaborationWhitelistEntryDirectionArg
        """
        request_body: BaseObject = BaseObject(domain=domain, direction=direction)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_entries']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return CollaborationAllowlistEntry.from_dict(json.loads(response.text))
    def get_collaboration_whitelist_entry_by_id(self, collaboration_whitelist_entry_id: str) -> CollaborationAllowlistEntry:
        """
        Returns a domain that has been deemed safe to create collaborations
        
        for within the current enterprise.

        :param collaboration_whitelist_entry_id: The ID of the entry in the list.
            Example: "213123"
        :type collaboration_whitelist_entry_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_entries/', collaboration_whitelist_entry_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return CollaborationAllowlistEntry.from_dict(json.loads(response.text))
    def delete_collaboration_whitelist_entry_by_id(self, collaboration_whitelist_entry_id: str):
        """
        Removes a domain from the list of domains that have been deemed safe to create
        
        collaborations for within the current enterprise.

        :param collaboration_whitelist_entry_id: The ID of the entry in the list.
            Example: "213123"
        :type collaboration_whitelist_entry_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_entries/', collaboration_whitelist_entry_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content