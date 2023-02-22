from enum import Enum

from typing import Union

from base_object import BaseObject

from typing import List

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import Users

from schemas import ClientError

from schemas import User

from schemas import TrackingCode

class GetUsersOptionsArgUserTypeField(str, Enum):
    ALL = 'all'
    MANAGED = 'managed'
    EXTERNAL = 'external'

class GetUsersOptionsArg(BaseObject):
    def __init__(self, filterTerm: Union[None, str] = None, userType: Union[None, GetUsersOptionsArgUserTypeField] = None, externalAppUserId: Union[None, str] = None, fields: Union[None, str] = None, offset: Union[None, int] = None, limit: Union[None, int] = None, usemarker: Union[None, bool] = None, marker: Union[None, str] = None, **kwargs):
        """
        :param filterTerm: Limits the results to only users who's `name` or
            `login` start with the search term.
            For externally managed users, the search term needs
            to completely match the in order to find the user, and
            it will only return one user at a time.
        :type filterTerm: Union[None, str], optional
        :param userType: Limits the results to the kind of user specified.
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
        :type userType: Union[None, GetUsersOptionsArgUserTypeField], optional
        :param externalAppUserId: Limits the results to app users with the given
            `external_app_user_id` value.
            When creating an app user, an
            `external_app_user_id` value can be set. This value can
            then be used in this endpoint to find any users that
            match that `external_app_user_id` value.
        :type externalAppUserId: Union[None, str], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Union[None, int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param usemarker: Specifies whether to use marker-based pagination instead of
            offset-based pagination. Only one pagination method can
            be used at a time.
            By setting this value to true, the API will return a `marker` field
            that can be passed as a parameter to this endpoint to get the next
            page of the response.
        :type usemarker: Union[None, bool], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.filterTerm = filterTerm
        self.userType = userType
        self.externalAppUserId = externalAppUserId
        self.fields = fields
        self.offset = offset
        self.limit = limit
        self.usemarker = usemarker
        self.marker = marker

class PostUsersRequestBodyArgRoleField(str, Enum):
    COADMIN = 'coadmin'
    USER = 'user'

class PostUsersRequestBodyArgStatusField(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    CANNOT_DELETE_EDIT = 'cannot_delete_edit'
    CANNOT_DELETE_EDIT_UPLOAD = 'cannot_delete_edit_upload'

class PostUsersRequestBodyArg(BaseObject):
    def __init__(self, name: str, login: Union[None, str] = None, is_platform_access_only: Union[None, bool] = None, role: Union[None, PostUsersRequestBodyArgRoleField] = None, language: Union[None, str] = None, is_sync_enabled: Union[None, bool] = None, job_title: Union[None, str] = None, phone: Union[None, str] = None, address: Union[None, str] = None, space_amount: Union[None, int] = None, tracking_codes: Union[None, List[TrackingCode]] = None, can_see_managed_users: Union[None, bool] = None, timezone: Union[None, str] = None, is_external_collab_restricted: Union[None, bool] = None, is_exempt_from_device_limits: Union[None, bool] = None, is_exempt_from_login_verification: Union[None, bool] = None, status: Union[None, PostUsersRequestBodyArgStatusField] = None, external_app_user_id: Union[None, str] = None, **kwargs):
        """
        :param name: The name of the user
        :type name: str
        :param login: The email address the user uses to log in
            Required, unless `is_platform_access_only`
            is set to `true`.
        :type login: Union[None, str], optional
        :param is_platform_access_only: Specifies that the user is an app user.
        :type is_platform_access_only: Union[None, bool], optional
        :param role: The user’s enterprise role
        :type role: Union[None, PostUsersRequestBodyArgRoleField], optional
        :param language: The language of the user, formatted in modified version of the
            [ISO 639-1](/guides/api-calls/language-codes) format.
        :type language: Union[None, str], optional
        :param is_sync_enabled: Whether the user can use Box Sync
        :type is_sync_enabled: Union[None, bool], optional
        :param job_title: The user’s job title
        :type job_title: Union[None, str], optional
        :param phone: The user’s phone number
        :type phone: Union[None, str], optional
        :param address: The user’s address
        :type address: Union[None, str], optional
        :param space_amount: The user’s total available space in bytes. Set this to `-1` to
            indicate unlimited storage.
        :type space_amount: Union[None, int], optional
        :param tracking_codes: Tracking codes allow an admin to generate reports from the
            admin console and assign an attribute to a specific group
            of users. This setting must be enabled for an enterprise before it
            can be used.
        :type tracking_codes: Union[None, List[TrackingCode]], optional
        :param can_see_managed_users: Whether the user can see other enterprise users in their
            contact list
        :type can_see_managed_users: Union[None, bool], optional
        :param timezone: The user's timezone
        :type timezone: Union[None, str], optional
        :param is_external_collab_restricted: Whether the user is allowed to collaborate with users outside
            their enterprise
        :type is_external_collab_restricted: Union[None, bool], optional
        :param is_exempt_from_device_limits: Whether to exempt the user from enterprise device limits
        :type is_exempt_from_device_limits: Union[None, bool], optional
        :param is_exempt_from_login_verification: Whether the user must use two-factor authentication
        :type is_exempt_from_login_verification: Union[None, bool], optional
        :param status: The user's account status
        :type status: Union[None, PostUsersRequestBodyArgStatusField], optional
        :param external_app_user_id: An external identifier for an app user, which can be used to look
            up the user. This can be used to tie user IDs from external
            identity providers to Box users.
        :type external_app_user_id: Union[None, str], optional
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

class PostUsersOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class GetUsersMeOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class GetUsersIdOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class PutUsersIdRequestBodyArgRoleField(str, Enum):
    COADMIN = 'coadmin'
    USER = 'user'

class PutUsersIdRequestBodyArgStatusField(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    CANNOT_DELETE_EDIT = 'cannot_delete_edit'
    CANNOT_DELETE_EDIT_UPLOAD = 'cannot_delete_edit_upload'

class PutUsersIdRequestBodyArgNotificationEmailField(BaseObject):
    def __init__(self, email: Union[None, str] = None, **kwargs):
        """
        :param email: The email address to send the notifications to.
        :type email: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.email = email

class PutUsersIdRequestBodyArg(BaseObject):
    def __init__(self, enterprise: Union[None, str] = None, notify: Union[None, bool] = None, name: Union[None, str] = None, login: Union[None, str] = None, role: Union[None, PutUsersIdRequestBodyArgRoleField] = None, language: Union[None, str] = None, is_sync_enabled: Union[None, bool] = None, job_title: Union[None, str] = None, phone: Union[None, str] = None, address: Union[None, str] = None, tracking_codes: Union[None, List[TrackingCode]] = None, can_see_managed_users: Union[None, bool] = None, timezone: Union[None, str] = None, is_external_collab_restricted: Union[None, bool] = None, is_exempt_from_device_limits: Union[None, bool] = None, is_exempt_from_login_verification: Union[None, bool] = None, is_password_reset_required: Union[None, bool] = None, status: Union[None, PutUsersIdRequestBodyArgStatusField] = None, space_amount: Union[None, int] = None, notification_email: Union[None, PutUsersIdRequestBodyArgNotificationEmailField] = None, external_app_user_id: Union[None, str] = None, **kwargs):
        """
        :param enterprise: Set this to `null` to roll the user out of the enterprise
            and make them a free user
        :type enterprise: Union[None, str], optional
        :param notify: Whether the user should receive an email when they
            are rolled out of an enterprise
        :type notify: Union[None, bool], optional
        :param name: The name of the user
        :type name: Union[None, str], optional
        :param login: The email address the user uses to log in
            Note: If the target user's email is not confirmed, then the
            primary login address cannot be changed.
        :type login: Union[None, str], optional
        :param role: The user’s enterprise role
        :type role: Union[None, PutUsersIdRequestBodyArgRoleField], optional
        :param language: The language of the user, formatted in modified version of the
            [ISO 639-1](/guides/api-calls/language-codes) format.
        :type language: Union[None, str], optional
        :param is_sync_enabled: Whether the user can use Box Sync
        :type is_sync_enabled: Union[None, bool], optional
        :param job_title: The user’s job title
        :type job_title: Union[None, str], optional
        :param phone: The user’s phone number
        :type phone: Union[None, str], optional
        :param address: The user’s address
        :type address: Union[None, str], optional
        :param tracking_codes: Tracking codes allow an admin to generate reports from the
            admin console and assign an attribute to a specific group
            of users. This setting must be enabled for an enterprise before it
            can be used.
        :type tracking_codes: Union[None, List[TrackingCode]], optional
        :param can_see_managed_users: Whether the user can see other enterprise users in their
            contact list
        :type can_see_managed_users: Union[None, bool], optional
        :param timezone: The user's timezone
        :type timezone: Union[None, str], optional
        :param is_external_collab_restricted: Whether the user is allowed to collaborate with users outside
            their enterprise
        :type is_external_collab_restricted: Union[None, bool], optional
        :param is_exempt_from_device_limits: Whether to exempt the user from enterprise device limits
        :type is_exempt_from_device_limits: Union[None, bool], optional
        :param is_exempt_from_login_verification: Whether the user must use two-factor authentication
        :type is_exempt_from_login_verification: Union[None, bool], optional
        :param is_password_reset_required: Whether the user is required to reset their password
        :type is_password_reset_required: Union[None, bool], optional
        :param status: The user's account status
        :type status: Union[None, PutUsersIdRequestBodyArgStatusField], optional
        :param space_amount: The user’s total available space in bytes. Set this to `-1` to
            indicate unlimited storage.
        :type space_amount: Union[None, int], optional
        :param notification_email: An alternate notification email address to which email
            notifications are sent. When it's confirmed, this will be
            the email address to which notifications are sent instead of
            to the primary email address.
            Set this value to `null` to remove the notification email.
        :type notification_email: Union[None, PutUsersIdRequestBodyArgNotificationEmailField], optional
        :param external_app_user_id: An external identifier for an app user, which can be used to look
            up the user. This can be used to tie user IDs from external
            identity providers to Box users.
            Note: In order to update this field, you need to request a token
            using the application that created the app user.
        :type external_app_user_id: Union[None, str], optional
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

class PutUsersIdOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class DeleteUsersIdOptionsArg(BaseObject):
    def __init__(self, notify: Union[None, bool] = None, force: Union[None, bool] = None, **kwargs):
        """
        :param notify: Whether the user will receive email notification of
            the deletion
        :type notify: Union[None, bool], optional
        :param force: Whether the user should be deleted even if this user
            still own files
        :type force: Union[None, bool], optional
        """
        super().__init__(**kwargs)
        self.notify = notify
        self.force = force

class UsersManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getUsers(self, options: GetUsersOptionsArg = None) -> Users:
        """
        Returns a list of all users for the Enterprise along with their `user_id`,
        
        `public_name`, and `login`.

        
        The application and the authenticated user need to

        
        have the permission to look up users in the entire

        
        enterprise.

        """
        if options is None:
            options = GetUsersOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users']), FetchOptions(method='GET', params={'filter_term': options.filterTerm, 'user_type': options.userType, 'external_app_user_id': options.externalAppUserId, 'fields': options.fields, 'offset': options.offset, 'limit': options.limit, 'usemarker': options.usemarker, 'marker': options.marker}, auth=self.auth))
        return Users.from_dict(json.loads(response.text))
    def postUsers(self, requestBody: PostUsersRequestBodyArg, options: PostUsersOptionsArg = None) -> User:
        """
        Creates a new managed user in an enterprise. This endpoint
        
        is only available to users and applications with the right

        
        admin permissions.

        """
        if options is None:
            options = PostUsersOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return User.from_dict(json.loads(response.text))
    def getUsersMe(self, options: GetUsersMeOptionsArg = None) -> User:
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
            options = GetUsersMeOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/me']), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return User.from_dict(json.loads(response.text))
    def getUsersId(self, userId: str, options: GetUsersIdOptionsArg = None) -> User:
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

        :param userId: The ID of the user.
            Example: "12345"
        :type userId: str
        """
        if options is None:
            options = GetUsersIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', userId]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return User.from_dict(json.loads(response.text))
    def putUsersId(self, userId: str, requestBody: PutUsersIdRequestBodyArg, options: PutUsersIdOptionsArg = None) -> User:
        """
        Updates a managed or app user in an enterprise. This endpoint
        
        is only available to users and applications with the right

        
        admin permissions.

        :param userId: The ID of the user.
            Example: "12345"
        :type userId: str
        """
        if options is None:
            options = PutUsersIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', userId]), FetchOptions(method='PUT', params={'fields': options.fields}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return User.from_dict(json.loads(response.text))
    def deleteUsersId(self, userId: str, options: DeleteUsersIdOptionsArg = None):
        """
        Deletes a user. By default this will fail if the user
        
        still owns any content. Move their owned content first

        
        before proceeding, or use the `force` field to delete

        
        the user and their files.

        :param userId: The ID of the user.
            Example: "12345"
        :type userId: str
        """
        if options is None:
            options = DeleteUsersIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', userId]), FetchOptions(method='DELETE', params={'notify': options.notify, 'force': options.force}, auth=self.auth))
        return response.content