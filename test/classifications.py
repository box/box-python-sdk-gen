from typing import List

from box_sdk_gen.client import BoxClient

from box_sdk_gen.managers.classifications import CreateClassificationTemplateScopeArg

from box_sdk_gen.managers.classifications import (
    CreateClassificationTemplateTemplateKeyArg,
)

from box_sdk_gen.managers.classifications import (
    CreateClassificationTemplateDisplayNameArg,
)

from box_sdk_gen.managers.classifications import CreateClassificationTemplateFieldsArg

from box_sdk_gen.managers.classifications import (
    CreateClassificationTemplateFieldsArgTypeField,
)

from box_sdk_gen.managers.classifications import (
    CreateClassificationTemplateFieldsArgKeyField,
)

from box_sdk_gen.managers.classifications import (
    CreateClassificationTemplateFieldsArgDisplayNameField,
)

from box_sdk_gen.schemas import ClassificationTemplateFieldsFieldOptionsField

from box_sdk_gen.managers.classifications import AddClassificationRequestBodyArg

from box_sdk_gen.managers.classifications import AddClassificationRequestBodyArgOpField

from box_sdk_gen.managers.classifications import (
    AddClassificationRequestBodyArgFieldKeyField,
)

from box_sdk_gen.managers.classifications import (
    AddClassificationRequestBodyArgDataField,
)

from box_sdk_gen.managers.classifications import (
    AddClassificationRequestBodyArgDataFieldStaticConfigField,
)

from box_sdk_gen.managers.classifications import (
    AddClassificationRequestBodyArgDataFieldStaticConfigFieldClassificationField,
)

from box_sdk_gen.managers.classifications import UpdateClassificationRequestBodyArg

from box_sdk_gen.managers.classifications import (
    UpdateClassificationRequestBodyArgOpField,
)

from box_sdk_gen.managers.classifications import (
    UpdateClassificationRequestBodyArgFieldKeyField,
)

from box_sdk_gen.managers.classifications import (
    UpdateClassificationRequestBodyArgDataField,
)

from box_sdk_gen.managers.classifications import (
    UpdateClassificationRequestBodyArgDataFieldStaticConfigField,
)

from box_sdk_gen.managers.classifications import (
    UpdateClassificationRequestBodyArgDataFieldStaticConfigFieldClassificationField,
)

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

from test.commons import upload_new_file

from box_sdk_gen.schemas import ClassificationTemplate

client: BoxClient = get_default_client()


def get_or_create_classification_template() -> ClassificationTemplate:
    try:
        return client.classifications.get_classification_template()
    except Exception:
        return client.classifications.create_classification_template(
            scope=CreateClassificationTemplateScopeArg.ENTERPRISE.value,
            template_key=CreateClassificationTemplateTemplateKeyArg.SECURITYCLASSIFICATION_6VMVOCHWUWO.value,
            display_name=CreateClassificationTemplateDisplayNameArg.CLASSIFICATION.value,
            fields=[
                CreateClassificationTemplateFieldsArg(
                    type=CreateClassificationTemplateFieldsArgTypeField.ENUM.value,
                    key=CreateClassificationTemplateFieldsArgKeyField.BOX__SECURITY__CLASSIFICATION__KEY.value,
                    display_name=CreateClassificationTemplateFieldsArgDisplayNameField.CLASSIFICATION.value,
                    options=[],
                )
            ],
        )


def get_or_create_classification(
    classification_template: ClassificationTemplate,
) -> ClassificationTemplateFieldsFieldOptionsField:
    classifications: List[ClassificationTemplateFieldsFieldOptionsField] = (
        classification_template.fields[0].options
    )
    current_number_of_classifications: int = len(classifications)
    if current_number_of_classifications == 0:
        classification_template_with_new_classification: ClassificationTemplate = (
            client.classifications.add_classification(
                request_body=[
                    AddClassificationRequestBodyArg(
                        op=AddClassificationRequestBodyArgOpField.ADDENUMOPTION.value,
                        field_key=AddClassificationRequestBodyArgFieldKeyField.BOX__SECURITY__CLASSIFICATION__KEY.value,
                        data=AddClassificationRequestBodyArgDataField(
                            key=get_uuid(),
                            static_config=AddClassificationRequestBodyArgDataFieldStaticConfigField(
                                classification=AddClassificationRequestBodyArgDataFieldStaticConfigFieldClassificationField(
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
    return classifications[current_number_of_classifications - 1]


def testClassifications():
    classification_template: ClassificationTemplate = (
        get_or_create_classification_template()
    )
    classification: ClassificationTemplateFieldsFieldOptionsField = (
        get_or_create_classification(classification_template)
    )
    assert not classification.key == ''
    assert not classification.static_config.classification.color_id == 100
    assert (
        not classification.static_config.classification.classification_definition == ''
    )
    updated_classification_name: str = get_uuid()
    updated_classification_description: str = get_uuid()
    classification_template_with_updated_classification: ClassificationTemplate = (
        client.classifications.update_classification(
            request_body=[
                UpdateClassificationRequestBodyArg(
                    op=UpdateClassificationRequestBodyArgOpField.EDITENUMOPTION.value,
                    field_key=UpdateClassificationRequestBodyArgFieldKeyField.BOX__SECURITY__CLASSIFICATION__KEY.value,
                    enum_option_key=classification.key,
                    data=UpdateClassificationRequestBodyArgDataField(
                        key=updated_classification_name,
                        static_config=UpdateClassificationRequestBodyArgDataFieldStaticConfigField(
                            classification=UpdateClassificationRequestBodyArgDataFieldStaticConfigFieldClassificationField(
                                color_id=2,
                                classification_definition=updated_classification_description,
                            )
                        ),
                    ),
                )
            ]
        )
    )
    updated_classifications: List[ClassificationTemplateFieldsFieldOptionsField] = (
        classification_template_with_updated_classification.fields[0].options
    )
    number_of_classifications_after_update: int = len(updated_classifications)
    updated_classification: ClassificationTemplateFieldsFieldOptionsField = (
        updated_classifications[number_of_classifications_after_update - 1]
    )
    assert updated_classification.key == updated_classification_name
    assert updated_classification.static_config.classification.color_id == 2
    assert (
        updated_classification.static_config.classification.classification_definition
        == updated_classification_description
    )
