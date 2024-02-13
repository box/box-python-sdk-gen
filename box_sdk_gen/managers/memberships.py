from box_sdk_gen.base_object import BaseObject

from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from typing import List

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import GroupMemberships

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import GroupMembership

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json_data import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json_data import SerializedData


class CreateGroupMembershipUser(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of the user to add to the group
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id


class CreateGroupMembershipGroup(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of the group to add the user to
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id


class CreateGroupMembershipRole(str, Enum):
    MEMBER = 'member'
    ADMIN = 'admin'


class UpdateGroupMembershipByIdRole(str, Enum):
    MEMBER = 'member'
    ADMIN = 'admin'


class MembershipsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: NetworkSession = None,
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session

    def get_user_memberships(
        self,
        user_id: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> GroupMemberships:
        """
        Retrieves all the groups for a user. Only members of this

        group or users with admin-level permissions will be able to


        use this API.

        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {'limit': to_string(limit), 'offset': to_string(offset)}
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/users/',
                    to_string(user_id),
                    '/memberships',
                ]
            ),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, GroupMemberships)

    def get_group_memberships(
        self,
        group_id: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> GroupMemberships:
        """
        Retrieves all the members for a group. Only members of this

        group or users with admin-level permissions will be able to


        use this API.

        :param group_id: The ID of the group.
            Example: "57645"
        :type group_id: str
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {'limit': to_string(limit), 'offset': to_string(offset)}
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/groups/',
                    to_string(group_id),
                    '/memberships',
                ]
            ),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, GroupMemberships)

    def create_group_membership(
        self,
        user: CreateGroupMembershipUser,
        group: CreateGroupMembershipGroup,
        role: Optional[CreateGroupMembershipRole] = None,
        configurable_permissions: Optional[Dict[str, bool]] = None,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> GroupMembership:
        """
        Creates a group membership. Only users with

        admin-level permissions will be able to use this API.

        :param user: The user to add to the group.
        :type user: CreateGroupMembershipUser
        :param group: The group to add the user to.
        :type group: CreateGroupMembershipGroup
        :param role: The role of the user in the group.
        :type role: Optional[CreateGroupMembershipRole], optional
        :param configurable_permissions: Custom configuration for the permissions an admin
            if a group will receive. This option has no effect
            on members with a role of `member`.
            Setting these permissions overwrites the default
            access levels of an admin.
            Specifying a value of "null" for this object will disable
            all configurable permissions. Specifying permissions will set
            them accordingly, omitted permissions will be enabled by default.
        :type configurable_permissions: Optional[Dict[str, bool]], optional
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
        request_body: Dict = {
            'user': user,
            'group': group,
            'role': role,
            'configurable_permissions': configurable_permissions,
        }
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([self.network_session.base_urls.base_url, '/group_memberships']),
            FetchOptions(
                method='POST',
                params=query_params_map,
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, GroupMembership)

    def get_group_membership_by_id(
        self,
        group_membership_id: str,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> GroupMembership:
        """
        Retrieves a specific group membership. Only admins of this

        group or users with admin-level permissions will be able to


        use this API.

        :param group_membership_id: The ID of the group membership.
            Example: "434534"
        :type group_membership_id: str
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
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/group_memberships/',
                    to_string(group_membership_id),
                ]
            ),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, GroupMembership)

    def update_group_membership_by_id(
        self,
        group_membership_id: str,
        role: Optional[UpdateGroupMembershipByIdRole] = None,
        configurable_permissions: Optional[Dict[str, bool]] = None,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> GroupMembership:
        """
        Updates a user's group membership. Only admins of this

        group or users with admin-level permissions will be able to


        use this API.

        :param group_membership_id: The ID of the group membership.
            Example: "434534"
        :type group_membership_id: str
        :param role: The role of the user in the group.
        :type role: Optional[UpdateGroupMembershipByIdRole], optional
        :param configurable_permissions: Custom configuration for the permissions an admin
            if a group will receive. This option has no effect
            on members with a role of `member`.
            Setting these permissions overwrites the default
            access levels of an admin.
            Specifying a value of "null" for this object will disable
            all configurable permissions. Specifying permissions will set
            them accordingly, omitted permissions will be enabled by default.
        :type configurable_permissions: Optional[Dict[str, bool]], optional
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
        request_body: Dict = {
            'role': role,
            'configurable_permissions': configurable_permissions,
        }
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/group_memberships/',
                    to_string(group_membership_id),
                ]
            ),
            FetchOptions(
                method='PUT',
                params=query_params_map,
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, GroupMembership)

    def delete_group_membership_by_id(
        self,
        group_membership_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Deletes a specific group membership. Only admins of this

        group or users with admin-level permissions will be able to


        use this API.

        :param group_membership_id: The ID of the group membership.
            Example: "434534"
        :type group_membership_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/group_memberships/',
                    to_string(group_membership_id),
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
