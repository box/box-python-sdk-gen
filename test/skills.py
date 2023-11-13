from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import File

from box_sdk_gen.schemas import SkillCardsMetadata

from box_sdk_gen.schemas import KeywordSkillCardTypeField

from box_sdk_gen.schemas import KeywordSkillCardSkillCardTypeField

from box_sdk_gen.schemas import KeywordSkillCardSkillCardTitleField

from box_sdk_gen.schemas import KeywordSkillCardSkillField

from box_sdk_gen.schemas import KeywordSkillCardSkillFieldTypeField

from box_sdk_gen.schemas import KeywordSkillCardInvocationField

from box_sdk_gen.schemas import KeywordSkillCardInvocationFieldTypeField

from box_sdk_gen.schemas import KeywordSkillCardEntriesField

from box_sdk_gen.managers.skills import (
    UpdateFileMetadataGlobalBoxSkillsCardRequestBodyArg,
)

from box_sdk_gen.managers.skills import (
    UpdateFileMetadataGlobalBoxSkillsCardRequestBodyArgOpField,
)

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

from test.commons import upload_new_file

from box_sdk_gen.schemas import KeywordSkillCard

client: BoxClient = get_default_client()


def test_skills_cards_CRUD():
    file: File = upload_new_file()
    skill_id: str = get_uuid()
    invocation_id: str = get_uuid()
    title_message: str = 'License Plates'
    skill_cards_metadata: SkillCardsMetadata = (
        client.skills.create_file_metadata_global_box_skills_card(
            file_id=file.id,
            cards=[
                KeywordSkillCard(
                    type=KeywordSkillCardTypeField.SKILL_CARD.value,
                    skill_card_type=KeywordSkillCardSkillCardTypeField.KEYWORD.value,
                    skill_card_title=KeywordSkillCardSkillCardTitleField(
                        code='license-plates', message=title_message
                    ),
                    skill=KeywordSkillCardSkillField(
                        id=skill_id,
                        type=KeywordSkillCardSkillFieldTypeField.SERVICE.value,
                    ),
                    invocation=KeywordSkillCardInvocationField(
                        id=invocation_id,
                        type=KeywordSkillCardInvocationFieldTypeField.SKILL_INVOCATION.value,
                    ),
                    entries=[KeywordSkillCardEntriesField(text='DN86 BOX')],
                )
            ],
        )
    )
    assert len(skill_cards_metadata.cards) == 1
    assert skill_cards_metadata.cards[0].skill.id == skill_id
    assert skill_cards_metadata.cards[0].skill_card_title.message == title_message
    updated_title_message: str = 'Updated License Plates'
    updated_skill_cards_metadata: SkillCardsMetadata = (
        client.skills.update_file_metadata_global_box_skills_card(
            file_id=file.id,
            request_body=[
                UpdateFileMetadataGlobalBoxSkillsCardRequestBodyArg(
                    op=UpdateFileMetadataGlobalBoxSkillsCardRequestBodyArgOpField.REPLACE.value,
                    path='/cards/0',
                    value=KeywordSkillCard(
                        type=KeywordSkillCardTypeField.SKILL_CARD.value,
                        skill_card_type=KeywordSkillCardSkillCardTypeField.KEYWORD.value,
                        skill_card_title=KeywordSkillCardSkillCardTitleField(
                            code='license-plates', message=updated_title_message
                        ),
                        skill=KeywordSkillCardSkillField(
                            id=skill_id,
                            type=KeywordSkillCardSkillFieldTypeField.SERVICE.value,
                        ),
                        invocation=KeywordSkillCardInvocationField(
                            id=invocation_id,
                            type=KeywordSkillCardInvocationFieldTypeField.SKILL_INVOCATION.value,
                        ),
                        entries=[KeywordSkillCardEntriesField(text='DN86 BOX')],
                    ),
                )
            ],
        )
    )
    assert updated_skill_cards_metadata.cards[0].skill.id == skill_id
    assert (
        updated_skill_cards_metadata.cards[0].skill_card_title.message
        == updated_title_message
    )
    received_skill_cards_metadata: SkillCardsMetadata = (
        client.skills.get_file_metadata_global_box_skills_cards(file_id=file.id)
    )
    assert updated_skill_cards_metadata.cards[0].skill.id == skill_id
    client.skills.delete_file_metadata_global_box_skills_card(file_id=file.id)
    client.files.delete_file_by_id(file_id=file.id)
