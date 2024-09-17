from typing import Optional

from typing import Union

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.ai_llm_endpoint_params_open_ai import AiLlmEndpointParamsOpenAi

from box_sdk_gen.schemas.ai_llm_endpoint_params_google import AiLlmEndpointParamsGoogle


class AiAgentBasicTextToolBase(BaseObject):
    def __init__(
        self,
        *,
        model: Optional[str] = None,
        num_tokens_for_completion: Optional[int] = None,
        llm_endpoint_params: Optional[
            Union[AiLlmEndpointParamsOpenAi, AiLlmEndpointParamsGoogle]
        ] = None,
        **kwargs
    ):
        """
        :param model: The model used for the AI agent for basic text. For specific model values, see the [available models list](g://box-ai/supported-models)., defaults to None
        :type model: Optional[str], optional
        :param num_tokens_for_completion: The number of tokens for completion., defaults to None
        :type num_tokens_for_completion: Optional[int], optional
        :param llm_endpoint_params: The parameters for the LLM endpoint specific to OpenAI / Google models., defaults to None
        :type llm_endpoint_params: Optional[Union[AiLlmEndpointParamsOpenAi, AiLlmEndpointParamsGoogle]], optional
        """
        super().__init__(**kwargs)
        self.model = model
        self.num_tokens_for_completion = num_tokens_for_completion
        self.llm_endpoint_params = llm_endpoint_params
