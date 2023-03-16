from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import Classification

from box_sdk.schemas import ClientError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class PostFilesIdMetadataEnterpriseSecurityClassification6VmVochwUWoRequestBodyArg(BaseObject):
    def __init__(self, box_security_classification_key: Union[None, str] = None, **kwargs):
        """
        :param box_security_classification_key: The name of the classification to apply to this file.
            To list the available classifications in an enterprise,
            use the classification API to retrieve the
            [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema)
            which lists all available classification keys.
        :type box_security_classification_key: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.box_security_classification_key = box_security_classification_key

class FileClassificationsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_files_id_metadata_enterprise_security_classification_6_vm_vochw_u_wo(self, file_id: str) -> Classification:
        """
        Retrieves the classification metadata instance that
        
        has been applied to a file.

        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='GET', auth=self.auth))
        return Classification.from_dict(json.loads(response.text))
    def post_files_id_metadata_enterprise_security_classification_6_vm_vochw_u_wo(self, file_id: str, request_body: PostFilesIdMetadataEnterpriseSecurityClassification6VmVochwUWoRequestBodyArg) -> Classification:
        """
        Adds a classification to a file by specifying the label of the
        
        classification to add.

        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return Classification.from_dict(json.loads(response.text))
    def delete_files_id_metadata_enterprise_security_classification_6_vm_vochw_u_wo(self, file_id: str):
        """
        Removes any classifications from a file.
        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content