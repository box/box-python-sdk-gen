from typing import List

import pytest

from box_sdk_gen.client import BoxClient

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

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.schemas import Classification

from box_sdk_gen.managers.folder_classifications import (
    UpdateClassificationOnFolderRequestBody,
)

from box_sdk_gen.managers.folder_classifications import (
    UpdateClassificationOnFolderRequestBodyOpField,
)

from box_sdk_gen.managers.folder_classifications import (
    UpdateClassificationOnFolderRequestBodyPathField,
)

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

from test.commons import create_new_folder

from test.commons import get_or_create_classification_template

from test.commons import get_or_create_classification

from box_sdk_gen.schemas import ClassificationTemplate

client: BoxClient = get_default_client()


def get_or_create_second_classification(
    classification_template: ClassificationTemplate,
):
    classifications: List[ClassificationTemplateFieldsOptionsField] = (
        classification_template.fields[0].options
    )
    current_number_of_classifications: int = len(classifications)
    if current_number_of_classifications == 1:
        classification_template_with_new_classification: ClassificationTemplate = (
            client.classifications.add_classification(
                request_body=[
                    AddClassificationRequestBody(
                        op=AddClassificationRequestBodyOpField.ADDENUMOPTION.value,
                        field_key=AddClassificationRequestBodyFieldKeyField.BOX__SECURITY__CLASSIFICATION__KEY.value,
                        data=AddClassificationRequestBodyDataField(
                            key=get_uuid(),
                            static_config=AddClassificationRequestBodyDataStaticConfigField(
                                classification=AddClassificationRequestBodyDataStaticConfigClassificationField(
                                    color_id=4,
                                    classification_definition='Other description',
                                )
                            ),
                        ),
                    )
                ]
            )
        )
        return classification_template_with_new_classification.fields[0].options[1]
    return classifications[1]


def testFolderClassifications():
    classification_template: ClassificationTemplate = (
        get_or_create_classification_template()
    )
    classification = get_or_create_classification(classification_template)
    folder: FolderFull = create_new_folder()
    with pytest.raises(Exception):
        client.folder_classifications.get_classification_on_folder(folder_id=folder.id)
    created_folder_classification: Classification = (
        client.folder_classifications.add_classification_to_folder(
            folder_id=folder.id, box_security_classification_key=classification.key
        )
    )
    assert (
        created_folder_classification.box_security_classification_key
        == classification.key
    )
    folder_classification: Classification = (
        client.folder_classifications.get_classification_on_folder(folder_id=folder.id)
    )
    assert folder_classification.box_security_classification_key == classification.key
    second_classification = get_or_create_second_classification(classification_template)
    updated_folder_classification: Classification = (
        client.folder_classifications.update_classification_on_folder(
            folder_id=folder.id,
            request_body=[
                UpdateClassificationOnFolderRequestBody(
                    op=UpdateClassificationOnFolderRequestBodyOpField.REPLACE.value,
                    path=UpdateClassificationOnFolderRequestBodyPathField._BOX__SECURITY__CLASSIFICATION__KEY.value,
                    value=second_classification.key,
                )
            ],
        )
    )
    assert (
        updated_folder_classification.box_security_classification_key
        == second_classification.key
    )
    client.folder_classifications.delete_classification_from_folder(folder_id=folder.id)
    with pytest.raises(Exception):
        client.folder_classifications.get_classification_on_folder(folder_id=folder.id)
    client.folders.delete_folder_by_id(folder_id=folder.id)
