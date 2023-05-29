from enum import Enum

from typing import Optional

from box_sdk.base_object import BaseObject

from typing import List

import json

from typing import Dict

from box_sdk.schemas import Users

from box_sdk.schemas import ClientError

from box_sdk.schemas import User

from box_sdk.schemas import TrackingCode

from box_sdk.schemas import UserFull

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetUsersOptionsArgUserTypeField(str, Enum):
    ALL = 'all'
    MANAGED = 'managed'
    EXTERNAL = 'external'

class GetUsersOptionsArg(BaseObject):
    def __init__(self, filter_term: Optional[str] = None, user_type: Optional[GetUsersOptionsArgUserTypeField] = None, external_app_user_id: Optional[str] = None, fields: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, usemarker: Optional[bool] = None, marker: Optional[str] = None, **kwargs):
        """
        :param filter_term: Limits the results to only users who's `name` or
            `login` start with the search term.
            For externally managed users, the search term needs
            to completely match the in order to find the user, and
            it will only return one user at a time.
        :type filter_term: Optional[str], optional
        :param user_type: Limits the results to the kind of user specified.
            * `all` returns every kind of user for whom the
              `login` or `name` partially matches the
              `filter_term`. It will only return an external user
              if the login matches the `filter_term` completely,
              and in that case it will only return that user.
            * `managed` returns all managed and app users for whom
              the `login` or `name` partially matches the
              `filter_term`.
            * `external` returns all external users for whom the
              `login` matches the `filter_term` exactly.
        :type user_type: Optional[GetUsersOptionsArgUserTypeField], optional
        :param external_app_user_id: Limits the results to app users with the given
            `external_app_user_id` value.
            When creating an app user, an
            `external_app_user_id` value can be set. This value can
            then be used in this endpoint to find any users that
            match that `external_app_user_id` value.
        :type external_app_user_id: Optional[str], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param usemarker: Specifies whether to use marker-based pagination instead of
            offset-based pagination. Only one pagination method can
            be used at a time.
            By setting this value to true, the API will return a `marker` field
            that can be passed as a parameter to this endpoint to get the next
            page of the response.
        :type usemarker: Optional[bool], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.filter_term = filter_term
        self.user_type = user_type
        self.external_app_user_id = external_app_user_id
        self.fields = fields
        self.offset = offset
        self.limit = limit
        self.usemarker = usemarker
        self.marker = marker

class CreateUserRequestBodyArgRoleField(str, Enum):
    COADMIN = 'coadmin'
    USER = 'user'

class CreateUserRequestBodyArgStatusField(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    CANNOT_DELETE_EDIT = 'cannot_delete_edit'
    CANNOT_DELETE_EDIT_UPLOAD = 'cannot_delete_edit_upload'

class CreateUserRequestBodyArg(BaseObject):
    def __init__(self, name: str, login: Optional[str] = None, is_platform_access_only: Optional[bool] = None, role: Optional[CreateUserRequestBodyArgRoleField] = None, language: Optional[str] = None, is_sync_enabled: Optional[bool] = None, job_title: Optional[str] = None, phone: Optional[str] = None, address: Optional[str] = None, space_amount: Optional[int] = None, tracking_codes: Optional[List[TrackingCode]] = None, can_see_managed_users: Optional[bool] = None, timezone: Optional[str] = None, is_external_collab_restricted: Optional[bool] = None, is_exempt_from_device_limits: Optional[bool] = None, is_exempt_from_login_verification: Optional[bool] = None, status: Optional[CreateUserRequestBodyArgStatusField] = None, external_app_user_id: Optional[str] = None, **kwargs):
        """
        :param name: The name of the user
        :type name: str
        :param login: The email address the user uses to log in
            Required, unless `is_platform_access_only`
            is set to `true`.
        :type login: Optional[str], optional
        :param is_platform_access_only: Specifies that the user is an app user.
        :type is_platform_access_only: Optional[bool], optional
        :param role: The user’s enterprise role
        :type role: Optional[CreateUserRequestBodyArgRoleField], optional
        :param language: The language of the user, formatted in modified version of the
            [ISO 639-1](/guides/api-calls/language-codes) format.
        :type language: Optional[str], optional
        :param is_sync_enabled: Whether the user can use Box Sync
        :type is_sync_enabled: Optional[bool], optional
        :param job_title: The user’s job title
        :type job_title: Optional[str], optional
        :param phone: The user’s phone number
        :type phone: Optional[str], optional
        :param address: The user’s address
        :type address: Optional[str], optional
        :param space_amount: The user’s total available space in bytes. Set this to `-1` to
            indicate unlimited storage.
        :type space_amount: Optional[int], optional
        :param tracking_codes: Tracking codes allow an admin to generate reports from the
            admin console and assign an attribute to a specific group
            of users. This setting must be enabled for an enterprise before it
            can be used.
        :type tracking_codes: Optional[List[TrackingCode]], optional
        :param can_see_managed_users: Whether the user can see other enterprise users in their
            contact list
        :type can_see_managed_users: Optional[bool], optional
        :param timezone: The user's timezone
        :type timezone: Optional[str], optional
        :param is_external_collab_restricted: Whether the user is allowed to collaborate with users outside
            their enterprise
        :type is_external_collab_restricted: Optional[bool], optional
        :param is_exempt_from_device_limits: Whether to exempt the user from enterprise device limits
        :type is_exempt_from_device_limits: Optional[bool], optional
        :param is_exempt_from_login_verification: Whether the user must use two-factor authentication
        :type is_exempt_from_login_verification: Optional[bool], optional
        :param status: The user's account status
        :type status: Optional[CreateUserRequestBodyArgStatusField], optional
        :param external_app_user_id: An external identifier for an app user, which can be used to look
            up the user. This can be used to tie user IDs from external
            identity providers to Box users.
        :type external_app_user_id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.login = login
        self.is_platform_access_only = is_platform_access_only
        self.role = role
        self.language = language
        self.is_sync_enabled = is_sync_enabled
        self.job_title = job_title
        self.phone = phone
        self.address = address
        self.space_amount = space_amount
        self.tracking_codes = tracking_codes
        self.can_see_managed_users = can_see_managed_users
        self.timezone = timezone
        self.is_external_collab_restricted = is_external_collab_restricted
        self.is_exempt_from_device_limits = is_exempt_from_device_limits
        self.is_exempt_from_login_verification = is_exempt_from_login_verification
        self.status = status
        self.external_app_user_id = external_app_user_id

class CreateUserOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class GetUserMeOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class GetUserByIdOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class UpdateUserByIdRequestBodyArgRoleField(str, Enum):
    COADMIN = 'coadmin'
    USER = 'user'

class UpdateUserByIdRequestBodyArgStatusField(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    CANNOT_DELETE_EDIT = 'cannot_delete_edit'
    CANNOT_DELETE_EDIT_UPLOAD = 'cannot_delete_edit_upload'

class UpdateUserByIdRequestBodyArgNotificationEmailField(BaseObject):
    def __init__(self, email: Optional[str] = None, **kwargs):
        """
        :param email: The email address to send the notifications to.
        :type email: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.email = email

class UpdateUserByIdRequestBodyArg(BaseObject):
    def __init__(self, enterprise: Optional[str] = None, notify: Optional[bool] = None, name: Optional[str] = None, login: Optional[str] = None, role: Optional[UpdateUserByIdRequestBodyArgRoleField] = None, language: Optional[str] = None, is_sync_enabled: Optional[bool] = None, job_title: Optional[str] = None, phone: Optional[str] = None, address: Optional[str] = None, tracking_codes: Optional[List[TrackingCode]] = None, can_see_managed_users: Optional[bool] = None, timezone: Optional[str] = None, is_external_collab_restricted: Optional[bool] = None, is_exempt_from_device_limits: Optional[bool] = None, is_exempt_from_login_verification: Optional[bool] = None, is_password_reset_required: Optional[bool] = None, status: Optional[UpdateUserByIdRequestBodyArgStatusField] = None, space_amount: Optional[int] = None, notification_email: Optional[UpdateUserByIdRequestBodyArgNotificationEmailField] = None, external_app_user_id: Optional[str] = None, **kwargs):
        """
        :param enterprise: Set this to `null` to roll the user out of the enterprise
            and make them a free user
        :type enterprise: Optional[str], optional
        :param notify: Whether the user should receive an email when they
            are rolled out of an enterprise
        :type notify: Optional[bool], optional
        :param name: The name of the user
        :type name: Optional[str], optional
        :param login: The email address the user uses to log in
            Note: If the target user's email is not confirmed, then the
            primary login address cannot be changed.
        :type login: Optional[str], optional
        :param role: The user’s enterprise role
        :type role: Optional[UpdateUserByIdRequestBodyArgRoleField], optional
        :param language: The language of the user, formatted in modified version of the
            [ISO 639-1](/guides/api-calls/language-codes) format.
        :type language: Optional[str], optional
        :param is_sync_enabled: Whether the user can use Box Sync
        :type is_sync_enabled: Optional[bool], optional
        :param job_title: The user’s job title
        :type job_title: Optional[str], optional
        :param phone: The user’s phone number
        :type phone: Optional[str], optional
        :param address: The user’s address
        :type address: Optional[str], optional
        :param tracking_codes: Tracking codes allow an admin to generate reports from the
            admin console and assign an attribute to a specific group
            of users. This setting must be enabled for an enterprise before it
            can be used.
        :type tracking_codes: Optional[List[TrackingCode]], optional
        :param can_see_managed_users: Whether the user can see other enterprise users in their
            contact list
        :type can_see_managed_users: Optional[bool], optional
        :param timezone: The user's timezone
        :type timezone: Optional[str], optional
        :param is_external_collab_restricted: Whether the user is allowed to collaborate with users outside
            their enterprise
        :type is_external_collab_restricted: Optional[bool], optional
        :param is_exempt_from_device_limits: Whether to exempt the user from enterprise device limits
        :type is_exempt_from_device_limits: Optional[bool], optional
        :param is_exempt_from_login_verification: Whether the user must use two-factor authentication
        :type is_exempt_from_login_verification: Optional[bool], optional
        :param is_password_reset_required: Whether the user is required to reset their password
        :type is_password_reset_required: Optional[bool], optional
        :param status: The user's account status
        :type status: Optional[UpdateUserByIdRequestBodyArgStatusField], optional
        :param space_amount: The user’s total available space in bytes. Set this to `-1` to
            indicate unlimited storage.
        :type space_amount: Optional[int], optional
        :param notification_email: An alternate notification email address to which email
            notifications are sent. When it's confirmed, this will be
            the email address to which notifications are sent instead of
            to the primary email address.
            Set this value to `null` to remove the notification email.
        :type notification_email: Optional[UpdateUserByIdRequestBodyArgNotificationEmailField], optional
        :param external_app_user_id: An external identifier for an app user, which can be used to look
            up the user. This can be used to tie user IDs from external
            identity providers to Box users.
            Note: In order to update this field, you need to request a token
            using the application that created the app user.
        :type external_app_user_id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.enterprise = enterprise
        self.notify = notify
        self.name = name
        self.login = login
        self.role = role
        self.language = language
        self.is_sync_enabled = is_sync_enabled
        self.job_title = job_title
        self.phone = phone
        self.address = address
        self.tracking_codes = tracking_codes
        self.can_see_managed_users = can_see_managed_users
        self.timezone = timezone
        self.is_external_collab_restricted = is_external_collab_restricted
        self.is_exempt_from_device_limits = is_exempt_from_device_limits
        self.is_exempt_from_login_verification = is_exempt_from_login_verification
        self.is_password_reset_required = is_password_reset_required
        self.status = status
        self.space_amount = space_amount
        self.notification_email = notification_email
        self.external_app_user_id = external_app_user_id

class UpdateUserByIdOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class DeleteUserByIdOptionsArg(BaseObject):
    def __init__(self, notify: Optional[bool] = None, force: Optional[bool] = None, **kwargs):
        """
        :param notify: Whether the user will receive email notification of
            the deletion
        :type notify: Optional[bool], optional
        :param force: Whether the user should be deleted even if this user
            still own files
        :type force: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.notify = notify
        self.force = force

class UsersManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def get_users(self, options: GetUsersOptionsArg = None) -> Users:
        """
        Returns a list of all users for the Enterprise along with their `user_id`,
        
        `public_name`, and `login`.

        
        The application and the authenticated user need to

        
        have the permission to look up users in the entire

        
        enterprise.

        """
        if options is None:
            options = GetUsersOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users']), FetchOptions(method='GET', params={'filter_term': options.filter_term, 'user_type': options.user_type, 'external_app_user_id': options.external_app_user_id, 'fields': options.fields, 'offset': options.offset, 'limit': options.limit, 'usemarker': options.usemarker, 'marker': options.marker}, auth=self.auth, network_session=self.network_session))
        return Users.from_dict(json.loads(response.text))
    def create_user(self, request_body: CreateUserRequestBodyArg, options: CreateUserOptionsArg = None) -> User:
        """
        Creates a new managed user in an enterprise. This endpoint
        
        is only available to users and applications with the right

        
        admin permissions.

        """
        if options is None:
            options = CreateUserOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return User.from_dict(json.loads(response.text))
    def get_user_me(self, options: GetUserMeOptionsArg = None) -> UserFull:
        """
        Retrieves information about the user who is currently authenticated.
        
        In the case of a client-side authenticated OAuth 2.0 application

        
        this will be the user who authorized the app.

        
        In the case of a JWT, server-side authenticated application

        
        this will be the service account that belongs to the application

        
        by default.

        
        Use the `As-User` header to change who this API call is made on behalf of.

        """
        if options is None:
            options = GetUserMeOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/me']), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth, network_session=self.network_session))
        return UserFull.from_dict(json.loads(response.text))
    def get_user_by_id(self, user_id: str, options: GetUserByIdOptionsArg = None) -> UserFull:
        """
        Retrieves information about a user in the enterprise.
        
        The application and the authenticated user need to

        
        have the permission to look up users in the entire

        
        enterprise.

        
        This endpoint also returns a limited set of information

        
        for external users who are collaborated on content

        
        owned by the enterprise for authenticated users with the

        
        right scopes. In this case, disallowed fields will return

        
        null instead.

        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        """
        if options is None:
            options = GetUserByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth, network_session=self.network_session))
        return UserFull.from_dict(json.loads(response.text))
    def update_user_by_id(self, user_id: str, request_body: UpdateUserByIdRequestBodyArg, options: UpdateUserByIdOptionsArg = None) -> UserFull:
        """
        Updates a managed or app user in an enterprise. This endpoint
        
        is only available to users and applications with the right

        
        admin permissions.

        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        """
        if options is None:
            options = UpdateUserByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id]), FetchOptions(method='PUT', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return UserFull.from_dict(json.loads(response.text))
    def delete_user_by_id(self, user_id: str, options: DeleteUserByIdOptionsArg = None):
        """
        Deletes a user. By default this will fail if the user
        
        still owns any content. Move their owned content first

        
        before proceeding, or use the `force` field to delete

        
        the user and their files.

        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        """
        if options is None:
            options = DeleteUserByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id]), FetchOptions(method='DELETE', params={'notify': options.notify, 'force': options.force}, auth=self.auth, network_session=self.network_session))
        return response.content