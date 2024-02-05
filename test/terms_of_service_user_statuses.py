from box_sdk_gen.utils import to_string

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import TermsOfService

from box_sdk_gen.schemas import UserFull

from box_sdk_gen.schemas import TermsOfServiceUserStatus

from box_sdk_gen.managers.terms_of_service_user_statuses import (
    CreateTermsOfServiceStatusForUserTos,
)

from box_sdk_gen.managers.terms_of_service_user_statuses import (
    CreateTermsOfServiceStatusForUserTosTypeField,
)

from box_sdk_gen.managers.terms_of_service_user_statuses import (
    CreateTermsOfServiceStatusForUserUser,
)

from box_sdk_gen.managers.terms_of_service_user_statuses import (
    CreateTermsOfServiceStatusForUserUserTypeField,
)

from box_sdk_gen.schemas import TermsOfServiceUserStatuses

from test.commons import get_default_client_as_user

from test.commons import get_or_create_terms_of_services

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import get_env_var


def testGetTermsOfServiceUserStatuses():
    admin_user_id: str = get_env_var('USER_ID')
    client: BoxClient = get_default_client_as_user(admin_user_id)
    tos: TermsOfService = get_or_create_terms_of_services()
    user: UserFull = client.users.create_user(
        name=get_uuid(),
        login=''.join([get_uuid(), '@boxdemo.com']),
        is_platform_access_only=True,
    )
    created_tos_user_status: TermsOfServiceUserStatus = (
        client.terms_of_service_user_statuses.create_terms_of_service_status_for_user(
            tos=CreateTermsOfServiceStatusForUserTos(
                type=CreateTermsOfServiceStatusForUserTosTypeField.TERMS_OF_SERVICE.value,
                id=tos.id,
            ),
            user=CreateTermsOfServiceStatusForUserUser(
                type=CreateTermsOfServiceStatusForUserUserTypeField.USER.value,
                id=user.id,
            ),
            is_accepted=False,
        )
    )
    assert created_tos_user_status.is_accepted == False
    assert to_string(created_tos_user_status.type) == 'terms_of_service_user_status'
    assert to_string(created_tos_user_status.tos.type) == 'terms_of_service'
    assert to_string(created_tos_user_status.user.type) == 'user'
    assert created_tos_user_status.tos.id == tos.id
    assert created_tos_user_status.user.id == user.id
    updated_tos_user_status: TermsOfServiceUserStatus = (
        client.terms_of_service_user_statuses.update_terms_of_service_status_for_user_by_id(
            terms_of_service_user_status_id=created_tos_user_status.id, is_accepted=True
        )
    )
    assert updated_tos_user_status.is_accepted == True
    list_tos_user_statuses: TermsOfServiceUserStatuses = (
        client.terms_of_service_user_statuses.get_terms_of_service_user_statuses(
            tos_id=tos.id, user_id=user.id
        )
    )
    assert list_tos_user_statuses.total_count > 0
    client.users.delete_user_by_id(user_id=user.id)
