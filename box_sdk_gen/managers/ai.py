from enum import Enum

from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject

from typing import List

from typing import Dict

from box_sdk_gen.serialization.json.serializer import serialize

from box_sdk_gen.serialization.json.serializer import deserialize

from box_sdk_gen.internal.utils import to_string

from typing import Union

from box_sdk_gen.schemas.ai_dialogue_history import AiDialogueHistory

from box_sdk_gen.schemas.ai_response_full import AiResponseFull

from box_sdk_gen.schemas.client_error import ClientError

from box_sdk_gen.schemas.ai_ask import AiAsk

from box_sdk_gen.schemas.ai_response import AiResponse

from box_sdk_gen.schemas.ai_text_gen import AiTextGen

from box_sdk_gen.schemas.ai_agent_ask import AiAgentAsk

from box_sdk_gen.schemas.ai_agent_text_gen import AiAgentTextGen

from box_sdk_gen.networking.auth import Authentication

from box_sdk_gen.networking.network import NetworkSession

from box_sdk_gen.internal.utils import prepare_params

from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.internal.utils import ByteStream

from box_sdk_gen.networking.fetch import FetchOptions

from box_sdk_gen.networking.fetch import FetchResponse

from box_sdk_gen.networking.fetch import fetch

from box_sdk_gen.serialization.json.json_data import SerializedData

from box_sdk_gen.serialization.json.json_data import sd_to_json


class CreateAiAskMode(str, Enum):
    MULTIPLE_ITEM_QA = 'multiple_item_qa'
    SINGLE_ITEM_QA = 'single_item_qa'


class CreateAiAskItemsTypeField(str, Enum):
    FILE = 'file'


class CreateAiAskItems(BaseObject):
    _discriminator = 'type', {'file'}

    def __init__(
        self,
        id: str,
        *,
        type: CreateAiAskItemsTypeField = CreateAiAskItemsTypeField.FILE.value,
        content: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The id of the item.
        :type id: str
        :param type: The type of the item., defaults to CreateAiAskItemsTypeField.FILE.value
        :type type: CreateAiAskItemsTypeField, optional
        :param content: The content of the item, often the text representation., defaults to None
        :type content: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.content = content


class CreateAiTextGenItemsTypeField(str, Enum):
    FILE = 'file'


class CreateAiTextGenItems(BaseObject):
    _discriminator = 'type', {'file'}

    def __init__(
        self,
        id: str,
        *,
        type: CreateAiTextGenItemsTypeField = CreateAiTextGenItemsTypeField.FILE.value,
        content: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The ID of the item.
        :type id: str
        :param type: The type of the item., defaults to CreateAiTextGenItemsTypeField.FILE.value
        :type type: CreateAiTextGenItemsTypeField, optional
        :param content: The content to use as context for generating new text or editing existing text., defaults to None
        :type content: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.content = content


class GetAiAgentDefaultConfigMode(str, Enum):
    ASK = 'ask'
    TEXT_GEN = 'text_gen'


class AiManager:
    def __init__(
        self,
        *,
        auth: Optional[Authentication] = None,
        network_session: NetworkSession = None
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session

    def create_ai_ask(
        self,
        mode: CreateAiAskMode,
        prompt: str,
        items: List[CreateAiAskItems],
        *,
        dialogue_history: Optional[List[AiDialogueHistory]] = None,
        include_citations: Optional[bool] = None,
        ai_agent: Optional[AiAgentAsk] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> AiResponseFull:
        """
                Sends an AI request to supported LLMs and returns an answer specifically focused on the user's question given the provided context.
                :param mode: The mode specifies if this request is for a single or multiple items. If you select `single_item_qa` the `items` array can have one element only. Selecting `multiple_item_qa` allows you to provide up to 25 items.
                :type mode: CreateAiAskMode
                :param prompt: The prompt provided by the client to be answered by the LLM. The prompt's length is limited to 10000 characters.
                :type prompt: str
                :param items: The items to be processed by the LLM, often files.

        **Note**: Box AI handles documents with text representations up to 1MB in size, or a maximum of 25 files, whichever comes first.
        If the file size exceeds 1MB, the first 1MB of text representation will be processed.
        If you set `mode` parameter to `single_item_qa`, the `items` array can have one element only.
                :type items: List[CreateAiAskItems]
                :param dialogue_history: The history of prompts and answers previously passed to the LLM. This provides additional context to the LLM in generating the response., defaults to None
                :type dialogue_history: Optional[List[AiDialogueHistory]], optional
                :param include_citations: A flag to indicate whether citations should be returned., defaults to None
                :type include_citations: Optional[bool], optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'mode': mode,
            'prompt': prompt,
            'items': items,
            'dialogue_history': dialogue_history,
            'include_citations': include_citations,
            'ai_agent': ai_agent,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            FetchOptions(
                url=''.join([self.network_session.base_urls.base_url, '/2.0/ai/ask']),
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            )
        )
        return deserialize(response.data, AiResponseFull)

    def create_ai_text_gen(
        self,
        prompt: str,
        items: List[CreateAiTextGenItems],
        *,
        dialogue_history: Optional[List[AiDialogueHistory]] = None,
        ai_agent: Optional[AiAgentTextGen] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> AiResponse:
        """
                Sends an AI request to supported LLMs and returns an answer specifically focused on the creation of new text.
                :param prompt: The prompt provided by the client to be answered by the LLM. The prompt's length is limited to 10000 characters.
                :type prompt: str
                :param items: The items to be processed by the LLM, often files.
        The array can include **exactly one** element.

        **Note**: Box AI handles documents with text representations up to 1MB in size.
        If the file size exceeds 1MB, the first 1MB of text representation will be processed.
                :type items: List[CreateAiTextGenItems]
                :param dialogue_history: The history of prompts and answers previously passed to the LLM. This parameter provides the additional context to the LLM when generating the response., defaults to None
                :type dialogue_history: Optional[List[AiDialogueHistory]], optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'prompt': prompt,
            'items': items,
            'dialogue_history': dialogue_history,
            'ai_agent': ai_agent,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            FetchOptions(
                url=''.join(
                    [self.network_session.base_urls.base_url, '/2.0/ai/text_gen']
                ),
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            )
        )
        return deserialize(response.data, AiResponse)

    def get_ai_agent_default_config(
        self,
        mode: GetAiAgentDefaultConfigMode,
        *,
        language: Optional[str] = None,
        model: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> Union[AiAgentAsk, AiAgentTextGen]:
        """
                Get the AI agent default config
                :param mode: The mode to filter the agent config to return.
                :type mode: GetAiAgentDefaultConfigMode
                :param language: The ISO language code to return the agent config for.
        If the language is not supported the default agent config is returned., defaults to None
                :type language: Optional[str], optional
                :param model: The model to return the default agent config for., defaults to None
                :type model: Optional[str], optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {
                'mode': to_string(mode),
                'language': to_string(language),
                'model': to_string(model),
            }
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            FetchOptions(
                url=''.join(
                    [self.network_session.base_urls.base_url, '/2.0/ai_agent_default']
                ),
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            )
        )
        return deserialize(response.data, Union[AiAgentAsk, AiAgentTextGen])
