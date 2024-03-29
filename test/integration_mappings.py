import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParent

from box_sdk_gen.schemas import IntegrationMappingPartnerItemSlack

from box_sdk_gen.schemas import IntegrationMappingBoxItemSlack

from box_sdk_gen.schemas import IntegrationMappings

from box_sdk_gen.internal.utils import generate_byte_stream

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import get_env_var

from test.commons import get_default_client

from test.commons import get_default_client_with_user_subject

client: BoxClient = get_default_client()


def testIntegrationMappings():
    folder: FolderFull = client.folders.create_folder(
        get_uuid(), CreateFolderParent(id='0')
    )
    slack_org_id: str = '1'
    partner_item_id: str = '1'
    user_id: str = get_env_var('USER_ID')
    user_client: BoxClient = get_default_client_with_user_subject(user_id)
    with pytest.raises(Exception):
        user_client.integration_mappings.create_slack_integration_mapping(
            IntegrationMappingPartnerItemSlack(
                id=partner_item_id, slack_org_id=slack_org_id
            ),
            IntegrationMappingBoxItemSlack(id=folder.id),
        )
    integration_mappings: IntegrationMappings = (
        user_client.integration_mappings.get_slack_integration_mapping()
    )
    assert len(integration_mappings.entries) == 0
    client.folders.delete_folder_by_id(folder.id)
