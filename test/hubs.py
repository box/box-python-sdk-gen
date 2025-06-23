from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas.v2025_r0.hubs_v2025_r0 import HubsV2025R0

from box_sdk_gen.managers.hubs import GetHubsV2025R0Direction

from box_sdk_gen.schemas.v2025_r0.hub_v2025_r0 import HubV2025R0

from box_sdk_gen.managers.hubs import GetEnterpriseHubsV2025R0Direction

from test.commons import get_default_client_with_user_subject

from box_sdk_gen.internal.utils import get_env_var

client: BoxClient = get_default_client_with_user_subject(get_env_var('USER_ID'))


def testGetAndDeleteHubs():
    user_hubs: HubsV2025R0 = client.hubs.get_hubs_v2025_r0(
        scope='all', sort='name', direction=GetHubsV2025R0Direction.ASC
    )
    assert len(user_hubs.entries) > 0
    user_hub: HubV2025R0 = user_hubs.entries[0]
    assert not user_hub.title == ''
    assert not user_hub.id == ''
    assert to_string(user_hub.type) == 'hubs'
    enterprise_hubs: HubsV2025R0 = client.hubs.get_enterprise_hubs_v2025_r0(
        sort='name', direction=GetEnterpriseHubsV2025R0Direction.ASC
    )
    assert len(enterprise_hubs.entries) > 0
    enterprise_hub: HubV2025R0 = enterprise_hubs.entries[0]
    assert not enterprise_hub.title == ''
    assert not enterprise_hub.id == ''
    assert to_string(enterprise_hub.type) == 'hubs'
    hub: HubV2025R0 = client.hubs.get_hub_by_id_v2025_r0(user_hub.id)
    assert not hub.title == ''
    assert not hub.id == ''
    assert to_string(hub.type) == 'hubs'
    if len(enterprise_hubs.entries) > 10:
        client.hubs.delete_hub_by_id_v2025_r0(hub.id)
