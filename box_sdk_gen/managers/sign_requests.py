from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from typing import List

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import FileBase

from box_sdk_gen.schemas import SignRequestCreateSigner

from box_sdk_gen.schemas import FolderMini

from box_sdk_gen.schemas import SignRequestPrefillTag

from box_sdk_gen.schemas import SignRequest

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import SignRequests

from box_sdk_gen.schemas import SignRequestCreateRequest

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json_data import sd_to_json

from box_sdk_gen.json_data import SerializedData


class CreateSignRequestSignatureColor(str, Enum):
    BLUE = 'blue'
    BLACK = 'black'
    RED = 'red'


class SignRequestsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: NetworkSession = None,
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session

    def cancel_sign_request(
        self,
        sign_request_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> SignRequest:
        """
        Cancels a sign request.
        :param sign_request_id: The ID of the sign request
            Example: "33243242"
        :type sign_request_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/sign_requests/',
                    to_string(sign_request_id),
                    '/cancel',
                ]
            ),
            FetchOptions(
                method='POST',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, SignRequest)

    def resend_sign_request(
        self,
        sign_request_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Resends a sign request email to all outstanding signers.
        :param sign_request_id: The ID of the sign request
            Example: "33243242"
        :type sign_request_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/sign_requests/',
                    to_string(sign_request_id),
                    '/resend',
                ]
            ),
            FetchOptions(
                method='POST',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def get_sign_request_by_id(
        self,
        sign_request_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> SignRequest:
        """
        Gets a sign request by ID.
        :param sign_request_id: The ID of the sign request
            Example: "33243242"
        :type sign_request_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/sign_requests/',
                    to_string(sign_request_id),
                ]
            ),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, SignRequest)

    def get_sign_requests(
        self,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> SignRequests:
        """
        Gets sign requests created by a user. If the `sign_files` and/or

        `parent_folder` are deleted, the sign request will not return in the list.

        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {'marker': to_string(marker), 'limit': to_string(limit)}
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([self.network_session.base_urls.base_url, '/sign_requests']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, SignRequests)

    def create_sign_request(
        self,
        signers: List[SignRequestCreateSigner],
        parent_folder: FolderMini,
        source_files: Optional[List[FileBase]] = None,
        signature_color: Optional[CreateSignRequestSignatureColor] = None,
        is_document_preparation_needed: Optional[bool] = None,
        redirect_url: Optional[str] = None,
        declined_redirect_url: Optional[str] = None,
        are_text_signatures_enabled: Optional[bool] = None,
        email_subject: Optional[str] = None,
        email_message: Optional[str] = None,
        are_reminders_enabled: Optional[bool] = None,
        name: Optional[str] = None,
        prefill_tags: Optional[List[SignRequestPrefillTag]] = None,
        days_valid: Optional[int] = None,
        external_id: Optional[str] = None,
        is_phone_verification_required_to_view: Optional[bool] = None,
        template_id: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> SignRequest:
        """
        Creates a sign request. This involves preparing a document for signing and

        sending the sign request to signers.

        :param signers: Array of signers for the sign request. 35 is the max number of signers permitted.
        :type signers: List[SignRequestCreateSigner]
        :param source_files: List of files to create a signing document from. This is currently limited to ten files. Only the ID and type fields are required for each file.
        :type source_files: Optional[List[FileBase]], optional
        :param signature_color: Force a specific color for the signature (blue, black, or red)
        :type signature_color: Optional[CreateSignRequestSignatureColor], optional
        :param is_document_preparation_needed: Indicates if the sender should receive a `prepare_url` in the response to complete document preparation via UI.
        :type is_document_preparation_needed: Optional[bool], optional
        :param redirect_url: When specified, signature request will be redirected to this url when a document is signed.
        :type redirect_url: Optional[str], optional
        :param declined_redirect_url: The uri that a signer will be redirected to after declining to sign a document.
        :type declined_redirect_url: Optional[str], optional
        :param are_text_signatures_enabled: Disables the usage of signatures generated by typing (text).
        :type are_text_signatures_enabled: Optional[bool], optional
        :param email_subject: Subject of sign request email. This is cleaned by sign request. If this field is not passed, a default subject will be used.
        :type email_subject: Optional[str], optional
        :param email_message: Message to include in sign request email. The field is cleaned through sanitization of specific characters. However, some html tags are allowed. Links included in the message are also converted to hyperlinks in the email. The message may contain the following html tags including `a`, `abbr`, `acronym`, `b`, `blockquote`, `code`, `em`, `i`, `ul`, `li`, `ol`, and `strong`. Be aware that when the text to html ratio is too high, the email may end up in spam filters. Custom styles on these tags are not allowed. If this field is not passed, a default message will be used.
        :type email_message: Optional[str], optional
        :param are_reminders_enabled: Reminds signers to sign a document on day 3, 8, 13 and 18. Reminders are only sent to outstanding signers.
        :type are_reminders_enabled: Optional[bool], optional
        :param name: Name of the sign request.
        :type name: Optional[str], optional
        :param prefill_tags: When a document contains sign related tags in the content, you can prefill them using this `prefill_tags` by referencing the 'id' of the tag as the `external_id` field of the prefill tag.
        :type prefill_tags: Optional[List[SignRequestPrefillTag]], optional
        :param days_valid: Set the number of days after which the created signature request will automatically expire if not completed. By default, we do not apply any expiration date on signature requests, and the signature request does not expire.
        :type days_valid: Optional[int], optional
        :param external_id: This can be used to reference an ID in an external system that the sign request is related to.
        :type external_id: Optional[str], optional
        :param is_phone_verification_required_to_view: Forces signers to verify a text message prior to viewing the document. You must specify the phone number of signers to have this setting apply to them.
        :type is_phone_verification_required_to_view: Optional[bool], optional
        :param template_id: When a signature request is created from a template this field will indicate the id of that template.
        :type template_id: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'source_files': source_files,
            'signature_color': signature_color,
            'signers': signers,
            'is_document_preparation_needed': is_document_preparation_needed,
            'redirect_url': redirect_url,
            'declined_redirect_url': declined_redirect_url,
            'are_text_signatures_enabled': are_text_signatures_enabled,
            'email_subject': email_subject,
            'email_message': email_message,
            'are_reminders_enabled': are_reminders_enabled,
            'parent_folder': parent_folder,
            'name': name,
            'prefill_tags': prefill_tags,
            'days_valid': days_valid,
            'external_id': external_id,
            'is_phone_verification_required_to_view': is_phone_verification_required_to_view,
            'template_id': template_id,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([self.network_session.base_urls.base_url, '/sign_requests']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, SignRequest)
