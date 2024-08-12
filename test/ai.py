from typing import Union

from box_sdk_gen.client import BoxClient

from box_sdk_gen.managers.ai import GetAiAgentDefaultConfigMode

from box_sdk_gen.schemas.file_full import FileFull

from box_sdk_gen.schemas.ai_response import AiResponse

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

from box_sdk_gen.schemas.ai_agent_ask import AiAgentAsk

from box_sdk_gen.schemas.ai_agent_text_gen import AiAgentTextGen

client: BoxClient = get_default_client()


def testAskAISingleItem():
    ai_ask_agent_config: AiAgentAsk = client.ai.get_ai_agent_default_config(
        GetAiAgentDefaultConfigMode.ASK.value, language='en-US'
    )
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
        ai_agent=ai_ask_agent_config,
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
    ai_text_gen_agent_config: AiAgentTextGen = client.ai.get_ai_agent_default_config(
        GetAiAgentDefaultConfigMode.TEXT_GEN.value, language='en-US'
    )
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
        ai_agent=ai_text_gen_agent_config,
    )
    assert 'sun' in response.answer
    assert response.completion_reason == 'done'
    client.files.delete_file_by_id(file_to_ask.id)


def testGettingAIAskAgentConfig():
    ai_ask_config: Union[AiAgentAsk, AiAgentTextGen] = (
        client.ai.get_ai_agent_default_config(
            GetAiAgentDefaultConfigMode.ASK.value, language='en-US'
        )
    )
    assert ai_ask_config.type == 'ai_agent_ask'
    assert not ai_ask_config.basic_text.model == ''
    assert not ai_ask_config.basic_text.prompt_template == ''
    assert not ai_ask_config.basic_text.system_message == ''
    assert ai_ask_config.basic_text.num_tokens_for_completion > -1
    assert not ai_ask_config.basic_text.llm_endpoint_params == None
    assert not ai_ask_config.basic_text_multi.model == ''
    assert not ai_ask_config.basic_text_multi.prompt_template == ''
    assert ai_ask_config.basic_text_multi.num_tokens_for_completion > -1
    assert not ai_ask_config.basic_text_multi.llm_endpoint_params == None
    assert not ai_ask_config.long_text.model == ''
    assert not ai_ask_config.long_text.prompt_template == ''
    assert not ai_ask_config.long_text.system_message == ''
    assert ai_ask_config.long_text.num_tokens_for_completion > -1
    assert not ai_ask_config.long_text.embeddings.model == ''
    assert not ai_ask_config.long_text.embeddings.strategy.id == ''
    assert not ai_ask_config.long_text.llm_endpoint_params == None
    assert not ai_ask_config.long_text_multi.model == ''
    assert not ai_ask_config.long_text_multi.prompt_template == ''
    assert ai_ask_config.long_text_multi.num_tokens_for_completion > -1
    assert not ai_ask_config.long_text_multi.embeddings.model == ''
    assert not ai_ask_config.long_text_multi.embeddings.strategy.id == ''
    assert not ai_ask_config.long_text_multi.llm_endpoint_params == None


def testGettingAITextGenAgentConfig():
    ai_text_gen_config: Union[AiAgentAsk, AiAgentTextGen] = (
        client.ai.get_ai_agent_default_config(
            GetAiAgentDefaultConfigMode.TEXT_GEN.value, language='en-US'
        )
    )
    assert ai_text_gen_config.type == 'ai_agent_text_gen'
    assert not ai_text_gen_config.basic_gen.llm_endpoint_params == None
    assert not ai_text_gen_config.basic_gen.model == ''
    assert not ai_text_gen_config.basic_gen.prompt_template == ''
    assert not ai_text_gen_config.basic_gen.system_message == ''
    assert ai_text_gen_config.basic_gen.num_tokens_for_completion > -1
    assert not ai_text_gen_config.basic_gen.content_template == ''
    assert not ai_text_gen_config.basic_gen.embeddings.model == ''
    assert not ai_text_gen_config.basic_gen.embeddings.strategy.id == ''
