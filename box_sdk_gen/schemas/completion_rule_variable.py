from enum import Enum

from box_sdk_gen.internal.base_object import BaseObject


class CompletionRuleVariableTypeField(str, Enum):
    VARIABLE = 'variable'


class CompletionRuleVariableVariableTypeField(str, Enum):
    TASK_COMPLETION_RULE = 'task_completion_rule'


class CompletionRuleVariableVariableValueField(str, Enum):
    ALL_ASSIGNEES = 'all_assignees'
    ANY_ASSIGNEES = 'any_assignees'


class CompletionRuleVariable(BaseObject):
    _discriminator = 'type', {'variable'}

    def __init__(
        self,
        variable_value: CompletionRuleVariableVariableValueField,
        *,
        type: CompletionRuleVariableTypeField = CompletionRuleVariableTypeField.VARIABLE.value,
        variable_type: CompletionRuleVariableVariableTypeField = CompletionRuleVariableVariableTypeField.TASK_COMPLETION_RULE.value,
        **kwargs
    ):
        """
                :param variable_value: Variable
        values for a completion
        rule.

                :type variable_value: CompletionRuleVariableVariableValueField
                :param type: Completion
        Rule object type.
        , defaults to CompletionRuleVariableTypeField.VARIABLE.value
                :type type: CompletionRuleVariableTypeField, optional
                :param variable_type: Variable type
        for the Completion
        Rule object.
        , defaults to CompletionRuleVariableVariableTypeField.TASK_COMPLETION_RULE.value
                :type variable_type: CompletionRuleVariableVariableTypeField, optional
        """
        super().__init__(**kwargs)
        self.variable_value = variable_value
        self.type = type
        self.variable_type = variable_type
