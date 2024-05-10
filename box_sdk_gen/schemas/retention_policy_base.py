from enum import Enum

from box_sdk_gen.internal.base_object import BaseObject


class RetentionPolicyBaseTypeField(str, Enum):
    RETENTION_POLICY = 'retention_policy'


class RetentionPolicyBase(BaseObject):
    _discriminator = 'type', {'retention_policy'}

    def __init__(
        self,
        id: str,
        *,
        type: RetentionPolicyBaseTypeField = RetentionPolicyBaseTypeField.RETENTION_POLICY.value,
        **kwargs
    ):
        """
        :param id: The unique identifier that represents a retention policy.
        :type id: str
        :param type: `retention_policy`, defaults to RetentionPolicyBaseTypeField.RETENTION_POLICY.value
        :type type: RetentionPolicyBaseTypeField, optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
