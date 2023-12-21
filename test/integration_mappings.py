import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParent

from box_sdk_gen.schemas import IntegrationMappingPartnerItemSlack

from box_sdk_gen.schemas import IntegrationMappingPartnerItemSlackTypeField

from box_sdk_gen.schemas import IntegrationMappingBoxItemSlack

from box_sdk_gen.schemas import IntegrationMappingBoxItemSlackTypeField

from box_sdk_gen.schemas import IntegrationMappings

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import get_env_var

from test.commons import get_default_client

from test.commons import get_default_client_as_user

client: BoxClient = get_default_client()


def testIntegrationMappings():
    folder: FolderFull = client.folders.create_folder(
        name=get_uuid(), parent=CreateFolderParent(id='0')
    )
    slack_org_id: str = '1'
    partner_item_id: str = '1'
    user_id: str = get_env_var('USER_ID')
    user_client: BoxClient = get_default_client_as_user(user_id)
    with pytest.raises(Exception):
        user_client.integration_mappings.create_slack_integration_mapping(
            partner_item=IntegrationMappingPartnerItemSlack(
                type=IntegrationMappingPartnerItemSlackTypeField.CHANNEL.value,
                id=partner_item_id,
                slack_org_id=slack_org_id,
            ),
            box_item=IntegrationMappingBoxItemSlack(
                id=folder.id, type=IntegrationMappingBoxItemSlackTypeField.FOLDER.value
            ),
        )
    integration_mappings: IntegrationMappings = (
        user_client.integration_mappings.get_slack_integration_mapping()
    )
    assert len(integration_mappings.entries) == 0
    client.folders.delete_folder_by_id(folder_id=folder.id)
