from box_sdk_gen.base_object import BaseObject

from typing import Optional

from typing import List

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import serialize

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.schemas import Invite

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class CreateInviteEnterpriseArg(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of the enterprise
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id


class CreateInviteActionableByArg(BaseObject):
    def __init__(self, login: Optional[str] = None, **kwargs):
        """
        :param login: The login of the invited user
        :type login: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.login = login


class InvitesManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def create_invite(
        self,
        enterprise: CreateInviteEnterpriseArg,
        actionable_by: CreateInviteActionableByArg,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Invite:
        """
        Invites an existing external user to join an enterprise.

        The existing user can not be part of another enterprise and


        must already have a Box account. Once invited, the user will receive an


        email and are prompted to accept the invitation within the


        Box web application.


        This method requires the "Manage An Enterprise" scope enabled for


        the application, which can be enabled within the developer console.

        :param enterprise: The enterprise to invite the user to
        :type enterprise: CreateInviteEnterpriseArg
        :param actionable_by: The user to invite
        :type actionable_by: CreateInviteActionableByArg
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[List[str]], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = {'enterprise': enterprise, 'actionable_by': actionable_by}
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/invites']),
            FetchOptions(
                method='POST',
                params=query_params_map,
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, Invite)

    def get_invite_by_id(
        self,
        invite_id: str,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Invite:
        """
        Returns the status of a user invite.
        :param invite_id: The ID of an invite.
            Example: "213723"
        :type invite_id: str
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[List[str]], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/invites/', to_string(invite_id)]),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, Invite)
