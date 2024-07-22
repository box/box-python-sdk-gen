from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject

from typing import Union

from box_sdk_gen.schemas.ai_llm_endpoint_params_open_ai import AiLlmEndpointParamsOpenAi

from box_sdk_gen.schemas.ai_llm_endpoint_params_google import AiLlmEndpointParamsGoogle

from box_sdk_gen.schemas.ai_agent_basic_text_tool_text_gen import (
    AiAgentBasicTextToolTextGen,
)


class AiAgentLongTextToolEmbeddingsStrategyField(BaseObject):
    def __init__(
        self,
        *,
        id: Optional[str] = None,
        num_tokens_per_chunk: Optional[int] = None,
        **kwargs
    ):
        """
        :param id: The strategy used for the AI Agent for calculating embeddings., defaults to None
        :type id: Optional[str], optional
        :param num_tokens_per_chunk: The number of tokens per chunk., defaults to None
        :type num_tokens_per_chunk: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.num_tokens_per_chunk = num_tokens_per_chunk


class AiAgentLongTextToolEmbeddingsField(BaseObject):
    def __init__(
        self,
        *,
        model: Optional[str] = None,
        strategy: Optional[AiAgentLongTextToolEmbeddingsStrategyField] = None,
        **kwargs
    ):
        """
        :param model: The model used for the AI Agent for calculating embeddings., defaults to None
        :type model: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.model = model
        self.strategy = strategy


class AiAgentLongTextTool(AiAgentBasicTextToolTextGen):
    def __init__(
        self,
        *,
        embeddings: Optional[AiAgentLongTextToolEmbeddingsField] = None,
        model: Optional[str] = None,
        system_message: Optional[str] = None,
        prompt_template: Optional[str] = None,
        num_tokens_for_completion: Optional[int] = None,
        llm_endpoint_params: Optional[
            Union[AiLlmEndpointParamsOpenAi, AiLlmEndpointParamsGoogle]
        ] = None,
        **kwargs
    ):
        """
                :param model: The model to be used for the AI Agent for basic text., defaults to None
                :type model: Optional[str], optional
                :param system_message: System messages try to help the LLM "understand" its role and what it is supposed to do.
        This parameter requires using `{current_date}`., defaults to None
                :type system_message: Optional[str], optional
                :param prompt_template: The prompt template contains contextual information of the request and the user prompt.

        When using the `prompt_template` parameter, you **must include** input for `{user_question}`.
        Inputs for  `{current_date}` and`{content}` are optional, depending on the use., defaults to None
                :type prompt_template: Optional[str], optional
                :param num_tokens_for_completion: The number of tokens for completion., defaults to None
                :type num_tokens_for_completion: Optional[int], optional
        """
        super().__init__(
            model=model,
            system_message=system_message,
            prompt_template=prompt_template,
            num_tokens_for_completion=num_tokens_for_completion,
            llm_endpoint_params=llm_endpoint_params,
            **kwargs
        )
        self.embeddings = embeddings
