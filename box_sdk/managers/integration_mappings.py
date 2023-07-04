from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Optional

from typing import Dict

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import IntegrationMappings

from box_sdk.schemas import ClientError

from box_sdk.schemas import IntegrationMapping

from box_sdk.schemas import IntegrationMappingSlackCreateRequest

from box_sdk.schemas import IntegrationMappingBoxItemSlack

from box_sdk.schemas import IntegrationMappingSlackOptions

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import to_map

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetIntegrationMappingSlackPartnerItemTypeArg(str, Enum):
    CHANNEL = 'channel'

class GetIntegrationMappingSlackBoxItemTypeArg(str, Enum):
    FOLDER = 'folder'

class CreateIntegrationMappingSlackPartnerItemArg(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class CreateIntegrationMappingSlackBoxItemArg(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class CreateIntegrationMappingSlackOptionsArg(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class UpdateIntegrationMappingSlackByIdBoxItemArg(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class UpdateIntegrationMappingSlackByIdOptionsArg(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class IntegrationMappingsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_integration_mapping_slack(self, marker: Optional[str] = None, limit: Optional[int] = None, partner_item_type: Optional[GetIntegrationMappingSlackPartnerItemTypeArg] = None, partner_item_id: Optional[str] = None, box_item_id: Optional[str] = None, box_item_type: Optional[GetIntegrationMappingSlackBoxItemTypeArg] = None, is_manually_created: Optional[bool] = None) -> IntegrationMappings:
        """
        Lists [Slack integration mappings](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack) in a users' enterprise.
        
        You need Admin or Co-Admin role to

        
        use this endpoint.

        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param partner_item_type: Mapped item type, for which the mapping should be returned
        :type partner_item_type: Optional[GetIntegrationMappingSlackPartnerItemTypeArg], optional
        :param partner_item_id: ID of the mapped item, for which the mapping should be returned
        :type partner_item_id: Optional[str], optional
        :param box_item_id: Box item ID, for which the mappings should be returned
        :type box_item_id: Optional[str], optional
        :param box_item_type: Box item type, for which the mappings should be returned
        :type box_item_type: Optional[GetIntegrationMappingSlackBoxItemTypeArg], optional
        :param is_manually_created: Whether the mapping has been manually created
        :type is_manually_created: Optional[bool], optional
        """
        query_params: Dict = {'marker': marker, 'limit': limit, 'partner_item_type': partner_item_type, 'partner_item_id': partner_item_id, 'box_item_id': box_item_id, 'box_item_type': box_item_type, 'is_manually_created': is_manually_created}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/integration_mappings/slack']), FetchOptions(method='GET', params=to_map(query_params), auth=self.auth, network_session=self.network_session))
        return IntegrationMappings.from_dict(json.loads(response.text))
    def create_integration_mapping_slack(self, partner_item: CreateIntegrationMappingSlackPartnerItemArg, box_item: CreateIntegrationMappingSlackBoxItemArg, options: Optional[CreateIntegrationMappingSlackOptionsArg] = None) -> IntegrationMapping:
        """
        Creates a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack)
        
        by mapping a Slack channel to a Box item.

        
        You need Admin or Co-Admin role to

        
        use this endpoint.

        """
        request_body: BaseObject = BaseObject(partner_item=partner_item, box_item=box_item, options=options)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/integration_mappings/slack']), FetchOptions(method='POST', body=json.dumps(to_map(request_body)), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return IntegrationMapping.from_dict(json.loads(response.text))
    def update_integration_mapping_slack_by_id(self, integration_mapping_id: str, box_item: Optional[UpdateIntegrationMappingSlackByIdBoxItemArg] = None, options: Optional[UpdateIntegrationMappingSlackByIdOptionsArg] = None) -> IntegrationMapping:
        """
        Updates a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack).
        
        Supports updating the Box folder ID and options.

        
        You need Admin or Co-Admin role to

        
        use this endpoint.

        :param integration_mapping_id: An ID of an integration mapping
            Example: "11235432"
        :type integration_mapping_id: str
        """
        request_body: BaseObject = BaseObject(box_item=box_item, options=options)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/integration_mappings/slack/', integration_mapping_id]), FetchOptions(method='PUT', body=json.dumps(to_map(request_body)), content_type='application/json', auth=self.auth, network_session=self.network_session))
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