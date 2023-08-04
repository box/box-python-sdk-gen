from box_sdk_gen.base_object import BaseObject

from typing import Optional

from typing import Dict

import json

from box_sdk_gen.base_object import BaseObject

from box_sdk_gen.schemas import CollaborationAllowlistExemptTargets

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import CollaborationAllowlistExemptTarget

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class CreateCollaborationWhitelistExemptTargetUserArg(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of the user to exempt.
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id


class CollaborationAllowlistExemptTargetsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session

    def get_collaboration_whitelist_exempt_targets(self, marker: Optional[str] = None, limit: Optional[int] = None) -> CollaborationAllowlistExemptTargets:
        """
        Returns a list of users who have been exempt from the collaboration

        domain restrictions.

        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        query_params_map: Dict[str, str] = prepare_params({'marker': to_string(marker), 'limit': to_string(limit)})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_exempt_targets']), FetchOptions(method='GET', params=query_params_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return CollaborationAllowlistExemptTargets.from_dict(json.loads(response.text))

    def create_collaboration_whitelist_exempt_target(self, user: CreateCollaborationWhitelistExemptTargetUserArg) -> CollaborationAllowlistExemptTarget:
        """
        Exempts a user from the restrictions set out by the allowed list of domains

        for collaborations.

        :param user: The user to exempt.
        :type user: CreateCollaborationWhitelistExemptTargetUserArg
        """
        request_body: BaseObject = BaseObject(user=user)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_exempt_targets']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', response_format='json', auth=self.auth, network_session=self.network_session))
        return CollaborationAllowlistExemptTarget.from_dict(json.loads(response.text))

    def get_collaboration_whitelist_exempt_target_by_id(self, collaboration_whitelist_exempt_target_id: str) -> CollaborationAllowlistExemptTarget:
        """
        Returns a users who has been exempt from the collaboration

        domain restrictions.

        :param collaboration_whitelist_exempt_target_id: The ID of the exemption to the list.
            Example: "984923"
        :type collaboration_whitelist_exempt_target_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_exempt_targets/', collaboration_whitelist_exempt_target_id]), FetchOptions(method='GET', response_format='json', auth=self.auth, network_session=self.network_session))
        return CollaborationAllowlistExemptTarget.from_dict(json.loads(response.text))

    def delete_collaboration_whitelist_exempt_target_by_id(self, collaboration_whitelist_exempt_target_id: str) -> None:
        """
        Removes a user's exemption from the restrictions set out by the allowed list

        of domains for collaborations.

        :param collaboration_whitelist_exempt_target_id: The ID of the exemption to the list.
            Example: "984923"
        :type collaboration_whitelist_exempt_target_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_exempt_targets/', collaboration_whitelist_exempt_target_id]), FetchOptions(method='DELETE', response_format=None, auth=self.auth, network_session=self.network_session))
        return None