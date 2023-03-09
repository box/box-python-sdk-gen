from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import Classification

from box_sdk.schemas import ClientError

class PostFoldersIdMetadataEnterpriseSecurityClassification6VmVochwUWoRequestBodyArg(BaseObject):
    def __init__(self, Box__Security__Classification__Key: Union[None, str] = None, **kwargs):
        """
        :param Box__Security__Classification__Key: The name of the classification to apply to this folder.
            To list the available classifications in an enterprise,
            use the classification API to retrieve the
            [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema)
            which lists all available classification keys.
        :type Box__Security__Classification__Key: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.Box__Security__Classification__Key = Box__Security__Classification__Key

class FolderClassificationsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFoldersIdMetadataEnterpriseSecurityClassification6VmVochwUWo(self, folderId: str) -> Classification:
        """
        Retrieves the classification metadata instance that
        
        has been applied to a folder.

        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='GET', auth=self.auth))
        return Classification.from_dict(json.loads(response.text))
    def postFoldersIdMetadataEnterpriseSecurityClassification6VmVochwUWo(self, folderId: str, requestBody: PostFoldersIdMetadataEnterpriseSecurityClassification6VmVochwUWoRequestBodyArg) -> Classification:
        """
        Adds a classification to a folder by specifying the label of the
        
        classification to add.

        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Classification.from_dict(json.loads(response.text))
    def deleteFoldersIdMetadataEnterpriseSecurityClassification6VmVochwUWo(self, folderId: str):
        """
        Removes any classifications from a folder.
        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content