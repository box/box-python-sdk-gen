from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import Classification

from box_sdk.schemas import ClientError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateFolderMetadataEnterpriseSecurityClassification6VmVochwUWoRequestBodyArg(BaseObject):
    def __init__(self, box_security_classification_key: Union[None, str] = None, **kwargs):
        """
        :param box_security_classification_key: The name of the classification to apply to this folder.
            To list the available classifications in an enterprise,
            use the classification API to retrieve the
            [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema)
            which lists all available classification keys.
        :type box_security_classification_key: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.box_security_classification_key = box_security_classification_key

class FolderClassificationsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_folder_metadata_enterprise_security_classification_6_vm_vochw_u_wo(self, folder_id: str) -> Classification:
        """
        Retrieves the classification metadata instance that
        
        has been applied to a folder.

        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='GET', auth=self.auth))
        return Classification.from_dict(json.loads(response.text))
    def create_folder_metadata_enterprise_security_classification_6_vm_vochw_u_wo(self, folder_id: str, request_body: CreateFolderMetadataEnterpriseSecurityClassification6VmVochwUWoRequestBodyArg) -> Classification:
        """
        Adds a classification to a folder by specifying the label of the
        
        classification to add.

        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return Classification.from_dict(json.loads(response.text))
    def delete_folder_metadata_enterprise_security_classification_6_vm_vochw_u_wo(self, folder_id: str):
        """
        Removes any classifications from a folder.
        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content