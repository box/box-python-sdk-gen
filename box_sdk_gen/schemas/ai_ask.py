from enum import Enum

from typing import List

from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.ai_item_base import AiItemBase

from box_sdk_gen.schemas.ai_dialogue_history import AiDialogueHistory

from box_sdk_gen.schemas.ai_agent_ask import AiAgentAsk

from box_sdk_gen.box.errors import BoxSDKError


class AiAskModeField(str, Enum):
    MULTIPLE_ITEM_QA = 'multiple_item_qa'
    SINGLE_ITEM_QA = 'single_item_qa'


class AiAsk(BaseObject):
    def __init__(
        self,
        mode: AiAskModeField,
        prompt: str,
        items: List[AiItemBase],
        *,
        dialogue_history: Optional[List[AiDialogueHistory]] = None,
        include_citations: Optional[bool] = None,
        ai_agent: Optional[AiAgentAsk] = None,
        **kwargs
    ):
        """
                :param mode: The mode specifies if this request is for a single or multiple items. If you select `single_item_qa` the `items` array can have one element only. Selecting `multiple_item_qa` allows you to provide up to 25 items.
                :type mode: AiAskModeField
                :param prompt: The prompt provided by the client to be answered by the LLM. The prompt's length is limited to 10000 characters.
                :type prompt: str
                :param items: The items to be processed by the LLM, often files.

        **Note**: Box AI handles documents with text representations up to 1MB in size, or a maximum of 25 files, whichever comes first.
        If the file size exceeds 1MB, the first 1MB of text representation will be processed.
        If you set `mode` parameter to `single_item_qa`, the `items` array can have one element only.
                :type items: List[AiItemBase]
                :param dialogue_history: The history of prompts and answers previously passed to the LLM. This provides additional context to the LLM in generating the response., defaults to None
                :type dialogue_history: Optional[List[AiDialogueHistory]], optional
                :param include_citations: A flag to indicate whether citations should be returned., defaults to None
                :type include_citations: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.mode = mode
        self.prompt = prompt
        self.items = items
        self.dialogue_history = dialogue_history
        self.include_citations = include_citations
        self.ai_agent = ai_agent
