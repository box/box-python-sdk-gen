from enum import Enum

from box_sdk_gen.internal.base_object import BaseObject


class LegalHoldPolicyMiniTypeField(str, Enum):
    LEGAL_HOLD_POLICY = 'legal_hold_policy'


class LegalHoldPolicyMini(BaseObject):
    _discriminator = 'type', {'legal_hold_policy'}

    def __init__(
        self,
        id: str,
        *,
        type: LegalHoldPolicyMiniTypeField = LegalHoldPolicyMiniTypeField.LEGAL_HOLD_POLICY.value,
        **kwargs
    ):
        """
        :param id: The unique identifier for this legal hold policy
        :type id: str
        :param type: `legal_hold_policy`, defaults to LegalHoldPolicyMiniTypeField.LEGAL_HOLD_POLICY.value
        :type type: LegalHoldPolicyMiniTypeField, optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
