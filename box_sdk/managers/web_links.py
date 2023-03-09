from box_sdk.base_object import BaseObject

from enum import Enum

from typing import Union

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

import json

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

from box_sdk.schemas import WebLink

from box_sdk.schemas import ClientError

from box_sdk.schemas import TrashWebLinkRestored

class PostWebLinksRequestBodyArgParentField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of parent folder
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class PostWebLinksRequestBodyArgSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class PostWebLinksRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, access: Union[None, PostWebLinksRequestBodyArgSharedLinkFieldAccessField] = None, password: Union[None, str] = None, vanity_name: Union[None, str] = None, unshared_at: Union[None, str] = None, **kwargs):
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
        :type access: Union[None, PostWebLinksRequestBodyArgSharedLinkFieldAccessField], optional
        :param password: The password required to access the shared link. Set the
            password to `null` to remove it.
            A password can only be set when `access` is set to `open`.
        :type password: Union[None, str], optional
        :param vanity_name: Defines a custom vanity name to use in the shared link URL,
            for example `https://app.box.com/v/my-shared-link`.
            Custom URLs should not be used when sharing sensitive content
            as vanity URLs are a lot easier to guess than regular shared
            links.
        :type vanity_name: Union[None, str], optional
        :param unshared_at: The timestamp at which this shared link will
            expire. This field can only be set by
            users with paid accounts. The value must be greater than the
            current date and time.
        :type unshared_at: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.password = password
        self.vanity_name = vanity_name
        self.unshared_at = unshared_at

class PostWebLinksRequestBodyArg(BaseObject):
    def __init__(self, url: str, parent: PostWebLinksRequestBodyArgParentField, name: Union[None, str] = None, description: Union[None, str] = None, shared_link: Union[None, PostWebLinksRequestBodyArgSharedLinkField] = None, **kwargs):
        """
        :param url: The URL that this web link links to. Must start with
            `"http://"` or `"https://"`.
        :type url: str
        :param parent: The parent folder to create the web link within.
        :type parent: PostWebLinksRequestBodyArgParentField
        :param name: Name of the web link. Defaults to the URL if not set.
        :type name: Union[None, str], optional
        :param description: Description of the web link.
        :type description: Union[None, str], optional
        :param shared_link: The settings for the shared link to update.
        :type shared_link: Union[None, PostWebLinksRequestBodyArgSharedLinkField], optional
        """
        super().__init__(**kwargs)
        self.url = url
        self.parent = parent
        self.name = name
        self.description = description
        self.shared_link = shared_link

class GetWebLinksIdOptionsArg(BaseObject):
    def __init__(self, boxapi: Union[None, str] = None, **kwargs):
        """
        :param boxapi: The URL, and optional password, for the shared link of this item.
            This header can be used to access items that have not been
            explicitly shared with a user.
            Use the format `shared_link=[link]` or if a password is required then
            use `shared_link=[link]&shared_link_password=[password]`.
            This header can be used on the file or folder shared, as well as on any files
            or folders nested within the item.
        :type boxapi: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.boxapi = boxapi

class PostWebLinksIdRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class PostWebLinksIdRequestBodyArg(BaseObject):
    def __init__(self, name: Union[None, str] = None, parent: Union[None, PostWebLinksIdRequestBodyArgParentField] = None, **kwargs):
        """
        :param name: An optional new name for the web link.
        :type name: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.parent = parent

class PostWebLinksIdOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class PutWebLinksIdRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class PutWebLinksIdRequestBodyArgSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class PutWebLinksIdRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, access: Union[None, PutWebLinksIdRequestBodyArgSharedLinkFieldAccessField] = None, password: Union[None, str] = None, vanity_name: Union[None, str] = None, unshared_at: Union[None, str] = None, **kwargs):
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
        :type access: Union[None, PutWebLinksIdRequestBodyArgSharedLinkFieldAccessField], optional
        :param password: The password required to access the shared link. Set the
            password to `null` to remove it.
            A password can only be set when `access` is set to `open`.
        :type password: Union[None, str], optional
        :param vanity_name: Defines a custom vanity name to use in the shared link URL,
            for example `https://app.box.com/v/my-shared-link`.
            Custom URLs should not be used when sharing sensitive content
            as vanity URLs are a lot easier to guess than regular shared
            links.
        :type vanity_name: Union[None, str], optional
        :param unshared_at: The timestamp at which this shared link will
            expire. This field can only be set by
            users with paid accounts. The value must be greater than the
            current date and time.
        :type unshared_at: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.password = password
        self.vanity_name = vanity_name
        self.unshared_at = unshared_at

class PutWebLinksIdRequestBodyArg(BaseObject):
    def __init__(self, url: Union[None, str] = None, parent: Union[None, PutWebLinksIdRequestBodyArgParentField] = None, name: Union[None, str] = None, description: Union[None, str] = None, shared_link: Union[None, PutWebLinksIdRequestBodyArgSharedLinkField] = None, **kwargs):
        """
        :param url: The new URL that the web link links to. Must start with
            `"http://"` or `"https://"`.
        :type url: Union[None, str], optional
        :param name: A new name for the web link. Defaults to the URL if not set.
        :type name: Union[None, str], optional
        :param description: A new description of the web link.
        :type description: Union[None, str], optional
        :param shared_link: The settings for the shared link to update.
        :type shared_link: Union[None, PutWebLinksIdRequestBodyArgSharedLinkField], optional
        """
        super().__init__(**kwargs)
        self.url = url
        self.parent = parent
        self.name = name
        self.description = description
        self.shared_link = shared_link

class WebLinksManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def postWebLinks(self, requestBody: PostWebLinksRequestBodyArg) -> WebLink:
        """
        Creates a web link object within a folder.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return WebLink.from_dict(json.loads(response.text))
    def getWebLinksId(self, webLinkId: str, options: GetWebLinksIdOptionsArg = None) -> WebLink:
        """
        Retrieve information about a web link.
        :param webLinkId: The ID of the web link.
            Example: "12345"
        :type webLinkId: str
        """
        if options is None:
            options = GetWebLinksIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', webLinkId]), FetchOptions(method='GET', headers={'boxapi': options.boxapi}, auth=self.auth))
        return WebLink.from_dict(json.loads(response.text))
    def postWebLinksId(self, webLinkId: str, requestBody: PostWebLinksIdRequestBodyArg, options: PostWebLinksIdOptionsArg = None) -> TrashWebLinkRestored:
        """
        Restores a web link that has been moved to the trash.
        
        An optional new parent ID can be provided to restore the  web link to in case

        
        the original folder has been deleted.

        :param webLinkId: The ID of the web link.
            Example: "12345"
        :type webLinkId: str
        """
        if options is None:
            options = PostWebLinksIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', webLinkId]), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return TrashWebLinkRestored.from_dict(json.loads(response.text))
    def putWebLinksId(self, webLinkId: str, requestBody: PutWebLinksIdRequestBodyArg) -> WebLink:
        """
        Updates a web link object.
        :param webLinkId: The ID of the web link.
            Example: "12345"
        :type webLinkId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', webLinkId]), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return WebLink.from_dict(json.loads(response.text))
    def deleteWebLinksId(self, webLinkId: str):
        """
        Deletes a web link.
        :param webLinkId: The ID of the web link.
            Example: "12345"
        :type webLinkId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', webLinkId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content