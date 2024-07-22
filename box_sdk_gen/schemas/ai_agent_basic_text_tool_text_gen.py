from typing import Optional

from typing import Union

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.ai_llm_endpoint_params_open_ai import AiLlmEndpointParamsOpenAi

from box_sdk_gen.schemas.ai_llm_endpoint_params_google import AiLlmEndpointParamsGoogle


class AiAgentBasicTextToolTextGen(BaseObject):
    def __init__(
        self,
        *,
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
        super().__init__(**kwargs)
        self.model = model
        self.system_message = system_message
        self.prompt_template = prompt_template
        self.num_tokens_for_completion = num_tokens_for_completion
        self.llm_endpoint_params = llm_endpoint_params
