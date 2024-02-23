from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import UserFull

from box_sdk_gen.schemas import SessionTerminationMessage

from box_sdk_gen.schemas import GroupFull

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import get_env_var

from test.commons import get_default_client

from test.commons import get_default_client_as_user

client: BoxClient = get_default_client()


def testSessionTerminationUser():
    admin_client: BoxClient = get_default_client_as_user(get_env_var('USER_ID'))
    user: UserFull = admin_client.users.get_user_me()
    result: SessionTerminationMessage = (
        client.session_termination.terminate_users_sessions(
            user_ids=[get_env_var('USER_ID')], user_logins=[user.login]
        )
    )
    assert (
        result.message
        == 'Request is successful, please check the admin events for the status of the job'
    )


def testSessionTerminationGroup():
    group_name: str = get_uuid()
    group: GroupFull = client.groups.create_group(name=group_name)
    result: SessionTerminationMessage = (
        client.session_termination.terminate_groups_sessions(group_ids=[group.id])
    )
    assert (
        result.message
        == 'Request is successful, please check the admin events for the status of the job'
    )
    client.groups.delete_group_by_id(group_id=group.id)
