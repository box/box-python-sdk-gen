from box_sdk_gen.utils import to_string

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import UserFull

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

client: BoxClient = get_default_client()


def testWithAsUserHeader():
    user_name: str = get_uuid()
    created_user: UserFull = client.users.create_user(
        name=user_name, is_platform_access_only=True
    )
    as_user_client: BoxClient = client.with_as_user_header(created_user.id)
    admin_user: UserFull = client.users.get_user_me()
    assert not to_string(admin_user.name) == user_name
    app_user: UserFull = as_user_client.users.get_user_me()
    assert to_string(app_user.name) == user_name
    client.users.delete_user_by_id(user_id=created_user.id)


def testWithSuppressedNotifications():
    new_client: BoxClient = client.with_suppressed_notifications()
    user: UserFull = new_client.users.get_user_me()
    assert not user.id == ''


def testWithExtraHeaders():
    user_name: str = get_uuid()
    created_user: UserFull = client.users.create_user(
        name=user_name, is_platform_access_only=True
    )
    as_user_client: BoxClient = client.with_extra_headers({'As-User': created_user.id})
    admin_user: UserFull = client.users.get_user_me()
    assert not to_string(admin_user.name) == user_name
    app_user: UserFull = as_user_client.users.get_user_me()
    assert to_string(app_user.name) == user_name
    client.users.delete_user_by_id(user_id=created_user.id)
