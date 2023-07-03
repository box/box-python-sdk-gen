from enum import Enum

from typing import Optional

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import IntegrationMappings

from box_sdk.schemas import ClientError

from box_sdk.schemas import IntegrationMapping

from box_sdk.schemas import IntegrationMappingSlackCreateRequest

from box_sdk.schemas import IntegrationMappingBoxItemSlack

from box_sdk.schemas import IntegrationMappingSlackOptions

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetIntegrationMappingSlackOptionsArgPartnerItemTypeField(str, Enum):
    CHANNEL = 'channel'

class GetIntegrationMappingSlackOptionsArgBoxItemTypeField(str, Enum):
    FOLDER = 'folder'

class GetIntegrationMappingSlackOptionsArg(BaseObject):
    def __init__(self, marker: Optional[str] = None, limit: Optional[int] = None, partner_item_type: Optional[GetIntegrationMappingSlackOptionsArgPartnerItemTypeField] = None, partner_item_id: Optional[str] = None, box_item_id: Optional[str] = None, box_item_type: Optional[GetIntegrationMappingSlackOptionsArgBoxItemTypeField] = None, is_manually_created: Optional[bool] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param partner_item_type: Mapped item type, for which the mapping should be returned
        :type partner_item_type: Optional[GetIntegrationMappingSlackOptionsArgPartnerItemTypeField], optional
        :param partner_item_id: ID of the mapped item, for which the mapping should be returned
        :type partner_item_id: Optional[str], optional
        :param box_item_id: Box item ID, for which the mappings should be returned
        :type box_item_id: Optional[str], optional
        :param box_item_type: Box item type, for which the mappings should be returned
        :type box_item_type: Optional[GetIntegrationMappingSlackOptionsArgBoxItemTypeField], optional
        :param is_manually_created: Whether the mapping has been manually created
        :type is_manually_created: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit
        self.partner_item_type = partner_item_type
        self.partner_item_id = partner_item_id
        self.box_item_id = box_item_id
        self.box_item_type = box_item_type
        self.is_manually_created = is_manually_created

class UpdateIntegrationMappingSlackByIdRequestBodyArgBoxItemField(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class UpdateIntegrationMappingSlackByIdRequestBodyArgOptionsField(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class UpdateIntegrationMappingSlackByIdRequestBodyArg(BaseObject):
    def __init__(self, box_item: Optional[UpdateIntegrationMappingSlackByIdRequestBodyArgBoxItemField] = None, options: Optional[UpdateIntegrationMappingSlackByIdRequestBodyArgOptionsField] = None, **kwargs):
        super().__init__(**kwargs)
        self.box_item = box_item
        self.options = options

class IntegrationMappingsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_integration_mapping_slack(self, options: GetIntegrationMappingSlackOptionsArg = None) -> IntegrationMappings:
        """
        Lists [Slack integration mappings](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack) in a users' enterprise.
        
        You need Admin or Co-Admin role to

        
        use this endpoint.

        """
        if options is None:
            options = GetIntegrationMappingSlackOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/integration_mappings/slack']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit, 'partner_item_type': options.partner_item_type, 'partner_item_id': options.partner_item_id, 'box_item_id': options.box_item_id, 'box_item_type': options.box_item_type, 'is_manually_created': options.is_manually_created}, auth=self.auth, network_session=self.network_session))
        return IntegrationMappings.from_dict(json.loads(response.text))
    def create_integration_mapping_slack(self, request_body: IntegrationMappingSlackCreateRequest) -> IntegrationMapping:
        """
        Creates a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack)
        
        by mapping a Slack channel to a Box item.

        
        You need Admin or Co-Admin role to

        
        use this endpoint.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/integration_mappings/slack']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return IntegrationMapping.from_dict(json.loads(response.text))
    def update_integration_mapping_slack_by_id(self, integration_mapping_id: str, request_body: UpdateIntegrationMappingSlackByIdRequestBodyArg) -> IntegrationMapping:
        """
        Updates a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack).
        
        Supports updating the Box folder ID and options.

        
        You need Admin or Co-Admin role to

        
        use this endpoint.

        :param integration_mapping_id: An ID of an integration mapping
            Example: "11235432"
        :type integration_mapping_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/integration_mappings/slack/', integration_mapping_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return IntegrationMapping.from_dict(json.loads(response.text))
    def delete_integration_mapping_slack_by_id(self, integration_mapping_id: str):
        """
        Deletes a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack).
        
        You need Admin or Co-Admin role to

        
        use this endpoint.

        :param integration_mapping_id: An ID of an integration mapping
            Example: "11235432"
        :type integration_mapping_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/integration_mappings/slack/', integration_mapping_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content