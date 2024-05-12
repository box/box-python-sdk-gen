from enum import Enum

from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject


class IntegrationMappingBaseIntegrationTypeField(str, Enum):
    SLACK = 'slack'


class IntegrationMappingBase(BaseObject):
    def __init__(
        self,
        *,
        id: Optional[str] = None,
        integration_type: Optional[IntegrationMappingBaseIntegrationTypeField] = None,
        **kwargs
    ):
        """
                :param id: A unique identifier of a folder mapping
        (part of a composite key together
        with `integration_type`), defaults to None
                :type id: Optional[str], optional
                :param integration_type: Identifies the Box partner app,
        with which the mapping is associated.
        Currently only supports Slack.
        (part of the composite key together with `id`), defaults to None
                :type integration_type: Optional[IntegrationMappingBaseIntegrationTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.integration_type = integration_type
