from box_sdk_gen.utils import to_string

import pytest

from typing import Dict

from box_sdk_gen.client import BoxClient

from box_sdk_gen.managers.metadata_templates import CreateMetadataTemplateFields

from box_sdk_gen.managers.metadata_templates import (
    CreateMetadataTemplateFieldsTypeField,
)

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.schemas import MetadataCascadePolicy

from box_sdk_gen.managers.metadata_cascade_policies import (
    CreateMetadataCascadePolicyScope,
)

from box_sdk_gen.schemas import MetadataCascadePolicies

from box_sdk_gen.managers.metadata_cascade_policies import (
    ApplyMetadataCascadePolicyConflictResolution,
)

from box_sdk_gen.managers.folder_metadata import CreateFolderMetadataByIdScope

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import to_string

from test.commons import get_default_client

from test.commons import create_new_folder

from test.commons import upload_new_file

client: BoxClient = get_default_client()


def testMetadataCascadePolicies():
    template_key: str = ''.join(['key', get_uuid()])
    client.metadata_templates.create_metadata_template(
        scope='enterprise',
        template_key=template_key,
        display_name=template_key,
        fields=[
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.STRING.value,
                key='testName',
                display_name='testName',
            )
        ],
    )
    folder: FolderFull = create_new_folder()
    enterprise_id: str = get_env_var('ENTERPRISE_ID')
    cascade_policy: MetadataCascadePolicy = (
        client.metadata_cascade_policies.create_metadata_cascade_policy(
            folder_id=folder.id,
            scope=CreateMetadataCascadePolicyScope.ENTERPRISE.value,
            template_key=template_key,
        )
    )
    assert to_string(cascade_policy.type) == 'metadata_cascade_policy'
    assert to_string(cascade_policy.owner_enterprise.type) == 'enterprise'
    assert to_string(cascade_policy.owner_enterprise.id) == enterprise_id
    assert to_string(cascade_policy.parent.type) == 'folder'
    assert cascade_policy.parent.id == folder.id
    assert to_string(cascade_policy.scope) == ''.join(['enterprise_', enterprise_id])
    assert cascade_policy.template_key == template_key
    cascade_policy_id: str = cascade_policy.id
    policy_from_the_api: MetadataCascadePolicy = (
        client.metadata_cascade_policies.get_metadata_cascade_policy_by_id(
            metadata_cascade_policy_id=cascade_policy_id
        )
    )
    assert cascade_policy_id == policy_from_the_api.id
    policies: MetadataCascadePolicies = (
        client.metadata_cascade_policies.get_metadata_cascade_policies(
            folder_id=folder.id
        )
    )
    assert len(policies.entries) == 1
    with pytest.raises(Exception):
        client.metadata_cascade_policies.apply_metadata_cascade_policy(
            metadata_cascade_policy_id=cascade_policy_id,
            conflict_resolution=ApplyMetadataCascadePolicyConflictResolution.OVERWRITE.value,
        )
    data: Dict[str, str] = {'testName': 'xyz'}
    client.folder_metadata.create_folder_metadata_by_id(
        folder_id=folder.id,
        scope=CreateFolderMetadataByIdScope.ENTERPRISE.value,
        template_key=template_key,
        request_body=data,
    )
    client.metadata_cascade_policies.apply_metadata_cascade_policy(
        metadata_cascade_policy_id=cascade_policy_id,
        conflict_resolution=ApplyMetadataCascadePolicyConflictResolution.OVERWRITE.value,
    )
    client.metadata_cascade_policies.delete_metadata_cascade_policy_by_id(
        metadata_cascade_policy_id=cascade_policy_id
    )
    with pytest.raises(Exception):
        client.metadata_cascade_policies.get_metadata_cascade_policy_by_id(
            metadata_cascade_policy_id=cascade_policy_id
        )
    client.folders.delete_folder_by_id(folder_id=folder.id)
