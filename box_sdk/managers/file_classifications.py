from typing import Optional

from box_sdk.base_object import BaseObject

import json

from typing import Dict

from box_sdk.schemas import Classification

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateFileMetadataEnterpriseSecurityClassificationRequestBodyArg(BaseObject):
    def __init__(self, box_security_classification_key: Optional[str] = None, **kwargs):
        """
        :param box_security_classification_key: The name of the classification to apply to this file.
            To list the available classifications in an enterprise,
            use the classification API to retrieve the
            [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema)
            which lists all available classification keys.
        :type box_security_classification_key: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.box_security_classification_key = box_security_classification_key

class FileClassificationsManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def get_file_metadata_enterprise_security_classification_6_vm_vochw_u_wo(self, file_id: str) -> Classification:
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return Classification.from_dict(json.loads(response.text))
    def create_file_metadata_enterprise_security_classification(self, file_id: str, request_body: CreateFileMetadataEnterpriseSecurityClassificationRequestBodyArg) -> Classification:
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return Classification.from_dict(json.loads(response.text))
    def delete_file_metadata_enterprise_security_classification(self, file_id: str):
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content