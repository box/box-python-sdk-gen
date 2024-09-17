from typing import Union

from box_sdk_gen.client import BoxClient

from box_sdk_gen.managers.ai import GetAiAgentDefaultConfigMode

from box_sdk_gen.schemas.file_full import FileFull

from box_sdk_gen.schemas.ai_response_full import AiResponseFull

from box_sdk_gen.managers.ai import CreateAiAskMode

from box_sdk_gen.schemas.ai_item_base import AiItemBase

from box_sdk_gen.schemas.ai_item_base import AiItemBaseTypeField

from box_sdk_gen.schemas.ai_response import AiResponse

from box_sdk_gen.managers.ai import CreateAiTextGenItems

from box_sdk_gen.managers.ai import CreateAiTextGenItemsTypeField

from box_sdk_gen.schemas.ai_dialogue_history import AiDialogueHistory

from box_sdk_gen.schemas.files import Files

from box_sdk_gen.managers.uploads import UploadFileAttributes

from box_sdk_gen.managers.uploads import UploadFileAttributesParentField

from box_sdk_gen.schemas.ai_extract_response import AiExtractResponse

from box_sdk_gen.managers.ai import CreateAiExtractStructuredFields

from box_sdk_gen.schemas.metadata_template import MetadataTemplate

from box_sdk_gen.managers.metadata_templates import CreateMetadataTemplateFields

from box_sdk_gen.managers.metadata_templates import (
    CreateMetadataTemplateFieldsTypeField,
)

from box_sdk_gen.managers.ai import CreateAiExtractStructuredMetadataTemplate

from box_sdk_gen.managers.metadata_templates import DeleteMetadataTemplateScope

from test.commons import get_default_client

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import string_to_byte_stream

from box_sdk_gen.internal.utils import delay_in_seconds

from box_sdk_gen.internal.utils import generate_byte_stream

from box_sdk_gen.internal.utils import date_time_from_string

from box_sdk_gen.internal.utils import date_time_to_string

from test.commons import upload_new_file

from box_sdk_gen.schemas.ai_agent_ask import AiAgentAsk

from box_sdk_gen.schemas.ai_agent_text_gen import AiAgentTextGen

from box_sdk_gen.schemas.ai_agent_extract import AiAgentExtract

from box_sdk_gen.schemas.ai_agent_extract_structured import AiAgentExtractStructured

client: BoxClient = get_default_client()


def testAskAISingleItem():
    ai_ask_agent_config: AiAgentAsk = client.ai.get_ai_agent_default_config(
        GetAiAgentDefaultConfigMode.ASK.value, language='en-US'
    )
    file_to_ask: FileFull = upload_new_file()
    response: AiResponseFull = client.ai.create_ai_ask(
        CreateAiAskMode.SINGLE_ITEM_QA.value,
        'which direction sun rises',
        [
            AiItemBase(
                id=file_to_ask.id,
                type=AiItemBaseTypeField.FILE.value,
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
    response: AiResponseFull = client.ai.create_ai_ask(
        CreateAiAskMode.MULTIPLE_ITEM_QA.value,
        'Which direction sun rises?',
        [
            AiItemBase(
                id=file_to_ask_1.id,
                type=AiItemBaseTypeField.FILE.value,
                content='Earth goes around the sun',
            ),
            AiItemBase(
                id=file_to_ask_2.id,
                type=AiItemBaseTypeField.FILE.value,
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
            AiDialogueHistory(
                prompt='What does the earth go around?',
                answer='The sun',
                created_at=date_time_from_string('2021-01-01T00:00:00Z'),
            ),
            AiDialogueHistory(
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
    ai_ask_config: Union[
        AiAgentAsk, AiAgentTextGen, AiAgentExtract, AiAgentExtractStructured
    ] = client.ai.get_ai_agent_default_config(
        GetAiAgentDefaultConfigMode.ASK.value, language='en-US'
    )
    assert ai_ask_config.type == 'ai_agent_ask'
    assert not ai_ask_config.basic_text.model == ''
    assert not ai_ask_config.basic_text.prompt_template == ''
    assert ai_ask_config.basic_text.num_tokens_for_completion > -1
    assert not ai_ask_config.basic_text.llm_endpoint_params == None
    assert not ai_ask_config.basic_text_multi.model == ''
    assert not ai_ask_config.basic_text_multi.prompt_template == ''
    assert ai_ask_config.basic_text_multi.num_tokens_for_completion > -1
    assert not ai_ask_config.basic_text_multi.llm_endpoint_params == None
    assert not ai_ask_config.long_text.model == ''
    assert not ai_ask_config.long_text.prompt_template == ''
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
    ai_text_gen_config: Union[
        AiAgentAsk, AiAgentTextGen, AiAgentExtract, AiAgentExtractStructured
    ] = client.ai.get_ai_agent_default_config(
        GetAiAgentDefaultConfigMode.TEXT_GEN.value, language='en-US'
    )
    assert ai_text_gen_config.type == 'ai_agent_text_gen'
    assert not ai_text_gen_config.basic_gen.llm_endpoint_params == None
    assert not ai_text_gen_config.basic_gen.model == ''
    assert not ai_text_gen_config.basic_gen.prompt_template == ''
    assert ai_text_gen_config.basic_gen.num_tokens_for_completion > -1
    assert not ai_text_gen_config.basic_gen.content_template == ''
    assert not ai_text_gen_config.basic_gen.embeddings.model == ''
    assert not ai_text_gen_config.basic_gen.embeddings.strategy.id == ''


def testAIExtract():
    ai_extract_agent_config: AiAgentExtract = client.ai.get_ai_agent_default_config(
        GetAiAgentDefaultConfigMode.EXTRACT.value, language='en-US'
    )
    uploaded_files: Files = client.uploads.upload_file(
        UploadFileAttributes(
            name=''.join([get_uuid(), '.txt']),
            parent=UploadFileAttributesParentField(id='0'),
        ),
        string_to_byte_stream(
            'My name is John Doe. I live in San Francisco. I was born in 1990. I work at Box.'
        ),
    )
    file: FileFull = uploaded_files.entries[0]
    delay_in_seconds(1)
    response: AiResponse = client.ai.create_ai_extract(
        'firstName, lastName, location, yearOfBirth, company',
        [AiItemBase(id=file.id)],
        ai_agent=ai_extract_agent_config,
    )
    expected_response: str = (
        '{"firstName": "John", "lastName": "Doe", "location": "San Francisco", "yearOfBirth": "1990", "company": "Box"}'
    )
    assert response.answer == expected_response
    assert response.completion_reason == 'done'
    client.files.delete_file_by_id(file.id)


def testAIExtractStructuredWithFields():
    ai_extract_structured_agent_config: AiAgentExtractStructured = (
        client.ai.get_ai_agent_default_config(
            GetAiAgentDefaultConfigMode.EXTRACT_STRUCTURED.value, language='en-US'
        )
    )
    uploaded_files: Files = client.uploads.upload_file(
        UploadFileAttributes(
            name=''.join([get_uuid(), '.txt']),
            parent=UploadFileAttributesParentField(id='0'),
        ),
        string_to_byte_stream(
            'My name is John Doe. I was born in 4th July 1990. I am 34 years old. My hobby is guitar and books.'
        ),
    )
    file: FileFull = uploaded_files.entries[0]
    delay_in_seconds(1)
    response: AiExtractResponse = client.ai.create_ai_extract_structured(
        [AiItemBase(id=file.id)],
        fields=[
            CreateAiExtractStructuredFields(
                key='firstName',
                display_name='First name',
                description='Person first name',
                prompt='What is the your first name?',
                type='string',
            ),
            CreateAiExtractStructuredFields(
                key='lastName',
                display_name='Last name',
                description='Person last name',
                prompt='What is the your last name?',
                type='string',
            ),
            CreateAiExtractStructuredFields(
                key='dateOfBirth',
                display_name='Birth date',
                description='Person date of birth',
                prompt='What is the date of your birth?',
                type='date',
            ),
            CreateAiExtractStructuredFields(
                key='age',
                display_name='Age',
                description='Person age',
                prompt='How old are you?',
                type='float',
            ),
            CreateAiExtractStructuredFields(
                key='hobby',
                display_name='Hobby',
                description='Person hobby',
                prompt='What is your hobby?',
                type='multiSelect',
            ),
        ],
        ai_agent=ai_extract_structured_agent_config,
    )
    assert response.firstName == 'John'
    assert response.lastName == 'Doe'
    assert response.dateOfBirth == '1990-07-04'
    assert response.age == 34
    assert response.hobby == ['guitar', 'books']
    client.files.delete_file_by_id(file.id)


def testAIExtractStructuredWithMetadataTemplate():
    uploaded_files: Files = client.uploads.upload_file(
        UploadFileAttributes(
            name=''.join([get_uuid(), '.txt']),
            parent=UploadFileAttributesParentField(id='0'),
        ),
        string_to_byte_stream(
            'My name is John Doe. I was born in 4th July 1990. I am 34 years old. My hobby is guitar and books.'
        ),
    )
    file: FileFull = uploaded_files.entries[0]
    template_key: str = ''.join(['key', get_uuid()])
    template: MetadataTemplate = client.metadata_templates.create_metadata_template(
        'enterprise',
        template_key,
        template_key=template_key,
        fields=[
            CreateMetadataTemplateFields(
                key='firstName',
                display_name='First name',
                description='Person first name',
                type=CreateMetadataTemplateFieldsTypeField.STRING.value,
            ),
            CreateMetadataTemplateFields(
                key='lastName',
                display_name='Last name',
                description='Person last name',
                type=CreateMetadataTemplateFieldsTypeField.STRING.value,
            ),
            CreateMetadataTemplateFields(
                key='dateOfBirth',
                display_name='Birth date',
                description='Person date of birth',
                type=CreateMetadataTemplateFieldsTypeField.DATE.value,
            ),
            CreateMetadataTemplateFields(
                key='age',
                display_name='Age',
                description='Person age',
                type=CreateMetadataTemplateFieldsTypeField.FLOAT.value,
            ),
            CreateMetadataTemplateFields(
                key='hobby',
                display_name='Hobby',
                description='Person hobby',
                type=CreateMetadataTemplateFieldsTypeField.MULTISELECT.value,
            ),
        ],
    )
    response: AiExtractResponse = client.ai.create_ai_extract_structured(
        [AiItemBase(id=file.id)],
        metadata_template=CreateAiExtractStructuredMetadataTemplate(
            template_key=template_key, scope='enterprise'
        ),
    )
    assert response.firstName == 'John'
    assert response.lastName == 'Doe'
    assert response.dateOfBirth == '1990-07-04'
    assert response.age == 34
    assert response.hobby == ['guitar', 'books']
    client.metadata_templates.delete_metadata_template(
        DeleteMetadataTemplateScope.ENTERPRISE.value, template.template_key
    )
    client.files.delete_file_by_id(file.id)
