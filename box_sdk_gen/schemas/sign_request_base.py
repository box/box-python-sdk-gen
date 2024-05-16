from typing import Optional

from typing import List

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.sign_request_prefill_tag import SignRequestPrefillTag


class SignRequestBase(BaseObject):
    def __init__(
        self,
        *,
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
        external_system_name: Optional[str] = None,
        **kwargs
    ):
        """
        :param is_document_preparation_needed: Indicates if the sender should receive a `prepare_url` in the response to complete document preparation using the UI., defaults to None
        :type is_document_preparation_needed: Optional[bool], optional
        :param redirect_url: When specified, the signature request will be redirected to this url when a document is signed., defaults to None
        :type redirect_url: Optional[str], optional
        :param declined_redirect_url: The uri that a signer will be redirected to after declining to sign a document., defaults to None
        :type declined_redirect_url: Optional[str], optional
        :param are_text_signatures_enabled: Disables the usage of signatures generated by typing (text)., defaults to None
        :type are_text_signatures_enabled: Optional[bool], optional
        :param email_subject: Subject of sign request email. This is cleaned by sign request. If this field is not passed, a default subject will be used., defaults to None
        :type email_subject: Optional[str], optional
        :param email_message: Message to include in sign request email. The field is cleaned through sanitization of specific characters. However, some html tags are allowed. Links included in the message are also converted to hyperlinks in the email. The message may contain the following html tags including `a`, `abbr`, `acronym`, `b`, `blockquote`, `code`, `em`, `i`, `ul`, `li`, `ol`, and `strong`. Be aware that when the text to html ratio is too high, the email may end up in spam filters. Custom styles on these tags are not allowed. If this field is not passed, a default message will be used., defaults to None
        :type email_message: Optional[str], optional
        :param are_reminders_enabled: Reminds signers to sign a document on day 3, 8, 13 and 18. Reminders are only sent to outstanding signers., defaults to None
        :type are_reminders_enabled: Optional[bool], optional
        :param name: Name of the signature request., defaults to None
        :type name: Optional[str], optional
        :param prefill_tags: When a document contains sign-related tags in the content, you can prefill them using this `prefill_tags` by referencing the 'id' of the tag as the `external_id` field of the prefill tag., defaults to None
        :type prefill_tags: Optional[List[SignRequestPrefillTag]], optional
        :param days_valid: Set the number of days after which the created signature request will automatically expire if not completed. By default, we do not apply any expiration date on signature requests, and the signature request does not expire., defaults to None
        :type days_valid: Optional[int], optional
        :param external_id: This can be used to reference an ID in an external system that the sign request is related to., defaults to None
        :type external_id: Optional[str], optional
        :param is_phone_verification_required_to_view: Forces signers to verify a text message prior to viewing the document. You must specify the phone number of signers to have this setting apply to them., defaults to None
        :type is_phone_verification_required_to_view: Optional[bool], optional
        :param template_id: When a signature request is created from a template this field will indicate the id of that template., defaults to None
        :type template_id: Optional[str], optional
        :param external_system_name: Used as an optional system name to appear in the signature log next to the signers who have been assigned an `embed_url_external_id`, defaults to None
        :type external_system_name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.is_document_preparation_needed = is_document_preparation_needed
        self.redirect_url = redirect_url
        self.declined_redirect_url = declined_redirect_url
        self.are_text_signatures_enabled = are_text_signatures_enabled
        self.email_subject = email_subject
        self.email_message = email_message
        self.are_reminders_enabled = are_reminders_enabled
        self.name = name
        self.prefill_tags = prefill_tags
        self.days_valid = days_valid
        self.external_id = external_id
        self.is_phone_verification_required_to_view = (
            is_phone_verification_required_to_view
        )
        self.template_id = template_id
        self.external_system_name = external_system_name