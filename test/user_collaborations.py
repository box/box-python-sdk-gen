from box_sdk_gen.utils import to_string

import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import UserFull

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.schemas import Collaboration

from box_sdk_gen.managers.user_collaborations import CreateCollaborationItemArg

from box_sdk_gen.managers.user_collaborations import CreateCollaborationItemArgTypeField

from box_sdk_gen.managers.user_collaborations import CreateCollaborationAccessibleByArg

from box_sdk_gen.managers.user_collaborations import (
    CreateCollaborationAccessibleByArgTypeField,
)

from box_sdk_gen.managers.user_collaborations import CreateCollaborationRoleArg

from box_sdk_gen.managers.user_collaborations import UpdateCollaborationByIdRoleArg

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

from test.commons import create_new_folder

client: BoxClient = get_default_client()


def testUserCollaborations():
    user_name: str = get_uuid()
    user_login: str = ''.join([get_uuid(), '@gmail.com'])
    user: UserFull = client.users.create_user(
        name=user_name, login=user_login, is_platform_access_only=True
    )
    folder: FolderFull = create_new_folder()
    collaboration: Collaboration = client.user_collaborations.create_collaboration(
        item=CreateCollaborationItemArg(
            type=CreateCollaborationItemArgTypeField.FOLDER.value, id=folder.id
        ),
        accessible_by=CreateCollaborationAccessibleByArg(
            type=CreateCollaborationAccessibleByArgTypeField.USER.value, id=user.id
        ),
        role=CreateCollaborationRoleArg.EDITOR.value,
    )
    assert to_string(collaboration.role) == 'editor'
    collaboration_id: str = collaboration.id
    collaboration_from_api: Collaboration = (
        client.user_collaborations.get_collaboration_by_id(
            collaboration_id=collaboration_id
        )
    )
    assert collaboration_id == collaboration_from_api.id
    assert to_string(collaboration_from_api.status) == 'accepted'
    assert to_string(collaboration_from_api.type) == 'collaboration'
    assert collaboration_from_api.invite_email == None
    updated_collaboration: Collaboration = (
        client.user_collaborations.update_collaboration_by_id(
            collaboration_id=collaboration_id,
            role=UpdateCollaborationByIdRoleArg.VIEWER.value,
        )
    )
    assert to_string(updated_collaboration.role) == 'viewer'
    client.user_collaborations.delete_collaboration_by_id(
        collaboration_id=collaboration_id
    )
    with pytest.raises(Exception):
        client.user_collaborations.get_collaboration_by_id(
            collaboration_id=collaboration_id
        )
    client.folders.delete_folder_by_id(folder_id=folder.id)
    client.users.delete_user_by_id(user_id=user.id)
