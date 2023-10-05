from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import CollaborationAllowlistEntries

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import CollaborationAllowlistEntry

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class CreateCollaborationWhitelistEntryDirectionArg(str, Enum):
    INBOUND = 'inbound'
    OUTBOUND = 'outbound'
    BOTH = 'both'


class CollaborationAllowlistEntriesManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_collaboration_whitelist_entries(
        self,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> CollaborationAllowlistEntries:
        """
        Returns the list domains that have been deemed safe to create collaborations

        for within the current enterprise.

        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {'marker': to_string(marker), 'limit': to_string(limit)}
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/collaboration_whitelist_entries']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, CollaborationAllowlistEntries)

    def create_collaboration_whitelist_entry(
        self,
        domain: str,
        direction: CreateCollaborationWhitelistEntryDirectionArg,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> CollaborationAllowlistEntry:
        """
        Creates a new entry in the list of allowed domains to allow

        collaboration for.

        :param domain: The domain to add to the list of allowed domains.
        :type domain: str
        :param direction: The direction in which to allow collaborations.
        :type direction: CreateCollaborationWhitelistEntryDirectionArg
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = {'domain': domain, 'direction': direction}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/collaboration_whitelist_entries']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, CollaborationAllowlistEntry)

    def get_collaboration_whitelist_entry_by_id(
        self,
        collaboration_whitelist_entry_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> CollaborationAllowlistEntry:
        """
        Returns a domain that has been deemed safe to create collaborations

        for within the current enterprise.

        :param collaboration_whitelist_entry_id: The ID of the entry in the list.
            Example: "213123"
        :type collaboration_whitelist_entry_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://api.box.com/2.0/collaboration_whitelist_entries/',
                    to_string(collaboration_whitelist_entry_id),
                ]
            ),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, CollaborationAllowlistEntry)

    def delete_collaboration_whitelist_entry_by_id(
        self,
        collaboration_whitelist_entry_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Removes a domain from the list of domains that have been deemed safe to create

        collaborations for within the current enterprise.

        :param collaboration_whitelist_entry_id: The ID of the entry in the list.
            Example: "213123"
        :type collaboration_whitelist_entry_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://api.box.com/2.0/collaboration_whitelist_entries/',
                    to_string(collaboration_whitelist_entry_id),
                ]
            ),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None
