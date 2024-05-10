from enum import Enum

from typing import Optional

from box_sdk_gen.schemas.integration_mapping_base import (
    IntegrationMappingBaseIntegrationTypeField,
)

from box_sdk_gen.schemas.integration_mapping_base import IntegrationMappingBase


class IntegrationMappingMiniPartnerItemTypeField(str, Enum):
    CHANNEL = 'channel'


class IntegrationMappingMiniBoxItemTypeField(str, Enum):
    FOLDER = 'folder'


class IntegrationMappingMini(IntegrationMappingBase):
    def __init__(
        self,
        *,
        partner_item_id: Optional[str] = None,
        partner_item_type: Optional[IntegrationMappingMiniPartnerItemTypeField] = None,
        box_item_id: Optional[str] = None,
        box_item_type: Optional[IntegrationMappingMiniBoxItemTypeField] = None,
        id: Optional[str] = None,
        integration_type: Optional[IntegrationMappingBaseIntegrationTypeField] = None,
        **kwargs
    ):
        """
                :param partner_item_id: ID of the mapped partner item, defaults to None
                :type partner_item_id: Optional[str], optional
                :param partner_item_type: Domain-specific type of the mapped partner item, defaults to None
                :type partner_item_type: Optional[IntegrationMappingMiniPartnerItemTypeField], optional
                :param box_item_id: ID of the Box item mapped to the object referenced in `partner_item_id`, defaults to None
                :type box_item_id: Optional[str], optional
                :param box_item_type: Type of the Box object referenced in `box_item_id`, defaults to None
                :type box_item_type: Optional[IntegrationMappingMiniBoxItemTypeField], optional
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
        super().__init__(id=id, integration_type=integration_type, **kwargs)
        self.partner_item_id = partner_item_id
        self.partner_item_type = partner_item_type
        self.box_item_id = box_item_id
        self.box_item_type = box_item_type
