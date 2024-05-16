from enum import Enum

from typing import Optional

from typing import List

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.template_signer_input import TemplateSignerInput


class TemplateSignerRoleField(str, Enum):
    SIGNER = 'signer'
    APPROVER = 'approver'
    FINAL_COPY_READER = 'final_copy_reader'


class TemplateSigner(BaseObject):
    def __init__(
        self,
        *,
        inputs: Optional[List[TemplateSignerInput]] = None,
        email: Optional[str] = None,
        role: Optional[TemplateSignerRoleField] = None,
        is_in_person: Optional[bool] = None,
        order: Optional[int] = None,
        signer_group_id: Optional[str] = None,
        **kwargs
    ):
        """
                :param email: Email address of the signer, defaults to None
                :type email: Optional[str], optional
                :param role: Defines the role of the signer in the signature request. A role of
        `signer` needs to sign the document, a role `approver`
        approves the document and
        a `final_copy_reader` role only
        receives the final signed document and signing log., defaults to None
                :type role: Optional[TemplateSignerRoleField], optional
                :param is_in_person: Used in combination with an embed URL for a sender.
        After the sender signs, they will be
        redirected to the next `in_person` signer., defaults to None
                :type is_in_person: Optional[bool], optional
                :param order: Order of the signer, defaults to None
                :type order: Optional[int], optional
                :param signer_group_id: If provided, this value points signers that are assigned the same inputs and belongs to same signer group.
        A signer group is not a Box Group. It is an entity that belongs to the template itself and can only be used
        within Box Sign requests created from it., defaults to None
                :type signer_group_id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.inputs = inputs
        self.email = email
        self.role = role
        self.is_in_person = is_in_person
        self.order = order
        self.signer_group_id = signer_group_id
