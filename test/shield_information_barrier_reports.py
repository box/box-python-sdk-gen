from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.schemas import ShieldInformationBarrierReports

from box_sdk_gen.schemas import ShieldInformationBarrierReport

from box_sdk_gen.schemas import ShieldInformationBarrierBase

from box_sdk_gen.schemas import ShieldInformationBarrierBaseTypeField

from box_sdk_gen.internal.utils import get_env_var

from test.commons import get_default_client_as_user

from test.commons import get_or_create_shield_information_barrier

from box_sdk_gen.schemas import ShieldInformationBarrier

from box_sdk_gen.client import BoxClient


def shieldInformationBarrierReports():
    client: BoxClient = get_default_client_as_user(get_env_var('USER_ID'))
    enterprise_id: str = get_env_var('ENTERPRISE_ID')
    barrier: ShieldInformationBarrier = get_or_create_shield_information_barrier(
        client, enterprise_id
    )
    assert to_string(barrier.status) == 'draft'
    assert to_string(barrier.type) == 'shield_information_barrier'
    assert barrier.enterprise.id == enterprise_id
    assert to_string(barrier.enterprise.type) == 'enterprise'
    barrier_id: str = barrier.id
    existing_reports: ShieldInformationBarrierReports = (
        client.shield_information_barrier_reports.get_shield_information_barrier_reports(
            shield_information_barrier_id=barrier_id
        )
    )
    if len(existing_reports.entries) > 0:
        return None
    created_report: ShieldInformationBarrierReport = (
        client.shield_information_barrier_reports.create_shield_information_barrier_report(
            shield_information_barrier=ShieldInformationBarrierBase(
                id=barrier_id,
                type=ShieldInformationBarrierBaseTypeField.SHIELD_INFORMATION_BARRIER.value,
            )
        )
    )
    assert (
        created_report.shield_information_barrier.shield_information_barrier.id
        == barrier_id
    )
    retrieved_report: ShieldInformationBarrierReport = (
        client.shield_information_barrier_reports.get_shield_information_barrier_report_by_id(
            shield_information_barrier_report_id=created_report.id
        )
    )
    assert retrieved_report.id == created_report.id
    retrieved_reports: ShieldInformationBarrierReports = (
        client.shield_information_barrier_reports.get_shield_information_barrier_reports(
            shield_information_barrier_id=barrier_id
        )
    )
    assert len(retrieved_reports.entries) > 0
