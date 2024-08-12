from typing import Optional

from typing import List

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.ai_citation import AiCitation

from box_sdk_gen.internal.utils import DateTime


class AiAskResponse(BaseObject):
    def __init__(
        self,
        answer: str,
        created_at: DateTime,
        *,
        completion_reason: Optional[str] = None,
        citations: Optional[List[AiCitation]] = None,
        **kwargs
    ):
        """
        :param answer: The answer provided by the LLM.
        :type answer: str
        :param created_at: The ISO date formatted timestamp of when the answer to the prompt was created.
        :type created_at: DateTime
        :param completion_reason: The reason the response finishes., defaults to None
        :type completion_reason: Optional[str], optional
        :param citations: The citations of the LLM's answer reference., defaults to None
        :type citations: Optional[List[AiCitation]], optional
        """
        super().__init__(**kwargs)
        self.answer = answer
        self.created_at = created_at
        self.completion_reason = completion_reason
        self.citations = citations