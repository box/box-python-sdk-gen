from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.schemas import GroupFull

from box_sdk_gen.schemas import Collaboration

from box_sdk_gen.managers.user_collaborations import CreateCollaborationItem

from box_sdk_gen.managers.user_collaborations import CreateCollaborationItemTypeField

from box_sdk_gen.managers.user_collaborations import CreateCollaborationAccessibleBy

from box_sdk_gen.managers.user_collaborations import (
    CreateCollaborationAccessibleByTypeField,
)

from box_sdk_gen.managers.user_collaborations import CreateCollaborationRole

from box_sdk_gen.schemas import Collaborations

from box_sdk_gen.managers.list_collaborations import GetCollaborationsStatus

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import get_env_var

from test.commons import get_default_client

from test.commons import create_new_folder

from test.commons import upload_new_file


def testListCollaborations():
    client: BoxClient = get_default_client()
    folder: FolderFull = create_new_folder()
    file: FileFull = upload_new_file()
    group: GroupFull = client.groups.create_group(name=get_uuid())
    group_collaboration: Collaboration = (
        client.user_collaborations.create_collaboration(
            item=CreateCollaborationItem(
                type=CreateCollaborationItemTypeField.FOLDER.value, id=folder.id
            ),
            accessible_by=CreateCollaborationAccessibleBy(
                type=CreateCollaborationAccessibleByTypeField.GROUP.value, id=group.id
            ),
            role=CreateCollaborationRole.EDITOR.value,
        )
    )
    file_collaboration: Collaboration = client.user_collaborations.create_collaboration(
        item=CreateCollaborationItem(
            type=CreateCollaborationItemTypeField.FILE.value, id=file.id
        ),
        accessible_by=CreateCollaborationAccessibleBy(
            type=CreateCollaborationAccessibleByTypeField.USER.value,
            id=get_env_var('USER_ID'),
        ),
        role=CreateCollaborationRole.EDITOR.value,
    )
    assert to_string(group_collaboration.role) == 'editor'
    assert to_string(group_collaboration.type) == 'collaboration'
    file_collaborations: Collaborations = (
        client.list_collaborations.get_file_collaborations(file_id=file.id)
    )
    assert len(file_collaborations.entries) > 0
    folder_collaborations: Collaborations = (
        client.list_collaborations.get_folder_collaborations(folder_id=folder.id)
    )
    assert len(folder_collaborations.entries) > 0
    pending_collaborations: Collaborations = (
        client.list_collaborations.get_collaborations(
            status=GetCollaborationsStatus.PENDING.value
        )
    )
    assert len(pending_collaborations.entries) >= 0
    group_collaborations: Collaborations = (
        client.list_collaborations.get_group_collaborations(group_id=group.id)
    )
    assert len(group_collaborations.entries) > 0
    client.user_collaborations.delete_collaboration_by_id(
        collaboration_id=group_collaboration.id
    )
    client.files.delete_file_by_id(file_id=file.id)
    client.folders.delete_folder_by_id(folder_id=folder.id)
    client.groups.delete_group_by_id(group_id=group.id)
