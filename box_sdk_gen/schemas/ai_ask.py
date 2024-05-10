from enum import Enum

from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject

from typing import List


class AiAskModeField(str, Enum):
    MULTIPLE_ITEM_QA = 'multiple_item_qa'
    SINGLE_ITEM_QA = 'single_item_qa'


class AiAskItemsTypeField(str, Enum):
    FILE = 'file'


class AiAskItemsField(BaseObject):
    _discriminator = 'type', {'file'}

    def __init__(
        self,
        id: str,
        *,
        type: AiAskItemsTypeField = AiAskItemsTypeField.FILE.value,
        content: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The id of the item
        :type id: str
        :param type: The type of the item, defaults to AiAskItemsTypeField.FILE.value
        :type type: AiAskItemsTypeField, optional
        :param content: The content of the item, often the text representation., defaults to None
        :type content: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.content = content


class AiAsk(BaseObject):
    def __init__(
        self, mode: AiAskModeField, prompt: str, items: List[AiAskItemsField], **kwargs
    ):
        """
        :param mode: The mode specifies if this request is for a single or multiple items.
        :type mode: AiAskModeField
        :param prompt: The prompt provided by the client to be answered by the LLM.
        :type prompt: str
        :param items: The items to be processed by the LLM, often files.
        :type items: List[AiAskItemsField]
        """
        super().__init__(**kwargs)
        self.mode = mode
        self.prompt = prompt
        self.items = items
