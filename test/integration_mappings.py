import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas.folder_full import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParent

from box_sdk_gen.schemas.integration_mapping_partner_item_slack import (
    IntegrationMappingPartnerItemSlack,
)

from box_sdk_gen.schemas.integration_mapping_box_item_slack import (
    IntegrationMappingBoxItemSlack,
)

from box_sdk_gen.schemas.integration_mappings import IntegrationMappings

from box_sdk_gen.schemas.integration_mapping_partner_item_teams_create_request import (
    IntegrationMappingPartnerItemTeamsCreateRequest,
)

from box_sdk_gen.schemas.integration_mapping_partner_item_teams_create_request import (
    IntegrationMappingPartnerItemTeamsCreateRequestTypeField,
)

from box_sdk_gen.schemas.folder_reference import FolderReference

from box_sdk_gen.internal.utils import generate_byte_stream

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import get_env_var

from test.commons import get_default_client

from test.commons import get_default_client_with_user_subject

client: BoxClient = get_default_client()


def testSlackIntegrationMappings():
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
    integration_mapping_id: str = '123456'
    with pytest.raises(Exception):
        user_client.integration_mappings.update_slack_integration_mapping_by_id(
            integration_mapping_id,
            box_item=IntegrationMappingBoxItemSlack(id='1234567'),
        )
    with pytest.raises(Exception):
        user_client.integration_mappings.delete_slack_integration_mapping_by_id(
            integration_mapping_id
        )
    client.folders.delete_folder_by_id(folder.id)


def testTeamsIntegrationMappings():
    folder: FolderFull = client.folders.create_folder(
        get_uuid(), CreateFolderParent(id='0')
    )
    tenant_id: str = '1'
    team_id: str = '2'
    partner_item_id: str = '3'
    user_id: str = get_env_var('USER_ID')
    user_client: BoxClient = get_default_client_with_user_subject(user_id)
    with pytest.raises(Exception):
        user_client.integration_mappings.create_teams_integration_mapping(
            IntegrationMappingPartnerItemTeamsCreateRequest(
                type=IntegrationMappingPartnerItemTeamsCreateRequestTypeField.CHANNEL,
                id=partner_item_id,
                tenant_id=tenant_id,
                team_id=team_id,
            ),
            FolderReference(id=folder.id),
        )
    with pytest.raises(Exception):
        user_client.integration_mappings.get_teams_integration_mapping()
    integration_mapping_id: str = '123456'
    with pytest.raises(Exception):
        user_client.integration_mappings.update_teams_integration_mapping_by_id(
            integration_mapping_id, box_item=FolderReference(id='1234567')
        )
    with pytest.raises(Exception):
        user_client.integration_mappings.delete_teams_integration_mapping_by_id(
            integration_mapping_id
        )
    client.folders.delete_folder_by_id(folder.id)
