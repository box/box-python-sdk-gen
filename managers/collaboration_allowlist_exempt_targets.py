from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import CollaborationAllowlistExemptTargets

from schemas import ClientError

from schemas import CollaborationAllowlistExemptTarget

class GetCollaborationWhitelistExemptTargetsOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, limit: Union[None, int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class PostCollaborationWhitelistExemptTargetsRequestBodyArgUserField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of the user to exempt.
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class PostCollaborationWhitelistExemptTargetsRequestBodyArg(BaseObject):
    def __init__(self, user: PostCollaborationWhitelistExemptTargetsRequestBodyArgUserField, **kwargs):
        """
        :param user: The user to exempt.
        :type user: PostCollaborationWhitelistExemptTargetsRequestBodyArgUserField
        """
        super().__init__(**kwargs)
        self.user = user

class CollaborationAllowlistExemptTargetsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getCollaborationWhitelistExemptTargets(self, options: GetCollaborationWhitelistExemptTargetsOptionsArg = None) -> CollaborationAllowlistExemptTargets:
        """
        Returns a list of users who have been exempt from the collaboration
        
        domain restrictions.

        """
        if options is None:
            options = GetCollaborationWhitelistExemptTargetsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_exempt_targets']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return CollaborationAllowlistExemptTargets.from_dict(json.loads(response.text))
    def postCollaborationWhitelistExemptTargets(self, requestBody: PostCollaborationWhitelistExemptTargetsRequestBodyArg) -> CollaborationAllowlistExemptTarget:
        """
        Exempts a user from the restrictions set out by the allowed list of domains
        
        for collaborations.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_exempt_targets']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return CollaborationAllowlistExemptTarget.from_dict(json.loads(response.text))
    def getCollaborationWhitelistExemptTargetsId(self, collaborationWhitelistExemptTargetId: str) -> CollaborationAllowlistExemptTarget:
        """
        Returns a users who has been exempt from the collaboration
        
        domain restrictions.

        :param collaborationWhitelistExemptTargetId: The ID of the exemption to the list.
            Example: "984923"
        :type collaborationWhitelistExemptTargetId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_exempt_targets/', collaborationWhitelistExemptTargetId]), FetchOptions(method='GET', auth=self.auth))
        return CollaborationAllowlistExemptTarget.from_dict(json.loads(response.text))
    def deleteCollaborationWhitelistExemptTargetsId(self, collaborationWhitelistExemptTargetId: str):
        """
        Removes a user's exemption from the restrictions set out by the allowed list
        
        of domains for collaborations.

        :param collaborationWhitelistExemptTargetId: The ID of the exemption to the list.
            Example: "984923"
        :type collaborationWhitelistExemptTargetId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaboration_whitelist_exempt_targets/', collaborationWhitelistExemptTargetId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content