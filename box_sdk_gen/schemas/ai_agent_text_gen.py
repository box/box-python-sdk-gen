from enum import Enum

from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.ai_agent_basic_gen_tool import AiAgentBasicGenTool


class AiAgentTextGenTypeField(str, Enum):
    AI_AGENT_TEXT_GEN = 'ai_agent_text_gen'


class AiAgentTextGen(BaseObject):
    _discriminator = 'type', {'ai_agent_text_gen'}

    def __init__(
        self,
        *,
        type: Optional[AiAgentTextGenTypeField] = None,
        basic_gen: Optional[AiAgentBasicGenTool] = None,
        **kwargs
    ):
        """
        :param type: The type of AI agent used for generating text., defaults to None
        :type type: Optional[AiAgentTextGenTypeField], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.basic_gen = basic_gen
