from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import UserFull

from box_sdk_gen.schemas import Invite

from box_sdk_gen.managers.invites import CreateInviteEnterprise

from box_sdk_gen.managers.invites import CreateInviteActionableBy

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import get_env_var

from test.commons import get_default_client_as_user


def testInvites():
    user_id: str = get_env_var('USER_ID')
    client: BoxClient = get_default_client_as_user(user_id)
    current_user: UserFull = client.users.get_user_me(fields=['enterprise'])
    email: str = get_env_var('BOX_EXTERNAL_USER_EMAIL')
    invitation: Invite = client.invites.create_invite(
        enterprise=CreateInviteEnterprise(id=current_user.enterprise.id),
        actionable_by=CreateInviteActionableBy(login=email),
    )
    assert to_string(invitation.type) == 'invite'
    assert invitation.invited_to.id == current_user.enterprise.id
    assert invitation.actionable_by.login == email
    get_invitation: Invite = client.invites.get_invite_by_id(invite_id=invitation.id)
    assert get_invitation.id == invitation.id
