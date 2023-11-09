from box_sdk_gen.base_object import BaseObject

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import CollaborationAllowlistExemptTargets

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import CollaborationAllowlistExemptTarget

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json import SerializedData


class CreateCollaborationWhitelistExemptTargetUserArg(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of the user to exempt.
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id


class CollaborationAllowlistExemptTargetsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_collaboration_whitelist_exempt_targets(
        self,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> CollaborationAllowlistExemptTargets:
        """
        Returns a list of users who have been exempt from the collaboration

        domain restrictions.

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
        query_params_map: Dict[str, str] = prepare_params({
            'marker': to_string(marker), 'limit': to_string(limit)
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/collaboration_whitelist_exempt_targets']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, CollaborationAllowlistExemptTargets)

    def create_collaboration_whitelist_exempt_target(
        self,
        user: CreateCollaborationWhitelistExemptTargetUserArg,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> CollaborationAllowlistExemptTarget:
        """
        Exempts a user from the restrictions set out by the allowed list of domains

        for collaborations.

        :param user: The user to exempt.
        :type user: CreateCollaborationWhitelistExemptTargetUserArg
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'user': user}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/collaboration_whitelist_exempt_targets']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, CollaborationAllowlistExemptTarget)

    def get_collaboration_whitelist_exempt_target_by_id(
        self,
        collaboration_whitelist_exempt_target_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> CollaborationAllowlistExemptTarget:
        """
        Returns a users who has been exempt from the collaboration

        domain restrictions.

        :param collaboration_whitelist_exempt_target_id: The ID of the exemption to the list.
            Example: "984923"
        :type collaboration_whitelist_exempt_target_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/collaboration_whitelist_exempt_targets/',
                to_string(collaboration_whitelist_exempt_target_id),
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, CollaborationAllowlistExemptTarget)

    def delete_collaboration_whitelist_exempt_target_by_id(
        self,
        collaboration_whitelist_exempt_target_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Removes a user's exemption from the restrictions set out by the allowed list

        of domains for collaborations.

        :param collaboration_whitelist_exempt_target_id: The ID of the exemption to the list.
            Example: "984923"
        :type collaboration_whitelist_exempt_target_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/collaboration_whitelist_exempt_targets/',
                to_string(collaboration_whitelist_exempt_target_id),
            ]),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None
