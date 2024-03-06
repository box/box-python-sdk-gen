from box_sdk_gen.internal.utils import to_string

from typing import List

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParent

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.internal.utils import ByteStream

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributes

from box_sdk_gen.managers.uploads import UploadFileAttributesParentField

from box_sdk_gen.schemas import TermsOfServices

from box_sdk_gen.managers.terms_of_services import CreateTermsOfServiceStatus

from box_sdk_gen.managers.terms_of_services import CreateTermsOfServiceTosType

from box_sdk_gen.schemas import ClassificationTemplateFieldsOptionsField

from box_sdk_gen.managers.classifications import AddClassificationRequestBody

from box_sdk_gen.managers.classifications import AddClassificationRequestBodyOpField

from box_sdk_gen.managers.classifications import (
    AddClassificationRequestBodyFieldKeyField,
)

from box_sdk_gen.managers.classifications import AddClassificationRequestBodyDataField

from box_sdk_gen.managers.classifications import (
    AddClassificationRequestBodyDataStaticConfigField,
)

from box_sdk_gen.managers.classifications import (
    AddClassificationRequestBodyDataStaticConfigClassificationField,
)

from box_sdk_gen.managers.classifications import CreateClassificationTemplateScope

from box_sdk_gen.managers.classifications import CreateClassificationTemplateTemplateKey

from box_sdk_gen.managers.classifications import CreateClassificationTemplateDisplayName

from box_sdk_gen.managers.classifications import CreateClassificationTemplateFields

from box_sdk_gen.managers.classifications import (
    CreateClassificationTemplateFieldsTypeField,
)

from box_sdk_gen.managers.classifications import (
    CreateClassificationTemplateFieldsKeyField,
)

from box_sdk_gen.managers.classifications import (
    CreateClassificationTemplateFieldsDisplayNameField,
)

from box_sdk_gen.schemas import ShieldInformationBarrier

from box_sdk_gen.schemas import ShieldInformationBarriers

from box_sdk_gen.schemas import EnterpriseBase

from box_sdk_gen.schemas import EnterpriseBaseTypeField

from box_sdk_gen.internal.utils import decode_base_64

from box_sdk_gen.internal.utils import get_env_var

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import generate_byte_stream

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import ClassificationTemplate

from box_sdk_gen.schemas import TermsOfService

from box_sdk_gen.box.jwt_auth import BoxJWTAuth

from box_sdk_gen.box.jwt_auth import JWTConfig


def get_jwt_auth() -> BoxJWTAuth:
    jwt_config: JWTConfig = JWTConfig.from_config_json_string(
        decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
    )
    auth: BoxJWTAuth = BoxJWTAuth(config=jwt_config)
    return auth


def get_default_client_as_user(user_id: str) -> BoxClient:
    auth: BoxJWTAuth = get_jwt_auth()
    auth_user: BoxJWTAuth = auth.as_user(user_id)
    return BoxClient(auth=auth_user)


def get_default_client() -> BoxClient:
    client: BoxClient = BoxClient(auth=get_jwt_auth())
    return client


def create_new_folder() -> FolderFull:
    client: BoxClient = get_default_client()
    new_folder_name: str = get_uuid()
    return client.folders.create_folder(new_folder_name, CreateFolderParent(id='0'))


def upload_new_file() -> FileFull:
    client: BoxClient = get_default_client()
    new_file_name: str = ''.join([get_uuid(), '.pdf'])
    file_content_stream: ByteStream = generate_byte_stream(1024 * 1024)
    uploaded_files: Files = client.uploads.upload_file(
        UploadFileAttributes(
            name=new_file_name, parent=UploadFileAttributesParentField(id='0')
        ),
        file_content_stream,
    )
    return uploaded_files.entries[0]


def get_or_create_terms_of_services() -> TermsOfService:
    client: BoxClient = get_default_client()
    tos: TermsOfServices = client.terms_of_services.get_terms_of_service()
    number_of_tos: int = len(tos.entries)
    if number_of_tos >= 1:
        first_tos: TermsOfService = tos.entries[0]
        if to_string(first_tos.tos_type) == 'managed':
            return first_tos
    if number_of_tos >= 2:
        second_tos: TermsOfService = tos.entries[1]
        if to_string(second_tos.tos_type) == 'managed':
            return second_tos
    return client.terms_of_services.create_terms_of_service(
        CreateTermsOfServiceStatus.DISABLED.value,
        'Test TOS',
        tos_type=CreateTermsOfServiceTosType.MANAGED.value,
    )


def get_or_create_classification(
    classification_template: ClassificationTemplate,
) -> ClassificationTemplateFieldsOptionsField:
    client: BoxClient = get_default_client()
    classifications: List[ClassificationTemplateFieldsOptionsField] = (
        classification_template.fields[0].options
    )
    current_number_of_classifications: int = len(classifications)
    if current_number_of_classifications == 0:
        classification_template_with_new_classification: ClassificationTemplate = (
            client.classifications.add_classification(
                [
                    AddClassificationRequestBody(
                        op=AddClassificationRequestBodyOpField.ADDENUMOPTION.value,
                        field_key=AddClassificationRequestBodyFieldKeyField.BOX__SECURITY__CLASSIFICATION__KEY.value,
                        data=AddClassificationRequestBodyDataField(
                            key=get_uuid(),
                            static_config=AddClassificationRequestBodyDataStaticConfigField(
                                classification=AddClassificationRequestBodyDataStaticConfigClassificationField(
                                    color_id=3,
                                    classification_definition='Some description',
                                )
                            ),
                        ),
                    )
                ]
            )
        )
        return classification_template_with_new_classification.fields[0].options[0]
    return classifications[0]


def get_or_create_classification_template() -> ClassificationTemplate:
    client: BoxClient = get_default_client()
    try:
        return client.classifications.get_classification_template()
    except Exception:
        return client.classifications.create_classification_template(
            CreateClassificationTemplateScope.ENTERPRISE.value,
            CreateClassificationTemplateTemplateKey.SECURITYCLASSIFICATION_6VMVOCHWUWO.value,
            CreateClassificationTemplateDisplayName.CLASSIFICATION.value,
            [
                CreateClassificationTemplateFields(
                    type=CreateClassificationTemplateFieldsTypeField.ENUM.value,
                    key=CreateClassificationTemplateFieldsKeyField.BOX__SECURITY__CLASSIFICATION__KEY.value,
                    display_name=CreateClassificationTemplateFieldsDisplayNameField.CLASSIFICATION.value,
                    options=[],
                )
            ],
        )


def get_or_create_shield_information_barrier(
    client: BoxClient, enterprise_id: str
) -> ShieldInformationBarrier:
    barriers: ShieldInformationBarriers = (
        client.shield_information_barriers.get_shield_information_barriers()
    )
    number_of_barriers: int = len(barriers.entries)
    if number_of_barriers == 0:
        return client.shield_information_barriers.create_shield_information_barrier(
            EnterpriseBase(
                id=enterprise_id, type=EnterpriseBaseTypeField.ENTERPRISE.value
            )
        )
    return barriers.entries[number_of_barriers - 1]
