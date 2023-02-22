from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import Classification

from schemas import ClientError

class PostFilesIdMetadataEnterpriseSecurityClassification6VmVochwUWoRequestBodyArg(BaseObject):
    def __init__(self, Box__Security__Classification__Key: Union[None, str] = None, **kwargs):
        """
        :param Box__Security__Classification__Key: The name of the classification to apply to this file.
            To list the available classifications in an enterprise,
            use the classification API to retrieve the
            [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema)
            which lists all available classification keys.
        :type Box__Security__Classification__Key: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.Box__Security__Classification__Key = Box__Security__Classification__Key

class FileClassificationsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFilesIdMetadataEnterpriseSecurityClassification6VmVochwUWo(self, fileId: str) -> Classification:
        """
        Retrieves the classification metadata instance that
        
        has been applied to a file.

        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='GET', auth=self.auth))
        return Classification.from_dict(json.loads(response.text))
    def postFilesIdMetadataEnterpriseSecurityClassification6VmVochwUWo(self, fileId: str, requestBody: PostFilesIdMetadataEnterpriseSecurityClassification6VmVochwUWoRequestBodyArg) -> Classification:
        """
        Adds a classification to a file by specifying the label of the
        
        classification to add.

        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Classification.from_dict(json.loads(response.text))
    def deleteFilesIdMetadataEnterpriseSecurityClassification6VmVochwUWo(self, fileId: str):
        """
        Removes any classifications from a file.
        
        This API can also be called by including the enterprise ID in the

        
        URL explicitly, for example

        
        `/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content