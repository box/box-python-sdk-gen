from typing import Union

from base_object import BaseObject

from enum import Enum

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import MetadataCascadePolicies

from schemas import ClientError

from schemas import MetadataCascadePolicy

from schemas import ConflictError

class GetMetadataCascadePoliciesOptionsArg(BaseObject):
    def __init__(self, ownerEnterpriseId: Union[None, str] = None, marker: Union[None, str] = None, offset: Union[None, int] = None, **kwargs):
        """
        :param ownerEnterpriseId: The ID of the enterprise ID for which to find metadata
            cascade policies. If not specified, it defaults to the
            current enterprise.
        :type ownerEnterpriseId: Union[None, str], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.ownerEnterpriseId = ownerEnterpriseId
        self.marker = marker
        self.offset = offset

class PostMetadataCascadePoliciesRequestBodyArgScopeField(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class PostMetadataCascadePoliciesRequestBodyArg(BaseObject):
    def __init__(self, folder_id: str, scope: PostMetadataCascadePoliciesRequestBodyArgScopeField, templateKey: str, **kwargs):
        """
        :param folder_id: The ID of the folder to apply the policy to. This folder will
            need to already have an instance of the targeted metadata
            template applied to it.
        :type folder_id: str
        :param scope: The scope of the targeted metadata template. This template will
            need to already have an instance applied to the targeted folder.
        :type scope: PostMetadataCascadePoliciesRequestBodyArgScopeField
        :param templateKey: The key of the targeted metadata template. This template will
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
        :type templateKey: str
        """
        super().__init__(**kwargs)
        self.folder_id = folder_id
        self.scope = scope
        self.templateKey = templateKey

class PostMetadataCascadePoliciesIdApplyRequestBodyArgConflictResolutionField(str, Enum):
    NONE = 'none'
    OVERWRITE = 'overwrite'

class PostMetadataCascadePoliciesIdApplyRequestBodyArg(BaseObject):
    def __init__(self, conflict_resolution: PostMetadataCascadePoliciesIdApplyRequestBodyArgConflictResolutionField, **kwargs):
        """
        :param conflict_resolution: Describes the desired behavior when dealing with the conflict
            where a metadata template already has an instance applied
            to a child.
            * `none` will preserve the existing value on the file
            * `overwrite` will force-apply the templates values over
              any existing values.
        :type conflict_resolution: PostMetadataCascadePoliciesIdApplyRequestBodyArgConflictResolutionField
        """
        super().__init__(**kwargs)
        self.conflict_resolution = conflict_resolution

class MetadataCascadePoliciesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getMetadataCascadePolicies(self, folderId: str, options: GetMetadataCascadePoliciesOptionsArg = None) -> MetadataCascadePolicies:
        """
        Retrieves a list of all the metadata cascade policies
        
        that are applied to a given folder. This can not be used on the root

        
        folder with ID `0`.

        :param folderId: Specifies which folder to return policies for. This can not be used on the
            root folder with ID `0`.
            Example: "31232"
        :type folderId: str
        """
        if options is None:
            options = GetMetadataCascadePoliciesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_cascade_policies']), FetchOptions(method='GET', params={'folder_id': folderId, 'owner_enterprise_id': options.ownerEnterpriseId, 'marker': options.marker, 'offset': options.offset}, auth=self.auth))
        return MetadataCascadePolicies.from_dict(json.loads(response.text))
    def postMetadataCascadePolicies(self, requestBody: PostMetadataCascadePoliciesRequestBodyArg) -> MetadataCascadePolicy:
        """
        Creates a new metadata cascade policy that applies a given
        
        metadata template to a given folder and automatically

        
        cascades it down to any files within that folder.

        
        In order for the policy to be applied a metadata instance must first

        
        be applied to the folder the policy is to be applied to.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_cascade_policies']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return MetadataCascadePolicy.from_dict(json.loads(response.text))
    def getMetadataCascadePoliciesId(self, metadataCascadePolicyId: str) -> MetadataCascadePolicy:
        """
        Retrieve a specific metadata cascade policy assigned to a folder.
        :param metadataCascadePolicyId: The ID of the metadata cascade policy.
            Example: "6fd4ff89-8fc1-42cf-8b29-1890dedd26d7"
        :type metadataCascadePolicyId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_cascade_policies/', metadataCascadePolicyId]), FetchOptions(method='GET', auth=self.auth))
        return MetadataCascadePolicy.from_dict(json.loads(response.text))
    def deleteMetadataCascadePoliciesId(self, metadataCascadePolicyId: str):
        """
        Deletes a metadata cascade policy.
        :param metadataCascadePolicyId: The ID of the metadata cascade policy.
            Example: "6fd4ff89-8fc1-42cf-8b29-1890dedd26d7"
        :type metadataCascadePolicyId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_cascade_policies/', metadataCascadePolicyId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def postMetadataCascadePoliciesIdApply(self, metadataCascadePolicyId: str, requestBody: PostMetadataCascadePoliciesIdApplyRequestBodyArg):
        """
        Force the metadata on a folder with a metadata cascade policy to be applied to
        
        all of its children. This can be used after creating a new cascade policy to

        
        enforce the metadata to be cascaded down to all existing files within that

        
        folder.

        :param metadataCascadePolicyId: The ID of the cascade policy to force-apply.
            Example: "6fd4ff89-8fc1-42cf-8b29-1890dedd26d7"
        :type metadataCascadePolicyId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_cascade_policies/', metadataCascadePolicyId, '/apply']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return response.content