from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.schemas import AiResponse

from box_sdk_gen.managers.ai import CreateAiAskMode

from box_sdk_gen.managers.ai import CreateAiAskItems

from box_sdk_gen.managers.ai import CreateAiAskItemsTypeField

from box_sdk_gen.managers.ai import CreateAiTextGenItems

from box_sdk_gen.managers.ai import CreateAiTextGenItemsTypeField

from box_sdk_gen.managers.ai import CreateAiTextGenDialogueHistory

from test.commons import get_default_client

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import generate_byte_stream

from box_sdk_gen.internal.utils import date_time_from_string

from box_sdk_gen.internal.utils import date_time_to_string

from test.commons import upload_new_file

client: BoxClient = get_default_client()


def testAskAISingleItem():
    file_to_ask: FileFull = upload_new_file()
    response: AiResponse = client.ai.create_ai_ask(
        CreateAiAskMode.SINGLE_ITEM_QA.value,
        'which direction sun rises',
        [
            CreateAiAskItems(
                id=file_to_ask.id,
                type=CreateAiAskItemsTypeField.FILE.value,
                content='Sun rises in the East',
            )
        ],
    )
    assert 'East' in response.answer
    assert response.completion_reason == 'done'
    client.files.delete_file_by_id(file_to_ask.id)


def testAskAIMultipleItems():
    file_to_ask_1: FileFull = upload_new_file()
    file_to_ask_2: FileFull = upload_new_file()
    response: AiResponse = client.ai.create_ai_ask(
        CreateAiAskMode.MULTIPLE_ITEM_QA.value,
        'Which direction sun rises?',
        [
            CreateAiAskItems(
                id=file_to_ask_1.id,
                type=CreateAiAskItemsTypeField.FILE.value,
                content='Earth goes around the sun',
            ),
            CreateAiAskItems(
                id=file_to_ask_2.id,
                type=CreateAiAskItemsTypeField.FILE.value,
                content='Sun rises in the East in the morning',
            ),
        ],
    )
    assert 'East' in response.answer
    assert response.completion_reason == 'done'
    client.files.delete_file_by_id(file_to_ask_1.id)
    client.files.delete_file_by_id(file_to_ask_2.id)


def testAITextGenWithDialogueHistory():
    file_to_ask: FileFull = upload_new_file()
    response: AiResponse = client.ai.create_ai_text_gen(
        'Parapharse the document.s',
        [
            CreateAiTextGenItems(
                id=file_to_ask.id,
                type=CreateAiTextGenItemsTypeField.FILE.value,
                content='The Earth goes around the sun. Sun rises in the East in the morning.',
            )
        ],
        dialogue_history=[
            CreateAiTextGenDialogueHistory(
                prompt='What does the earth go around?',
                answer='The sun',
                created_at=date_time_from_string('2021-01-01T00:00:00Z'),
            ),
            CreateAiTextGenDialogueHistory(
                prompt='On Earth, where does the sun rise?',
                answer='East',
                created_at=date_time_from_string('2021-01-01T00:00:00Z'),
            ),
        ],
    )
    assert 'sun' in response.answer
    assert response.completion_reason == 'done'
    client.files.delete_file_by_id(file_to_ask.id)
