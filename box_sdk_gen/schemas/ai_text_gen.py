from enum import Enum

from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject

from typing import List

from box_sdk_gen.schemas.ai_agent_text_gen import AiAgentTextGen

from box_sdk_gen.internal.utils import DateTime


class AiTextGenItemsTypeField(str, Enum):
    FILE = 'file'


class AiTextGenItemsField(BaseObject):
    _discriminator = 'type', {'file'}

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        type: Optional[AiTextGenItemsTypeField] = None,
        content: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The id of the item., defaults to None
        :type id: Optional[str], optional
        :param type: The type of the item., defaults to None
        :type type: Optional[AiTextGenItemsTypeField], optional
        :param content: The content to use as context for generating new text or editing existing text., defaults to None
        :type content: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.content = content


class AiTextGenDialogueHistoryField(BaseObject):
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


class AiTextGen(BaseObject):
    def __init__(
        self,
        prompt: str,
        items: List[AiTextGenItemsField],
        *,
        dialogue_history: Optional[List[AiTextGenDialogueHistoryField]] = None,
        ai_agent: Optional[AiAgentTextGen] = None,
        **kwargs
    ):
        """
                :param prompt: The prompt provided by the client to be answered by the LLM. The prompt's length is limited to 10000 characters.
                :type prompt: str
                :param items: The items to be processed by the LLM, often files.
        The array can include **exactly one** element.

        **Note**: Box AI handles documents with text representations up to 1MB in size.
        If the file size exceeds 1MB, the first 1MB of text representation will be processed.
                :type items: List[AiTextGenItemsField]
                :param dialogue_history: The history of prompts and answers previously passed to the LLM. This provides additional context to the LLM in generating the response., defaults to None
                :type dialogue_history: Optional[List[AiTextGenDialogueHistoryField]], optional
        """
        super().__init__(**kwargs)
        self.prompt = prompt
        self.items = items
        self.dialogue_history = dialogue_history
        self.ai_agent = ai_agent
