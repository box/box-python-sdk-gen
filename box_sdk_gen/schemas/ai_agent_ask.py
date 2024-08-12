from enum import Enum

from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.ai_agent_long_text_tool import AiAgentLongTextTool

from box_sdk_gen.schemas.ai_agent_basic_text_tool_ask import AiAgentBasicTextToolAsk


class AiAgentAskTypeField(str, Enum):
    AI_AGENT_ASK = 'ai_agent_ask'


class AiAgentAsk(BaseObject):
    _discriminator = 'type', {'ai_agent_ask'}

    def __init__(
        self,
        *,
        type: Optional[AiAgentAskTypeField] = None,
        long_text: Optional[AiAgentLongTextTool] = None,
        basic_text: Optional[AiAgentBasicTextToolAsk] = None,
        long_text_multi: Optional[AiAgentLongTextTool] = None,
        basic_text_multi: Optional[AiAgentBasicTextToolAsk] = None,
        **kwargs
    ):
        """
        :param type: The type of AI agent used to handle queries., defaults to None
        :type type: Optional[AiAgentAskTypeField], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.long_text = long_text
        self.basic_text = basic_text
        self.long_text_multi = long_text_multi
        self.basic_text_multi = basic_text_multi
