from box_sdk.base_object import BaseObject

from enum import Enum

from typing import Optional

import json

from typing import Dict

from box_sdk.schemas import WebLink

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateWebLinkRequestBodyArgParentField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of parent folder
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class CreateWebLinkRequestBodyArgSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class CreateWebLinkRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, access: Optional[CreateWebLinkRequestBodyArgSharedLinkFieldAccessField] = None, password: Optional[str] = None, vanity_name: Optional[str] = None, unshared_at: Optional[str] = None, **kwargs):
        """
        :param access: The level of access for the shared link. This can be
            restricted to anyone with the link (`open`), only people
            within the company (`company`) and only those who
            have been invited to the folder (`collaborators`).
            If not set, this field defaults to the access level specified
            by the enterprise admin. To create a shared link with this
            default setting pass the `shared_link` object with
            no `access` field, for example `{ "shared_link": {} }`.
            The `company` access level is only available to paid
            accounts.
        :type access: Optional[CreateWebLinkRequestBodyArgSharedLinkFieldAccessField], optional
        :param password: The password required to access the shared link. Set the
            password to `null` to remove it.
            Passwords must now be at least eight characters
            long and include a number, upper case letter, or
            a non-numeric or non-alphabetic character.
            A password can only be set when `access` is set to `open`.
        :type password: Optional[str], optional
        :param vanity_name: Defines a custom vanity name to use in the shared link URL,
            for example `https://app.box.com/v/my-shared-link`.
            Custom URLs should not be used when sharing sensitive content
            as vanity URLs are a lot easier to guess than regular shared
            links.
        :type vanity_name: Optional[str], optional
        :param unshared_at: The timestamp at which this shared link will
            expire. This field can only be set by
            users with paid accounts. The value must be greater than the
            current date and time.
        :type unshared_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.password = password
        self.vanity_name = vanity_name
        self.unshared_at = unshared_at

class CreateWebLinkRequestBodyArg(BaseObject):
    def __init__(self, url: str, parent: CreateWebLinkRequestBodyArgParentField, name: Optional[str] = None, description: Optional[str] = None, shared_link: Optional[CreateWebLinkRequestBodyArgSharedLinkField] = None, **kwargs):
        """
        :param url: The URL that this web link links to. Must start with
            `"http://"` or `"https://"`.
        :type url: str
        :param parent: The parent folder to create the web link within.
        :type parent: CreateWebLinkRequestBodyArgParentField
        :param name: Name of the web link. Defaults to the URL if not set.
        :type name: Optional[str], optional
        :param description: Description of the web link.
        :type description: Optional[str], optional
        :param shared_link: The settings for the shared link to update.
        :type shared_link: Optional[CreateWebLinkRequestBodyArgSharedLinkField], optional
        """
        super().__init__(**kwargs)
        self.url = url
        self.parent = parent
        self.name = name
        self.description = description
        self.shared_link = shared_link

class GetWebLinkByIdOptionsArg(BaseObject):
    def __init__(self, boxapi: Optional[str] = None, **kwargs):
        """
        :param boxapi: The URL, and optional password, for the shared link of this item.
            This header can be used to access items that have not been
            explicitly shared with a user.
            Use the format `shared_link=[link]` or if a password is required then
            use `shared_link=[link]&shared_link_password=[password]`.
            This header can be used on the file or folder shared, as well as on any files
            or folders nested within the item.
        :type boxapi: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.boxapi = boxapi

class UpdateWebLinkByIdRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Optional[str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class UpdateWebLinkByIdRequestBodyArgSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class UpdateWebLinkByIdRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, access: Optional[UpdateWebLinkByIdRequestBodyArgSharedLinkFieldAccessField] = None, password: Optional[str] = None, vanity_name: Optional[str] = None, unshared_at: Optional[str] = None, **kwargs):
        """
        :param access: The level of access for the shared link. This can be
            restricted to anyone with the link (`open`), only people
            within the company (`company`) and only those who
            have been invited to the folder (`collaborators`).
            If not set, this field defaults to the access level specified
            by the enterprise admin. To create a shared link with this
            default setting pass the `shared_link` object with
            no `access` field, for example `{ "shared_link": {} }`.
            The `company` access level is only available to paid
            accounts.
        :type access: Optional[UpdateWebLinkByIdRequestBodyArgSharedLinkFieldAccessField], optional
        :param password: The password required to access the shared link. Set the
            password to `null` to remove it.
            Passwords must now be at least eight characters
            long and include a number, upper case letter, or
            a non-numeric or non-alphabetic character.
            A password can only be set when `access` is set to `open`.
        :type password: Optional[str], optional
        :param vanity_name: Defines a custom vanity name to use in the shared link URL,
            for example `https://app.box.com/v/my-shared-link`.
            Custom URLs should not be used when sharing sensitive content
            as vanity URLs are a lot easier to guess than regular shared
            links.
        :type vanity_name: Optional[str], optional
        :param unshared_at: The timestamp at which this shared link will
            expire. This field can only be set by
            users with paid accounts. The value must be greater than the
            current date and time.
        :type unshared_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.password = password
        self.vanity_name = vanity_name
        self.unshared_at = unshared_at

class UpdateWebLinkByIdRequestBodyArg(BaseObject):
    def __init__(self, url: Optional[str] = None, parent: Optional[UpdateWebLinkByIdRequestBodyArgParentField] = None, name: Optional[str] = None, description: Optional[str] = None, shared_link: Optional[UpdateWebLinkByIdRequestBodyArgSharedLinkField] = None, **kwargs):
        """
        :param url: The new URL that the web link links to. Must start with
            `"http://"` or `"https://"`.
        :type url: Optional[str], optional
        :param name: A new name for the web link. Defaults to the URL if not set.
        :type name: Optional[str], optional
        :param description: A new description of the web link.
        :type description: Optional[str], optional
        :param shared_link: The settings for the shared link to update.
        :type shared_link: Optional[UpdateWebLinkByIdRequestBodyArgSharedLinkField], optional
        """
        super().__init__(**kwargs)
        self.url = url
        self.parent = parent
        self.name = name
        self.description = description
        self.shared_link = shared_link

class WebLinksManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def create_web_link(self, request_body: CreateWebLinkRequestBodyArg) -> WebLink:
        """
        Creates a web link object within a folder.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return WebLink.from_dict(json.loads(response.text))
    def get_web_link_by_id(self, web_link_id: str, options: GetWebLinkByIdOptionsArg = None) -> WebLink:
        """
        Retrieve information about a web link.
        :param web_link_id: The ID of the web link.
            Example: "12345"
        :type web_link_id: str
        """
        if options is None:
            options = GetWebLinkByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', web_link_id]), FetchOptions(method='GET', headers={'boxapi': options.boxapi}, auth=self.auth, network_session=self.network_session))
        return WebLink.from_dict(json.loads(response.text))
    def update_web_link_by_id(self, web_link_id: str, request_body: UpdateWebLinkByIdRequestBodyArg) -> WebLink:
        """
        Updates a web link object.
        :param web_link_id: The ID of the web link.
            Example: "12345"
        :type web_link_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', web_link_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return WebLink.from_dict(json.loads(response.text))
    def delete_web_link_by_id(self, web_link_id: str):
        """
        Deletes a web link.
        :param web_link_id: The ID of the web link.
            Example: "12345"
        :type web_link_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', web_link_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content