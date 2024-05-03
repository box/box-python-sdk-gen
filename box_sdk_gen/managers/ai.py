from enum import Enum

from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject

from typing import List

from typing import Dict

from box_sdk_gen.serialization.json.serializer import serialize

from box_sdk_gen.serialization.json.serializer import deserialize

from box_sdk_gen.internal.utils import DateTime

from box_sdk_gen.schemas import AiResponse

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import AiAsk

from box_sdk_gen.schemas import AiTextGen

from box_sdk_gen.networking.auth import Authentication

from box_sdk_gen.networking.network import NetworkSession

from box_sdk_gen.internal.utils import prepare_params

from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.internal.utils import ByteStream

from box_sdk_gen.networking.fetch import FetchOptions

from box_sdk_gen.networking.fetch import FetchResponse

from box_sdk_gen.networking.fetch import fetch

from box_sdk_gen.serialization.json.json_data import SerializedData


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
        :param id: The id of the item
        :type id: str
        :param type: The type of the item, defaults to CreateAiAskItemsTypeField.FILE.value
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
        *,
        id: Optional[str] = None,
        type: Optional[CreateAiTextGenItemsTypeField] = None,
        content: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The id of the item., defaults to None
        :type id: Optional[str], optional
        :param type: The type of the item., defaults to None
        :type type: Optional[CreateAiTextGenItemsTypeField], optional
        :param content: The content to use as context for generating new text or editing existing text., defaults to None
        :type content: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.content = content


class CreateAiTextGenDialogueHistory(BaseObject):
    def __init__(
        self,
        *,
        prompt: Optional[str] = None,
        answer: Optional[str] = None,
        created_at: Optional[DateTime] = None,
        **kwargs
    ):
        """
        :param prompt: The prompt previously provided by the client and answered by the LLM., defaults to None
        :type prompt: Optional[str], optional
        :param answer: The answer previously provided by the LLM., defaults to None
        :type answer: Optional[str], optional
        :param created_at: The ISO date formatted timestamp of when the previous answer to the prompt was created., defaults to None
        :type created_at: Optional[DateTime], optional
        """
        super().__init__(**kwargs)
        self.prompt = prompt
        self.answer = answer
        self.created_at = created_at


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
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> AiResponse:
        """
        Sends an AI request to supported LLMs and returns an answer specifically focused on the user's question given the provided context.
        :param mode: The mode specifies if this request is for a single or multiple items.
        :type mode: CreateAiAskMode
        :param prompt: The prompt provided by the client to be answered by the LLM.
        :type prompt: str
        :param items: The items to be processed by the LLM, often files.
        :type items: List[CreateAiAskItems]
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'mode': mode, 'prompt': prompt, 'items': items}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([self.network_session.base_urls.base_url, '/ai/ask']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, AiResponse)

    def create_ai_text_gen(
        self,
        prompt: str,
        items: List[CreateAiTextGenItems],
        *,
        dialogue_history: Optional[List[CreateAiTextGenDialogueHistory]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> AiResponse:
        """
        Sends an AI request to supported LLMs and returns an answer specifically focused on the creation of new text.
        :param prompt: The prompt provided by the client to be answered by the LLM.
        :type prompt: str
        :param items: The items to be processed by the LLM, often files.
        :type items: List[CreateAiTextGenItems]
        :param dialogue_history: The history of prompts and answers previously passed to the LLM. This provides additional context to the LLM in generating the response., defaults to None
        :type dialogue_history: Optional[List[CreateAiTextGenDialogueHistory]], optional
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'prompt': prompt,
            'items': items,
            'dialogue_history': dialogue_history,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([self.network_session.base_urls.base_url, '/ai/text_gen']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, AiResponse)
