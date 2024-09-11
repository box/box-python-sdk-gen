from typing import Optional

from typing import Union

from box_sdk_gen.schemas.ai_llm_endpoint_params_open_ai import AiLlmEndpointParamsOpenAi

from box_sdk_gen.schemas.ai_llm_endpoint_params_google import AiLlmEndpointParamsGoogle

from box_sdk_gen.schemas.ai_agent_basic_text_tool_base import AiAgentBasicTextToolBase

from box_sdk_gen.schemas.ai_agent_basic_text_tool_text_gen import (
    AiAgentBasicTextToolTextGen,
)

from box_sdk_gen.schemas.ai_agent_long_text_tool_text_gen import (
    AiAgentLongTextToolTextGenEmbeddingsField,
)

from box_sdk_gen.schemas.ai_agent_long_text_tool_text_gen import (
    AiAgentLongTextToolTextGen,
)


class AiAgentBasicGenTool(AiAgentLongTextToolTextGen):
    def __init__(
        self,
        *,
        content_template: Optional[str] = None,
        embeddings: Optional[AiAgentLongTextToolTextGenEmbeddingsField] = None,
        system_message: Optional[str] = None,
        prompt_template: Optional[str] = None,
        model: Optional[str] = None,
        num_tokens_for_completion: Optional[int] = None,
        llm_endpoint_params: Optional[
            Union[AiLlmEndpointParamsOpenAi, AiLlmEndpointParamsGoogle]
        ] = None,
        **kwargs
    ):
        """
                :param content_template: How the content should be included in a request to the LLM.
        Input for `{content}` is optional, depending on the use., defaults to None
                :type content_template: Optional[str], optional
                :param system_message: System messages try to help the LLM "understand" its role and what it is supposed to do.
        Input for `{current_date}` is optional, depending on the use., defaults to None
                :type system_message: Optional[str], optional
                :param prompt_template: The prompt template contains contextual information of the request and the user prompt.

        When using the `prompt_template` parameter, you **must include** input for `{user_question}`.
        Inputs for `{current_date}` and `{content}` are optional, depending on the use., defaults to None
                :type prompt_template: Optional[str], optional
                :param model: The model used for the AI Agent for basic text. For specific model values, see the [available models list](g://box-ai/supported-models)., defaults to None
                :type model: Optional[str], optional
                :param num_tokens_for_completion: The number of tokens for completion., defaults to None
                :type num_tokens_for_completion: Optional[int], optional
                :param llm_endpoint_params: The parameters for the LLM endpoint specific to OpenAI / Google models., defaults to None
                :type llm_endpoint_params: Optional[Union[AiLlmEndpointParamsOpenAi, AiLlmEndpointParamsGoogle]], optional
        """
        super().__init__(
            embeddings=embeddings,
            system_message=system_message,
            prompt_template=prompt_template,
            model=model,
            num_tokens_for_completion=num_tokens_for_completion,
            llm_endpoint_params=llm_endpoint_params,
            **kwargs
        )
        self.content_template = content_template
