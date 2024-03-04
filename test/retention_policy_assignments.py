from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import RetentionPolicy

from box_sdk_gen.managers.retention_policies import CreateRetentionPolicyPolicyType

from box_sdk_gen.managers.retention_policies import (
    CreateRetentionPolicyDispositionAction,
)

from box_sdk_gen.managers.retention_policies import CreateRetentionPolicyRetentionType

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParent

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributes

from box_sdk_gen.managers.uploads import UploadFileAttributesParentField

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.managers.uploads import UploadFileVersionAttributes

from box_sdk_gen.schemas import RetentionPolicyAssignment

from box_sdk_gen.managers.retention_policy_assignments import (
    CreateRetentionPolicyAssignmentAssignTo,
)

from box_sdk_gen.managers.retention_policy_assignments import (
    CreateRetentionPolicyAssignmentAssignToTypeField,
)

from box_sdk_gen.schemas import RetentionPolicyAssignments

from box_sdk_gen.schemas import FilesUnderRetention

from box_sdk_gen.internal.utils import decode_base_64

from box_sdk_gen.internal.utils import get_env_var

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import generate_byte_stream

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testCreateUpdateGetDeleteRetentionPolicyAssignment():
    retention_policy_name: str = get_uuid()
    retention_description: str = 'test description'
    retention_policy: RetentionPolicy = (
        client.retention_policies.create_retention_policy(
            policy_name=retention_policy_name,
            description=retention_description,
            policy_type=CreateRetentionPolicyPolicyType.FINITE.value,
            disposition_action=CreateRetentionPolicyDispositionAction.REMOVE_RETENTION.value,
            retention_length='1',
            retention_type=CreateRetentionPolicyRetentionType.MODIFIABLE.value,
            can_owner_extend_retention=True,
            are_owners_notified=True,
        )
    )
    folder: FolderFull = client.folders.create_folder(
        name=get_uuid(), parent=CreateFolderParent(id='0')
    )
    files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributes(
            name=get_uuid(), parent=UploadFileAttributesParentField(id=folder.id)
        ),
        file=generate_byte_stream(10),
    )
    file: FileFull = files.entries[0]
    new_versions: Files = client.uploads.upload_file_version(
        file_id=file.id,
        attributes=UploadFileVersionAttributes(name=get_uuid()),
        file=generate_byte_stream(20),
    )
    new_version: FileFull = new_versions.entries[0]
    retention_policy_assignment: RetentionPolicyAssignment = (
        client.retention_policy_assignments.create_retention_policy_assignment(
            policy_id=retention_policy.id,
            assign_to=CreateRetentionPolicyAssignmentAssignTo(
                type=CreateRetentionPolicyAssignmentAssignToTypeField.FOLDER.value,
                id=folder.id,
            ),
        )
    )
    assert retention_policy_assignment.retention_policy.id == retention_policy.id
    assert retention_policy_assignment.assigned_to.id == folder.id
    retention_policy_assignment_by_id: RetentionPolicyAssignment = (
        client.retention_policy_assignments.get_retention_policy_assignment_by_id(
            retention_policy_assignment_id=retention_policy_assignment.id
        )
    )
    assert retention_policy_assignment_by_id.id == retention_policy_assignment.id
    retention_policy_assignments: RetentionPolicyAssignments = (
        client.retention_policy_assignments.get_retention_policy_assignments(
            retention_policy_id=retention_policy.id
        )
    )
    assert len(retention_policy_assignments.entries) == 1
    files_under_retention: FilesUnderRetention = (
        client.retention_policy_assignments.get_files_under_retention_policy_assignment(
            retention_policy_assignment_id=retention_policy_assignment.id
        )
    )
    assert len(files_under_retention.entries) == 1
    client.retention_policy_assignments.delete_retention_policy_assignment_by_id(
        retention_policy_assignment_id=retention_policy_assignment.id
    )
    retention_policy_assignments_after_delete: RetentionPolicyAssignments = (
        client.retention_policy_assignments.get_retention_policy_assignments(
            retention_policy_id=retention_policy.id
        )
    )
    assert len(retention_policy_assignments_after_delete.entries) == 0
    client.retention_policies.delete_retention_policy_by_id(
        retention_policy_id=retention_policy.id
    )
    client.files.delete_file_by_id(file_id=file.id)
