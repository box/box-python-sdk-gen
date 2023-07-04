from enum import Enum

from typing import Optional

from typing import Dict

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import MetadataCascadePolicies

from box_sdk.schemas import ClientError

from box_sdk.schemas import MetadataCascadePolicy

from box_sdk.schemas import ConflictError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import to_map

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateMetadataCascadePolicyScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class CreateMetadataCascadePolicyApplyConflictResolutionArg(str, Enum):
    NONE = 'none'
    OVERWRITE = 'overwrite'

class MetadataCascadePoliciesManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_metadata_cascade_policies(self, folder_id: str, owner_enterprise_id: Optional[str] = None, marker: Optional[str] = None, offset: Optional[int] = None) -> MetadataCascadePolicies:
        """
        Retrieves a list of all the metadata cascade policies
        
        that are applied to a given folder. This can not be used on the root

        
        folder with ID `0`.

        :param folder_id: Specifies which folder to return policies for. This can not be used on the
            root folder with ID `0`.
        :type folder_id: str
        :param owner_enterprise_id: The ID of the enterprise ID for which to find metadata
            cascade policies. If not specified, it defaults to the
            current enterprise.
        :type owner_enterprise_id: Optional[str], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        """
        query_params: Dict = {'folder_id': folder_id, 'owner_enterprise_id': owner_enterprise_id, 'marker': marker, 'offset': offset}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_cascade_policies']), FetchOptions(method='GET', params=to_map(query_params), auth=self.auth, network_session=self.network_session))
        return MetadataCascadePolicies.from_dict(json.loads(response.text))
    def create_metadata_cascade_policy(self, folder_id: str, scope: CreateMetadataCascadePolicyScopeArg, template_key: str) -> MetadataCascadePolicy:
        """
        Creates a new metadata cascade policy that applies a given
        
        metadata template to a given folder and automatically

        
        cascades it down to any files within that folder.

        
        In order for the policy to be applied a metadata instance must first

        
        be applied to the folder the policy is to be applied to.

        :param folder_id: The ID of the folder to apply the policy to. This folder will
            need to already have an instance of the targeted metadata
            template applied to it.
        :type folder_id: str
        :param scope: The scope of the targeted metadata template. This template will
            need to already have an instance applied to the targeted folder.
        :type scope: CreateMetadataCascadePolicyScopeArg
        :param template_key: The key of the targeted metadata template. This template will
            need to already have an instance applied to the targeted folder.
            In many cases the template key is automatically derived
            of its display name, for example `Contract Template` would
            become `contractTemplate`. In some cases the creator of the
            template will have provided its own template key.
            Please [list the templates for an enterprise][list], or
            get all instances on a [file][file] or [folder][folder]
            to inspect a template's key.
            [list]: e://get-metadata-templates-enterprise
            [file]: e://get-files-id-metadata
            [folder]: e://get-folders-id-metadata
        :type template_key: str
        """
        request_body: BaseObject = BaseObject(folder_id=folder_id, scope=scope, template_key=template_key)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_cascade_policies']), FetchOptions(method='POST', body=json.dumps(to_map(request_body)), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return MetadataCascadePolicy.from_dict(json.loads(response.text))
    def get_metadata_cascade_policy_by_id(self, metadata_cascade_policy_id: str) -> MetadataCascadePolicy:
        """
        Retrieve a specific metadata cascade policy assigned to a folder.
        :param metadata_cascade_policy_id: The ID of the metadata cascade policy.
            Example: "6fd4ff89-8fc1-42cf-8b29-1890dedd26d7"
        :type metadata_cascade_policy_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_cascade_policies/', metadata_cascade_policy_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return MetadataCascadePolicy.from_dict(json.loads(response.text))
    def delete_metadata_cascade_policy_by_id(self, metadata_cascade_policy_id: str):
        """
        Deletes a metadata cascade policy.
        :param metadata_cascade_policy_id: The ID of the metadata cascade policy.
            Example: "6fd4ff89-8fc1-42cf-8b29-1890dedd26d7"
        :type metadata_cascade_policy_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_cascade_policies/', metadata_cascade_policy_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content
    def create_metadata_cascade_policy_apply(self, metadata_cascade_policy_id: str, conflict_resolution: CreateMetadataCascadePolicyApplyConflictResolutionArg):
        """
        Force the metadata on a folder with a metadata cascade policy to be applied to
        
        all of its children. This can be used after creating a new cascade policy to

        
        enforce the metadata to be cascaded down to all existing files within that

        
        folder.

        :param metadata_cascade_policy_id: The ID of the cascade policy to force-apply.
            Example: "6fd4ff89-8fc1-42cf-8b29-1890dedd26d7"
        :type metadata_cascade_policy_id: str
        :param conflict_resolution: Describes the desired behavior when dealing with the conflict
            where a metadata template already has an instance applied
            to a child.
            * `none` will preserve the existing value on the file
            * `overwrite` will force-apply the templates values over
              any existing values.
        :type conflict_resolution: CreateMetadataCascadePolicyApplyConflictResolutionArg
        """
        request_body: BaseObject = BaseObject(conflict_resolution=conflict_resolution)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_cascade_policies/', metadata_cascade_policy_id, '/apply']), FetchOptions(method='POST', body=json.dumps(to_map(request_body)), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return response.content