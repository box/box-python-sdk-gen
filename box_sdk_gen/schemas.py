from enum import Enum

from typing import Optional

from box_sdk_gen.base_object import BaseObject

from typing import List

from typing import Dict

from typing import Union


class PostOAuth2TokenGrantTypeField(str, Enum):
    AUTHORIZATION_CODE = 'authorization_code'
    REFRESH_TOKEN = 'refresh_token'
    CLIENT_CREDENTIALS = 'client_credentials'
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER = (
        'urn:ietf:params:oauth:grant-type:jwt-bearer'
    )
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE = (
        'urn:ietf:params:oauth:grant-type:token-exchange'
    )


class PostOAuth2TokenSubjectTokenTypeField(str, Enum):
    URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_ACCESS_TOKEN = (
        'urn:ietf:params:oauth:token-type:access_token'
    )


class PostOAuth2TokenActorTokenTypeField(str, Enum):
    URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_ID_TOKEN = (
        'urn:ietf:params:oauth:token-type:id_token'
    )


class PostOAuth2TokenBoxSubjectTypeField(str, Enum):
    ENTERPRISE = 'enterprise'
    USER = 'user'


class PostOAuth2Token(BaseObject):
    def __init__(
        self,
        grant_type: PostOAuth2TokenGrantTypeField,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        refresh_token: Optional[str] = None,
        assertion: Optional[str] = None,
        subject_token: Optional[str] = None,
        subject_token_type: Optional[PostOAuth2TokenSubjectTokenTypeField] = None,
        actor_token: Optional[str] = None,
        actor_token_type: Optional[PostOAuth2TokenActorTokenTypeField] = None,
        scope: Optional[str] = None,
        resource: Optional[str] = None,
        box_subject_type: Optional[PostOAuth2TokenBoxSubjectTypeField] = None,
        box_subject_id: Optional[str] = None,
        box_shared_link: Optional[str] = None,
        **kwargs
    ):
        """
        :param grant_type: The type of request being made, either using a client-side obtained
            authorization code, a refresh token, a JWT assertion, client credentials
            grant or another access token for the purpose of downscoping a token.
        :type grant_type: PostOAuth2TokenGrantTypeField
        :param client_id: The Client ID of the application requesting an access token.
            Used in combination with `authorization_code`, `client_credentials`, or
            `urn:ietf:params:oauth:grant-type:jwt-bearer` as the `grant_type`.
        :type client_id: Optional[str], optional
        :param client_secret: The client secret of the application requesting an access token.
            Used in combination with `authorization_code`, `client_credentials`, or
            `urn:ietf:params:oauth:grant-type:jwt-bearer` as the `grant_type`.
        :type client_secret: Optional[str], optional
        :param code: The client-side authorization code passed to your application by
            Box in the browser redirect after the user has successfully
            granted your application permission to make API calls on their
            behalf.
            Used in combination with `authorization_code` as the `grant_type`.
        :type code: Optional[str], optional
        :param refresh_token: A refresh token used to get a new access token with.
            Used in combination with `refresh_token` as the `grant_type`.
        :type refresh_token: Optional[str], optional
        :param assertion: A JWT assertion for which to request a new access token.
            Used in combination with `urn:ietf:params:oauth:grant-type:jwt-bearer`
            as the `grant_type`.
        :type assertion: Optional[str], optional
        :param subject_token: The token to exchange for a downscoped token. This can be a regular
            access token, a JWT assertion, or an app token.
            Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange`
            as the `grant_type`.
        :type subject_token: Optional[str], optional
        :param subject_token_type: The type of `subject_token` passed in.
            Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange`
            as the `grant_type`.
        :type subject_token_type: Optional[PostOAuth2TokenSubjectTokenTypeField], optional
        :param actor_token: The token used to create an annotator token.
            This is a JWT assertion.
            Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange`
            as the `grant_type`.
        :type actor_token: Optional[str], optional
        :param actor_token_type: The type of `actor_token` passed in.
            Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange`
            as the `grant_type`.
        :type actor_token_type: Optional[PostOAuth2TokenActorTokenTypeField], optional
        :param scope: The space-delimited list of scopes that you want apply to the
            new access token.
            The `subject_token` will need to have all of these scopes or
            the call will error with **401 Unauthorized**.
        :type scope: Optional[str], optional
        :param resource: Full URL for the file that the token should be generated for.
        :type resource: Optional[str], optional
        :param box_subject_type: Used in combination with `client_credentials` as the `grant_type`.
        :type box_subject_type: Optional[PostOAuth2TokenBoxSubjectTypeField], optional
        :param box_subject_id: Used in combination with `client_credentials` as the `grant_type`.
            Value is determined by `box_subject_type`. If `user` use user ID and if
            `enterprise` use enterprise ID.
        :type box_subject_id: Optional[str], optional
        :param box_shared_link: Full URL of the shared link on the file or folder
            that the token should be generated for.
        :type box_shared_link: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code
        self.refresh_token = refresh_token
        self.assertion = assertion
        self.subject_token = subject_token
        self.subject_token_type = subject_token_type
        self.actor_token = actor_token
        self.actor_token_type = actor_token_type
        self.scope = scope
        self.resource = resource
        self.box_subject_type = box_subject_type
        self.box_subject_id = box_subject_id
        self.box_shared_link = box_shared_link


class PostOAuth2TokenRefreshAccessTokenGrantTypeField(str, Enum):
    REFRESH_TOKEN = 'refresh_token'


class PostOAuth2TokenRefreshAccessToken(BaseObject):
    def __init__(
        self,
        grant_type: PostOAuth2TokenRefreshAccessTokenGrantTypeField,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        **kwargs
    ):
        """
        :param grant_type: The type of request being made, in this case a refresh request.
        :type grant_type: PostOAuth2TokenRefreshAccessTokenGrantTypeField
        :param client_id: The client ID of the application requesting to refresh the token.
        :type client_id: str
        :param client_secret: The client secret of the application requesting to refresh the token.
        :type client_secret: str
        :param refresh_token: The refresh token to refresh.
        :type refresh_token: str
        """
        super().__init__(**kwargs)
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token


class PostOAuth2Revoke(BaseObject):
    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        token: Optional[str] = None,
        **kwargs
    ):
        """
        :param client_id: The Client ID of the application requesting to revoke the
            access token.
        :type client_id: Optional[str], optional
        :param client_secret: The client secret of the application requesting to revoke
            an access token.
        :type client_secret: Optional[str], optional
        :param token: The access token to revoke.
        :type token: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token


class ZipDownloadRequestItemsFieldTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'


class ZipDownloadRequestItemsField(BaseObject):
    def __init__(self, type: ZipDownloadRequestItemsFieldTypeField, id: str, **kwargs):
        """
        :param type: The type of the item to add to the archive.
        :type type: ZipDownloadRequestItemsFieldTypeField
        :param id: The identifier of the item to add to the archive. When this item is
            a folder then this can not be the root folder with ID `0`.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class ZipDownloadRequest(BaseObject):
    def __init__(
        self,
        items: List[ZipDownloadRequestItemsField],
        download_file_name: Optional[str] = None,
        **kwargs
    ):
        """
        :param items: A list of items to add to the `zip` archive. These can
            be folders or files.
        :type items: List[ZipDownloadRequestItemsField]
        :param download_file_name: The optional name of the `zip` archive. This name will be appended by the
            `.zip` file extension, for example `January Financials.zip`.
        :type download_file_name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.items = items
        self.download_file_name = download_file_name


class MetadataQueryOrderByFieldDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class MetadataQueryOrderByField(BaseObject):
    def __init__(
        self,
        field_key: Optional[str] = None,
        direction: Optional[MetadataQueryOrderByFieldDirectionField] = None,
        **kwargs
    ):
        """
        :param field_key: The metadata template field to order by.
            The `field_key` represents the `key` value of a field from the
            metadata template being searched for.
        :type field_key: Optional[str], optional
        :param direction: The direction to order by, either ascending or descending.
            The `ordering` direction must be the same for each item in the
            array.
        :type direction: Optional[MetadataQueryOrderByFieldDirectionField], optional
        """
        super().__init__(**kwargs)
        self.field_key = field_key
        self.direction = direction


class MetadataQuery(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'from_': 'from',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'from': 'from_',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        from_: str,
        ancestor_folder_id: str,
        query: Optional[str] = None,
        query_params: Optional[Dict[str, str]] = None,
        order_by: Optional[List[MetadataQueryOrderByField]] = None,
        limit: Optional[int] = None,
        marker: Optional[str] = None,
        fields: Optional[List[str]] = None,
        **kwargs
    ):
        """
        :param from_: Specifies the template used in the query. Must be in the form
            `scope.templateKey`. Not all templates can be used in this field,
            most notably the built-in, Box-provided classification templates
            can not be used in a query.
        :type from_: str
        :param ancestor_folder_id: The ID of the folder that you are restricting the query to. A
            value of zero will return results from all folders you have access
            to. A non-zero value will only return results found in the folder
            corresponding to the ID or in any of its subfolders.
        :type ancestor_folder_id: str
        :param query: The query to perform. A query is a logical expression that is very similar
            to a SQL `SELECT` statement. Values in the search query can be turned into
            parameters specified in the `query_param` arguments list to prevent having
            to manually insert search values into the query string.
            For example, a value of `:amount` would represent the `amount` value in
            `query_params` object.
        :type query: Optional[str], optional
        :param query_params: Set of arguments corresponding to the parameters specified in the
            `query`. The type of each parameter used in the `query_params` must match
            the type of the corresponding metadata template field.
        :type query_params: Optional[Dict[str, str]], optional
        :param order_by: A list of template fields and directions to sort the metadata query
            results by.
            The ordering `direction` must be the same for each item in the array.
        :type order_by: Optional[List[MetadataQueryOrderByField]], optional
        :param limit: A value between 0 and 100 that indicates the maximum number of results
            to return for a single request. This only specifies a maximum
            boundary and will not guarantee the minimum number of results
            returned.
        :type limit: Optional[int], optional
        :param marker: Marker to use for requesting the next page.
        :type marker: Optional[str], optional
        :param fields: By default, this endpoint returns only the most basic info about the items for
            which the query matches. This attribute can be used to specify a list of
            additional attributes to return for any item, including its metadata.
            This attribute takes a list of item fields, metadata template identifiers,
            or metadata template field identifiers.
            For example:
            * `created_by` will add the details of the user who created the item to
            the response.
            * `metadata.<scope>.<templateKey>` will return the mini-representation
            of the metadata instance identified by the `scope` and `templateKey`.
            * `metadata.<scope>.<templateKey>.<field>` will return all the mini-representation
            of the metadata instance identified by the `scope` and `templateKey` plus
            the field specified by the `field` name. Multiple fields for the same
            `scope` and `templateKey` can be defined.
        :type fields: Optional[List[str]], optional
        """
        super().__init__(**kwargs)
        self.from_ = from_
        self.ancestor_folder_id = ancestor_folder_id
        self.query = query
        self.query_params = query_params
        self.order_by = order_by
        self.limit = limit
        self.marker = marker
        self.fields = fields


class FileRequestUpdateRequestStatusField(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class FileRequestUpdateRequest(BaseObject):
    def __init__(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[FileRequestUpdateRequestStatusField] = None,
        is_email_required: Optional[bool] = None,
        is_description_required: Optional[bool] = None,
        expires_at: Optional[str] = None,
        **kwargs
    ):
        """
        :param title: An optional new title for the file request. This can be
            used to change the title of the file request.
            This will default to the value on the existing file request.
        :type title: Optional[str], optional
        :param description: An optional new description for the file request. This can be
            used to change the description of the file request.
            This will default to the value on the existing file request.
        :type description: Optional[str], optional
        :param status: An optional new status of the file request.
            When the status is set to `inactive`, the file request
            will no longer accept new submissions, and any visitor
            to the file request URL will receive a `HTTP 404` status
            code.
            This will default to the value on the existing file request.
        :type status: Optional[FileRequestUpdateRequestStatusField], optional
        :param is_email_required: Whether a file request submitter is required to provide
            their email address.
            When this setting is set to true, the Box UI will show
            an email field on the file request form.
            This will default to the value on the existing file request.
        :type is_email_required: Optional[bool], optional
        :param is_description_required: Whether a file request submitter is required to provide
            a description of the files they are submitting.
            When this setting is set to true, the Box UI will show
            a description field on the file request form.
            This will default to the value on the existing file request.
        :type is_description_required: Optional[bool], optional
        :param expires_at: The date after which a file request will no longer accept new
            submissions.
            After this date, the `status` will automatically be set to
            `inactive`.
            This will default to the value on the existing file request.
        :type expires_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.title = title
        self.description = description
        self.status = status
        self.is_email_required = is_email_required
        self.is_description_required = is_description_required
        self.expires_at = expires_at


class FileRequestCopyRequestFolderFieldTypeField(str, Enum):
    FOLDER = 'folder'


class FileRequestCopyRequestFolderField(BaseObject):
    def __init__(
        self,
        id: str,
        type: Optional[FileRequestCopyRequestFolderFieldTypeField] = None,
        **kwargs
    ):
        """
        :param id: The ID of the folder to associate the new
            file request to.
        :type id: str
        :param type: `folder`
        :type type: Optional[FileRequestCopyRequestFolderFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class FileRequestCopyRequest(FileRequestUpdateRequest):
    def __init__(
        self,
        folder: FileRequestCopyRequestFolderField,
        title: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[FileRequestUpdateRequestStatusField] = None,
        is_email_required: Optional[bool] = None,
        is_description_required: Optional[bool] = None,
        expires_at: Optional[str] = None,
        **kwargs
    ):
        """
        :param folder: The folder to associate the new file request to.
        :type folder: FileRequestCopyRequestFolderField
        :param title: An optional new title for the file request. This can be
            used to change the title of the file request.
            This will default to the value on the existing file request.
        :type title: Optional[str], optional
        :param description: An optional new description for the file request. This can be
            used to change the description of the file request.
            This will default to the value on the existing file request.
        :type description: Optional[str], optional
        :param status: An optional new status of the file request.
            When the status is set to `inactive`, the file request
            will no longer accept new submissions, and any visitor
            to the file request URL will receive a `HTTP 404` status
            code.
            This will default to the value on the existing file request.
        :type status: Optional[FileRequestUpdateRequestStatusField], optional
        :param is_email_required: Whether a file request submitter is required to provide
            their email address.
            When this setting is set to true, the Box UI will show
            an email field on the file request form.
            This will default to the value on the existing file request.
        :type is_email_required: Optional[bool], optional
        :param is_description_required: Whether a file request submitter is required to provide
            a description of the files they are submitting.
            When this setting is set to true, the Box UI will show
            a description field on the file request form.
            This will default to the value on the existing file request.
        :type is_description_required: Optional[bool], optional
        :param expires_at: The date after which a file request will no longer accept new
            submissions.
            After this date, the `status` will automatically be set to
            `inactive`.
            This will default to the value on the existing file request.
        :type expires_at: Optional[str], optional
        """
        super().__init__(
            title=title,
            description=description,
            status=status,
            is_email_required=is_email_required,
            is_description_required=is_description_required,
            expires_at=expires_at,
            **kwargs
        )
        self.folder = folder


class ClientErrorTypeField(str, Enum):
    ERROR = 'error'


class ClientErrorCodeField(str, Enum):
    CREATED = 'created'
    ACCEPTED = 'accepted'
    NO_CONTENT = 'no_content'
    REDIRECT = 'redirect'
    NOT_MODIFIED = 'not_modified'
    BAD_REQUEST = 'bad_request'
    UNAUTHORIZED = 'unauthorized'
    FORBIDDEN = 'forbidden'
    NOT_FOUND = 'not_found'
    METHOD_NOT_ALLOWED = 'method_not_allowed'
    CONFLICT = 'conflict'
    PRECONDITION_FAILED = 'precondition_failed'
    TOO_MANY_REQUESTS = 'too_many_requests'
    INTERNAL_SERVER_ERROR = 'internal_server_error'
    UNAVAILABLE = 'unavailable'
    ITEM_NAME_INVALID = 'item_name_invalid'
    INSUFFICIENT_SCOPE = 'insufficient_scope'


class ClientErrorContextInfoField(BaseObject):
    def __init__(self, message: Optional[str] = None, **kwargs):
        """
        :param message: More details on the error.
        :type message: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.message = message


class ClientError(BaseObject):
    def __init__(
        self,
        type: Optional[ClientErrorTypeField] = None,
        status: Optional[int] = None,
        code: Optional[ClientErrorCodeField] = None,
        message: Optional[str] = None,
        context_info: Optional[ClientErrorContextInfoField] = None,
        help_url: Optional[str] = None,
        request_id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: error
        :type type: Optional[ClientErrorTypeField], optional
        :param status: The HTTP status of the response.
        :type status: Optional[int], optional
        :param code: A Box-specific error code
        :type code: Optional[ClientErrorCodeField], optional
        :param message: A short message describing the error.
        :type message: Optional[str], optional
        :param context_info: A free-form object that contains additional context
            about the error. The possible fields are defined on
            a per-endpoint basis. `message` is only one example.
        :type context_info: Optional[ClientErrorContextInfoField], optional
        :param help_url: A URL that links to more information about why this error occurred.
        :type help_url: Optional[str], optional
        :param request_id: A unique identifier for this response, which can be used
            when contacting Box support.
        :type request_id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.status = status
        self.code = code
        self.message = message
        self.context_info = context_info
        self.help_url = help_url
        self.request_id = request_id


class OAuth2Error(BaseObject):
    def __init__(
        self,
        error: Optional[str] = None,
        error_description: Optional[str] = None,
        **kwargs
    ):
        """
        :param error: The type of the error returned.
        :type error: Optional[str], optional
        :param error_description: The type of the error returned.
        :type error_description: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.error = error
        self.error_description = error_description


class ClassificationTemplateField(str, Enum):
    SECURITYCLASSIFICATION_6VMVOCHWUWO = 'securityClassification-6VMVochwUWo'


class Classification(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'box_security_classification_key': 'Box__Security__Classification__Key',
        'parent': '$parent',
        'template': '$template',
        'scope': '$scope',
        'version': '$version',
        'type': '$type',
        'type_version': '$typeVersion',
        'can_edit': '$canEdit',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'Box__Security__Classification__Key': 'box_security_classification_key',
        '$parent': 'parent',
        '$template': 'template',
        '$scope': 'scope',
        '$version': 'version',
        '$type': 'type',
        '$typeVersion': 'type_version',
        '$canEdit': 'can_edit',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        box_security_classification_key: Optional[str] = None,
        parent: Optional[str] = None,
        template: Optional[ClassificationTemplateField] = None,
        scope: Optional[str] = None,
        version: Optional[int] = None,
        type: Optional[str] = None,
        type_version: Optional[float] = None,
        can_edit: Optional[bool] = None,
        **kwargs
    ):
        """
        :param box_security_classification_key: The name of the classification applied to the item.
        :type box_security_classification_key: Optional[str], optional
        :param parent: The identifier of the item that this metadata instance
            has been attached to. This combines the `type` and the `id`
            of the parent in the form `{type}_{id}`.
        :type parent: Optional[str], optional
        :param template: `securityClassification-6VMVochwUWo`
        :type template: Optional[ClassificationTemplateField], optional
        :param scope: The scope of the enterprise that this classification has been
            applied for.
            This will be in the format `enterprise_{enterprise_id}`.
        :type scope: Optional[str], optional
        :param version: The version of the metadata instance. This version starts at 0 and
            increases every time a classification is updated.
        :type version: Optional[int], optional
        :param type: The unique ID of this classification instance. This will be include
            the name of the classification template and a unique ID.
        :type type: Optional[str], optional
        :param type_version: The version of the metadata template. This version starts at 0 and
            increases every time the template is updated. This is mostly for internal
            use.
        :type type_version: Optional[float], optional
        :param can_edit: Whether an end user can change the classification.
        :type can_edit: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.box_security_classification_key = box_security_classification_key
        self.parent = parent
        self.template = template
        self.scope = scope
        self.version = version
        self.type = type
        self.type_version = type_version
        self.can_edit = can_edit


class ClassificationTemplateTypeField(str, Enum):
    METADATA_TEMPLATE = 'metadata_template'


class ClassificationTemplateTemplateKeyField(str, Enum):
    SECURITYCLASSIFICATION_6VMVOCHWUWO = 'securityClassification-6VMVochwUWo'


class ClassificationTemplateDisplayNameField(str, Enum):
    CLASSIFICATION = 'Classification'


class ClassificationTemplateFieldsFieldTypeField(str, Enum):
    ENUM = 'enum'


class ClassificationTemplateFieldsFieldKeyField(str, Enum):
    BOX__SECURITY__CLASSIFICATION__KEY = 'Box__Security__Classification__Key'


class ClassificationTemplateFieldsFieldDisplayNameField(str, Enum):
    CLASSIFICATION = 'Classification'


class ClassificationTemplateFieldsFieldOptionsFieldStaticConfigFieldClassificationField(
    BaseObject
):
    _fields_to_json_mapping: Dict[str, str] = {
        'classification_definition': 'classificationDefinition',
        'color_id': 'colorID',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'classificationDefinition': 'classification_definition',
        'colorID': 'color_id',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        classification_definition: Optional[str] = None,
        color_id: Optional[float] = None,
        **kwargs
    ):
        """
        :param classification_definition: A longer description of the classification.
        :type classification_definition: Optional[str], optional
        :param color_id: An internal Box identifier used to assign a color to
            a classification label.
            Mapping between a `colorID` and a color may change
            without notice. Currently, the color mappings are as
            follows.
            * `0`: Yellow
            * `1`: Orange
            * `2`: Watermelon red
            * `3`: Purple rain
            * `4`: Light blue
            * `5`: Dark blue
            * `6`: Light green
            * `7`: Gray
        :type color_id: Optional[float], optional
        """
        super().__init__(**kwargs)
        self.classification_definition = classification_definition
        self.color_id = color_id


class ClassificationTemplateFieldsFieldOptionsFieldStaticConfigField(BaseObject):
    def __init__(
        self,
        classification: Optional[
            ClassificationTemplateFieldsFieldOptionsFieldStaticConfigFieldClassificationField
        ] = None,
        **kwargs
    ):
        """
        :param classification: Additional information about the classification.
            This is not an exclusive list of properties, and
            more object fields might be returned. These fields
            are used for internal Box Shield and Box Governance
            purposes and no additional value must be derived from
            these fields.
        :type classification: Optional[ClassificationTemplateFieldsFieldOptionsFieldStaticConfigFieldClassificationField], optional
        """
        super().__init__(**kwargs)
        self.classification = classification


class ClassificationTemplateFieldsFieldOptionsField(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'static_config': 'staticConfig',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'staticConfig': 'static_config',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        id: Optional[str] = None,
        key: Optional[str] = None,
        static_config: Optional[
            ClassificationTemplateFieldsFieldOptionsFieldStaticConfigField
        ] = None,
        **kwargs
    ):
        """
        :param id: The unique ID of this classification.
        :type id: Optional[str], optional
        :param key: The display name and key for this classification.
        :type key: Optional[str], optional
        :param static_config: Additional information about the classification.
        :type static_config: Optional[ClassificationTemplateFieldsFieldOptionsFieldStaticConfigField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.key = key
        self.static_config = static_config


class ClassificationTemplateFieldsField(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'display_name': 'displayName',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'displayName': 'display_name',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[ClassificationTemplateFieldsFieldTypeField] = None,
        key: Optional[ClassificationTemplateFieldsFieldKeyField] = None,
        display_name: Optional[
            ClassificationTemplateFieldsFieldDisplayNameField
        ] = None,
        hidden: Optional[bool] = None,
        options: Optional[List[ClassificationTemplateFieldsFieldOptionsField]] = None,
        **kwargs
    ):
        """
        :param id: The unique ID of the field.
        :type id: Optional[str], optional
        :param type: `enum`
        :type type: Optional[ClassificationTemplateFieldsFieldTypeField], optional
        :param key: `Box__Security__Classification__Key`
        :type key: Optional[ClassificationTemplateFieldsFieldKeyField], optional
        :param display_name: `Classification`
        :type display_name: Optional[ClassificationTemplateFieldsFieldDisplayNameField], optional
        :param hidden: Classifications are always visible to web and mobile users.
        :type hidden: Optional[bool], optional
        :param options: A list of classifications available in this enterprise.
        :type options: Optional[List[ClassificationTemplateFieldsFieldOptionsField]], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.key = key
        self.display_name = display_name
        self.hidden = hidden
        self.options = options


class ClassificationTemplate(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'template_key': 'templateKey',
        'display_name': 'displayName',
        'copy_instance_on_item_copy': 'copyInstanceOnItemCopy',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'templateKey': 'template_key',
        'displayName': 'display_name',
        'copyInstanceOnItemCopy': 'copy_instance_on_item_copy',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        type: ClassificationTemplateTypeField,
        id: Optional[str] = None,
        scope: Optional[str] = None,
        template_key: Optional[ClassificationTemplateTemplateKeyField] = None,
        display_name: Optional[ClassificationTemplateDisplayNameField] = None,
        hidden: Optional[bool] = None,
        copy_instance_on_item_copy: Optional[bool] = None,
        fields: Optional[List[ClassificationTemplateFieldsField]] = None,
        **kwargs
    ):
        """
        :param type: `metadata_template`
        :type type: ClassificationTemplateTypeField
        :param id: The ID of the classification template.
        :type id: Optional[str], optional
        :param scope: The scope of the classification template. This is in the format
            `enterprise_{id}` where the `id` is the enterprise ID.
        :type scope: Optional[str], optional
        :param template_key: `securityClassification-6VMVochwUWo`
        :type template_key: Optional[ClassificationTemplateTemplateKeyField], optional
        :param display_name: The name of this template as shown in web and mobile interfaces.
        :type display_name: Optional[ClassificationTemplateDisplayNameField], optional
        :param hidden: This template is always available in web and mobile interfaces.
        :type hidden: Optional[bool], optional
        :param copy_instance_on_item_copy: Classifications are always copied along when the file or folder is
            copied.
        :type copy_instance_on_item_copy: Optional[bool], optional
        :param fields: A list of fields for this classification template. This includes
            only one field, the `Box__Security__Classification__Key`, which defines
            the different classifications available in this enterprise.
        :type fields: Optional[List[ClassificationTemplateFieldsField]], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id
        self.scope = scope
        self.template_key = template_key
        self.display_name = display_name
        self.hidden = hidden
        self.copy_instance_on_item_copy = copy_instance_on_item_copy
        self.fields = fields


class CollaborationAllowlistEntryTypeField(str, Enum):
    COLLABORATION_WHITELIST_ENTRY = 'collaboration_whitelist_entry'


class CollaborationAllowlistEntryDirectionField(str, Enum):
    INBOUND = 'inbound'
    OUTBOUND = 'outbound'
    BOTH = 'both'


class CollaborationAllowlistEntryEnterpriseFieldTypeField(str, Enum):
    ENTERPRISE = 'enterprise'


class CollaborationAllowlistEntryEnterpriseField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[CollaborationAllowlistEntryEnterpriseFieldTypeField] = None,
        name: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this enterprise.
        :type id: Optional[str], optional
        :param type: `enterprise`
        :type type: Optional[CollaborationAllowlistEntryEnterpriseFieldTypeField], optional
        :param name: The name of the enterprise
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name


class CollaborationAllowlistEntry(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[CollaborationAllowlistEntryTypeField] = None,
        domain: Optional[str] = None,
        direction: Optional[CollaborationAllowlistEntryDirectionField] = None,
        enterprise: Optional[CollaborationAllowlistEntryEnterpriseField] = None,
        created_at: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this entry
        :type id: Optional[str], optional
        :param type: `collaboration_whitelist_entry`
        :type type: Optional[CollaborationAllowlistEntryTypeField], optional
        :param domain: The whitelisted domain
        :type domain: Optional[str], optional
        :param direction: The direction of the collaborations to allow.
        :type direction: Optional[CollaborationAllowlistEntryDirectionField], optional
        :param created_at: The time the entry was created at
        :type created_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.domain = domain
        self.direction = direction
        self.enterprise = enterprise
        self.created_at = created_at


class CollaborationAllowlistEntries(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[CollaborationAllowlistEntry]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of allowed collaboration domains
        :type entries: Optional[List[CollaborationAllowlistEntry]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class CollectionTypeField(str, Enum):
    COLLECTION = 'collection'


class CollectionNameField(str, Enum):
    FAVORITES = 'Favorites'


class CollectionCollectionTypeField(str, Enum):
    FAVORITES = 'favorites'


class Collection(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[CollectionTypeField] = None,
        name: Optional[CollectionNameField] = None,
        collection_type: Optional[CollectionCollectionTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this collection.
        :type id: Optional[str], optional
        :param type: `collection`
        :type type: Optional[CollectionTypeField], optional
        :param name: The name of the collection.
        :type name: Optional[CollectionNameField], optional
        :param collection_type: The type of the collection. This is used to
            determine the proper visual treatment for
            collections.
        :type collection_type: Optional[CollectionCollectionTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name
        self.collection_type = collection_type


class CollectionsOrderFieldDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class CollectionsOrderField(BaseObject):
    def __init__(
        self,
        by: Optional[str] = None,
        direction: Optional[CollectionsOrderFieldDirectionField] = None,
        **kwargs
    ):
        """
        :param by: The field to order by
        :type by: Optional[str], optional
        :param direction: The direction to order by, either ascending or descending
        :type direction: Optional[CollectionsOrderFieldDirectionField], optional
        """
        super().__init__(**kwargs)
        self.by = by
        self.direction = direction


class Collections(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[List[CollectionsOrderField]] = None,
        entries: Optional[List[Collection]] = None,
        **kwargs
    ):
        """
        :param total_count: One greater than the offset of the last entry in the entire collection.
            The total number of entries in the collection may be less than
            `total_count`.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type total_count: Optional[int], optional
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param offset: The 0-based offset of the first entry in this set. This will be the same
            as the `offset` query parameter.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type offset: Optional[int], optional
        :param order: The order by which items are returned.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type order: Optional[List[CollectionsOrderField]], optional
        :param entries: A list of collections
        :type entries: Optional[List[Collection]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.limit = limit
        self.offset = offset
        self.order = order
        self.entries = entries


class CommentBaseTypeField(str, Enum):
    COMMENT = 'comment'


class CommentBase(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[CommentBaseTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this comment.
        :type id: Optional[str], optional
        :param type: `comment`
        :type type: Optional[CommentBaseTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class EmailAliasTypeField(str, Enum):
    EMAIL_ALIAS = 'email_alias'


class EmailAlias(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[EmailAliasTypeField] = None,
        email: Optional[str] = None,
        is_confirmed: Optional[bool] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this object
        :type id: Optional[str], optional
        :param type: `email_alias`
        :type type: Optional[EmailAliasTypeField], optional
        :param email: The email address
        :type email: Optional[str], optional
        :param is_confirmed: Whether the email address has been confirmed
        :type is_confirmed: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.email = email
        self.is_confirmed = is_confirmed


class EmailAliases(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        entries: Optional[List[EmailAlias]] = None,
        **kwargs
    ):
        """
        :param total_count: The number of email aliases.
        :type total_count: Optional[int], optional
        :param entries: A list of email aliases
        :type entries: Optional[List[EmailAlias]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class EnterpriseBaseTypeField(str, Enum):
    ENTERPRISE = 'enterprise'


class EnterpriseBase(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[EnterpriseBaseTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this enterprise
        :type id: Optional[str], optional
        :param type: `enterprise`
        :type type: Optional[EnterpriseBaseTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class FileBaseTypeField(str, Enum):
    FILE = 'file'


class FileBase(BaseObject):
    def __init__(
        self, id: str, type: FileBaseTypeField, etag: Optional[str] = None, **kwargs
    ):
        """
        :param id: The unique identifier that represent a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
        :type id: str
        :param type: `file`
        :type type: FileBaseTypeField
        :param etag: The HTTP `etag` of this file. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the file if (no) changes have happened.
        :type etag: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.etag = etag


class FileVersionBaseTypeField(str, Enum):
    FILE_VERSION = 'file_version'


class FileVersionBase(BaseObject):
    def __init__(self, id: str, type: FileVersionBaseTypeField, **kwargs):
        """
        :param id: The unique identifier that represent a file version.
        :type id: str
        :param type: `file_version`
        :type type: FileVersionBaseTypeField
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class FileVersionMini(FileVersionBase):
    _fields_to_json_mapping: Dict[str, str] = {
        'sha_1': 'sha1',
        **FileVersionBase._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'sha1': 'sha_1',
        **FileVersionBase._json_to_fields_mapping,
    }

    def __init__(
        self,
        id: str,
        type: FileVersionBaseTypeField,
        sha_1: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a file version.
        :type id: str
        :param type: `file_version`
        :type type: FileVersionBaseTypeField
        :param sha_1: The SHA1 hash of this version of the file.
        :type sha_1: Optional[str], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.sha_1 = sha_1


class FileMini(FileBase):
    _fields_to_json_mapping: Dict[str, str] = {
        'sha_1': 'sha1',
        **FileBase._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'sha1': 'sha_1',
        **FileBase._json_to_fields_mapping,
    }

    def __init__(
        self,
        id: str,
        type: FileBaseTypeField,
        sequence_id: Optional[str] = None,
        name: Optional[str] = None,
        sha_1: Optional[str] = None,
        file_version: Optional[FileVersionMini] = None,
        etag: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
        :type id: str
        :param type: `file`
        :type type: FileBaseTypeField
        :param name: The name of the file
        :type name: Optional[str], optional
        :param sha_1: The SHA1 hash of the file. This can be used to compare the contents
            of a file on Box with a local file.
        :type sha_1: Optional[str], optional
        :param etag: The HTTP `etag` of this file. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the file if (no) changes have happened.
        :type etag: Optional[str], optional
        """
        super().__init__(id=id, type=type, etag=etag, **kwargs)
        self.sequence_id = sequence_id
        self.name = name
        self.sha_1 = sha_1
        self.file_version = file_version


class FileScopeScopeField(str, Enum):
    ANNOTATION_EDIT = 'annotation_edit'
    ANNOTATION_VIEW_ALL = 'annotation_view_all'
    ANNOTATION_VIEW_SELF = 'annotation_view_self'
    BASE_EXPLORER = 'base_explorer'
    BASE_PICKER = 'base_picker'
    BASE_PREVIEW = 'base_preview'
    BASE_UPLOAD = 'base_upload'
    ITEM_DELETE = 'item_delete'
    ITEM_DOWNLOAD = 'item_download'
    ITEM_PREVIEW = 'item_preview'
    ITEM_RENAME = 'item_rename'
    ITEM_SHARE = 'item_share'


class FileScope(BaseObject):
    def __init__(
        self,
        scope: Optional[FileScopeScopeField] = None,
        object: Optional[FileMini] = None,
        **kwargs
    ):
        """
        :param scope: The file scopes for the file access
        :type scope: Optional[FileScopeScopeField], optional
        """
        super().__init__(**kwargs)
        self.scope = scope
        self.object = object


class AccessTokenTokenTypeField(str, Enum):
    BEARER = 'bearer'


class AccessTokenIssuedTokenTypeField(str, Enum):
    URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_ACCESS_TOKEN = (
        'urn:ietf:params:oauth:token-type:access_token'
    )


class AccessToken(BaseObject):
    def __init__(
        self,
        access_token: Optional[str] = None,
        expires_in: Optional[int] = None,
        token_type: Optional[AccessTokenTokenTypeField] = None,
        restricted_to: Optional[List[FileScope]] = None,
        refresh_token: Optional[str] = None,
        issued_token_type: Optional[AccessTokenIssuedTokenTypeField] = None,
        **kwargs
    ):
        """
        :param access_token: The requested access token.
        :type access_token: Optional[str], optional
        :param expires_in: The time in seconds by which this token will expire.
        :type expires_in: Optional[int], optional
        :param token_type: The type of access token returned.
        :type token_type: Optional[AccessTokenTokenTypeField], optional
        :param restricted_to: The permissions that this access token permits,
            providing a list of resources (files, folders, etc)
            and the scopes permitted for each of those resources.
        :type restricted_to: Optional[List[FileScope]], optional
        :param refresh_token: The refresh token for this access token, which can be used
            to request a new access token when the current one expires.
        :type refresh_token: Optional[str], optional
        :param issued_token_type: The type of downscoped access token returned. This is only
            returned if an access token has been downscoped.
        :type issued_token_type: Optional[AccessTokenIssuedTokenTypeField], optional
        """
        super().__init__(**kwargs)
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.restricted_to = restricted_to
        self.refresh_token = refresh_token
        self.issued_token_type = issued_token_type


class FilesUnderRetention(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[FileMini]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of files
        :type entries: Optional[List[FileMini]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class FileConflict(FileMini):
    def __init__(
        self,
        id: str,
        type: FileBaseTypeField,
        sequence_id: Optional[str] = None,
        name: Optional[str] = None,
        sha_1: Optional[str] = None,
        file_version: Optional[FileVersionMini] = None,
        etag: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
        :type id: str
        :param type: `file`
        :type type: FileBaseTypeField
        :param name: The name of the file
        :type name: Optional[str], optional
        :param sha_1: The SHA1 hash of the file. This can be used to compare the contents
            of a file on Box with a local file.
        :type sha_1: Optional[str], optional
        :param etag: The HTTP `etag` of this file. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the file if (no) changes have happened.
        :type etag: Optional[str], optional
        """
        super().__init__(
            id=id,
            type=type,
            sequence_id=sequence_id,
            name=name,
            sha_1=sha_1,
            file_version=file_version,
            etag=etag,
            **kwargs
        )


class ConflictErrorContextInfoField(BaseObject):
    def __init__(self, conflicts: Optional[List[FileConflict]] = None, **kwargs):
        """
        :param conflicts: A list of the file conflicts that caused this error.
        :type conflicts: Optional[List[FileConflict]], optional
        """
        super().__init__(**kwargs)
        self.conflicts = conflicts


class ConflictError(ClientError):
    def __init__(
        self,
        type: Optional[ClientErrorTypeField] = None,
        status: Optional[int] = None,
        code: Optional[ClientErrorCodeField] = None,
        message: Optional[str] = None,
        context_info: Optional[ClientErrorContextInfoField] = None,
        help_url: Optional[str] = None,
        request_id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: error
        :type type: Optional[ClientErrorTypeField], optional
        :param status: The HTTP status of the response.
        :type status: Optional[int], optional
        :param code: A Box-specific error code
        :type code: Optional[ClientErrorCodeField], optional
        :param message: A short message describing the error.
        :type message: Optional[str], optional
        :param context_info: A free-form object that contains additional context
            about the error. The possible fields are defined on
            a per-endpoint basis. `message` is only one example.
        :type context_info: Optional[ClientErrorContextInfoField], optional
        :param help_url: A URL that links to more information about why this error occurred.
        :type help_url: Optional[str], optional
        :param request_id: A unique identifier for this response, which can be used
            when contacting Box support.
        :type request_id: Optional[str], optional
        """
        super().__init__(
            type=type,
            status=status,
            code=code,
            message=message,
            context_info=context_info,
            help_url=help_url,
            request_id=request_id,
            **kwargs
        )


class FolderBaseTypeField(str, Enum):
    FOLDER = 'folder'


class FolderBase(BaseObject):
    def __init__(
        self, id: str, type: FolderBaseTypeField, etag: Optional[str] = None, **kwargs
    ):
        """
        :param id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting a folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folders/123`
            the `folder_id` is `123`.
        :type id: str
        :param type: `folder`
        :type type: FolderBaseTypeField
        :param etag: The HTTP `etag` of this folder. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the folder if (no) changes have happened.
        :type etag: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.etag = etag


class FolderMini(FolderBase):
    def __init__(
        self,
        id: str,
        type: FolderBaseTypeField,
        sequence_id: Optional[str] = None,
        name: Optional[str] = None,
        etag: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting a folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folders/123`
            the `folder_id` is `123`.
        :type id: str
        :param type: `folder`
        :type type: FolderBaseTypeField
        :param name: The name of the folder.
        :type name: Optional[str], optional
        :param etag: The HTTP `etag` of this folder. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the folder if (no) changes have happened.
        :type etag: Optional[str], optional
        """
        super().__init__(id=id, type=type, etag=etag, **kwargs)
        self.sequence_id = sequence_id
        self.name = name


class IntegrationMappingBaseIntegrationTypeField(str, Enum):
    SLACK = 'slack'


class IntegrationMappingBase(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        integration_type: Optional[IntegrationMappingBaseIntegrationTypeField] = None,
        **kwargs
    ):
        """
        :param id: A unique identifier of a folder mapping
            (part of a composite key together
            with `integration_type`)
        :type id: Optional[str], optional
        :param integration_type: Identifies the Box partner app,
            with which the mapping is associated.
            Currently only supports Slack.
            (part of the composite key together with `id`)
        :type integration_type: Optional[IntegrationMappingBaseIntegrationTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.integration_type = integration_type


class IntegrationMappingMiniPartnerItemTypeField(str, Enum):
    CHANNEL = 'channel'


class IntegrationMappingMiniBoxItemTypeField(str, Enum):
    FOLDER = 'folder'


class IntegrationMappingMini(IntegrationMappingBase):
    def __init__(
        self,
        partner_item_id: Optional[str] = None,
        partner_item_type: Optional[IntegrationMappingMiniPartnerItemTypeField] = None,
        box_item_id: Optional[str] = None,
        box_item_type: Optional[IntegrationMappingMiniBoxItemTypeField] = None,
        id: Optional[str] = None,
        integration_type: Optional[IntegrationMappingBaseIntegrationTypeField] = None,
        **kwargs
    ):
        """
        :param partner_item_id: ID of the mapped partner item
        :type partner_item_id: Optional[str], optional
        :param partner_item_type: Domain-specific type of the mapped partner item
        :type partner_item_type: Optional[IntegrationMappingMiniPartnerItemTypeField], optional
        :param box_item_id: ID of the Box item mapped to the object referenced in `partner_item_id`
        :type box_item_id: Optional[str], optional
        :param box_item_type: Type of the Box object referenced in `box_item_id`
        :type box_item_type: Optional[IntegrationMappingMiniBoxItemTypeField], optional
        :param id: A unique identifier of a folder mapping
            (part of a composite key together
            with `integration_type`)
        :type id: Optional[str], optional
        :param integration_type: Identifies the Box partner app,
            with which the mapping is associated.
            Currently only supports Slack.
            (part of the composite key together with `id`)
        :type integration_type: Optional[IntegrationMappingBaseIntegrationTypeField], optional
        """
        super().__init__(id=id, integration_type=integration_type, **kwargs)
        self.partner_item_id = partner_item_id
        self.partner_item_type = partner_item_type
        self.box_item_id = box_item_id
        self.box_item_type = box_item_type


class GroupBaseTypeField(str, Enum):
    GROUP = 'group'


class GroupBase(BaseObject):
    def __init__(self, id: str, type: GroupBaseTypeField, **kwargs):
        """
        :param id: The unique identifier for this object
        :type id: str
        :param type: `group`
        :type type: GroupBaseTypeField
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class GroupMiniGroupTypeField(str, Enum):
    MANAGED_GROUP = 'managed_group'
    ALL_USERS_GROUP = 'all_users_group'


class GroupMini(GroupBase):
    def __init__(
        self,
        id: str,
        type: GroupBaseTypeField,
        name: Optional[str] = None,
        group_type: Optional[GroupMiniGroupTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this object
        :type id: str
        :param type: `group`
        :type type: GroupBaseTypeField
        :param name: The name of the group
        :type name: Optional[str], optional
        :param group_type: The type of the group.
        :type group_type: Optional[GroupMiniGroupTypeField], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.name = name
        self.group_type = group_type


class GroupsOrderFieldDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class GroupsOrderField(BaseObject):
    def __init__(
        self,
        by: Optional[str] = None,
        direction: Optional[GroupsOrderFieldDirectionField] = None,
        **kwargs
    ):
        """
        :param by: The field to order by
        :type by: Optional[str], optional
        :param direction: The direction to order by, either ascending or descending
        :type direction: Optional[GroupsOrderFieldDirectionField], optional
        """
        super().__init__(**kwargs)
        self.by = by
        self.direction = direction


class Groups(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[List[GroupsOrderField]] = None,
        entries: Optional[List[GroupMini]] = None,
        **kwargs
    ):
        """
        :param total_count: One greater than the offset of the last entry in the entire collection.
            The total number of entries in the collection may be less than
            `total_count`.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type total_count: Optional[int], optional
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param offset: The 0-based offset of the first entry in this set. This will be the same
            as the `offset` query parameter.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type offset: Optional[int], optional
        :param order: The order by which items are returned.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type order: Optional[List[GroupsOrderField]], optional
        :param entries: A list of groups
        :type entries: Optional[List[GroupMini]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.limit = limit
        self.offset = offset
        self.order = order
        self.entries = entries


class Group(GroupMini):
    def __init__(
        self,
        id: str,
        type: GroupBaseTypeField,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        name: Optional[str] = None,
        group_type: Optional[GroupMiniGroupTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this object
        :type id: str
        :param type: `group`
        :type type: GroupBaseTypeField
        :param created_at: When the group object was created
        :type created_at: Optional[str], optional
        :param modified_at: When the group object was last modified
        :type modified_at: Optional[str], optional
        :param name: The name of the group
        :type name: Optional[str], optional
        :param group_type: The type of the group.
        :type group_type: Optional[GroupMiniGroupTypeField], optional
        """
        super().__init__(id=id, type=type, name=name, group_type=group_type, **kwargs)
        self.created_at = created_at
        self.modified_at = modified_at


class GroupFullInvitabilityLevelField(str, Enum):
    ADMINS_ONLY = 'admins_only'
    ADMINS_AND_MEMBERS = 'admins_and_members'
    ALL_MANAGED_USERS = 'all_managed_users'


class GroupFullMemberViewabilityLevelField(str, Enum):
    ADMINS_ONLY = 'admins_only'
    ADMINS_AND_MEMBERS = 'admins_and_members'
    ALL_MANAGED_USERS = 'all_managed_users'


class GroupFullPermissionsField(BaseObject):
    def __init__(self, can_invite_as_collaborator: Optional[bool] = None, **kwargs):
        """
        :param can_invite_as_collaborator: Specifies if the user can invite the group to collaborate on any items.
        :type can_invite_as_collaborator: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.can_invite_as_collaborator = can_invite_as_collaborator


class GroupFull(Group):
    def __init__(
        self,
        id: str,
        type: GroupBaseTypeField,
        provenance: Optional[str] = None,
        external_sync_identifier: Optional[str] = None,
        description: Optional[str] = None,
        invitability_level: Optional[GroupFullInvitabilityLevelField] = None,
        member_viewability_level: Optional[GroupFullMemberViewabilityLevelField] = None,
        permissions: Optional[GroupFullPermissionsField] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        name: Optional[str] = None,
        group_type: Optional[GroupMiniGroupTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this object
        :type id: str
        :param type: `group`
        :type type: GroupBaseTypeField
        :param provenance: Keeps track of which external source this group is
            coming from (e.g. "Active Directory", "Google Groups",
            "Facebook Groups").  Setting this will
            also prevent Box users from editing the group name
            and its members directly via the Box web application.
            This is desirable for one-way syncing of groups.
        :type provenance: Optional[str], optional
        :param external_sync_identifier: An arbitrary identifier that can be used by
            external group sync tools to link this Box Group to
            an external group. Example values of this field
            could be an Active Directory Object ID or a Google
            Group ID.  We recommend you use of this field in
            order to avoid issues when group names are updated in
            either Box or external systems.
        :type external_sync_identifier: Optional[str], optional
        :param description: Human readable description of the group.
        :type description: Optional[str], optional
        :param invitability_level: Specifies who can invite the group to collaborate
            on items.
            When set to `admins_only` the enterprise admin, co-admins,
            and the group's admin can invite the group.
            When set to `admins_and_members` all the admins listed
            above and group members can invite the group.
            When set to `all_managed_users` all managed users in the
            enterprise can invite the group.
        :type invitability_level: Optional[GroupFullInvitabilityLevelField], optional
        :param member_viewability_level: Specifies who can view the members of the group
            (Get Memberships for Group).
            * `admins_only` - the enterprise admin, co-admins, group's
              group admin
            * `admins_and_members` - all admins and group members
            * `all_managed_users` - all managed users in the
              enterprise
        :type member_viewability_level: Optional[GroupFullMemberViewabilityLevelField], optional
        :param created_at: When the group object was created
        :type created_at: Optional[str], optional
        :param modified_at: When the group object was last modified
        :type modified_at: Optional[str], optional
        :param name: The name of the group
        :type name: Optional[str], optional
        :param group_type: The type of the group.
        :type group_type: Optional[GroupMiniGroupTypeField], optional
        """
        super().__init__(
            id=id,
            type=type,
            created_at=created_at,
            modified_at=modified_at,
            name=name,
            group_type=group_type,
            **kwargs
        )
        self.provenance = provenance
        self.external_sync_identifier = external_sync_identifier
        self.description = description
        self.invitability_level = invitability_level
        self.member_viewability_level = member_viewability_level
        self.permissions = permissions


class LegalHoldPolicyMiniTypeField(str, Enum):
    LEGAL_HOLD_POLICY = 'legal_hold_policy'


class LegalHoldPolicyMini(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[LegalHoldPolicyMiniTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this legal hold policy
        :type id: Optional[str], optional
        :param type: `legal_hold_policy`
        :type type: Optional[LegalHoldPolicyMiniTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class LegalHoldPolicyAssignmentBaseTypeField(str, Enum):
    LEGAL_HOLD_POLICY_ASSIGNMENT = 'legal_hold_policy_assignment'


class LegalHoldPolicyAssignmentBase(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[LegalHoldPolicyAssignmentBaseTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this legal hold assignment
        :type id: Optional[str], optional
        :param type: `legal_hold_policy_assignment`
        :type type: Optional[LegalHoldPolicyAssignmentBaseTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class LegalHoldPolicyAssignments(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[LegalHoldPolicyAssignmentBase]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of legal hold
            policy assignments
        :type entries: Optional[List[LegalHoldPolicyAssignmentBase]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class MetadataBase(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'parent': '$parent',
        'template': '$template',
        'scope': '$scope',
        'version': '$version',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        '$parent': 'parent',
        '$template': 'template',
        '$scope': 'scope',
        '$version': 'version',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        parent: Optional[str] = None,
        template: Optional[str] = None,
        scope: Optional[str] = None,
        version: Optional[int] = None,
        **kwargs
    ):
        """
        :param parent: The identifier of the item that this metadata instance
            has been attached to. This combines the `type` and the `id`
            of the parent in the form `{type}_{id}`.
        :type parent: Optional[str], optional
        :param template: The name of the template
        :type template: Optional[str], optional
        :param scope: An ID for the scope in which this template
            has been applied. This will be `enterprise_{enterprise_id}` for templates
            defined for use in this enterprise, and `global` for general templates
            that are available to all enterprises using Box.
        :type scope: Optional[str], optional
        :param version: The version of the metadata instance. This version starts at 0 and
            increases every time a user-defined property is modified.
        :type version: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.parent = parent
        self.template = template
        self.scope = scope
        self.version = version


class Metadata(MetadataBase):
    def __init__(
        self,
        parent: Optional[str] = None,
        template: Optional[str] = None,
        scope: Optional[str] = None,
        version: Optional[int] = None,
        **kwargs
    ):
        """
        :param parent: The identifier of the item that this metadata instance
            has been attached to. This combines the `type` and the `id`
            of the parent in the form `{type}_{id}`.
        :type parent: Optional[str], optional
        :param template: The name of the template
        :type template: Optional[str], optional
        :param scope: An ID for the scope in which this template
            has been applied. This will be `enterprise_{enterprise_id}` for templates
            defined for use in this enterprise, and `global` for general templates
            that are available to all enterprises using Box.
        :type scope: Optional[str], optional
        :param version: The version of the metadata instance. This version starts at 0 and
            increases every time a user-defined property is modified.
        :type version: Optional[int], optional
        """
        super().__init__(
            parent=parent, template=template, scope=scope, version=version, **kwargs
        )


class Metadatas(BaseObject):
    def __init__(
        self,
        entries: Optional[List[Metadata]] = None,
        limit: Optional[int] = None,
        **kwargs
    ):
        """
        :param entries: A list of metadata instances, as applied to this file or folder.
        :type entries: Optional[List[Metadata]], optional
        :param limit: The limit that was used for this page of results.
        :type limit: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.entries = entries
        self.limit = limit


class MetadataFull(Metadata):
    _fields_to_json_mapping: Dict[str, str] = {
        'can_edit': '$canEdit',
        'id': '$id',
        'type': '$type',
        'type_version': '$typeVersion',
        **Metadata._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        '$canEdit': 'can_edit',
        '$id': 'id',
        '$type': 'type',
        '$typeVersion': 'type_version',
        **Metadata._json_to_fields_mapping,
    }

    def __init__(
        self,
        can_edit: Optional[bool] = None,
        id: Optional[str] = None,
        type: Optional[str] = None,
        type_version: Optional[int] = None,
        parent: Optional[str] = None,
        template: Optional[str] = None,
        scope: Optional[str] = None,
        version: Optional[int] = None,
        **kwargs
    ):
        """
        :param can_edit: Whether the user can edit this metadata instance.
        :type can_edit: Optional[bool], optional
        :param id: A UUID to identify the metadata instance.
        :type id: Optional[str], optional
        :param type: A unique identifier for the "type" of this instance. This is an
            internal system property and should not be used by a client
            application.
        :type type: Optional[str], optional
        :param type_version: The last-known version of the template of the object. This is an
            internal system property and should not be used by a client
            application.
        :type type_version: Optional[int], optional
        :param parent: The identifier of the item that this metadata instance
            has been attached to. This combines the `type` and the `id`
            of the parent in the form `{type}_{id}`.
        :type parent: Optional[str], optional
        :param template: The name of the template
        :type template: Optional[str], optional
        :param scope: An ID for the scope in which this template
            has been applied. This will be `enterprise_{enterprise_id}` for templates
            defined for use in this enterprise, and `global` for general templates
            that are available to all enterprises using Box.
        :type scope: Optional[str], optional
        :param version: The version of the metadata instance. This version starts at 0 and
            increases every time a user-defined property is modified.
        :type version: Optional[int], optional
        """
        super().__init__(
            parent=parent, template=template, scope=scope, version=version, **kwargs
        )
        self.can_edit = can_edit
        self.id = id
        self.type = type
        self.type_version = type_version
        self.extra_data = kwargs


class MetadataCascadePolicyTypeField(str, Enum):
    METADATA_CASCADE_POLICY = 'metadata_cascade_policy'


class MetadataCascadePolicyOwnerEnterpriseFieldTypeField(str, Enum):
    ENTERPRISE = 'enterprise'


class MetadataCascadePolicyOwnerEnterpriseField(BaseObject):
    def __init__(
        self,
        type: Optional[MetadataCascadePolicyOwnerEnterpriseFieldTypeField] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: `enterprise`
        :type type: Optional[MetadataCascadePolicyOwnerEnterpriseFieldTypeField], optional
        :param id: The ID of the enterprise that owns the policy.
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class MetadataCascadePolicyParentFieldTypeField(str, Enum):
    FOLDER = 'folder'


class MetadataCascadePolicyParentField(BaseObject):
    def __init__(
        self,
        type: Optional[MetadataCascadePolicyParentFieldTypeField] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: `folder`
        :type type: Optional[MetadataCascadePolicyParentFieldTypeField], optional
        :param id: The ID of the folder the policy is applied to.
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class MetadataCascadePolicyScopeField(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE__ = 'enterprise_*'


class MetadataCascadePolicy(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'template_key': 'templateKey',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'templateKey': 'template_key',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[MetadataCascadePolicyTypeField] = None,
        owner_enterprise: Optional[MetadataCascadePolicyOwnerEnterpriseField] = None,
        parent: Optional[MetadataCascadePolicyParentField] = None,
        scope: Optional[MetadataCascadePolicyScopeField] = None,
        template_key: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The ID of the metadata cascade policy object
        :type id: Optional[str], optional
        :param type: `metadata_cascade_policy`
        :type type: Optional[MetadataCascadePolicyTypeField], optional
        :param owner_enterprise: The enterprise that owns this policy.
        :type owner_enterprise: Optional[MetadataCascadePolicyOwnerEnterpriseField], optional
        :param parent: Represent the folder the policy is applied to.
        :type parent: Optional[MetadataCascadePolicyParentField], optional
        :param scope: The scope of the of the template that is cascaded down to the folder's
            children.
        :type scope: Optional[MetadataCascadePolicyScopeField], optional
        :param template_key: The key of the template that is cascaded down to the folder's
            children.
            In many cases the template key is automatically derived
            of its display name, for example `Contract Template` would
            become `contractTemplate`. In some cases the creator of the
            template will have provided its own template key.
            Please [list the templates for an enterprise][list], or
            get all instances on a [file][file] or [folder][folder]
            to inspect a template's key.
            [list]: e://get-metadata-templates-enterprise
            [file]: e://get-files-id-metadata
            [folder]: e://get-folders-id-metadata
        :type template_key: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.owner_enterprise = owner_enterprise
        self.parent = parent
        self.scope = scope
        self.template_key = template_key


class MetadataCascadePolicies(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[MetadataCascadePolicy]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of metadata cascade policies
        :type entries: Optional[List[MetadataCascadePolicy]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class MetadataQueryIndexStatusField(str, Enum):
    BUILDING = 'building'
    ACTIVE = 'active'
    DISABLED = 'disabled'


class MetadataQueryIndexFieldsFieldSortDirectionField(str, Enum):
    ASC = 'asc'
    DESC = 'desc'


class MetadataQueryIndexFieldsField(BaseObject):
    def __init__(
        self,
        key: Optional[str] = None,
        sort_direction: Optional[
            MetadataQueryIndexFieldsFieldSortDirectionField
        ] = None,
        **kwargs
    ):
        """
        :param key: The metadata template field key.
        :type key: Optional[str], optional
        :param sort_direction: The sort direction of the field.
        :type sort_direction: Optional[MetadataQueryIndexFieldsFieldSortDirectionField], optional
        """
        super().__init__(**kwargs)
        self.key = key
        self.sort_direction = sort_direction


class MetadataQueryIndex(BaseObject):
    def __init__(
        self,
        type: str,
        status: MetadataQueryIndexStatusField,
        id: Optional[str] = None,
        fields: Optional[List[MetadataQueryIndexFieldsField]] = None,
        **kwargs
    ):
        """
        :param type: Value is always `metadata_query_index`
        :type type: str
        :param status: The status of the metadata query index
        :type status: MetadataQueryIndexStatusField
        :param id: The ID of the metadata query index.
        :type id: Optional[str], optional
        :param fields: A list of template fields which make up the index.
        :type fields: Optional[List[MetadataQueryIndexFieldsField]], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.status = status
        self.id = id
        self.fields = fields


class MetadataQueryIndices(BaseObject):
    def __init__(
        self,
        entries: Optional[List[MetadataQueryIndex]] = None,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        **kwargs
    ):
        """
        :param entries: A collection of metadata query indices.
        :type entries: Optional[List[MetadataQueryIndex]], optional
        :param limit: The limit that was used for this request.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.entries = entries
        self.limit = limit
        self.next_marker = next_marker


class MetadataTemplateTypeField(str, Enum):
    METADATA_TEMPLATE = 'metadata_template'


class MetadataTemplateFieldsFieldTypeField(str, Enum):
    STRING = 'string'
    FLOAT = 'float'
    DATE = 'date'
    ENUM = 'enum'
    MULTISELECT = 'multiSelect'
    INTEGER = 'integer'


class MetadataTemplateFieldsFieldOptionsField(BaseObject):
    def __init__(self, key: str, id: Optional[str] = None, **kwargs):
        """
        :param key: The text value of the option. This represents both the display name of the
            option and the internal key used when updating templates.
        :type key: str
        :param id: The internal unique identifier of the the option.
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.key = key
        self.id = id


class MetadataTemplateFieldsField(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'display_name': 'displayName',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'displayName': 'display_name',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        type: MetadataTemplateFieldsFieldTypeField,
        key: str,
        display_name: str,
        description: Optional[str] = None,
        hidden: Optional[bool] = None,
        options: Optional[List[MetadataTemplateFieldsFieldOptionsField]] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: The type of field. The basic fields are a `string` field for text, a
            `float` field for numbers, and a `date` fields to present the user with a
            date-time picker.
            Additionally, metadata templates support an `enum` field for a basic list
            of items, and ` multiSelect` field for a similar list of items where the
            user can select more than one value.
            **Note**: The `integer` value is deprecated.
            It is still present in the response,
            but cannot be used in the POST request.
        :type type: MetadataTemplateFieldsFieldTypeField
        :param key: A unique identifier for the field. The identifier must
            be unique within the template to which it belongs.
        :type key: str
        :param display_name: The display name of the field as it is shown to the user in the web and
            mobile apps.
        :type display_name: str
        :param description: A description of the field. This is not shown to the user.
        :type description: Optional[str], optional
        :param hidden: Whether this field is hidden in the UI for the user and can only be set
            through the API instead.
        :type hidden: Optional[bool], optional
        :param options: A list of options for this field. This is used in combination
            with the `enum` and `multiSelect` field types.
        :type options: Optional[List[MetadataTemplateFieldsFieldOptionsField]], optional
        :param id: The unique ID of the metadata template field.
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.key = key
        self.display_name = display_name
        self.description = description
        self.hidden = hidden
        self.options = options
        self.id = id


class MetadataTemplate(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'template_key': 'templateKey',
        'display_name': 'displayName',
        'copy_instance_on_item_copy': 'copyInstanceOnItemCopy',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'templateKey': 'template_key',
        'displayName': 'display_name',
        'copyInstanceOnItemCopy': 'copy_instance_on_item_copy',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        type: MetadataTemplateTypeField,
        id: Optional[str] = None,
        scope: Optional[str] = None,
        template_key: Optional[str] = None,
        display_name: Optional[str] = None,
        hidden: Optional[bool] = None,
        fields: Optional[List[MetadataTemplateFieldsField]] = None,
        copy_instance_on_item_copy: Optional[bool] = None,
        **kwargs
    ):
        """
        :param type: `metadata_template`
        :type type: MetadataTemplateTypeField
        :param id: The ID of the metadata template.
        :type id: Optional[str], optional
        :param scope: The scope of the metadata template can either be `global` or
            `enterprise_*`. The `global` scope is used for templates that are
            available to any Box enterprise. The `enterprise_*` scope represents
            templates that have been created within a specific enterprise, where `*`
            will be the ID of that enterprise.
        :type scope: Optional[str], optional
        :param template_key: A unique identifier for the template. This identifier is unique across
            the `scope` of the enterprise to which the metadata template is being
            applied, yet is not necessarily unique across different enterprises.
        :type template_key: Optional[str], optional
        :param display_name: The display name of the template. This can be seen in the Box web app
            and mobile apps.
        :type display_name: Optional[str], optional
        :param hidden: Defines if this template is visible in the Box web app UI, or if
            it is purely intended for usage through the API.
        :type hidden: Optional[bool], optional
        :param fields: An ordered list of template fields which are part of the template. Each
            field can be a regular text field, date field, number field, as well as a
            single or multi-select list.
        :type fields: Optional[List[MetadataTemplateFieldsField]], optional
        :param copy_instance_on_item_copy: Whether or not to include the metadata when a file or folder is copied.
        :type copy_instance_on_item_copy: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id
        self.scope = scope
        self.template_key = template_key
        self.display_name = display_name
        self.hidden = hidden
        self.fields = fields
        self.copy_instance_on_item_copy = copy_instance_on_item_copy


class MetadataTemplates(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[MetadataTemplate]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of metadata templates
        :type entries: Optional[List[MetadataTemplate]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class RealtimeServer(BaseObject):
    def __init__(
        self,
        type: Optional[str] = None,
        url: Optional[str] = None,
        ttl: Optional[int] = None,
        max_retries: Optional[int] = None,
        retry_timeout: Optional[int] = None,
        **kwargs
    ):
        """
        :param type: `realtime_server`
        :type type: Optional[str], optional
        :param url: The URL for the server.
        :type url: Optional[str], optional
        :param ttl: The time in minutes for which this server is available
        :type ttl: Optional[int], optional
        :param max_retries: The maximum number of retries this server will
            allow before a new long poll should be started by
            getting a [new list of server](#options-events).
        :type max_retries: Optional[int], optional
        :param retry_timeout: The maximum number of seconds without a response
            after which you should retry the long poll connection.
            This helps to overcome network issues where the long
            poll looks to be working but no packages are coming
            through.
        :type retry_timeout: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.url = url
        self.ttl = ttl
        self.max_retries = max_retries
        self.retry_timeout = retry_timeout


class RealtimeServers(BaseObject):
    def __init__(
        self,
        chunk_size: Optional[int] = None,
        entries: Optional[List[RealtimeServer]] = None,
        **kwargs
    ):
        """
        :param chunk_size: The number of items in this response.
        :type chunk_size: Optional[int], optional
        :param entries: A list of real-time servers
        :type entries: Optional[List[RealtimeServer]], optional
        """
        super().__init__(**kwargs)
        self.chunk_size = chunk_size
        self.entries = entries


class RetentionPolicyBaseTypeField(str, Enum):
    RETENTION_POLICY = 'retention_policy'


class RetentionPolicyBase(BaseObject):
    def __init__(self, id: str, type: RetentionPolicyBaseTypeField, **kwargs):
        """
        :param id: The unique identifier that represents a retention policy.
        :type id: str
        :param type: `retention_policy`
        :type type: RetentionPolicyBaseTypeField
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class RetentionPolicyMiniDispositionActionField(str, Enum):
    PERMANENTLY_DELETE = 'permanently_delete'
    REMOVE_RETENTION = 'remove_retention'


class RetentionPolicyMini(RetentionPolicyBase):
    def __init__(
        self,
        id: str,
        type: RetentionPolicyBaseTypeField,
        policy_name: Optional[str] = None,
        retention_length: Optional[str] = None,
        disposition_action: Optional[RetentionPolicyMiniDispositionActionField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represents a retention policy.
        :type id: str
        :param type: `retention_policy`
        :type type: RetentionPolicyBaseTypeField
        :param policy_name: The name given to the retention policy.
        :type policy_name: Optional[str], optional
        :param retention_length: The length of the retention policy. This value
            specifies the duration in days that the retention
            policy will be active for after being assigned to
            content.  If the policy has a `policy_type` of
            `indefinite`, the `retention_length` will also be
            `indefinite`.
        :type retention_length: Optional[str], optional
        :param disposition_action: The disposition action of the retention policy.
            This action can be `permanently_delete`, which
            will cause the content retained by the policy
            to be permanently deleted, or `remove_retention`,
            which will lift the retention policy from the content,
            allowing it to be deleted by users,
            once the retention policy has expired.
        :type disposition_action: Optional[RetentionPolicyMiniDispositionActionField], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.policy_name = policy_name
        self.retention_length = retention_length
        self.disposition_action = disposition_action


class RetentionPolicies(BaseObject):
    def __init__(
        self,
        entries: Optional[List[RetentionPolicyMini]] = None,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        **kwargs
    ):
        """
        :param entries: A list in which each entry represents a retention policy object.
        :type entries: Optional[List[RetentionPolicyMini]], optional
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.entries = entries
        self.limit = limit
        self.next_marker = next_marker


class FileVersionRetentionTypeField(str, Enum):
    FILE_VERSION_RETENTION = 'file_version_retention'


class FileVersionRetention(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[FileVersionRetentionTypeField] = None,
        file_version: Optional[FileVersionMini] = None,
        file: Optional[FileMini] = None,
        applied_at: Optional[str] = None,
        disposition_at: Optional[str] = None,
        winning_retention_policy: Optional[RetentionPolicyMini] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this file version retention.
        :type id: Optional[str], optional
        :param type: `file_version_retention`
        :type type: Optional[FileVersionRetentionTypeField], optional
        :param applied_at: When this file version retention object was
            created
        :type applied_at: Optional[str], optional
        :param disposition_at: When the retention expires on this file
            version retention
        :type disposition_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.file_version = file_version
        self.file = file
        self.applied_at = applied_at
        self.disposition_at = disposition_at
        self.winning_retention_policy = winning_retention_policy


class FileVersionRetentions(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[FileVersionRetention]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of file version retentions
        :type entries: Optional[List[FileVersionRetention]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class RetentionPolicyAssignmentBaseTypeField(str, Enum):
    RETENTION_POLICY_ASSIGNMENT = 'retention_policy_assignment'


class RetentionPolicyAssignmentBase(BaseObject):
    def __init__(self, id: str, type: RetentionPolicyAssignmentBaseTypeField, **kwargs):
        """
        :param id: The unique identifier that represents a file version.
        :type id: str
        :param type: `retention_policy_assignment`
        :type type: RetentionPolicyAssignmentBaseTypeField
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class ShieldInformationBarrierBaseTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER = 'shield_information_barrier'


class ShieldInformationBarrierBase(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[ShieldInformationBarrierBaseTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for the shield information barrier
        :type id: Optional[str], optional
        :param type: The type of the shield information barrier
        :type type: Optional[ShieldInformationBarrierBaseTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class ShieldInformationBarrierReference(BaseObject):
    def __init__(
        self,
        shield_information_barrier: Optional[ShieldInformationBarrierBase] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.shield_information_barrier = shield_information_barrier


class ShieldInformationBarrierReportBaseTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER_REPORT = 'shield_information_barrier_report'


class ShieldInformationBarrierReportBase(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[ShieldInformationBarrierReportBaseTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for the shield information barrier report
        :type id: Optional[str], optional
        :param type: The type of the shield information barrier report
        :type type: Optional[ShieldInformationBarrierReportBaseTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class ShieldInformationBarrierSegmentMemberBaseTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBER = (
        'shield_information_barrier_segment_member'
    )


class ShieldInformationBarrierSegmentMemberBase(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[ShieldInformationBarrierSegmentMemberBaseTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for the
            shield information barrier segment member
        :type id: Optional[str], optional
        :param type: The type of the shield information barrier segment member
        :type type: Optional[ShieldInformationBarrierSegmentMemberBaseTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class ShieldInformationBarrierSegmentRestrictionBaseTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTION = (
        'shield_information_barrier_segment_restriction'
    )


class ShieldInformationBarrierSegmentRestrictionBase(BaseObject):
    def __init__(
        self,
        type: Optional[ShieldInformationBarrierSegmentRestrictionBaseTypeField] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: Shield information barrier segment restriction
        :type type: Optional[ShieldInformationBarrierSegmentRestrictionBaseTypeField], optional
        :param id: The unique identifier for the
            shield information barrier segment restriction.
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class ShieldInformationBarrierSegmentRestrictionMiniShieldInformationBarrierSegmentFieldTypeField(
    str, Enum
):
    SHIELD_INFORMATION_BARRIER_SEGMENT = 'shield_information_barrier_segment'


class ShieldInformationBarrierSegmentRestrictionMiniShieldInformationBarrierSegmentField(
    BaseObject
):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[
            ShieldInformationBarrierSegmentRestrictionMiniShieldInformationBarrierSegmentFieldTypeField
        ] = None,
        **kwargs
    ):
        """
        :param id: The ID reference of the
            requesting shield information barrier segment.
        :type id: Optional[str], optional
        :param type: The type of the shield information barrier segment
        :type type: Optional[ShieldInformationBarrierSegmentRestrictionMiniShieldInformationBarrierSegmentFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class ShieldInformationBarrierSegmentRestrictionMiniRestrictedSegmentFieldTypeField(
    str, Enum
):
    SHIELD_INFORMATION_BARRIER_SEGMENT = 'shield_information_barrier_segment'


class ShieldInformationBarrierSegmentRestrictionMiniRestrictedSegmentField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[
            ShieldInformationBarrierSegmentRestrictionMiniRestrictedSegmentFieldTypeField
        ] = None,
        **kwargs
    ):
        """
        :param id: The ID reference of the
            restricted shield information barrier segment.
        :type id: Optional[str], optional
        :param type: The type of the shield information segment
        :type type: Optional[ShieldInformationBarrierSegmentRestrictionMiniRestrictedSegmentFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class ShieldInformationBarrierSegmentRestrictionMini(
    ShieldInformationBarrierSegmentRestrictionBase
):
    def __init__(
        self,
        shield_information_barrier_segment: ShieldInformationBarrierSegmentRestrictionMiniShieldInformationBarrierSegmentField,
        restricted_segment: ShieldInformationBarrierSegmentRestrictionMiniRestrictedSegmentField,
        type: Optional[ShieldInformationBarrierSegmentRestrictionBaseTypeField] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        """
        :param shield_information_barrier_segment: The `type` and `id` of the
            requested shield information barrier segment.
        :type shield_information_barrier_segment: ShieldInformationBarrierSegmentRestrictionMiniShieldInformationBarrierSegmentField
        :param restricted_segment: The `type` and `id` of the
            restricted shield information barrier segment.
        :type restricted_segment: ShieldInformationBarrierSegmentRestrictionMiniRestrictedSegmentField
        :param type: Shield information barrier segment restriction
        :type type: Optional[ShieldInformationBarrierSegmentRestrictionBaseTypeField], optional
        :param id: The unique identifier for the
            shield information barrier segment restriction.
        :type id: Optional[str], optional
        """
        super().__init__(type=type, id=id, **kwargs)
        self.shield_information_barrier_segment = shield_information_barrier_segment
        self.restricted_segment = restricted_segment


class SessionTerminationMessage(BaseObject):
    def __init__(self, message: Optional[str] = None, **kwargs):
        """
        :param message: The unique identifier for the termination job status
        :type message: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.message = message


class StoragePolicyMiniTypeField(str, Enum):
    STORAGE_POLICY = 'storage_policy'


class StoragePolicyMini(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[StoragePolicyMiniTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this storage policy
        :type id: Optional[str], optional
        :param type: `storage_policy`
        :type type: Optional[StoragePolicyMiniTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class StoragePolicyAssignmentAssignedToField(BaseObject):
    def __init__(self, id: Optional[str] = None, type: Optional[str] = None, **kwargs):
        """
        :param id: The unique identifier for this object
        :type id: Optional[str], optional
        :param type: The type for this object
        :type type: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class StoragePolicyAssignment(BaseObject):
    def __init__(
        self,
        storage_policy: Optional[StoragePolicyMini] = None,
        assigned_to: Optional[StoragePolicyAssignmentAssignedToField] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.storage_policy = storage_policy
        self.assigned_to = assigned_to


class StoragePolicyAssignments(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[StoragePolicyAssignment]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of storage policy assignments
        :type entries: Optional[List[StoragePolicyAssignment]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class StoragePolicy(StoragePolicyMini):
    def __init__(
        self,
        name: Optional[str] = None,
        id: Optional[str] = None,
        type: Optional[StoragePolicyMiniTypeField] = None,
        **kwargs
    ):
        """
        :param name: A descriptive name of the region
        :type name: Optional[str], optional
        :param id: The unique identifier for this storage policy
        :type id: Optional[str], optional
        :param type: `storage_policy`
        :type type: Optional[StoragePolicyMiniTypeField], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.name = name


class StoragePolicies(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[StoragePolicy]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of storage policies
        :type entries: Optional[List[StoragePolicy]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class TermsOfServiceBaseTypeField(str, Enum):
    TERMS_OF_SERVICE = 'terms_of_service'


class TermsOfServiceBase(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[TermsOfServiceBaseTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this terms of service.
        :type id: Optional[str], optional
        :param type: `terms_of_service`
        :type type: Optional[TermsOfServiceBaseTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class TermsOfServiceStatusField(str, Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'


class TermsOfServiceEnterpriseFieldTypeField(str, Enum):
    ENTERPRISE = 'enterprise'


class TermsOfServiceEnterpriseField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[TermsOfServiceEnterpriseFieldTypeField] = None,
        name: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this enterprise.
        :type id: Optional[str], optional
        :param type: `enterprise`
        :type type: Optional[TermsOfServiceEnterpriseFieldTypeField], optional
        :param name: The name of the enterprise
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name


class TermsOfServiceTosTypeField(str, Enum):
    MANAGED = 'managed'
    EXTERNAL = 'external'


class TermsOfService(TermsOfServiceBase):
    def __init__(
        self,
        status: Optional[TermsOfServiceStatusField] = None,
        enterprise: Optional[TermsOfServiceEnterpriseField] = None,
        tos_type: Optional[TermsOfServiceTosTypeField] = None,
        text: Optional[str] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        id: Optional[str] = None,
        type: Optional[TermsOfServiceBaseTypeField] = None,
        **kwargs
    ):
        """
        :param status: Whether these terms are enabled or not
        :type status: Optional[TermsOfServiceStatusField], optional
        :param tos_type: Whether to apply these terms to managed users or external users
        :type tos_type: Optional[TermsOfServiceTosTypeField], optional
        :param text: The text for your terms and conditions. This text could be
            empty if the `status` is set to `disabled`.
        :type text: Optional[str], optional
        :param created_at: When the legal item was created
        :type created_at: Optional[str], optional
        :param modified_at: When the legal item was modified.
        :type modified_at: Optional[str], optional
        :param id: The unique identifier for this terms of service.
        :type id: Optional[str], optional
        :param type: `terms_of_service`
        :type type: Optional[TermsOfServiceBaseTypeField], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.status = status
        self.enterprise = enterprise
        self.tos_type = tos_type
        self.text = text
        self.created_at = created_at
        self.modified_at = modified_at


class TermsOfServices(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        entries: Optional[List[TermsOfService]] = None,
        **kwargs
    ):
        """
        :param total_count: The total number of objects.
        :type total_count: Optional[int], optional
        :param entries: A list of terms of service objects
        :type entries: Optional[List[TermsOfService]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class UploadPartMini(BaseObject):
    def __init__(
        self,
        part_id: Optional[str] = None,
        offset: Optional[int] = None,
        size: Optional[int] = None,
        **kwargs
    ):
        """
        :param part_id: The unique ID of the chunk.
        :type part_id: Optional[str], optional
        :param offset: The offset of the chunk within the file
            in bytes. The lower bound of the position
            of the chunk within the file.
        :type offset: Optional[int], optional
        :param size: The size of the chunk in bytes.
        :type size: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.part_id = part_id
        self.offset = offset
        self.size = size


class UploadPart(UploadPartMini):
    _fields_to_json_mapping: Dict[str, str] = {
        'sha_1': 'sha1',
        **UploadPartMini._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'sha1': 'sha_1',
        **UploadPartMini._json_to_fields_mapping,
    }

    def __init__(
        self,
        sha_1: Optional[str] = None,
        part_id: Optional[str] = None,
        offset: Optional[int] = None,
        size: Optional[int] = None,
        **kwargs
    ):
        """
        :param sha_1: The SHA1 hash of the chunk.
        :type sha_1: Optional[str], optional
        :param part_id: The unique ID of the chunk.
        :type part_id: Optional[str], optional
        :param offset: The offset of the chunk within the file
            in bytes. The lower bound of the position
            of the chunk within the file.
        :type offset: Optional[int], optional
        :param size: The size of the chunk in bytes.
        :type size: Optional[int], optional
        """
        super().__init__(part_id=part_id, offset=offset, size=size, **kwargs)
        self.sha_1 = sha_1


class UploadPartsOrderFieldDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class UploadPartsOrderField(BaseObject):
    def __init__(
        self,
        by: Optional[str] = None,
        direction: Optional[UploadPartsOrderFieldDirectionField] = None,
        **kwargs
    ):
        """
        :param by: The field to order by
        :type by: Optional[str], optional
        :param direction: The direction to order by, either ascending or descending
        :type direction: Optional[UploadPartsOrderFieldDirectionField], optional
        """
        super().__init__(**kwargs)
        self.by = by
        self.direction = direction


class UploadParts(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[List[UploadPartsOrderField]] = None,
        entries: Optional[List[UploadPart]] = None,
        **kwargs
    ):
        """
        :param total_count: One greater than the offset of the last entry in the entire collection.
            The total number of entries in the collection may be less than
            `total_count`.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type total_count: Optional[int], optional
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param offset: The 0-based offset of the first entry in this set. This will be the same
            as the `offset` query parameter.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type offset: Optional[int], optional
        :param order: The order by which items are returned.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type order: Optional[List[UploadPartsOrderField]], optional
        :param entries: A list of uploaded chunks for an upload
            session
        :type entries: Optional[List[UploadPart]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.limit = limit
        self.offset = offset
        self.order = order
        self.entries = entries


class UploadedPart(BaseObject):
    def __init__(self, part: Optional[UploadPart] = None, **kwargs):
        super().__init__(**kwargs)
        self.part = part


class UploadSessionTypeField(str, Enum):
    UPLOAD_SESSION = 'upload_session'


class UploadSessionSessionEndpointsField(BaseObject):
    def __init__(
        self,
        upload_part: Optional[str] = None,
        commit: Optional[str] = None,
        abort: Optional[str] = None,
        list_parts: Optional[str] = None,
        status: Optional[str] = None,
        log_event: Optional[str] = None,
        **kwargs
    ):
        """
        :param upload_part: The URL to upload parts to
        :type upload_part: Optional[str], optional
        :param commit: The URL used to commit the file
        :type commit: Optional[str], optional
        :param abort: The URL for used to abort the session.
        :type abort: Optional[str], optional
        :param list_parts: The URL users to list all parts.
        :type list_parts: Optional[str], optional
        :param status: The URL used to get the status of the upload.
        :type status: Optional[str], optional
        :param log_event: The URL used to get the upload log from.
        :type log_event: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.upload_part = upload_part
        self.commit = commit
        self.abort = abort
        self.list_parts = list_parts
        self.status = status
        self.log_event = log_event


class UploadSession(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[UploadSessionTypeField] = None,
        session_expires_at: Optional[str] = None,
        part_size: Optional[int] = None,
        total_parts: Optional[int] = None,
        num_parts_processed: Optional[int] = None,
        session_endpoints: Optional[UploadSessionSessionEndpointsField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this session
        :type id: Optional[str], optional
        :param type: `upload_session`
        :type type: Optional[UploadSessionTypeField], optional
        :param session_expires_at: The date and time when this session expires.
        :type session_expires_at: Optional[str], optional
        :param part_size: The  size in bytes that must be used for all parts of of the
            upload.
            Only the last part is allowed to be of a smaller size.
        :type part_size: Optional[int], optional
        :param total_parts: The total number of parts expected in this upload session,
            as determined by the file size and part size.
        :type total_parts: Optional[int], optional
        :param num_parts_processed: The number of parts that have been uploaded and processed
            by the server. This starts at `0`.
            When committing a file files, inspecting this property can
            provide insight if all parts have been uploaded correctly.
        :type num_parts_processed: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.session_expires_at = session_expires_at
        self.part_size = part_size
        self.total_parts = total_parts
        self.num_parts_processed = num_parts_processed
        self.session_endpoints = session_endpoints


class UploadUrl(BaseObject):
    def __init__(
        self,
        upload_url: Optional[str] = None,
        upload_token: Optional[str] = None,
        **kwargs
    ):
        """
        :param upload_url: A URL for an upload session that can be used to upload
            the file.
        :type upload_url: Optional[str], optional
        :param upload_token: An optional access token to use to upload the file
        :type upload_token: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.upload_url = upload_url
        self.upload_token = upload_token


class UserAvatarPicUrlsField(BaseObject):
    def __init__(
        self,
        small: Optional[str] = None,
        large: Optional[str] = None,
        preview: Optional[str] = None,
        **kwargs
    ):
        """
        :param small: The location of a small-sized avatar.
        :type small: Optional[str], optional
        :param large: The location of a large-sized avatar.
        :type large: Optional[str], optional
        :param preview: The location of the avatar preview.
        :type preview: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.small = small
        self.large = large
        self.preview = preview


class UserAvatar(BaseObject):
    def __init__(self, pic_urls: Optional[UserAvatarPicUrlsField] = None, **kwargs):
        """
        :param pic_urls: Represents an object with user avatar URLs.
        :type pic_urls: Optional[UserAvatarPicUrlsField], optional
        """
        super().__init__(**kwargs)
        self.pic_urls = pic_urls


class UserBaseTypeField(str, Enum):
    USER = 'user'


class UserBase(BaseObject):
    def __init__(self, id: str, type: UserBaseTypeField, **kwargs):
        """
        :param id: The unique identifier for this user
        :type id: str
        :param type: `user`
        :type type: UserBaseTypeField
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class UserIntegrationMappings(UserBase):
    def __init__(
        self,
        id: str,
        type: UserBaseTypeField,
        name: Optional[str] = None,
        login: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this user
        :type id: str
        :param type: `user`
        :type type: UserBaseTypeField
        :param name: The display name of this user
        :type name: Optional[str], optional
        :param login: The primary email address of this user
        :type login: Optional[str], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.name = name
        self.login = login


class UserCollaborations(UserBase):
    def __init__(
        self,
        id: str,
        type: UserBaseTypeField,
        name: Optional[str] = None,
        login: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this user
        :type id: str
        :param type: `user`
        :type type: UserBaseTypeField
        :param name: The display name of this user. If the collaboration status is `pending`, an empty string is returned.
        :type name: Optional[str], optional
        :param login: The primary email address of this user. If the collaboration status is `pending`, an empty string is returned.
        :type login: Optional[str], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.name = name
        self.login = login


class UserMini(UserBase):
    def __init__(
        self,
        id: str,
        type: UserBaseTypeField,
        name: Optional[str] = None,
        login: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this user
        :type id: str
        :param type: `user`
        :type type: UserBaseTypeField
        :param name: The display name of this user
        :type name: Optional[str], optional
        :param login: The primary email address of this user
        :type login: Optional[str], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.name = name
        self.login = login


class EventSourceItemTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'


class EventSourceClassificationField(BaseObject):
    def __init__(self, name: Optional[str] = None, **kwargs):
        """
        :param name: The classification's name
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.name = name


class EventSource(BaseObject):
    def __init__(
        self,
        item_type: EventSourceItemTypeField,
        item_id: str,
        item_name: str,
        classification: Optional[EventSourceClassificationField] = None,
        parent: Optional[FolderMini] = None,
        owned_by: Optional[UserMini] = None,
        **kwargs
    ):
        """
        :param item_type: The type of the item that the event
            represents. Can be `file` or `folder`.
        :type item_type: EventSourceItemTypeField
        :param item_id: The unique identifier that represents the
            item.
        :type item_id: str
        :param item_name: The name of the item.
        :type item_name: str
        :param classification: The object containing classification information for the item that
            triggered the event. This field will not appear if the item does not
            have a classification set.
        :type classification: Optional[EventSourceClassificationField], optional
        """
        super().__init__(**kwargs)
        self.item_type = item_type
        self.item_id = item_id
        self.item_name = item_name
        self.classification = classification
        self.parent = parent
        self.owned_by = owned_by


class UserStatusField(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    CANNOT_DELETE_EDIT = 'cannot_delete_edit'
    CANNOT_DELETE_EDIT_UPLOAD = 'cannot_delete_edit_upload'


class UserNotificationEmailField(BaseObject):
    def __init__(
        self, email: Optional[str] = None, is_confirmed: Optional[bool] = None, **kwargs
    ):
        """
        :param email: The email address to send the notifications to.
        :type email: Optional[str], optional
        :param is_confirmed: Specifies if this email address has been confirmed.
        :type is_confirmed: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.email = email
        self.is_confirmed = is_confirmed


class User(UserMini):
    def __init__(
        self,
        id: str,
        type: UserBaseTypeField,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        language: Optional[str] = None,
        timezone: Optional[str] = None,
        space_amount: Optional[int] = None,
        space_used: Optional[int] = None,
        max_upload_size: Optional[int] = None,
        status: Optional[UserStatusField] = None,
        job_title: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None,
        avatar_url: Optional[str] = None,
        notification_email: Optional[UserNotificationEmailField] = None,
        name: Optional[str] = None,
        login: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this user
        :type id: str
        :param type: `user`
        :type type: UserBaseTypeField
        :param created_at: When the user object was created
        :type created_at: Optional[str], optional
        :param modified_at: When the user object was last modified
        :type modified_at: Optional[str], optional
        :param language: The language of the user, formatted in modified version of the
            [ISO 639-1](/guides/api-calls/language-codes) format.
        :type language: Optional[str], optional
        :param timezone: The user's timezone
        :type timezone: Optional[str], optional
        :param space_amount: The user’s total available space amount in bytes
        :type space_amount: Optional[int], optional
        :param space_used: The amount of space in use by the user
        :type space_used: Optional[int], optional
        :param max_upload_size: The maximum individual file size in bytes the user can have
        :type max_upload_size: Optional[int], optional
        :param status: The user's account status
        :type status: Optional[UserStatusField], optional
        :param job_title: The user’s job title
        :type job_title: Optional[str], optional
        :param phone: The user’s phone number
        :type phone: Optional[str], optional
        :param address: The user’s address
        :type address: Optional[str], optional
        :param avatar_url: URL of the user’s avatar image
        :type avatar_url: Optional[str], optional
        :param notification_email: An alternate notification email address to which email
            notifications are sent. When it's confirmed, this will be
            the email address to which notifications are sent instead of
            to the primary email address.
        :type notification_email: Optional[UserNotificationEmailField], optional
        :param name: The display name of this user
        :type name: Optional[str], optional
        :param login: The primary email address of this user
        :type login: Optional[str], optional
        """
        super().__init__(id=id, type=type, name=name, login=login, **kwargs)
        self.created_at = created_at
        self.modified_at = modified_at
        self.language = language
        self.timezone = timezone
        self.space_amount = space_amount
        self.space_used = space_used
        self.max_upload_size = max_upload_size
        self.status = status
        self.job_title = job_title
        self.phone = phone
        self.address = address
        self.avatar_url = avatar_url
        self.notification_email = notification_email


class UsersOrderFieldDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class UsersOrderField(BaseObject):
    def __init__(
        self,
        by: Optional[str] = None,
        direction: Optional[UsersOrderFieldDirectionField] = None,
        **kwargs
    ):
        """
        :param by: The field to order by
        :type by: Optional[str], optional
        :param direction: The direction to order by, either ascending or descending
        :type direction: Optional[UsersOrderFieldDirectionField], optional
        """
        super().__init__(**kwargs)
        self.by = by
        self.direction = direction


class Users(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[List[UsersOrderField]] = None,
        entries: Optional[List[User]] = None,
        **kwargs
    ):
        """
        :param total_count: One greater than the offset of the last entry in the entire collection.
            The total number of entries in the collection may be less than
            `total_count`.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type total_count: Optional[int], optional
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param offset: The 0-based offset of the first entry in this set. This will be the same
            as the `offset` query parameter.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type offset: Optional[int], optional
        :param order: The order by which items are returned.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type order: Optional[List[UsersOrderField]], optional
        :param entries: A list of users
        :type entries: Optional[List[User]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.limit = limit
        self.offset = offset
        self.order = order
        self.entries = entries


class TrashWebLinkRestoredTypeField(str, Enum):
    WEB_LINK = 'web_link'


class TrashWebLinkRestoredPathCollectionField(BaseObject):
    def __init__(self, total_count: int, entries: List[FolderMini], **kwargs):
        """
        :param total_count: The number of folders in this list.
        :type total_count: int
        :param entries: The parent folders for this item
        :type entries: List[FolderMini]
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class TrashWebLinkRestoredItemStatusField(str, Enum):
    ACTIVE = 'active'
    TRASHED = 'trashed'
    DELETED = 'deleted'


class TrashWebLinkRestored(BaseObject):
    def __init__(
        self,
        sequence_id: str,
        path_collection: TrashWebLinkRestoredPathCollectionField,
        type: Optional[TrashWebLinkRestoredTypeField] = None,
        id: Optional[str] = None,
        etag: Optional[str] = None,
        name: Optional[str] = None,
        url: Optional[str] = None,
        parent: Optional[FolderMini] = None,
        description: Optional[str] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        trashed_at: Optional[str] = None,
        purged_at: Optional[str] = None,
        created_by: Optional[UserMini] = None,
        modified_by: Optional[UserMini] = None,
        owned_by: Optional[UserMini] = None,
        shared_link: Optional[str] = None,
        item_status: Optional[TrashWebLinkRestoredItemStatusField] = None,
        **kwargs
    ):
        """
        :param type: `web_link`
        :type type: Optional[TrashWebLinkRestoredTypeField], optional
        :param id: The unique identifier for this web link
        :type id: Optional[str], optional
        :param etag: The entity tag of this web link. Used with `If-Match`
            headers.
        :type etag: Optional[str], optional
        :param name: The name of the web link
        :type name: Optional[str], optional
        :param url: The URL this web link points to
        :type url: Optional[str], optional
        :param description: The description accompanying the web link. This is
            visible within the Box web application.
        :type description: Optional[str], optional
        :param created_at: When this file was created on Box’s servers.
        :type created_at: Optional[str], optional
        :param modified_at: When this file was last updated on the Box
            servers.
        :type modified_at: Optional[str], optional
        :param trashed_at: The time at which this bookmark was put in the
            trash - becomes `null` after restore.
        :type trashed_at: Optional[str], optional
        :param purged_at: The time at which this bookmark will be permanently
            deleted - becomes `null` after restore.
        :type purged_at: Optional[str], optional
        :param shared_link: The shared link for this bookmark. This will
            be `null` if a bookmark had been trashed, even though the original shared
            link does become active again.
        :type shared_link: Optional[str], optional
        :param item_status: Whether this item is deleted or not. Values include `active`,
            `trashed` if the file has been moved to the trash, and `deleted` if
            the file has been permanently deleted
        :type item_status: Optional[TrashWebLinkRestoredItemStatusField], optional
        """
        super().__init__(**kwargs)
        self.sequence_id = sequence_id
        self.path_collection = path_collection
        self.type = type
        self.id = id
        self.etag = etag
        self.name = name
        self.url = url
        self.parent = parent
        self.description = description
        self.created_at = created_at
        self.modified_at = modified_at
        self.trashed_at = trashed_at
        self.purged_at = purged_at
        self.created_by = created_by
        self.modified_by = modified_by
        self.owned_by = owned_by
        self.shared_link = shared_link
        self.item_status = item_status


class TrashFolderRestoredTypeField(str, Enum):
    FOLDER = 'folder'


class TrashFolderRestoredPathCollectionField(BaseObject):
    def __init__(self, total_count: int, entries: List[FolderMini], **kwargs):
        """
        :param total_count: The number of folders in this list.
        :type total_count: int
        :param entries: The parent folders for this item
        :type entries: List[FolderMini]
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class TrashFolderRestoredItemStatusField(str, Enum):
    ACTIVE = 'active'
    TRASHED = 'trashed'
    DELETED = 'deleted'


class TrashFolderRestored(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        etag: Optional[str] = None,
        type: Optional[TrashFolderRestoredTypeField] = None,
        sequence_id: Optional[str] = None,
        name: Optional[str] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        description: Optional[str] = None,
        size: Optional[int] = None,
        path_collection: Optional[TrashFolderRestoredPathCollectionField] = None,
        created_by: Optional[UserMini] = None,
        modified_by: Optional[UserMini] = None,
        trashed_at: Optional[str] = None,
        purged_at: Optional[str] = None,
        content_created_at: Optional[str] = None,
        content_modified_at: Optional[str] = None,
        owned_by: Optional[UserMini] = None,
        shared_link: Optional[str] = None,
        folder_upload_email: Optional[str] = None,
        parent: Optional[FolderMini] = None,
        item_status: Optional[TrashFolderRestoredItemStatusField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting a folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folders/123`
            the `folder_id` is `123`.
        :type id: Optional[str], optional
        :param etag: The HTTP `etag` of this folder. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the folder if (no) changes have happened.
        :type etag: Optional[str], optional
        :param type: `folder`
        :type type: Optional[TrashFolderRestoredTypeField], optional
        :param name: The name of the folder.
        :type name: Optional[str], optional
        :param created_at: The date and time when the folder was created. This value may
            be `null` for some folders such as the root folder or the trash
            folder.
        :type created_at: Optional[str], optional
        :param modified_at: The date and time when the folder was last updated. This value may
            be `null` for some folders such as the root folder or the trash
            folder.
        :type modified_at: Optional[str], optional
        :param size: The folder size in bytes.
            Be careful parsing this integer as its
            value can get very large.
        :type size: Optional[int], optional
        :param trashed_at: The time at which this folder was put in the
            trash - becomes `null` after restore.
        :type trashed_at: Optional[str], optional
        :param purged_at: The time at which this folder is expected to be purged
            from the trash  - becomes `null` after restore.
        :type purged_at: Optional[str], optional
        :param content_created_at: The date and time at which this folder was originally
            created.
        :type content_created_at: Optional[str], optional
        :param content_modified_at: The date and time at which this folder was last updated.
        :type content_modified_at: Optional[str], optional
        :param shared_link: The shared link for this file. This will
            be `null` if a folder had been trashed, even though the original shared
            link does become active again.
        :type shared_link: Optional[str], optional
        :param folder_upload_email: The folder upload email for this folder. This will
            be `null` if a folder has been trashed, even though the original upload
            email does become active again.
        :type folder_upload_email: Optional[str], optional
        :param item_status: Defines if this item has been deleted or not.
            * `active` when the item has is not in the trash
            * `trashed` when the item has been moved to the trash but not deleted
            * `deleted` when the item has been permanently deleted.
        :type item_status: Optional[TrashFolderRestoredItemStatusField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.etag = etag
        self.type = type
        self.sequence_id = sequence_id
        self.name = name
        self.created_at = created_at
        self.modified_at = modified_at
        self.description = description
        self.size = size
        self.path_collection = path_collection
        self.created_by = created_by
        self.modified_by = modified_by
        self.trashed_at = trashed_at
        self.purged_at = purged_at
        self.content_created_at = content_created_at
        self.content_modified_at = content_modified_at
        self.owned_by = owned_by
        self.shared_link = shared_link
        self.folder_upload_email = folder_upload_email
        self.parent = parent
        self.item_status = item_status


class TrashFileRestoredTypeField(str, Enum):
    FILE = 'file'


class TrashFileRestoredPathCollectionField(BaseObject):
    def __init__(self, total_count: int, entries: List[FolderMini], **kwargs):
        """
        :param total_count: The number of folders in this list.
        :type total_count: int
        :param entries: The parent folders for this item
        :type entries: List[FolderMini]
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class TrashFileRestoredItemStatusField(str, Enum):
    ACTIVE = 'active'
    TRASHED = 'trashed'
    DELETED = 'deleted'


class TrashFileRestored(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'sha_1': 'sha1',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'sha1': 'sha_1',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        id: str,
        type: TrashFileRestoredTypeField,
        sequence_id: str,
        sha_1: str,
        description: str,
        size: int,
        path_collection: TrashFileRestoredPathCollectionField,
        created_at: str,
        modified_at: str,
        modified_by: UserMini,
        owned_by: UserMini,
        item_status: TrashFileRestoredItemStatusField,
        etag: Optional[str] = None,
        name: Optional[str] = None,
        file_version: Optional[FileVersionMini] = None,
        trashed_at: Optional[str] = None,
        purged_at: Optional[str] = None,
        content_created_at: Optional[str] = None,
        content_modified_at: Optional[str] = None,
        created_by: Optional[UserMini] = None,
        shared_link: Optional[str] = None,
        parent: Optional[FolderMini] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
        :type id: str
        :param type: `file`
        :type type: TrashFileRestoredTypeField
        :param sha_1: The SHA1 hash of the file. This can be used to compare the contents
            of a file on Box with a local file.
        :type sha_1: str
        :param description: The optional description of this file
        :type description: str
        :param size: The file size in bytes. Be careful parsing this integer as it can
            get very large and cause an integer overflow.
        :type size: int
        :param created_at: The date and time when the file was created on Box.
        :type created_at: str
        :param modified_at: The date and time when the file was last updated on Box.
        :type modified_at: str
        :param item_status: Defines if this item has been deleted or not.
            * `active` when the item has is not in the trash
            * `trashed` when the item has been moved to the trash but not deleted
            * `deleted` when the item has been permanently deleted.
        :type item_status: TrashFileRestoredItemStatusField
        :param etag: The HTTP `etag` of this file. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the file if (no) changes have happened.
        :type etag: Optional[str], optional
        :param name: The name of the file
        :type name: Optional[str], optional
        :param trashed_at: The time at which this file was put in the
            trash - becomes `null` after restore.
        :type trashed_at: Optional[str], optional
        :param purged_at: The time at which this file is expected to be purged
            from the trash  - becomes `null` after restore.
        :type purged_at: Optional[str], optional
        :param content_created_at: The date and time at which this file was originally
            created, which might be before it was uploaded to Box.
        :type content_created_at: Optional[str], optional
        :param content_modified_at: The date and time at which this file was last updated,
            which might be before it was uploaded to Box.
        :type content_modified_at: Optional[str], optional
        :param shared_link: The shared link for this file. This will
            be `null` if a file had been trashed, even though the original shared
            link does become active again.
        :type shared_link: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.sequence_id = sequence_id
        self.sha_1 = sha_1
        self.description = description
        self.size = size
        self.path_collection = path_collection
        self.created_at = created_at
        self.modified_at = modified_at
        self.modified_by = modified_by
        self.owned_by = owned_by
        self.item_status = item_status
        self.etag = etag
        self.name = name
        self.file_version = file_version
        self.trashed_at = trashed_at
        self.purged_at = purged_at
        self.content_created_at = content_created_at
        self.content_modified_at = content_modified_at
        self.created_by = created_by
        self.shared_link = shared_link
        self.parent = parent


class TrashWebLinkTypeField(str, Enum):
    WEB_LINK = 'web_link'


class TrashWebLinkPathCollectionFieldEntriesFieldTypeField(str, Enum):
    FOLDER = 'folder'


class TrashWebLinkPathCollectionFieldEntriesField(BaseObject):
    def __init__(
        self,
        type: Optional[TrashWebLinkPathCollectionFieldEntriesFieldTypeField] = None,
        id: Optional[str] = None,
        sequence_id: Optional[str] = None,
        etag: Optional[str] = None,
        name: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: `folder`
        :type type: Optional[TrashWebLinkPathCollectionFieldEntriesFieldTypeField], optional
        :param id: The unique identifier that represent a folder.
        :type id: Optional[str], optional
        :param sequence_id: This field is null for the Trash folder
        :type sequence_id: Optional[str], optional
        :param etag: This field is null for the Trash folder
        :type etag: Optional[str], optional
        :param name: The name of the Trash folder.
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id
        self.sequence_id = sequence_id
        self.etag = etag
        self.name = name


class TrashWebLinkPathCollectionField(BaseObject):
    def __init__(
        self,
        total_count: int,
        entries: List[TrashWebLinkPathCollectionFieldEntriesField],
        **kwargs
    ):
        """
        :param total_count: The number of folders in this list.
        :type total_count: int
        :param entries: Array of folders for this item's path collection
        :type entries: List[TrashWebLinkPathCollectionFieldEntriesField]
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class TrashWebLinkItemStatusField(str, Enum):
    ACTIVE = 'active'
    TRASHED = 'trashed'
    DELETED = 'deleted'


class TrashWebLink(BaseObject):
    def __init__(
        self,
        type: Optional[TrashWebLinkTypeField] = None,
        id: Optional[str] = None,
        sequence_id: Optional[str] = None,
        etag: Optional[str] = None,
        name: Optional[str] = None,
        url: Optional[str] = None,
        parent: Optional[FolderMini] = None,
        description: Optional[str] = None,
        path_collection: Optional[TrashWebLinkPathCollectionField] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        trashed_at: Optional[str] = None,
        purged_at: Optional[str] = None,
        created_by: Optional[UserMini] = None,
        modified_by: Optional[UserMini] = None,
        owned_by: Optional[UserMini] = None,
        shared_link: Optional[str] = None,
        item_status: Optional[TrashWebLinkItemStatusField] = None,
        **kwargs
    ):
        """
        :param type: `web_link`
        :type type: Optional[TrashWebLinkTypeField], optional
        :param id: The unique identifier for this web link
        :type id: Optional[str], optional
        :param etag: The entity tag of this web link. Used with `If-Match`
            headers.
        :type etag: Optional[str], optional
        :param name: The name of the web link
        :type name: Optional[str], optional
        :param url: The URL this web link points to
        :type url: Optional[str], optional
        :param description: The description accompanying the web link. This is
            visible within the Box web application.
        :type description: Optional[str], optional
        :param created_at: When this file was created on Box’s servers.
        :type created_at: Optional[str], optional
        :param modified_at: When this file was last updated on the Box
            servers.
        :type modified_at: Optional[str], optional
        :param trashed_at: When this file was last moved to the trash.
        :type trashed_at: Optional[str], optional
        :param purged_at: When this file will be permanently deleted.
        :type purged_at: Optional[str], optional
        :param shared_link: The shared link for this bookmark. This will
            be `null` if a bookmark has been trashed, since the link will no longer
            be active.
        :type shared_link: Optional[str], optional
        :param item_status: Whether this item is deleted or not. Values include `active`,
            `trashed` if the file has been moved to the trash, and `deleted` if
            the file has been permanently deleted
        :type item_status: Optional[TrashWebLinkItemStatusField], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id
        self.sequence_id = sequence_id
        self.etag = etag
        self.name = name
        self.url = url
        self.parent = parent
        self.description = description
        self.path_collection = path_collection
        self.created_at = created_at
        self.modified_at = modified_at
        self.trashed_at = trashed_at
        self.purged_at = purged_at
        self.created_by = created_by
        self.modified_by = modified_by
        self.owned_by = owned_by
        self.shared_link = shared_link
        self.item_status = item_status


class TrashFolderTypeField(str, Enum):
    FOLDER = 'folder'


class TrashFolderPathCollectionFieldEntriesFieldTypeField(str, Enum):
    FOLDER = 'folder'


class TrashFolderPathCollectionFieldEntriesField(BaseObject):
    def __init__(
        self,
        type: Optional[TrashFolderPathCollectionFieldEntriesFieldTypeField] = None,
        id: Optional[str] = None,
        sequence_id: Optional[str] = None,
        etag: Optional[str] = None,
        name: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: `folder`
        :type type: Optional[TrashFolderPathCollectionFieldEntriesFieldTypeField], optional
        :param id: The unique identifier that represent a folder.
        :type id: Optional[str], optional
        :param sequence_id: This field is null for the Trash folder
        :type sequence_id: Optional[str], optional
        :param etag: This field is null for the Trash folder
        :type etag: Optional[str], optional
        :param name: The name of the Trash folder.
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id
        self.sequence_id = sequence_id
        self.etag = etag
        self.name = name


class TrashFolderPathCollectionField(BaseObject):
    def __init__(
        self,
        total_count: int,
        entries: List[TrashFolderPathCollectionFieldEntriesField],
        **kwargs
    ):
        """
        :param total_count: The number of folders in this list.
        :type total_count: int
        :param entries: Array of folders for this item's path collection
        :type entries: List[TrashFolderPathCollectionFieldEntriesField]
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class TrashFolderItemStatusField(str, Enum):
    ACTIVE = 'active'
    TRASHED = 'trashed'
    DELETED = 'deleted'


class TrashFolder(BaseObject):
    def __init__(
        self,
        id: str,
        type: TrashFolderTypeField,
        name: str,
        description: str,
        size: int,
        path_collection: TrashFolderPathCollectionField,
        created_by: UserMini,
        modified_by: UserMini,
        owned_by: UserMini,
        item_status: TrashFolderItemStatusField,
        etag: Optional[str] = None,
        sequence_id: Optional[str] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        trashed_at: Optional[str] = None,
        purged_at: Optional[str] = None,
        content_created_at: Optional[str] = None,
        content_modified_at: Optional[str] = None,
        shared_link: Optional[str] = None,
        folder_upload_email: Optional[str] = None,
        parent: Optional[FolderMini] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting a folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folders/123`
            the `folder_id` is `123`.
        :type id: str
        :param type: `folder`
        :type type: TrashFolderTypeField
        :param name: The name of the folder.
        :type name: str
        :param size: The folder size in bytes.
            Be careful parsing this integer as its
            value can get very large.
        :type size: int
        :param item_status: Defines if this item has been deleted or not.
            * `active` when the item has is not in the trash
            * `trashed` when the item has been moved to the trash but not deleted
            * `deleted` when the item has been permanently deleted.
        :type item_status: TrashFolderItemStatusField
        :param etag: The HTTP `etag` of this folder. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the folder if (no) changes have happened.
        :type etag: Optional[str], optional
        :param created_at: The date and time when the folder was created. This value may
            be `null` for some folders such as the root folder or the trash
            folder.
        :type created_at: Optional[str], optional
        :param modified_at: The date and time when the folder was last updated. This value may
            be `null` for some folders such as the root folder or the trash
            folder.
        :type modified_at: Optional[str], optional
        :param trashed_at: The time at which this folder was put in the trash.
        :type trashed_at: Optional[str], optional
        :param purged_at: The time at which this folder is expected to be purged
            from the trash.
        :type purged_at: Optional[str], optional
        :param content_created_at: The date and time at which this folder was originally
            created.
        :type content_created_at: Optional[str], optional
        :param content_modified_at: The date and time at which this folder was last updated.
        :type content_modified_at: Optional[str], optional
        :param shared_link: The shared link for this folder. This will
            be `null` if a folder has been trashed, since the link will no longer
            be active.
        :type shared_link: Optional[str], optional
        :param folder_upload_email: The folder upload email for this folder. This will
            be `null` if a folder has been trashed, since the upload will no longer
            work.
        :type folder_upload_email: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name
        self.description = description
        self.size = size
        self.path_collection = path_collection
        self.created_by = created_by
        self.modified_by = modified_by
        self.owned_by = owned_by
        self.item_status = item_status
        self.etag = etag
        self.sequence_id = sequence_id
        self.created_at = created_at
        self.modified_at = modified_at
        self.trashed_at = trashed_at
        self.purged_at = purged_at
        self.content_created_at = content_created_at
        self.content_modified_at = content_modified_at
        self.shared_link = shared_link
        self.folder_upload_email = folder_upload_email
        self.parent = parent


class TrashFileTypeField(str, Enum):
    FILE = 'file'


class TrashFilePathCollectionFieldEntriesFieldTypeField(str, Enum):
    FOLDER = 'folder'


class TrashFilePathCollectionFieldEntriesField(BaseObject):
    def __init__(
        self,
        type: Optional[TrashFilePathCollectionFieldEntriesFieldTypeField] = None,
        id: Optional[str] = None,
        sequence_id: Optional[str] = None,
        etag: Optional[str] = None,
        name: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: `folder`
        :type type: Optional[TrashFilePathCollectionFieldEntriesFieldTypeField], optional
        :param id: The unique identifier that represent a folder.
        :type id: Optional[str], optional
        :param sequence_id: This field is null for the Trash folder
        :type sequence_id: Optional[str], optional
        :param etag: This field is null for the Trash folder
        :type etag: Optional[str], optional
        :param name: The name of the Trash folder.
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id
        self.sequence_id = sequence_id
        self.etag = etag
        self.name = name


class TrashFilePathCollectionField(BaseObject):
    def __init__(
        self,
        total_count: int,
        entries: List[TrashFilePathCollectionFieldEntriesField],
        **kwargs
    ):
        """
        :param total_count: The number of folders in this list.
        :type total_count: int
        :param entries: Array of folders for this item's path collection
        :type entries: List[TrashFilePathCollectionFieldEntriesField]
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class TrashFileItemStatusField(str, Enum):
    ACTIVE = 'active'
    TRASHED = 'trashed'
    DELETED = 'deleted'


class TrashFile(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'sha_1': 'sha1',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'sha1': 'sha_1',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        id: str,
        type: TrashFileTypeField,
        sequence_id: str,
        sha_1: str,
        description: str,
        size: int,
        path_collection: TrashFilePathCollectionField,
        created_at: str,
        modified_at: str,
        modified_by: UserMini,
        owned_by: UserMini,
        item_status: TrashFileItemStatusField,
        etag: Optional[str] = None,
        name: Optional[str] = None,
        file_version: Optional[FileVersionMini] = None,
        trashed_at: Optional[str] = None,
        purged_at: Optional[str] = None,
        content_created_at: Optional[str] = None,
        content_modified_at: Optional[str] = None,
        created_by: Optional[UserMini] = None,
        shared_link: Optional[str] = None,
        parent: Optional[FolderMini] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
        :type id: str
        :param type: `file`
        :type type: TrashFileTypeField
        :param sha_1: The SHA1 hash of the file. This can be used to compare the contents
            of a file on Box with a local file.
        :type sha_1: str
        :param description: The optional description of this file
        :type description: str
        :param size: The file size in bytes. Be careful parsing this integer as it can
            get very large and cause an integer overflow.
        :type size: int
        :param created_at: The date and time when the file was created on Box.
        :type created_at: str
        :param modified_at: The date and time when the file was last updated on Box.
        :type modified_at: str
        :param item_status: Defines if this item has been deleted or not.
            * `active` when the item has is not in the trash
            * `trashed` when the item has been moved to the trash but not deleted
            * `deleted` when the item has been permanently deleted.
        :type item_status: TrashFileItemStatusField
        :param etag: The HTTP `etag` of this file. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the file if (no) changes have happened.
        :type etag: Optional[str], optional
        :param name: The name of the file
        :type name: Optional[str], optional
        :param trashed_at: The time at which this file was put in the trash.
        :type trashed_at: Optional[str], optional
        :param purged_at: The time at which this file is expected to be purged
            from the trash.
        :type purged_at: Optional[str], optional
        :param content_created_at: The date and time at which this file was originally
            created, which might be before it was uploaded to Box.
        :type content_created_at: Optional[str], optional
        :param content_modified_at: The date and time at which this file was last updated,
            which might be before it was uploaded to Box.
        :type content_modified_at: Optional[str], optional
        :param shared_link: The shared link for this file. This will
            be `null` if a file has been trashed, since the link will no longer
            be active.
        :type shared_link: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.sequence_id = sequence_id
        self.sha_1 = sha_1
        self.description = description
        self.size = size
        self.path_collection = path_collection
        self.created_at = created_at
        self.modified_at = modified_at
        self.modified_by = modified_by
        self.owned_by = owned_by
        self.item_status = item_status
        self.etag = etag
        self.name = name
        self.file_version = file_version
        self.trashed_at = trashed_at
        self.purged_at = purged_at
        self.content_created_at = content_created_at
        self.content_modified_at = content_modified_at
        self.created_by = created_by
        self.shared_link = shared_link
        self.parent = parent


class TermsOfServiceUserStatusTypeField(str, Enum):
    TERMS_OF_SERVICE_USER_STATUS = 'terms_of_service_user_status'


class TermsOfServiceUserStatus(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[TermsOfServiceUserStatusTypeField] = None,
        tos: Optional[TermsOfServiceBase] = None,
        user: Optional[UserMini] = None,
        is_accepted: Optional[bool] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this terms of service user status
        :type id: Optional[str], optional
        :param type: `terms_of_service_user_status`
        :type type: Optional[TermsOfServiceUserStatusTypeField], optional
        :param is_accepted: If the user has accepted the terms of services
        :type is_accepted: Optional[bool], optional
        :param created_at: When the legal item was created
        :type created_at: Optional[str], optional
        :param modified_at: When the legal item was modified.
        :type modified_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.tos = tos
        self.user = user
        self.is_accepted = is_accepted
        self.created_at = created_at
        self.modified_at = modified_at


class TermsOfServiceUserStatuses(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        entries: Optional[List[TermsOfServiceUserStatus]] = None,
        **kwargs
    ):
        """
        :param total_count: The total number of objects.
        :type total_count: Optional[int], optional
        :param entries: A list of terms of service user statuses
        :type entries: Optional[List[TermsOfServiceUserStatus]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class TaskAssignmentTypeField(str, Enum):
    TASK_ASSIGNMENT = 'task_assignment'


class TaskAssignmentResolutionStateField(str, Enum):
    COMPLETED = 'completed'
    INCOMPLETE = 'incomplete'
    APPROVED = 'approved'
    REJECTED = 'rejected'


class TaskAssignment(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[TaskAssignmentTypeField] = None,
        item: Optional[FileMini] = None,
        assigned_to: Optional[UserMini] = None,
        message: Optional[str] = None,
        completed_at: Optional[str] = None,
        assigned_at: Optional[str] = None,
        reminded_at: Optional[str] = None,
        resolution_state: Optional[TaskAssignmentResolutionStateField] = None,
        assigned_by: Optional[UserMini] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this task assignment
        :type id: Optional[str], optional
        :param type: `task_assignment`
        :type type: Optional[TaskAssignmentTypeField], optional
        :param message: A message that will is included with the task
            assignment. This is visible to the assigned user in the web and mobile
            UI.
        :type message: Optional[str], optional
        :param completed_at: The date at which this task assignment was
            completed. This will be `null` if the task is not completed yet.
        :type completed_at: Optional[str], optional
        :param assigned_at: The date at which this task was assigned to the user.
        :type assigned_at: Optional[str], optional
        :param reminded_at: The date at which the assigned user was reminded of this task
            assignment.
        :type reminded_at: Optional[str], optional
        :param resolution_state: The current state of the assignment. The available states depend on
            the `action` value of the task object.
        :type resolution_state: Optional[TaskAssignmentResolutionStateField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.item = item
        self.assigned_to = assigned_to
        self.message = message
        self.completed_at = completed_at
        self.assigned_at = assigned_at
        self.reminded_at = reminded_at
        self.resolution_state = resolution_state
        self.assigned_by = assigned_by


class TaskAssignments(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        entries: Optional[List[TaskAssignment]] = None,
        **kwargs
    ):
        """
        :param total_count: The total number of items in this collection.
        :type total_count: Optional[int], optional
        :param entries: A list of task assignments
        :type entries: Optional[List[TaskAssignment]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class TaskTypeField(str, Enum):
    TASK = 'task'


class TaskActionField(str, Enum):
    REVIEW = 'review'
    COMPLETE = 'complete'


class TaskCompletionRuleField(str, Enum):
    ALL_ASSIGNEES = 'all_assignees'
    ANY_ASSIGNEE = 'any_assignee'


class Task(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[TaskTypeField] = None,
        item: Optional[FileMini] = None,
        due_at: Optional[str] = None,
        action: Optional[TaskActionField] = None,
        message: Optional[str] = None,
        task_assignment_collection: Optional[TaskAssignments] = None,
        is_completed: Optional[bool] = None,
        created_by: Optional[UserMini] = None,
        created_at: Optional[str] = None,
        completion_rule: Optional[TaskCompletionRuleField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this task
        :type id: Optional[str], optional
        :param type: `task`
        :type type: Optional[TaskTypeField], optional
        :param due_at: When the task is due
        :type due_at: Optional[str], optional
        :param action: The type of task the task assignee will be prompted to
            perform.
        :type action: Optional[TaskActionField], optional
        :param message: A message that will be included with the task
        :type message: Optional[str], optional
        :param is_completed: Whether the task has been completed
        :type is_completed: Optional[bool], optional
        :param created_at: When the task object was created
        :type created_at: Optional[str], optional
        :param completion_rule: Defines which assignees need to complete this task before the task
            is considered completed.
            * `all_assignees` requires all assignees to review or
            approve the the task in order for it to be considered completed.
            * `any_assignee` accepts any one assignee to review or
            approve the the task in order for it to be considered completed.
        :type completion_rule: Optional[TaskCompletionRuleField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.item = item
        self.due_at = due_at
        self.action = action
        self.message = message
        self.task_assignment_collection = task_assignment_collection
        self.is_completed = is_completed
        self.created_by = created_by
        self.created_at = created_at
        self.completion_rule = completion_rule


class Tasks(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        entries: Optional[List[Task]] = None,
        **kwargs
    ):
        """
        :param total_count: One greater than the offset of the last entry in the entire collection.
            The total number of entries in the collection may be less than
            `total_count`.
        :type total_count: Optional[int], optional
        :param entries: A list of tasks
        :type entries: Optional[List[Task]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class RetentionPolicyAssignmentTypeField(str, Enum):
    RETENTION_POLICY_ASSIGNMENT = 'retention_policy_assignment'


class RetentionPolicyAssignmentAssignedToFieldTypeField(str, Enum):
    FOLDER = 'folder'
    ENTERPRISE = 'enterprise'
    METADATA_TEMPLATE = 'metadata_template'


class RetentionPolicyAssignmentAssignedToField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[RetentionPolicyAssignmentAssignedToFieldTypeField] = None,
        **kwargs
    ):
        """
        :param id: The ID of the folder, enterprise, or metadata template
            the policy is assigned to.
            Set to null or omit when type is set to enterprise.
        :type id: Optional[str], optional
        :param type: The type of resource the policy is assigned to.
        :type type: Optional[RetentionPolicyAssignmentAssignedToFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class RetentionPolicyAssignmentFilterFieldsField(BaseObject):
    def __init__(
        self, field: Optional[str] = None, value: Optional[str] = None, **kwargs
    ):
        """
        :param field: The metadata attribute key id.
        :type field: Optional[str], optional
        :param value: The metadata attribute field id. For value, only
            enum and multiselect types are supported.
        :type value: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.field = field
        self.value = value


class RetentionPolicyAssignment(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[RetentionPolicyAssignmentTypeField] = None,
        retention_policy: Optional[RetentionPolicyMini] = None,
        assigned_to: Optional[RetentionPolicyAssignmentAssignedToField] = None,
        filter_fields: Optional[
            List[RetentionPolicyAssignmentFilterFieldsField]
        ] = None,
        assigned_by: Optional[UserMini] = None,
        assigned_at: Optional[str] = None,
        start_date_field: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for a retention policy assignment.
        :type id: Optional[str], optional
        :param type: `retention_policy_assignment`
        :type type: Optional[RetentionPolicyAssignmentTypeField], optional
        :param assigned_to: The `type` and `id` of the content that is under
            retention. The `type` can either be `folder`
            `enterprise`, or `metadata_template`.
        :type assigned_to: Optional[RetentionPolicyAssignmentAssignedToField], optional
        :param filter_fields: An array of field objects. Values are only returned if the `assigned_to`
            type is `metadata_template`. Otherwise, the array is blank.
        :type filter_fields: Optional[List[RetentionPolicyAssignmentFilterFieldsField]], optional
        :param assigned_at: When the retention policy assignment object was
            created.
        :type assigned_at: Optional[str], optional
        :param start_date_field: The date the retention policy assignment begins.
            If the `assigned_to` type is `metadata_template`,
            this field can be a date field's metadata attribute key id.
        :type start_date_field: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.retention_policy = retention_policy
        self.assigned_to = assigned_to
        self.filter_fields = filter_fields
        self.assigned_by = assigned_by
        self.assigned_at = assigned_at
        self.start_date_field = start_date_field


class RetentionPolicyAssignments(BaseObject):
    def __init__(
        self,
        entries: Optional[List[RetentionPolicyAssignment]] = None,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        **kwargs
    ):
        """
        :param entries: A list of retention policy assignments
        :type entries: Optional[List[RetentionPolicyAssignment]], optional
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.entries = entries
        self.limit = limit
        self.next_marker = next_marker


class RetentionPolicyPolicyTypeField(str, Enum):
    FINITE = 'finite'
    INDEFINITE = 'indefinite'


class RetentionPolicyRetentionTypeField(str, Enum):
    MODIFIABLE = 'modifiable'
    NON_MODIFIABLE = 'non_modifiable'


class RetentionPolicyStatusField(str, Enum):
    ACTIVE = 'active'
    RETIRED = 'retired'


class RetentionPolicyAssignmentCountsField(BaseObject):
    def __init__(
        self,
        enterprise: Optional[int] = None,
        folder: Optional[int] = None,
        metadata_template: Optional[int] = None,
        **kwargs
    ):
        """
        :param enterprise: The number of enterprise assignments this policy has. The maximum value is 1.
        :type enterprise: Optional[int], optional
        :param folder: The number of folder assignments this policy has.
        :type folder: Optional[int], optional
        :param metadata_template: The number of metadata template assignments this policy has.
        :type metadata_template: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.enterprise = enterprise
        self.folder = folder
        self.metadata_template = metadata_template


class RetentionPolicy(RetentionPolicyMini):
    def __init__(
        self,
        id: str,
        type: RetentionPolicyBaseTypeField,
        description: Optional[str] = None,
        policy_type: Optional[RetentionPolicyPolicyTypeField] = None,
        retention_type: Optional[RetentionPolicyRetentionTypeField] = None,
        status: Optional[RetentionPolicyStatusField] = None,
        created_by: Optional[UserMini] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        can_owner_extend_retention: Optional[bool] = None,
        are_owners_notified: Optional[bool] = None,
        custom_notification_recipients: Optional[List[UserMini]] = None,
        assignment_counts: Optional[RetentionPolicyAssignmentCountsField] = None,
        policy_name: Optional[str] = None,
        retention_length: Optional[str] = None,
        disposition_action: Optional[RetentionPolicyMiniDispositionActionField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represents a retention policy.
        :type id: str
        :param type: `retention_policy`
        :type type: RetentionPolicyBaseTypeField
        :param description: The additional text description of the retention policy.
        :type description: Optional[str], optional
        :param policy_type: The type of the retention policy. A retention
            policy type can either be `finite`, where a
            specific amount of time to retain the content is known
            upfront, or `indefinite`, where the amount of time
            to retain the content is still unknown.
        :type policy_type: Optional[RetentionPolicyPolicyTypeField], optional
        :param retention_type: Specifies the retention type:
            * `modifiable`: You can modify the retention policy. For example,
             you can add or remove folders, shorten or lengthen
             the policy duration, or delete the assignment.
             Use this type if your retention policy
             is not related to any regulatory purposes.
            * `non-modifiable`: You can modify the retention policy
             only in a limited way: add a folder, lengthen the duration,
             retire the policy, change the disposition action
             or notification settings. You cannot perform other actions,
             such as deleting the assignment or shortening the
             policy duration. Use this type to ensure
             compliance with regulatory retention policies.
        :type retention_type: Optional[RetentionPolicyRetentionTypeField], optional
        :param status: The status of the retention policy. The status of
            a policy will be `active`, unless explicitly retired by an
            administrator, in which case the status will be `retired`.
            Once a policy has been retired, it cannot become
            active again.
        :type status: Optional[RetentionPolicyStatusField], optional
        :param created_at: When the retention policy object was created.
        :type created_at: Optional[str], optional
        :param modified_at: When the retention policy object was last modified.
        :type modified_at: Optional[str], optional
        :param can_owner_extend_retention: Determines if the owner of items under the policy
            can extend the retention when the original
            retention duration is about to end.
        :type can_owner_extend_retention: Optional[bool], optional
        :param are_owners_notified: Determines if owners and co-owners of items
            under the policy are notified when
            the retention duration is about to end.
        :type are_owners_notified: Optional[bool], optional
        :param custom_notification_recipients: A list of users notified when the retention policy duration is about to end.
        :type custom_notification_recipients: Optional[List[UserMini]], optional
        :param assignment_counts: Counts the retention policy assignments for each item type.
        :type assignment_counts: Optional[RetentionPolicyAssignmentCountsField], optional
        :param policy_name: The name given to the retention policy.
        :type policy_name: Optional[str], optional
        :param retention_length: The length of the retention policy. This value
            specifies the duration in days that the retention
            policy will be active for after being assigned to
            content.  If the policy has a `policy_type` of
            `indefinite`, the `retention_length` will also be
            `indefinite`.
        :type retention_length: Optional[str], optional
        :param disposition_action: The disposition action of the retention policy.
            This action can be `permanently_delete`, which
            will cause the content retained by the policy
            to be permanently deleted, or `remove_retention`,
            which will lift the retention policy from the content,
            allowing it to be deleted by users,
            once the retention policy has expired.
        :type disposition_action: Optional[RetentionPolicyMiniDispositionActionField], optional
        """
        super().__init__(
            id=id,
            type=type,
            policy_name=policy_name,
            retention_length=retention_length,
            disposition_action=disposition_action,
            **kwargs
        )
        self.description = description
        self.policy_type = policy_type
        self.retention_type = retention_type
        self.status = status
        self.created_by = created_by
        self.created_at = created_at
        self.modified_at = modified_at
        self.can_owner_extend_retention = can_owner_extend_retention
        self.are_owners_notified = are_owners_notified
        self.custom_notification_recipients = custom_notification_recipients
        self.assignment_counts = assignment_counts


class LegalHoldPolicyStatusField(str, Enum):
    ACTIVE = 'active'
    APPLYING = 'applying'
    RELEASING = 'releasing'
    RELEASED = 'released'


class LegalHoldPolicyAssignmentCountsField(BaseObject):
    def __init__(
        self,
        user: Optional[int] = None,
        folder: Optional[int] = None,
        file: Optional[int] = None,
        file_version: Optional[int] = None,
        **kwargs
    ):
        """
        :param user: The number of users this policy is applied to
        :type user: Optional[int], optional
        :param folder: The number of folders this policy is applied to
        :type folder: Optional[int], optional
        :param file: The number of files this policy is applied to
        :type file: Optional[int], optional
        :param file_version: The number of file versions this policy is applied to
        :type file_version: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.user = user
        self.folder = folder
        self.file = file
        self.file_version = file_version


class LegalHoldPolicy(LegalHoldPolicyMini):
    def __init__(
        self,
        policy_name: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[LegalHoldPolicyStatusField] = None,
        assignment_counts: Optional[LegalHoldPolicyAssignmentCountsField] = None,
        created_by: Optional[UserMini] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        deleted_at: Optional[str] = None,
        filter_started_at: Optional[str] = None,
        filter_ended_at: Optional[str] = None,
        release_notes: Optional[str] = None,
        id: Optional[str] = None,
        type: Optional[LegalHoldPolicyMiniTypeField] = None,
        **kwargs
    ):
        """
        :param policy_name: Name of the legal hold policy.
        :type policy_name: Optional[str], optional
        :param description: Description of the legal hold policy. Optional
            property with a 500 character limit.
        :type description: Optional[str], optional
        :param status: * 'active' - the policy is not in a transition state
            * 'applying' - that the policy is in the process of
              being applied
            * 'releasing' - that the process is in the process
              of being released
            * 'released' - the policy is no longer active
        :type status: Optional[LegalHoldPolicyStatusField], optional
        :param assignment_counts: Counts of assignments within this a legal hold policy by item type
        :type assignment_counts: Optional[LegalHoldPolicyAssignmentCountsField], optional
        :param created_at: When the legal hold policy object was created
        :type created_at: Optional[str], optional
        :param modified_at: When the legal hold policy object was modified.
            Does not update when assignments are added or removed.
        :type modified_at: Optional[str], optional
        :param deleted_at: When the policy release request was sent. (Because
            it can take time for a policy to fully delete, this
            isn't quite the same time that the policy is fully deleted).
            If `null`, the policy was not deleted.
        :type deleted_at: Optional[str], optional
        :param filter_started_at: User-specified, optional date filter applies to
            Custodian assignments only
        :type filter_started_at: Optional[str], optional
        :param filter_ended_at: User-specified, optional date filter applies to
            Custodian assignments only
        :type filter_ended_at: Optional[str], optional
        :param release_notes: Optional notes about why the policy was created.
        :type release_notes: Optional[str], optional
        :param id: The unique identifier for this legal hold policy
        :type id: Optional[str], optional
        :param type: `legal_hold_policy`
        :type type: Optional[LegalHoldPolicyMiniTypeField], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.policy_name = policy_name
        self.description = description
        self.status = status
        self.assignment_counts = assignment_counts
        self.created_by = created_by
        self.created_at = created_at
        self.modified_at = modified_at
        self.deleted_at = deleted_at
        self.filter_started_at = filter_started_at
        self.filter_ended_at = filter_ended_at
        self.release_notes = release_notes


class LegalHoldPolicies(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[LegalHoldPolicy]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of legal hold policies
        :type entries: Optional[List[LegalHoldPolicy]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class InviteTypeField(str, Enum):
    INVITE = 'invite'


class InviteInvitedToFieldTypeField(str, Enum):
    ENTERPRISE = 'enterprise'


class InviteInvitedToField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[InviteInvitedToFieldTypeField] = None,
        name: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this enterprise.
        :type id: Optional[str], optional
        :param type: `enterprise`
        :type type: Optional[InviteInvitedToFieldTypeField], optional
        :param name: The name of the enterprise
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name


class Invite(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[InviteTypeField] = None,
        invited_to: Optional[InviteInvitedToField] = None,
        actionable_by: Optional[UserMini] = None,
        invited_by: Optional[UserMini] = None,
        status: Optional[str] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this invite
        :type id: Optional[str], optional
        :param type: `invite`
        :type type: Optional[InviteTypeField], optional
        :param invited_to: A representation of a Box enterprise
        :type invited_to: Optional[InviteInvitedToField], optional
        :param status: The status of the invite
        :type status: Optional[str], optional
        :param created_at: When the invite was created
        :type created_at: Optional[str], optional
        :param modified_at: When the invite was modified.
        :type modified_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.invited_to = invited_to
        self.actionable_by = actionable_by
        self.invited_by = invited_by
        self.status = status
        self.created_at = created_at
        self.modified_at = modified_at


class GroupMembershipTypeField(str, Enum):
    GROUP_MEMBERSHIP = 'group_membership'


class GroupMembershipRoleField(str, Enum):
    MEMBER = 'member'
    ADMIN = 'admin'


class GroupMembership(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[GroupMembershipTypeField] = None,
        user: Optional[UserMini] = None,
        group: Optional[GroupMini] = None,
        role: Optional[GroupMembershipRoleField] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this group membership
        :type id: Optional[str], optional
        :param type: `group_membership`
        :type type: Optional[GroupMembershipTypeField], optional
        :param role: The role of the user in the group.
        :type role: Optional[GroupMembershipRoleField], optional
        :param created_at: The time this membership was created.
        :type created_at: Optional[str], optional
        :param modified_at: The time this membership was last modified.
        :type modified_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.user = user
        self.group = group
        self.role = role
        self.created_at = created_at
        self.modified_at = modified_at


class GroupMembershipsOrderFieldDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class GroupMembershipsOrderField(BaseObject):
    def __init__(
        self,
        by: Optional[str] = None,
        direction: Optional[GroupMembershipsOrderFieldDirectionField] = None,
        **kwargs
    ):
        """
        :param by: The field to order by
        :type by: Optional[str], optional
        :param direction: The direction to order by, either ascending or descending
        :type direction: Optional[GroupMembershipsOrderFieldDirectionField], optional
        """
        super().__init__(**kwargs)
        self.by = by
        self.direction = direction


class GroupMemberships(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[List[GroupMembershipsOrderField]] = None,
        entries: Optional[List[GroupMembership]] = None,
        **kwargs
    ):
        """
        :param total_count: One greater than the offset of the last entry in the entire collection.
            The total number of entries in the collection may be less than
            `total_count`.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type total_count: Optional[int], optional
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param offset: The 0-based offset of the first entry in this set. This will be the same
            as the `offset` query parameter.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type offset: Optional[int], optional
        :param order: The order by which items are returned.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type order: Optional[List[GroupMembershipsOrderField]], optional
        :param entries: A list of group memberships
        :type entries: Optional[List[GroupMembership]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.limit = limit
        self.offset = offset
        self.order = order
        self.entries = entries


class FileVersion(FileVersionMini):
    def __init__(
        self,
        id: str,
        type: FileVersionBaseTypeField,
        name: Optional[str] = None,
        size: Optional[int] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        modified_by: Optional[UserMini] = None,
        trashed_at: Optional[str] = None,
        trashed_by: Optional[UserMini] = None,
        restored_at: Optional[str] = None,
        restored_by: Optional[UserMini] = None,
        purged_at: Optional[str] = None,
        uploader_display_name: Optional[str] = None,
        sha_1: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a file version.
        :type id: str
        :param type: `file_version`
        :type type: FileVersionBaseTypeField
        :param name: The name of the file version
        :type name: Optional[str], optional
        :param size: Size of the file version in bytes
        :type size: Optional[int], optional
        :param created_at: When the file version object was created
        :type created_at: Optional[str], optional
        :param modified_at: When the file version object was last updated
        :type modified_at: Optional[str], optional
        :param trashed_at: When the file version object was trashed.
        :type trashed_at: Optional[str], optional
        :param restored_at: When the file version was restored from the trash.
        :type restored_at: Optional[str], optional
        :param purged_at: When the file version object will be permanently deleted.
        :type purged_at: Optional[str], optional
        :param sha_1: The SHA1 hash of this version of the file.
        :type sha_1: Optional[str], optional
        """
        super().__init__(id=id, type=type, sha_1=sha_1, **kwargs)
        self.name = name
        self.size = size
        self.created_at = created_at
        self.modified_at = modified_at
        self.modified_by = modified_by
        self.trashed_at = trashed_at
        self.trashed_by = trashed_by
        self.restored_at = restored_at
        self.restored_by = restored_by
        self.purged_at = purged_at
        self.uploader_display_name = uploader_display_name


class FileVersionsOrderFieldDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class FileVersionsOrderField(BaseObject):
    def __init__(
        self,
        by: Optional[str] = None,
        direction: Optional[FileVersionsOrderFieldDirectionField] = None,
        **kwargs
    ):
        """
        :param by: The field to order by
        :type by: Optional[str], optional
        :param direction: The direction to order by, either ascending or descending
        :type direction: Optional[FileVersionsOrderFieldDirectionField], optional
        """
        super().__init__(**kwargs)
        self.by = by
        self.direction = direction


class FileVersions(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[List[FileVersionsOrderField]] = None,
        entries: Optional[List[FileVersion]] = None,
        **kwargs
    ):
        """
        :param total_count: One greater than the offset of the last entry in the entire collection.
            The total number of entries in the collection may be less than
            `total_count`.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type total_count: Optional[int], optional
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param offset: The 0-based offset of the first entry in this set. This will be the same
            as the `offset` query parameter.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type offset: Optional[int], optional
        :param order: The order by which items are returned.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type order: Optional[List[FileVersionsOrderField]], optional
        :param entries: A list of file versions
        :type entries: Optional[List[FileVersion]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.limit = limit
        self.offset = offset
        self.order = order
        self.entries = entries


class FileVersionFull(FileVersion):
    def __init__(
        self,
        id: str,
        type: FileVersionBaseTypeField,
        version_number: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[int] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        modified_by: Optional[UserMini] = None,
        trashed_at: Optional[str] = None,
        trashed_by: Optional[UserMini] = None,
        restored_at: Optional[str] = None,
        restored_by: Optional[UserMini] = None,
        purged_at: Optional[str] = None,
        uploader_display_name: Optional[str] = None,
        sha_1: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a file version.
        :type id: str
        :param type: `file_version`
        :type type: FileVersionBaseTypeField
        :param version_number: The version number of this file version
        :type version_number: Optional[str], optional
        :param name: The name of the file version
        :type name: Optional[str], optional
        :param size: Size of the file version in bytes
        :type size: Optional[int], optional
        :param created_at: When the file version object was created
        :type created_at: Optional[str], optional
        :param modified_at: When the file version object was last updated
        :type modified_at: Optional[str], optional
        :param trashed_at: When the file version object was trashed.
        :type trashed_at: Optional[str], optional
        :param restored_at: When the file version was restored from the trash.
        :type restored_at: Optional[str], optional
        :param purged_at: When the file version object will be permanently deleted.
        :type purged_at: Optional[str], optional
        :param sha_1: The SHA1 hash of this version of the file.
        :type sha_1: Optional[str], optional
        """
        super().__init__(
            id=id,
            type=type,
            name=name,
            size=size,
            created_at=created_at,
            modified_at=modified_at,
            modified_by=modified_by,
            trashed_at=trashed_at,
            trashed_by=trashed_by,
            restored_at=restored_at,
            restored_by=restored_by,
            purged_at=purged_at,
            uploader_display_name=uploader_display_name,
            sha_1=sha_1,
            **kwargs
        )
        self.version_number = version_number


class FileRequestTypeField(str, Enum):
    FILE_REQUEST = 'file_request'


class FileRequestStatusField(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class FileRequest(BaseObject):
    def __init__(
        self,
        id: str,
        type: FileRequestTypeField,
        folder: FolderMini,
        created_at: str,
        updated_at: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[FileRequestStatusField] = None,
        is_email_required: Optional[bool] = None,
        is_description_required: Optional[bool] = None,
        expires_at: Optional[str] = None,
        url: Optional[str] = None,
        etag: Optional[str] = None,
        created_by: Optional[UserMini] = None,
        updated_by: Optional[UserMini] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this file request.
        :type id: str
        :param type: `file_request`
        :type type: FileRequestTypeField
        :param created_at: The date and time when the file request was created.
        :type created_at: str
        :param updated_at: The date and time when the file request was last updated.
        :type updated_at: str
        :param title: The title of file request. This is shown
            in the Box UI to users uploading files.
            This defaults to title of the file request that was
            copied to create this file request.
        :type title: Optional[str], optional
        :param description: The optional description of this file request. This is
            shown in the Box UI to users uploading files.
            This defaults to description of the file request that was
            copied to create this file request.
        :type description: Optional[str], optional
        :param status: The status of the file request. This defaults
            to `active`.
            When the status is set to `inactive`, the file request
            will no longer accept new submissions, and any visitor
            to the file request URL will receive a `HTTP 404` status
            code.
            This defaults to status of file request that was
            copied to create this file request.
        :type status: Optional[FileRequestStatusField], optional
        :param is_email_required: Whether a file request submitter is required to provide
            their email address.
            When this setting is set to true, the Box UI will show
            an email field on the file request form.
            This defaults to setting of file request that was
            copied to create this file request.
        :type is_email_required: Optional[bool], optional
        :param is_description_required: Whether a file request submitter is required to provide
            a description of the files they are submitting.
            When this setting is set to true, the Box UI will show
            a description field on the file request form.
            This defaults to setting of file request that was
            copied to create this file request.
        :type is_description_required: Optional[bool], optional
        :param expires_at: The date after which a file request will no longer accept new
            submissions.
            After this date, the `status` will automatically be set to
            `inactive`.
        :type expires_at: Optional[str], optional
        :param url: The generated URL for this file request. This URL can be shared
            with users to let them upload files to the associated folder.
        :type url: Optional[str], optional
        :param etag: The HTTP `etag` of this file. This can be used in combination with
            the `If-Match` header when updating a file request. By providing that
            header, a change will only be performed on the  file request if the `etag`
            on the file request still matches the `etag` provided in the `If-Match`
            header.
        :type etag: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.folder = folder
        self.created_at = created_at
        self.updated_at = updated_at
        self.title = title
        self.description = description
        self.status = status
        self.is_email_required = is_email_required
        self.is_description_required = is_description_required
        self.expires_at = expires_at
        self.url = url
        self.etag = etag
        self.created_by = created_by
        self.updated_by = updated_by


class FilePathCollectionField(BaseObject):
    def __init__(self, total_count: int, entries: List[FolderMini], **kwargs):
        """
        :param total_count: The number of folders in this list.
        :type total_count: int
        :param entries: The parent folders for this item
        :type entries: List[FolderMini]
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class FileSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'


class FileSharedLinkFieldEffectiveAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'


class FileSharedLinkFieldEffectivePermissionField(str, Enum):
    CAN_EDIT = 'can_edit'
    CAN_DOWNLOAD = 'can_download'
    CAN_PREVIEW = 'can_preview'
    NO_ACCESS = 'no_access'


class FileSharedLinkFieldPermissionsField(BaseObject):
    def __init__(self, can_download: bool, can_preview: bool, can_edit: bool, **kwargs):
        """
        :param can_download: Defines if the shared link allows for the item to be downloaded. For
            shared links on folders, this also applies to any items in the folder.
            This value can be set to `true` when the effective access level is
            set to `open` or `company`, not `collaborators`.
        :type can_download: bool
        :param can_preview: Defines if the shared link allows for the item to be previewed.
            This value is always `true`. For shared links on folders this also
            applies to any items in the folder.
        :type can_preview: bool
        :param can_edit: Defines if the shared link allows for the item to be edited.
            This value can only be `true` if `can_download` is also `true` and if
            the item has a type of `file`.
        :type can_edit: bool
        """
        super().__init__(**kwargs)
        self.can_download = can_download
        self.can_preview = can_preview
        self.can_edit = can_edit


class FileSharedLinkField(BaseObject):
    def __init__(
        self,
        url: str,
        effective_access: FileSharedLinkFieldEffectiveAccessField,
        effective_permission: FileSharedLinkFieldEffectivePermissionField,
        is_password_enabled: bool,
        download_count: int,
        preview_count: int,
        download_url: Optional[str] = None,
        vanity_url: Optional[str] = None,
        vanity_name: Optional[str] = None,
        access: Optional[FileSharedLinkFieldAccessField] = None,
        unshared_at: Optional[str] = None,
        permissions: Optional[FileSharedLinkFieldPermissionsField] = None,
        **kwargs
    ):
        """
        :param url: The URL that can be used to access the item on Box.
            This URL will display the item in Box's preview UI where the file
            can be downloaded if allowed.
            This URL will continue to work even when a custom `vanity_url`
            has been set for this shared link.
        :type url: str
        :param effective_access: The effective access level for the shared link. This can be a more
            restrictive access level than the value in the `access` field when the
            enterprise settings restrict the allowed access levels.
        :type effective_access: FileSharedLinkFieldEffectiveAccessField
        :param effective_permission: The effective permissions for this shared link.
            These result in the more restrictive combination of
            the share link permissions and the item permissions set
            by the administrator, the owner, and any ancestor item
            such as a folder.
        :type effective_permission: FileSharedLinkFieldEffectivePermissionField
        :param is_password_enabled: Defines if the shared link requires a password to access the item.
        :type is_password_enabled: bool
        :param download_count: The number of times this item has been downloaded.
        :type download_count: int
        :param preview_count: The number of times this item has been previewed.
        :type preview_count: int
        :param download_url: A URL that can be used to download the file. This URL can be used in
            a browser to download the file. This URL includes the file
            extension so that the file will be saved with the right file type.
            This property will be `null` for folders.
        :type download_url: Optional[str], optional
        :param vanity_url: The "Custom URL" that can also be used to preview the item on Box.  Custom
            URLs can only be created or modified in the Box Web application.
        :type vanity_url: Optional[str], optional
        :param vanity_name: The custom name of a shared link, as used in the `vanity_url` field.
        :type vanity_name: Optional[str], optional
        :param access: The access level for this shared link.
            * `open` - provides access to this item to anyone with this link
            * `company` - only provides access to this item to people the same company
            * `collaborators` - only provides access to this item to people who are
               collaborators on this item
            If this field is omitted when creating the shared link, the access level
            will be set to the default access level specified by the enterprise admin.
        :type access: Optional[FileSharedLinkFieldAccessField], optional
        :param unshared_at: The date and time when this link will be unshared. This field can only be
            set by users with paid accounts.
        :type unshared_at: Optional[str], optional
        :param permissions: Defines if this link allows a user to preview, edit, and download an item.
            These permissions refer to the shared link only and
            do not supersede permissions applied to the item itself.
        :type permissions: Optional[FileSharedLinkFieldPermissionsField], optional
        """
        super().__init__(**kwargs)
        self.url = url
        self.effective_access = effective_access
        self.effective_permission = effective_permission
        self.is_password_enabled = is_password_enabled
        self.download_count = download_count
        self.preview_count = preview_count
        self.download_url = download_url
        self.vanity_url = vanity_url
        self.vanity_name = vanity_name
        self.access = access
        self.unshared_at = unshared_at
        self.permissions = permissions


class FileItemStatusField(str, Enum):
    ACTIVE = 'active'
    TRASHED = 'trashed'
    DELETED = 'deleted'


class File(FileMini):
    def __init__(
        self,
        id: str,
        type: FileBaseTypeField,
        description: Optional[str] = None,
        size: Optional[int] = None,
        path_collection: Optional[FilePathCollectionField] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        trashed_at: Optional[str] = None,
        purged_at: Optional[str] = None,
        content_created_at: Optional[str] = None,
        content_modified_at: Optional[str] = None,
        created_by: Optional[UserMini] = None,
        modified_by: Optional[UserMini] = None,
        owned_by: Optional[UserMini] = None,
        shared_link: Optional[FileSharedLinkField] = None,
        parent: Optional[FolderMini] = None,
        item_status: Optional[FileItemStatusField] = None,
        sequence_id: Optional[str] = None,
        name: Optional[str] = None,
        sha_1: Optional[str] = None,
        file_version: Optional[FileVersionMini] = None,
        etag: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
        :type id: str
        :param type: `file`
        :type type: FileBaseTypeField
        :param description: The optional description of this file
        :type description: Optional[str], optional
        :param size: The file size in bytes. Be careful parsing this integer as it can
            get very large and cause an integer overflow.
        :type size: Optional[int], optional
        :param created_at: The date and time when the file was created on Box.
        :type created_at: Optional[str], optional
        :param modified_at: The date and time when the file was last updated on Box.
        :type modified_at: Optional[str], optional
        :param trashed_at: The time at which this file was put in the trash.
        :type trashed_at: Optional[str], optional
        :param purged_at: The time at which this file is expected to be purged
            from the trash.
        :type purged_at: Optional[str], optional
        :param content_created_at: The date and time at which this file was originally
            created, which might be before it was uploaded to Box.
        :type content_created_at: Optional[str], optional
        :param content_modified_at: The date and time at which this file was last updated,
            which might be before it was uploaded to Box.
        :type content_modified_at: Optional[str], optional
        :param item_status: Defines if this item has been deleted or not.
            * `active` when the item has is not in the trash
            * `trashed` when the item has been moved to the trash but not deleted
            * `deleted` when the item has been permanently deleted.
        :type item_status: Optional[FileItemStatusField], optional
        :param name: The name of the file
        :type name: Optional[str], optional
        :param sha_1: The SHA1 hash of the file. This can be used to compare the contents
            of a file on Box with a local file.
        :type sha_1: Optional[str], optional
        :param etag: The HTTP `etag` of this file. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the file if (no) changes have happened.
        :type etag: Optional[str], optional
        """
        super().__init__(
            id=id,
            type=type,
            sequence_id=sequence_id,
            name=name,
            sha_1=sha_1,
            file_version=file_version,
            etag=etag,
            **kwargs
        )
        self.description = description
        self.size = size
        self.path_collection = path_collection
        self.created_at = created_at
        self.modified_at = modified_at
        self.trashed_at = trashed_at
        self.purged_at = purged_at
        self.content_created_at = content_created_at
        self.content_modified_at = content_modified_at
        self.created_by = created_by
        self.modified_by = modified_by
        self.owned_by = owned_by
        self.shared_link = shared_link
        self.parent = parent
        self.item_status = item_status


class FileFullPermissionsField(BaseObject):
    def __init__(
        self,
        can_delete: bool,
        can_download: bool,
        can_invite_collaborator: bool,
        can_rename: bool,
        can_set_share_access: bool,
        can_share: bool,
        can_annotate: Optional[bool] = None,
        can_comment: Optional[bool] = None,
        can_preview: Optional[bool] = None,
        can_upload: Optional[bool] = None,
        can_view_annotations_all: Optional[bool] = None,
        can_view_annotations_self: Optional[bool] = None,
        **kwargs
    ):
        """
        :param can_delete: Specifies if the current user can delete this item.
        :type can_delete: bool
        :param can_download: Specifies if the current user can download this item.
        :type can_download: bool
        :param can_invite_collaborator: Specifies if the current user can invite new
            users to collaborate on this item, and if the user can
            update the role of a user already collaborated on this
            item.
        :type can_invite_collaborator: bool
        :param can_rename: Specifies if the user can rename this item.
        :type can_rename: bool
        :param can_set_share_access: Specifies if the user can change the access level of an
            existing shared link on this item.
        :type can_set_share_access: bool
        :param can_share: Specifies if the user can create a shared link for this item.
        :type can_share: bool
        :param can_annotate: Specifies if the user can place annotations on this file.
        :type can_annotate: Optional[bool], optional
        :param can_comment: Specifies if the user can place comments on this file.
        :type can_comment: Optional[bool], optional
        :param can_preview: Specifies if the user can preview this file.
        :type can_preview: Optional[bool], optional
        :param can_upload: Specifies if the user can upload a new version of this file.
        :type can_upload: Optional[bool], optional
        :param can_view_annotations_all: Specifies if the user view all annotations placed on this file
        :type can_view_annotations_all: Optional[bool], optional
        :param can_view_annotations_self: Specifies if the user view annotations placed by themselves
            on this file
        :type can_view_annotations_self: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.can_delete = can_delete
        self.can_download = can_download
        self.can_invite_collaborator = can_invite_collaborator
        self.can_rename = can_rename
        self.can_set_share_access = can_set_share_access
        self.can_share = can_share
        self.can_annotate = can_annotate
        self.can_comment = can_comment
        self.can_preview = can_preview
        self.can_upload = can_upload
        self.can_view_annotations_all = can_view_annotations_all
        self.can_view_annotations_self = can_view_annotations_self


class FileFullLockFieldTypeField(str, Enum):
    LOCK = 'lock'


class FileFullLockFieldAppTypeField(str, Enum):
    GSUITE = 'gsuite'
    OFFICE_WOPI = 'office_wopi'
    OFFICE_WOPIPLUS = 'office_wopiplus'
    OTHER = 'other'


class FileFullLockField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[FileFullLockFieldTypeField] = None,
        created_by: Optional[UserMini] = None,
        created_at: Optional[str] = None,
        expired_at: Optional[str] = None,
        is_download_prevented: Optional[bool] = None,
        app_type: Optional[FileFullLockFieldAppTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this lock
        :type id: Optional[str], optional
        :param type: `lock`
        :type type: Optional[FileFullLockFieldTypeField], optional
        :param created_at: The time this lock was created at.
        :type created_at: Optional[str], optional
        :param expired_at: The time this lock is to expire at, which might be in the past.
        :type expired_at: Optional[str], optional
        :param is_download_prevented: Whether or not the file can be downloaded while locked.
        :type is_download_prevented: Optional[bool], optional
        :param app_type: If the lock is managed by an application rather than a user, this
            field identifies the type of the application that holds the lock.
            This is an open enum and may be extended with additional values in
            the future.
        :type app_type: Optional[FileFullLockFieldAppTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.created_by = created_by
        self.created_at = created_at
        self.expired_at = expired_at
        self.is_download_prevented = is_download_prevented
        self.app_type = app_type


class FileFullExpiringEmbedLinkFieldTokenTypeField(str, Enum):
    BEARER = 'bearer'


class FileFullExpiringEmbedLinkField(BaseObject):
    def __init__(
        self,
        access_token: Optional[str] = None,
        expires_in: Optional[int] = None,
        token_type: Optional[FileFullExpiringEmbedLinkFieldTokenTypeField] = None,
        restricted_to: Optional[List[FileScope]] = None,
        url: Optional[str] = None,
        **kwargs
    ):
        """
        :param access_token: The requested access token.
        :type access_token: Optional[str], optional
        :param expires_in: The time in seconds by which this token will expire.
        :type expires_in: Optional[int], optional
        :param token_type: The type of access token returned.
        :type token_type: Optional[FileFullExpiringEmbedLinkFieldTokenTypeField], optional
        :param restricted_to: The permissions that this access token permits,
            providing a list of resources (files, folders, etc)
            and the scopes permitted for each of those resources.
        :type restricted_to: Optional[List[FileScope]], optional
        :param url: The actual expiring embed URL for this file, constructed
            from the file ID and access tokens specified in this object.
        :type url: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.restricted_to = restricted_to
        self.url = url


class FileFullWatermarkInfoField(BaseObject):
    def __init__(self, is_watermarked: Optional[bool] = None, **kwargs):
        """
        :param is_watermarked: Specifies if this item has a watermark applied.
        :type is_watermarked: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.is_watermarked = is_watermarked


class FileFullAllowedInviteeRolesField(str, Enum):
    EDITOR = 'editor'
    VIEWER = 'viewer'
    PREVIEWER = 'previewer'
    UPLOADER = 'uploader'
    PREVIEWER_UPLOADER = 'previewer uploader'
    VIEWER_UPLOADER = 'viewer uploader'
    CO_OWNER = 'co-owner'


class FileFullMetadataField(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.extra_data = kwargs


class FileFullRepresentationsFieldEntriesFieldContentField(BaseObject):
    def __init__(self, url_template: Optional[str] = None, **kwargs):
        """
        :param url_template: The download URL that can be used to fetch the representation.
            Make sure to make an authenticated API call to this endpoint.
            This URL is a template and will require the `{+asset_path}` to
            be replaced by a path. In general, for unpaged representations
            it can be replaced by an empty string.
            For paged representations, replace the `{+asset_path}` with the
            page to request plus the extension for the file, for example
            `1.pdf`.
            When requesting the download URL the following additional
            query params can be passed along.
            * `set_content_disposition_type` - Sets the
            `Content-Disposition` header in the API response with the
            specified disposition type of either `inline` or `attachment`.
            If not supplied, the `Content-Disposition` header is not
            included in the response.
            * `set_content_disposition_filename` - Allows the application to
              define the representation's file name used in the
              `Content-Disposition` header.  If not defined, the filename
              is derived from the source file name in Box combined with the
              extension of the representation.
        :type url_template: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.url_template = url_template


class FileFullRepresentationsFieldEntriesFieldInfoField(BaseObject):
    def __init__(self, url: Optional[str] = None, **kwargs):
        """
        :param url: The API URL that can be used to get more info on this file
            representation. Make sure to make an authenticated API call
            to this endpoint.
        :type url: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.url = url


class FileFullRepresentationsFieldEntriesFieldPropertiesField(BaseObject):
    def __init__(
        self,
        dimensions: Optional[str] = None,
        paged: Optional[bool] = None,
        thumb: Optional[bool] = None,
        **kwargs
    ):
        """
        :param dimensions: The width by height size of this representation in pixels.
        :type dimensions: Optional[str], optional
        :param paged: Indicates if the representation is build up out of multiple
            pages.
        :type paged: Optional[bool], optional
        :param thumb: Indicates if the representation can be used as a thumbnail of
            the file.
        :type thumb: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.dimensions = dimensions
        self.paged = paged
        self.thumb = thumb


class FileFullRepresentationsFieldEntriesFieldStatusFieldStateField(str, Enum):
    SUCCESS = 'success'
    VIEWABLE = 'viewable'
    PENDING = 'pending'
    NONE = 'none'


class FileFullRepresentationsFieldEntriesFieldStatusField(BaseObject):
    def __init__(
        self,
        state: Optional[
            FileFullRepresentationsFieldEntriesFieldStatusFieldStateField
        ] = None,
        **kwargs
    ):
        """
        :param state: The status of the representation.
            * `success` defines the representation as ready to be viewed.
            * `viewable` defines a video to be ready for viewing.
            * `pending` defines the representation as to be generated. Retry
              this endpoint to re-check the status.
            * `none` defines that the representation will be created when
              requested. Request the URL defined in the `info` object to
              trigger this generation.
        :type state: Optional[FileFullRepresentationsFieldEntriesFieldStatusFieldStateField], optional
        """
        super().__init__(**kwargs)
        self.state = state


class FileFullRepresentationsFieldEntriesField(BaseObject):
    def __init__(
        self,
        content: Optional[FileFullRepresentationsFieldEntriesFieldContentField] = None,
        info: Optional[FileFullRepresentationsFieldEntriesFieldInfoField] = None,
        properties: Optional[
            FileFullRepresentationsFieldEntriesFieldPropertiesField
        ] = None,
        representation: Optional[str] = None,
        status: Optional[FileFullRepresentationsFieldEntriesFieldStatusField] = None,
        **kwargs
    ):
        """
        :param content: An object containing the URL that can be used to actually fetch
            the representation.
        :type content: Optional[FileFullRepresentationsFieldEntriesFieldContentField], optional
        :param info: An object containing the URL that can be used to fetch more info
            on this representation.
        :type info: Optional[FileFullRepresentationsFieldEntriesFieldInfoField], optional
        :param properties: An object containing the size and type of this presentation.
        :type properties: Optional[FileFullRepresentationsFieldEntriesFieldPropertiesField], optional
        :param representation: Indicates the file type of the returned representation.
        :type representation: Optional[str], optional
        :param status: An object containing the status of this representation.
        :type status: Optional[FileFullRepresentationsFieldEntriesFieldStatusField], optional
        """
        super().__init__(**kwargs)
        self.content = content
        self.info = info
        self.properties = properties
        self.representation = representation
        self.status = status


class FileFullRepresentationsField(BaseObject):
    def __init__(
        self,
        entries: Optional[List[FileFullRepresentationsFieldEntriesField]] = None,
        **kwargs
    ):
        """
        :param entries: A list of files
        :type entries: Optional[List[FileFullRepresentationsFieldEntriesField]], optional
        """
        super().__init__(**kwargs)
        self.entries = entries


class FileFullClassificationField(BaseObject):
    def __init__(
        self,
        name: Optional[str] = None,
        definition: Optional[str] = None,
        color: Optional[str] = None,
        **kwargs
    ):
        """
        :param name: The name of the classification
        :type name: Optional[str], optional
        :param definition: An explanation of the meaning of this classification.
        :type definition: Optional[str], optional
        :param color: The color that is used to display the
            classification label in a user-interface. Colors are defined by the admin
            or co-admin who created the classification in the Box web app.
        :type color: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.definition = definition
        self.color = color


class FileFullSharedLinkPermissionOptionsField(str, Enum):
    CAN_PREVIEW = 'can_preview'
    CAN_DOWNLOAD = 'can_download'
    CAN_EDIT = 'can_edit'


class FileFull(File):
    def __init__(
        self,
        id: str,
        type: FileBaseTypeField,
        version_number: Optional[str] = None,
        comment_count: Optional[int] = None,
        permissions: Optional[FileFullPermissionsField] = None,
        tags: Optional[List[str]] = None,
        lock: Optional[FileFullLockField] = None,
        extension: Optional[str] = None,
        is_package: Optional[bool] = None,
        expiring_embed_link: Optional[FileFullExpiringEmbedLinkField] = None,
        watermark_info: Optional[FileFullWatermarkInfoField] = None,
        is_accessible_via_shared_link: Optional[bool] = None,
        allowed_invitee_roles: Optional[List[FileFullAllowedInviteeRolesField]] = None,
        is_externally_owned: Optional[bool] = None,
        has_collaborations: Optional[bool] = None,
        metadata: Optional[FileFullMetadataField] = None,
        expires_at: Optional[str] = None,
        representations: Optional[FileFullRepresentationsField] = None,
        classification: Optional[FileFullClassificationField] = None,
        uploader_display_name: Optional[str] = None,
        disposition_at: Optional[str] = None,
        shared_link_permission_options: Optional[
            List[FileFullSharedLinkPermissionOptionsField]
        ] = None,
        description: Optional[str] = None,
        size: Optional[int] = None,
        path_collection: Optional[FilePathCollectionField] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        trashed_at: Optional[str] = None,
        purged_at: Optional[str] = None,
        content_created_at: Optional[str] = None,
        content_modified_at: Optional[str] = None,
        created_by: Optional[UserMini] = None,
        modified_by: Optional[UserMini] = None,
        owned_by: Optional[UserMini] = None,
        shared_link: Optional[FileSharedLinkField] = None,
        parent: Optional[FolderMini] = None,
        item_status: Optional[FileItemStatusField] = None,
        sequence_id: Optional[str] = None,
        name: Optional[str] = None,
        sha_1: Optional[str] = None,
        file_version: Optional[FileVersionMini] = None,
        etag: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
        :type id: str
        :param type: `file`
        :type type: FileBaseTypeField
        :param version_number: The version number of this file
        :type version_number: Optional[str], optional
        :param comment_count: The number of comments on this file
        :type comment_count: Optional[int], optional
        :param extension: Indicates the (optional) file extension for this file. By default,
            this is set to an empty string.
        :type extension: Optional[str], optional
        :param is_package: Indicates if the file is a package. Packages are commonly used
            by Mac Applications and can include iWork files.
        :type is_package: Optional[bool], optional
        :param is_accessible_via_shared_link: Specifies if the file can be accessed
            via the direct shared link or a shared link
            to a parent folder.
        :type is_accessible_via_shared_link: Optional[bool], optional
        :param allowed_invitee_roles: A list of the types of roles that user can be invited at
            when sharing this file.
        :type allowed_invitee_roles: Optional[List[FileFullAllowedInviteeRolesField]], optional
        :param is_externally_owned: Specifies if this file is owned by a user outside of the
            authenticated enterprise.
        :type is_externally_owned: Optional[bool], optional
        :param has_collaborations: Specifies if this file has any other collaborators.
        :type has_collaborations: Optional[bool], optional
        :param expires_at: When the file will automatically be deleted
        :type expires_at: Optional[str], optional
        :param disposition_at: The retention expiration timestamp for the given file
        :type disposition_at: Optional[str], optional
        :param shared_link_permission_options: A list of the types of roles that user can be invited at
            when sharing this file.
        :type shared_link_permission_options: Optional[List[FileFullSharedLinkPermissionOptionsField]], optional
        :param description: The optional description of this file
        :type description: Optional[str], optional
        :param size: The file size in bytes. Be careful parsing this integer as it can
            get very large and cause an integer overflow.
        :type size: Optional[int], optional
        :param created_at: The date and time when the file was created on Box.
        :type created_at: Optional[str], optional
        :param modified_at: The date and time when the file was last updated on Box.
        :type modified_at: Optional[str], optional
        :param trashed_at: The time at which this file was put in the trash.
        :type trashed_at: Optional[str], optional
        :param purged_at: The time at which this file is expected to be purged
            from the trash.
        :type purged_at: Optional[str], optional
        :param content_created_at: The date and time at which this file was originally
            created, which might be before it was uploaded to Box.
        :type content_created_at: Optional[str], optional
        :param content_modified_at: The date and time at which this file was last updated,
            which might be before it was uploaded to Box.
        :type content_modified_at: Optional[str], optional
        :param item_status: Defines if this item has been deleted or not.
            * `active` when the item has is not in the trash
            * `trashed` when the item has been moved to the trash but not deleted
            * `deleted` when the item has been permanently deleted.
        :type item_status: Optional[FileItemStatusField], optional
        :param name: The name of the file
        :type name: Optional[str], optional
        :param sha_1: The SHA1 hash of the file. This can be used to compare the contents
            of a file on Box with a local file.
        :type sha_1: Optional[str], optional
        :param etag: The HTTP `etag` of this file. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the file if (no) changes have happened.
        :type etag: Optional[str], optional
        """
        super().__init__(
            id=id,
            type=type,
            description=description,
            size=size,
            path_collection=path_collection,
            created_at=created_at,
            modified_at=modified_at,
            trashed_at=trashed_at,
            purged_at=purged_at,
            content_created_at=content_created_at,
            content_modified_at=content_modified_at,
            created_by=created_by,
            modified_by=modified_by,
            owned_by=owned_by,
            shared_link=shared_link,
            parent=parent,
            item_status=item_status,
            sequence_id=sequence_id,
            name=name,
            sha_1=sha_1,
            file_version=file_version,
            etag=etag,
            **kwargs
        )
        self.version_number = version_number
        self.comment_count = comment_count
        self.permissions = permissions
        self.tags = tags
        self.lock = lock
        self.extension = extension
        self.is_package = is_package
        self.expiring_embed_link = expiring_embed_link
        self.watermark_info = watermark_info
        self.is_accessible_via_shared_link = is_accessible_via_shared_link
        self.allowed_invitee_roles = allowed_invitee_roles
        self.is_externally_owned = is_externally_owned
        self.has_collaborations = has_collaborations
        self.metadata = metadata
        self.expires_at = expires_at
        self.representations = representations
        self.classification = classification
        self.uploader_display_name = uploader_display_name
        self.disposition_at = disposition_at
        self.shared_link_permission_options = shared_link_permission_options


class Files(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        entries: Optional[List[File]] = None,
        **kwargs
    ):
        """
        :param total_count: The number of files.
        :type total_count: Optional[int], optional
        :param entries: A list of files
        :type entries: Optional[List[File]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class DevicePinnerTypeField(str, Enum):
    DEVICE_PINNER = 'device_pinner'


class DevicePinner(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[DevicePinnerTypeField] = None,
        owned_by: Optional[UserMini] = None,
        product_name: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this device pin.
        :type id: Optional[str], optional
        :param type: `device_pinner`
        :type type: Optional[DevicePinnerTypeField], optional
        :param product_name: The type of device being pinned
        :type product_name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.owned_by = owned_by
        self.product_name = product_name


class DevicePinnersOrderFieldByField(str, Enum):
    ID = 'id'


class DevicePinnersOrderFieldDirectionField(str, Enum):
    ASC = 'asc'
    DESC = 'desc'


class DevicePinnersOrderField(BaseObject):
    def __init__(
        self,
        by: Optional[DevicePinnersOrderFieldByField] = None,
        direction: Optional[DevicePinnersOrderFieldDirectionField] = None,
        **kwargs
    ):
        """
        :param by: The field that is ordered by
        :type by: Optional[DevicePinnersOrderFieldByField], optional
        :param direction: The direction to order by, either ascending or descending
        :type direction: Optional[DevicePinnersOrderFieldDirectionField], optional
        """
        super().__init__(**kwargs)
        self.by = by
        self.direction = direction


class DevicePinners(BaseObject):
    def __init__(
        self,
        entries: Optional[List[DevicePinner]] = None,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        order: Optional[List[DevicePinnersOrderField]] = None,
        **kwargs
    ):
        """
        :param entries: A list of device pins
        :type entries: Optional[List[DevicePinner]], optional
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param order: The order by which items are returned.
        :type order: Optional[List[DevicePinnersOrderField]], optional
        """
        super().__init__(**kwargs)
        self.entries = entries
        self.limit = limit
        self.next_marker = next_marker
        self.order = order


class CommentItemField(BaseObject):
    def __init__(self, id: Optional[str] = None, type: Optional[str] = None, **kwargs):
        """
        :param id: The unique identifier for this object
        :type id: Optional[str], optional
        :param type: The type for this object
        :type type: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class Comment(CommentBase):
    def __init__(
        self,
        is_reply_comment: Optional[bool] = None,
        message: Optional[str] = None,
        created_by: Optional[UserMini] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        item: Optional[CommentItemField] = None,
        id: Optional[str] = None,
        type: Optional[CommentBaseTypeField] = None,
        **kwargs
    ):
        """
        :param is_reply_comment: Whether or not this comment is a reply to another
            comment
        :type is_reply_comment: Optional[bool], optional
        :param message: The text of the comment, as provided by the user
        :type message: Optional[str], optional
        :param created_at: The time this comment was created
        :type created_at: Optional[str], optional
        :param modified_at: The time this comment was last modified
        :type modified_at: Optional[str], optional
        :param id: The unique identifier for this comment.
        :type id: Optional[str], optional
        :param type: `comment`
        :type type: Optional[CommentBaseTypeField], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.is_reply_comment = is_reply_comment
        self.message = message
        self.created_by = created_by
        self.created_at = created_at
        self.modified_at = modified_at
        self.item = item


class CommentFull(Comment):
    def __init__(
        self,
        tagged_message: Optional[str] = None,
        is_reply_comment: Optional[bool] = None,
        message: Optional[str] = None,
        created_by: Optional[UserMini] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        item: Optional[CommentItemField] = None,
        id: Optional[str] = None,
        type: Optional[CommentBaseTypeField] = None,
        **kwargs
    ):
        """
        :param tagged_message: The string representing the comment text with
            @mentions included. @mention format is @[id:username]
            where `id` is user's Box ID and `username` is
            their display name.
        :type tagged_message: Optional[str], optional
        :param is_reply_comment: Whether or not this comment is a reply to another
            comment
        :type is_reply_comment: Optional[bool], optional
        :param message: The text of the comment, as provided by the user
        :type message: Optional[str], optional
        :param created_at: The time this comment was created
        :type created_at: Optional[str], optional
        :param modified_at: The time this comment was last modified
        :type modified_at: Optional[str], optional
        :param id: The unique identifier for this comment.
        :type id: Optional[str], optional
        :param type: `comment`
        :type type: Optional[CommentBaseTypeField], optional
        """
        super().__init__(
            is_reply_comment=is_reply_comment,
            message=message,
            created_by=created_by,
            created_at=created_at,
            modified_at=modified_at,
            item=item,
            id=id,
            type=type,
            **kwargs
        )
        self.tagged_message = tagged_message


class CommentsOrderFieldDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class CommentsOrderField(BaseObject):
    def __init__(
        self,
        by: Optional[str] = None,
        direction: Optional[CommentsOrderFieldDirectionField] = None,
        **kwargs
    ):
        """
        :param by: The field to order by
        :type by: Optional[str], optional
        :param direction: The direction to order by, either ascending or descending
        :type direction: Optional[CommentsOrderFieldDirectionField], optional
        """
        super().__init__(**kwargs)
        self.by = by
        self.direction = direction


class Comments(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[List[CommentsOrderField]] = None,
        entries: Optional[List[Comment]] = None,
        **kwargs
    ):
        """
        :param total_count: One greater than the offset of the last entry in the entire collection.
            The total number of entries in the collection may be less than
            `total_count`.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type total_count: Optional[int], optional
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param offset: The 0-based offset of the first entry in this set. This will be the same
            as the `offset` query parameter.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type offset: Optional[int], optional
        :param order: The order by which items are returned.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type order: Optional[List[CommentsOrderField]], optional
        :param entries: A list of comments
        :type entries: Optional[List[Comment]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.limit = limit
        self.offset = offset
        self.order = order
        self.entries = entries


class CollaborationAllowlistExemptTargetTypeField(str, Enum):
    COLLABORATION_WHITELIST_EXEMPT_TARGET = 'collaboration_whitelist_exempt_target'


class CollaborationAllowlistExemptTargetEnterpriseFieldTypeField(str, Enum):
    ENTERPRISE = 'enterprise'


class CollaborationAllowlistExemptTargetEnterpriseField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[
            CollaborationAllowlistExemptTargetEnterpriseFieldTypeField
        ] = None,
        name: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this enterprise.
        :type id: Optional[str], optional
        :param type: `enterprise`
        :type type: Optional[CollaborationAllowlistExemptTargetEnterpriseFieldTypeField], optional
        :param name: The name of the enterprise
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name


class CollaborationAllowlistExemptTarget(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[CollaborationAllowlistExemptTargetTypeField] = None,
        enterprise: Optional[CollaborationAllowlistExemptTargetEnterpriseField] = None,
        user: Optional[UserMini] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this exemption
        :type id: Optional[str], optional
        :param type: `collaboration_whitelist_exempt_target`
        :type type: Optional[CollaborationAllowlistExemptTargetTypeField], optional
        :param created_at: The time the entry was created
        :type created_at: Optional[str], optional
        :param modified_at: The time the entry was modified
        :type modified_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.enterprise = enterprise
        self.user = user
        self.created_at = created_at
        self.modified_at = modified_at


class CollaborationAllowlistExemptTargets(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[CollaborationAllowlistExemptTarget]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of users exempt from any of the restrictions
            imposed by the list of allowed collaboration domains
            for this enterprise.
        :type entries: Optional[List[CollaborationAllowlistExemptTarget]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class ShieldInformationBarrierSegmentRestriction(
    ShieldInformationBarrierSegmentRestrictionMini
):
    def __init__(
        self,
        shield_information_barrier_segment: ShieldInformationBarrierSegmentRestrictionMiniShieldInformationBarrierSegmentField,
        restricted_segment: ShieldInformationBarrierSegmentRestrictionMiniRestrictedSegmentField,
        shield_information_barrier: Optional[ShieldInformationBarrierBase] = None,
        created_at: Optional[str] = None,
        created_by: Optional[UserBase] = None,
        updated_at: Optional[str] = None,
        updated_by: Optional[UserBase] = None,
        type: Optional[ShieldInformationBarrierSegmentRestrictionBaseTypeField] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        """
        :param shield_information_barrier_segment: The `type` and `id` of the
            requested shield information barrier segment.
        :type shield_information_barrier_segment: ShieldInformationBarrierSegmentRestrictionMiniShieldInformationBarrierSegmentField
        :param restricted_segment: The `type` and `id` of the
            restricted shield information barrier segment.
        :type restricted_segment: ShieldInformationBarrierSegmentRestrictionMiniRestrictedSegmentField
        :param created_at: ISO date time string when this
            shield information barrier
            Segment Restriction object was created.
        :type created_at: Optional[str], optional
        :param updated_at: ISO date time string when this
            shield information barrier segment
            Restriction was updated.
        :type updated_at: Optional[str], optional
        :param type: Shield information barrier segment restriction
        :type type: Optional[ShieldInformationBarrierSegmentRestrictionBaseTypeField], optional
        :param id: The unique identifier for the
            shield information barrier segment restriction.
        :type id: Optional[str], optional
        """
        super().__init__(
            shield_information_barrier_segment=shield_information_barrier_segment,
            restricted_segment=restricted_segment,
            type=type,
            id=id,
            **kwargs
        )
        self.shield_information_barrier = shield_information_barrier
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by


class ShieldInformationBarrierSegmentRestrictions(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        entries: Optional[List[ShieldInformationBarrierSegmentRestriction]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        :param entries: A list of shield information barrier
            segment restriction objects
        :type entries: Optional[List[ShieldInformationBarrierSegmentRestriction]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.entries = entries


class ShieldInformationBarrierSegmentMemberMini(
    ShieldInformationBarrierSegmentMemberBase
):
    def __init__(
        self,
        user: Optional[UserBase] = None,
        id: Optional[str] = None,
        type: Optional[ShieldInformationBarrierSegmentMemberBaseTypeField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for the
            shield information barrier segment member
        :type id: Optional[str], optional
        :param type: The type of the shield information barrier segment member
        :type type: Optional[ShieldInformationBarrierSegmentMemberBaseTypeField], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.user = user


class ShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentFieldTypeField(
    str, Enum
):
    SHIELD_INFORMATION_BARRIER_SEGMENT = 'shield_information_barrier_segment'


class ShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentField(
    BaseObject
):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[
            ShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentFieldTypeField
        ] = None,
        **kwargs
    ):
        """
        :param id: The ID reference of the requesting
            shield information barrier segment.
        :type id: Optional[str], optional
        :param type: The type of the shield information barrier segment
        :type type: Optional[ShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class ShieldInformationBarrierSegmentMember(ShieldInformationBarrierSegmentMemberMini):
    def __init__(
        self,
        shield_information_barrier: Optional[ShieldInformationBarrierBase] = None,
        shield_information_barrier_segment: Optional[
            ShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentField
        ] = None,
        created_at: Optional[str] = None,
        created_by: Optional[UserBase] = None,
        updated_at: Optional[str] = None,
        updated_by: Optional[UserBase] = None,
        user: Optional[UserBase] = None,
        id: Optional[str] = None,
        type: Optional[ShieldInformationBarrierSegmentMemberBaseTypeField] = None,
        **kwargs
    ):
        """
        :param shield_information_barrier_segment: The `type` and `id` of the requested
            shield information barrier segment.
        :type shield_information_barrier_segment: Optional[ShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentField], optional
        :param created_at: ISO date time string when this shield
            information barrier object was created.
        :type created_at: Optional[str], optional
        :param updated_at: ISO date time string when this
            shield information barrier segment Member was updated.
        :type updated_at: Optional[str], optional
        :param id: The unique identifier for the
            shield information barrier segment member
        :type id: Optional[str], optional
        :param type: The type of the shield information barrier segment member
        :type type: Optional[ShieldInformationBarrierSegmentMemberBaseTypeField], optional
        """
        super().__init__(user=user, id=id, type=type, **kwargs)
        self.shield_information_barrier = shield_information_barrier
        self.shield_information_barrier_segment = shield_information_barrier_segment
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by


class ShieldInformationBarrierSegmentMembers(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        entries: Optional[List[ShieldInformationBarrierSegmentMember]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        :param entries: A list of shield information
            barrier segment members
        :type entries: Optional[List[ShieldInformationBarrierSegmentMember]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.entries = entries


class ShieldInformationBarrierSegmentTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER_SEGMENT = 'shield_information_barrier_segment'


class ShieldInformationBarrierSegment(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[ShieldInformationBarrierSegmentTypeField] = None,
        shield_information_barrier: Optional[ShieldInformationBarrierBase] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        created_at: Optional[str] = None,
        created_by: Optional[UserBase] = None,
        updated_at: Optional[str] = None,
        updated_by: Optional[UserBase] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for the shield information barrier segment
        :type id: Optional[str], optional
        :param type: The type of the shield information barrier segment
        :type type: Optional[ShieldInformationBarrierSegmentTypeField], optional
        :param name: Name of the shield information barrier segment
        :type name: Optional[str], optional
        :param description: Description of the shield information barrier segment
        :type description: Optional[str], optional
        :param created_at: ISO date time string when this shield information
            barrier object was created.
        :type created_at: Optional[str], optional
        :param updated_at: ISO date time string when this
            shield information barrier segment was updated.
        :type updated_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.shield_information_barrier = shield_information_barrier
        self.name = name
        self.description = description
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by


class ShieldInformationBarrierSegments(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        entries: Optional[List[ShieldInformationBarrierSegment]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        :param entries: A list of shield information barrier
            segments
        :type entries: Optional[List[ShieldInformationBarrierSegment]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.entries = entries


class ShieldInformationBarrierTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER = 'shield_information_barrier'


class ShieldInformationBarrierStatusField(str, Enum):
    DRAFT = 'draft'
    PENDING = 'pending'
    DISABLED = 'disabled'
    ENABLED = 'enabled'
    INVALID = 'invalid'


class ShieldInformationBarrier(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[ShieldInformationBarrierTypeField] = None,
        enterprise: Optional[EnterpriseBase] = None,
        status: Optional[ShieldInformationBarrierStatusField] = None,
        created_at: Optional[str] = None,
        created_by: Optional[UserBase] = None,
        updated_at: Optional[str] = None,
        updated_by: Optional[UserBase] = None,
        enabled_at: Optional[str] = None,
        enabled_by: Optional[UserBase] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for the shield information barrier
        :type id: Optional[str], optional
        :param type: The type of the shield information barrier
        :type type: Optional[ShieldInformationBarrierTypeField], optional
        :param enterprise: The `type` and `id` of enterprise this barrier is under.
        :type enterprise: Optional[EnterpriseBase], optional
        :param status: Status of the shield information barrier
        :type status: Optional[ShieldInformationBarrierStatusField], optional
        :param created_at: ISO date time string when this
            shield information barrier object was created.
        :type created_at: Optional[str], optional
        :param created_by: The user who created this shield information barrier.
        :type created_by: Optional[UserBase], optional
        :param updated_at: ISO date time string when this shield information barrier was updated.
        :type updated_at: Optional[str], optional
        :param updated_by: The user that updated this shield information barrier.
        :type updated_by: Optional[UserBase], optional
        :param enabled_at: ISO date time string when this shield information barrier was enabled.
        :type enabled_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.enterprise = enterprise
        self.status = status
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.enabled_at = enabled_at
        self.enabled_by = enabled_by


class ShieldInformationBarriers(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        entries: Optional[List[ShieldInformationBarrier]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        :param entries: A list of shield information barrier objects
        :type entries: Optional[List[ShieldInformationBarrier]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.entries = entries


class FolderLockLockedOperationsField(BaseObject):
    def __init__(self, move: bool, delete: bool, **kwargs):
        """
        :param move: Whether moving the folder is restricted.
        :type move: bool
        :param delete: Whether deleting the folder is restricted.
        :type delete: bool
        """
        super().__init__(**kwargs)
        self.move = move
        self.delete = delete


class FolderLock(BaseObject):
    def __init__(
        self,
        folder: Optional[FolderMini] = None,
        id: Optional[str] = None,
        type: Optional[str] = None,
        created_by: Optional[UserBase] = None,
        created_at: Optional[str] = None,
        locked_operations: Optional[FolderLockLockedOperationsField] = None,
        lock_type: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this folder lock.
        :type id: Optional[str], optional
        :param type: The object type, always `folder_lock`.
        :type type: Optional[str], optional
        :param created_at: When the folder lock object was created.
        :type created_at: Optional[str], optional
        :param locked_operations: The operations that have been locked. Currently the `move`
            and `delete` operations cannot be locked separately, and both need to be
            set to `true`.
        :type locked_operations: Optional[FolderLockLockedOperationsField], optional
        :param lock_type: The lock type, always `freeze`.
        :type lock_type: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.folder = folder
        self.id = id
        self.type = type
        self.created_by = created_by
        self.created_at = created_at
        self.locked_operations = locked_operations
        self.lock_type = lock_type


class FolderLocks(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[FolderLock]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of folder locks
        :type entries: Optional[List[FolderLock]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class WatermarkWatermarkField(BaseObject):
    def __init__(
        self,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        **kwargs
    ):
        """
        :param created_at: When this watermark was created
        :type created_at: Optional[str], optional
        :param modified_at: When this task was modified
        :type modified_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.created_at = created_at
        self.modified_at = modified_at


class Watermark(BaseObject):
    def __init__(self, watermark: Optional[WatermarkWatermarkField] = None, **kwargs):
        super().__init__(**kwargs)
        self.watermark = watermark


class WebhookMiniTypeField(str, Enum):
    WEBHOOK = 'webhook'


class WebhookMiniTargetFieldTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'


class WebhookMiniTargetField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[WebhookMiniTargetFieldTypeField] = None,
        **kwargs
    ):
        """
        :param id: The ID of the item to trigger a webhook
        :type id: Optional[str], optional
        :param type: The type of item to trigger a webhook
        :type type: Optional[WebhookMiniTargetFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class WebhookMini(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[WebhookMiniTypeField] = None,
        target: Optional[WebhookMiniTargetField] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this webhook.
        :type id: Optional[str], optional
        :param type: `webhook`
        :type type: Optional[WebhookMiniTypeField], optional
        :param target: The item that will trigger the webhook
        :type target: Optional[WebhookMiniTargetField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.target = target


class Webhooks(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[WebhookMini]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of webhooks
        :type entries: Optional[List[WebhookMini]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class WebhookTriggersField(str, Enum):
    FILE_UPLOADED = 'FILE.UPLOADED'
    FILE_PREVIEWED = 'FILE.PREVIEWED'
    FILE_DOWNLOADED = 'FILE.DOWNLOADED'
    FILE_TRASHED = 'FILE.TRASHED'
    FILE_DELETED = 'FILE.DELETED'
    FILE_RESTORED = 'FILE.RESTORED'
    FILE_COPIED = 'FILE.COPIED'
    FILE_MOVED = 'FILE.MOVED'
    FILE_LOCKED = 'FILE.LOCKED'
    FILE_UNLOCKED = 'FILE.UNLOCKED'
    FILE_RENAMED = 'FILE.RENAMED'
    COMMENT_CREATED = 'COMMENT.CREATED'
    COMMENT_UPDATED = 'COMMENT.UPDATED'
    COMMENT_DELETED = 'COMMENT.DELETED'
    TASK_ASSIGNMENT_CREATED = 'TASK_ASSIGNMENT.CREATED'
    TASK_ASSIGNMENT_UPDATED = 'TASK_ASSIGNMENT.UPDATED'
    METADATA_INSTANCE_CREATED = 'METADATA_INSTANCE.CREATED'
    METADATA_INSTANCE_UPDATED = 'METADATA_INSTANCE.UPDATED'
    METADATA_INSTANCE_DELETED = 'METADATA_INSTANCE.DELETED'
    FOLDER_CREATED = 'FOLDER.CREATED'
    FOLDER_RENAMED = 'FOLDER.RENAMED'
    FOLDER_DOWNLOADED = 'FOLDER.DOWNLOADED'
    FOLDER_RESTORED = 'FOLDER.RESTORED'
    FOLDER_DELETED = 'FOLDER.DELETED'
    FOLDER_COPIED = 'FOLDER.COPIED'
    FOLDER_MOVED = 'FOLDER.MOVED'
    FOLDER_TRASHED = 'FOLDER.TRASHED'
    WEBHOOK_DELETED = 'WEBHOOK.DELETED'
    COLLABORATION_CREATED = 'COLLABORATION.CREATED'
    COLLABORATION_ACCEPTED = 'COLLABORATION.ACCEPTED'
    COLLABORATION_REJECTED = 'COLLABORATION.REJECTED'
    COLLABORATION_REMOVED = 'COLLABORATION.REMOVED'
    COLLABORATION_UPDATED = 'COLLABORATION.UPDATED'
    SHARED_LINK_DELETED = 'SHARED_LINK.DELETED'
    SHARED_LINK_CREATED = 'SHARED_LINK.CREATED'
    SHARED_LINK_UPDATED = 'SHARED_LINK.UPDATED'
    SIGN_REQUEST_COMPLETED = 'SIGN_REQUEST.COMPLETED'
    SIGN_REQUEST_DECLINED = 'SIGN_REQUEST.DECLINED'
    SIGN_REQUEST_EXPIRED = 'SIGN_REQUEST.EXPIRED'
    SIGN_REQUEST_SIGNER_EMAIL_BOUNCED = 'SIGN_REQUEST.SIGNER_EMAIL_BOUNCED'


class Webhook(WebhookMini):
    def __init__(
        self,
        created_by: Optional[UserMini] = None,
        created_at: Optional[str] = None,
        address: Optional[str] = None,
        triggers: Optional[List[WebhookTriggersField]] = None,
        id: Optional[str] = None,
        type: Optional[WebhookMiniTypeField] = None,
        target: Optional[WebhookMiniTargetField] = None,
        **kwargs
    ):
        """
        :param created_at: A timestamp identifying the time that
            the webhook was created.
        :type created_at: Optional[str], optional
        :param address: The URL that is notified by this webhook
        :type address: Optional[str], optional
        :param triggers: An array of event names that this webhook is
            to be triggered for
        :type triggers: Optional[List[WebhookTriggersField]], optional
        :param id: The unique identifier for this webhook.
        :type id: Optional[str], optional
        :param type: `webhook`
        :type type: Optional[WebhookMiniTypeField], optional
        :param target: The item that will trigger the webhook
        :type target: Optional[WebhookMiniTargetField], optional
        """
        super().__init__(id=id, type=type, target=target, **kwargs)
        self.created_by = created_by
        self.created_at = created_at
        self.address = address
        self.triggers = triggers


class WebLinkBaseTypeField(str, Enum):
    WEB_LINK = 'web_link'


class WebLinkBase(BaseObject):
    def __init__(
        self, id: str, type: WebLinkBaseTypeField, etag: Optional[str] = None, **kwargs
    ):
        """
        :param id: The unique identifier for this web link
        :type id: str
        :param type: `web_link`
        :type type: WebLinkBaseTypeField
        :param etag: The entity tag of this web link. Used with `If-Match`
            headers.
        :type etag: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.etag = etag


class WebLinkMini(WebLinkBase):
    def __init__(
        self,
        id: str,
        type: WebLinkBaseTypeField,
        url: Optional[str] = None,
        sequence_id: Optional[str] = None,
        name: Optional[str] = None,
        etag: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this web link
        :type id: str
        :param type: `web_link`
        :type type: WebLinkBaseTypeField
        :param url: The URL this web link points to
        :type url: Optional[str], optional
        :param name: The name of the web link
        :type name: Optional[str], optional
        :param etag: The entity tag of this web link. Used with `If-Match`
            headers.
        :type etag: Optional[str], optional
        """
        super().__init__(id=id, type=type, etag=etag, **kwargs)
        self.url = url
        self.sequence_id = sequence_id
        self.name = name


class WebLinkPathCollectionField(BaseObject):
    def __init__(self, total_count: int, entries: List[FolderMini], **kwargs):
        """
        :param total_count: The number of folders in this list.
        :type total_count: int
        :param entries: The parent folders for this item
        :type entries: List[FolderMini]
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class WebLinkSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'


class WebLinkSharedLinkFieldEffectiveAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'


class WebLinkSharedLinkFieldEffectivePermissionField(str, Enum):
    CAN_EDIT = 'can_edit'
    CAN_DOWNLOAD = 'can_download'
    CAN_PREVIEW = 'can_preview'
    NO_ACCESS = 'no_access'


class WebLinkSharedLinkFieldPermissionsField(BaseObject):
    def __init__(self, can_download: bool, can_preview: bool, can_edit: bool, **kwargs):
        """
        :param can_download: Defines if the shared link allows for the item to be downloaded. For
            shared links on folders, this also applies to any items in the folder.
            This value can be set to `true` when the effective access level is
            set to `open` or `company`, not `collaborators`.
        :type can_download: bool
        :param can_preview: Defines if the shared link allows for the item to be previewed.
            This value is always `true`. For shared links on folders this also
            applies to any items in the folder.
        :type can_preview: bool
        :param can_edit: Defines if the shared link allows for the item to be edited.
            This value can only be `true` if `can_download` is also `true` and if
            the item has a type of `file`.
        :type can_edit: bool
        """
        super().__init__(**kwargs)
        self.can_download = can_download
        self.can_preview = can_preview
        self.can_edit = can_edit


class WebLinkSharedLinkField(BaseObject):
    def __init__(
        self,
        url: str,
        effective_access: WebLinkSharedLinkFieldEffectiveAccessField,
        effective_permission: WebLinkSharedLinkFieldEffectivePermissionField,
        is_password_enabled: bool,
        download_count: int,
        preview_count: int,
        download_url: Optional[str] = None,
        vanity_url: Optional[str] = None,
        vanity_name: Optional[str] = None,
        access: Optional[WebLinkSharedLinkFieldAccessField] = None,
        unshared_at: Optional[str] = None,
        permissions: Optional[WebLinkSharedLinkFieldPermissionsField] = None,
        **kwargs
    ):
        """
        :param url: The URL that can be used to access the item on Box.
            This URL will display the item in Box's preview UI where the file
            can be downloaded if allowed.
            This URL will continue to work even when a custom `vanity_url`
            has been set for this shared link.
        :type url: str
        :param effective_access: The effective access level for the shared link. This can be a more
            restrictive access level than the value in the `access` field when the
            enterprise settings restrict the allowed access levels.
        :type effective_access: WebLinkSharedLinkFieldEffectiveAccessField
        :param effective_permission: The effective permissions for this shared link.
            These result in the more restrictive combination of
            the share link permissions and the item permissions set
            by the administrator, the owner, and any ancestor item
            such as a folder.
        :type effective_permission: WebLinkSharedLinkFieldEffectivePermissionField
        :param is_password_enabled: Defines if the shared link requires a password to access the item.
        :type is_password_enabled: bool
        :param download_count: The number of times this item has been downloaded.
        :type download_count: int
        :param preview_count: The number of times this item has been previewed.
        :type preview_count: int
        :param download_url: A URL that can be used to download the file. This URL can be used in
            a browser to download the file. This URL includes the file
            extension so that the file will be saved with the right file type.
            This property will be `null` for folders.
        :type download_url: Optional[str], optional
        :param vanity_url: The "Custom URL" that can also be used to preview the item on Box.  Custom
            URLs can only be created or modified in the Box Web application.
        :type vanity_url: Optional[str], optional
        :param vanity_name: The custom name of a shared link, as used in the `vanity_url` field.
        :type vanity_name: Optional[str], optional
        :param access: The access level for this shared link.
            * `open` - provides access to this item to anyone with this link
            * `company` - only provides access to this item to people the same company
            * `collaborators` - only provides access to this item to people who are
               collaborators on this item
            If this field is omitted when creating the shared link, the access level
            will be set to the default access level specified by the enterprise admin.
        :type access: Optional[WebLinkSharedLinkFieldAccessField], optional
        :param unshared_at: The date and time when this link will be unshared. This field can only be
            set by users with paid accounts.
        :type unshared_at: Optional[str], optional
        :param permissions: Defines if this link allows a user to preview, edit, and download an item.
            These permissions refer to the shared link only and
            do not supersede permissions applied to the item itself.
        :type permissions: Optional[WebLinkSharedLinkFieldPermissionsField], optional
        """
        super().__init__(**kwargs)
        self.url = url
        self.effective_access = effective_access
        self.effective_permission = effective_permission
        self.is_password_enabled = is_password_enabled
        self.download_count = download_count
        self.preview_count = preview_count
        self.download_url = download_url
        self.vanity_url = vanity_url
        self.vanity_name = vanity_name
        self.access = access
        self.unshared_at = unshared_at
        self.permissions = permissions


class WebLinkItemStatusField(str, Enum):
    ACTIVE = 'active'
    TRASHED = 'trashed'
    DELETED = 'deleted'


class WebLink(WebLinkMini):
    def __init__(
        self,
        id: str,
        type: WebLinkBaseTypeField,
        parent: Optional[FolderMini] = None,
        description: Optional[str] = None,
        path_collection: Optional[WebLinkPathCollectionField] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        trashed_at: Optional[str] = None,
        purged_at: Optional[str] = None,
        created_by: Optional[UserMini] = None,
        modified_by: Optional[UserMini] = None,
        owned_by: Optional[UserMini] = None,
        shared_link: Optional[WebLinkSharedLinkField] = None,
        item_status: Optional[WebLinkItemStatusField] = None,
        url: Optional[str] = None,
        sequence_id: Optional[str] = None,
        name: Optional[str] = None,
        etag: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this web link
        :type id: str
        :param type: `web_link`
        :type type: WebLinkBaseTypeField
        :param description: The description accompanying the web link. This is
            visible within the Box web application.
        :type description: Optional[str], optional
        :param created_at: When this file was created on Box’s servers.
        :type created_at: Optional[str], optional
        :param modified_at: When this file was last updated on the Box
            servers.
        :type modified_at: Optional[str], optional
        :param trashed_at: When this file was moved to the trash.
        :type trashed_at: Optional[str], optional
        :param purged_at: When this file will be permanently deleted.
        :type purged_at: Optional[str], optional
        :param item_status: Whether this item is deleted or not. Values include `active`,
            `trashed` if the file has been moved to the trash, and `deleted` if
            the file has been permanently deleted
        :type item_status: Optional[WebLinkItemStatusField], optional
        :param url: The URL this web link points to
        :type url: Optional[str], optional
        :param name: The name of the web link
        :type name: Optional[str], optional
        :param etag: The entity tag of this web link. Used with `If-Match`
            headers.
        :type etag: Optional[str], optional
        """
        super().__init__(
            id=id,
            type=type,
            url=url,
            sequence_id=sequence_id,
            name=name,
            etag=etag,
            **kwargs
        )
        self.parent = parent
        self.description = description
        self.path_collection = path_collection
        self.created_at = created_at
        self.modified_at = modified_at
        self.trashed_at = trashed_at
        self.purged_at = purged_at
        self.created_by = created_by
        self.modified_by = modified_by
        self.owned_by = owned_by
        self.shared_link = shared_link
        self.item_status = item_status


class ItemsOrderFieldDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class ItemsOrderField(BaseObject):
    def __init__(
        self,
        by: Optional[str] = None,
        direction: Optional[ItemsOrderFieldDirectionField] = None,
        **kwargs
    ):
        """
        :param by: The field to order by
        :type by: Optional[str], optional
        :param direction: The direction to order by, either ascending or descending
        :type direction: Optional[ItemsOrderFieldDirectionField], optional
        """
        super().__init__(**kwargs)
        self.by = by
        self.direction = direction


class Items(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[List[ItemsOrderField]] = None,
        entries: Optional[List[Union[FileMini, FolderMini, WebLinkMini]]] = None,
        **kwargs
    ):
        """
        :param total_count: One greater than the offset of the last entry in the entire collection.
            The total number of entries in the collection may be less than
            `total_count`.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type total_count: Optional[int], optional
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param offset: The 0-based offset of the first entry in this set. This will be the same
            as the `offset` query parameter.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type offset: Optional[int], optional
        :param order: The order by which items are returned.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type order: Optional[List[ItemsOrderField]], optional
        :param entries: The items in this collection.
        :type entries: Optional[List[Union[FileMini, FolderMini, WebLinkMini]]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.limit = limit
        self.offset = offset
        self.order = order
        self.entries = entries


class FolderPathCollectionField(BaseObject):
    def __init__(self, total_count: int, entries: List[FolderMini], **kwargs):
        """
        :param total_count: The number of folders in this list.
        :type total_count: int
        :param entries: The parent folders for this item
        :type entries: List[FolderMini]
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries


class FolderSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'


class FolderSharedLinkFieldEffectiveAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'


class FolderSharedLinkFieldEffectivePermissionField(str, Enum):
    CAN_EDIT = 'can_edit'
    CAN_DOWNLOAD = 'can_download'
    CAN_PREVIEW = 'can_preview'
    NO_ACCESS = 'no_access'


class FolderSharedLinkFieldPermissionsField(BaseObject):
    def __init__(self, can_download: bool, can_preview: bool, can_edit: bool, **kwargs):
        """
        :param can_download: Defines if the shared link allows for the item to be downloaded. For
            shared links on folders, this also applies to any items in the folder.
            This value can be set to `true` when the effective access level is
            set to `open` or `company`, not `collaborators`.
        :type can_download: bool
        :param can_preview: Defines if the shared link allows for the item to be previewed.
            This value is always `true`. For shared links on folders this also
            applies to any items in the folder.
        :type can_preview: bool
        :param can_edit: Defines if the shared link allows for the item to be edited.
            This value can only be `true` if `can_download` is also `true` and if
            the item has a type of `file`.
        :type can_edit: bool
        """
        super().__init__(**kwargs)
        self.can_download = can_download
        self.can_preview = can_preview
        self.can_edit = can_edit


class FolderSharedLinkField(BaseObject):
    def __init__(
        self,
        url: str,
        effective_access: FolderSharedLinkFieldEffectiveAccessField,
        effective_permission: FolderSharedLinkFieldEffectivePermissionField,
        is_password_enabled: bool,
        download_count: int,
        preview_count: int,
        download_url: Optional[str] = None,
        vanity_url: Optional[str] = None,
        vanity_name: Optional[str] = None,
        access: Optional[FolderSharedLinkFieldAccessField] = None,
        unshared_at: Optional[str] = None,
        permissions: Optional[FolderSharedLinkFieldPermissionsField] = None,
        **kwargs
    ):
        """
        :param url: The URL that can be used to access the item on Box.
            This URL will display the item in Box's preview UI where the file
            can be downloaded if allowed.
            This URL will continue to work even when a custom `vanity_url`
            has been set for this shared link.
        :type url: str
        :param effective_access: The effective access level for the shared link. This can be a more
            restrictive access level than the value in the `access` field when the
            enterprise settings restrict the allowed access levels.
        :type effective_access: FolderSharedLinkFieldEffectiveAccessField
        :param effective_permission: The effective permissions for this shared link.
            These result in the more restrictive combination of
            the share link permissions and the item permissions set
            by the administrator, the owner, and any ancestor item
            such as a folder.
        :type effective_permission: FolderSharedLinkFieldEffectivePermissionField
        :param is_password_enabled: Defines if the shared link requires a password to access the item.
        :type is_password_enabled: bool
        :param download_count: The number of times this item has been downloaded.
        :type download_count: int
        :param preview_count: The number of times this item has been previewed.
        :type preview_count: int
        :param download_url: A URL that can be used to download the file. This URL can be used in
            a browser to download the file. This URL includes the file
            extension so that the file will be saved with the right file type.
            This property will be `null` for folders.
        :type download_url: Optional[str], optional
        :param vanity_url: The "Custom URL" that can also be used to preview the item on Box.  Custom
            URLs can only be created or modified in the Box Web application.
        :type vanity_url: Optional[str], optional
        :param vanity_name: The custom name of a shared link, as used in the `vanity_url` field.
        :type vanity_name: Optional[str], optional
        :param access: The access level for this shared link.
            * `open` - provides access to this item to anyone with this link
            * `company` - only provides access to this item to people the same company
            * `collaborators` - only provides access to this item to people who are
               collaborators on this item
            If this field is omitted when creating the shared link, the access level
            will be set to the default access level specified by the enterprise admin.
        :type access: Optional[FolderSharedLinkFieldAccessField], optional
        :param unshared_at: The date and time when this link will be unshared. This field can only be
            set by users with paid accounts.
        :type unshared_at: Optional[str], optional
        :param permissions: Defines if this link allows a user to preview, edit, and download an item.
            These permissions refer to the shared link only and
            do not supersede permissions applied to the item itself.
        :type permissions: Optional[FolderSharedLinkFieldPermissionsField], optional
        """
        super().__init__(**kwargs)
        self.url = url
        self.effective_access = effective_access
        self.effective_permission = effective_permission
        self.is_password_enabled = is_password_enabled
        self.download_count = download_count
        self.preview_count = preview_count
        self.download_url = download_url
        self.vanity_url = vanity_url
        self.vanity_name = vanity_name
        self.access = access
        self.unshared_at = unshared_at
        self.permissions = permissions


class FolderFolderUploadEmailFieldAccessField(str, Enum):
    OPEN = 'open'
    COLLABORATORS = 'collaborators'


class FolderFolderUploadEmailField(BaseObject):
    def __init__(
        self,
        access: Optional[FolderFolderUploadEmailFieldAccessField] = None,
        email: Optional[str] = None,
        **kwargs
    ):
        """
        :param access: When this parameter has been set, users can email files
            to the email address that has been automatically
            created for this folder.
            To create an email address, set this property either when
            creating or updating the folder.
            When set to `collaborators`, only emails from registered email
            addresses for collaborators will be accepted. This includes
            any email aliases a user might have registered.
            When set to `open` it will accept emails from any email
            address.
        :type access: Optional[FolderFolderUploadEmailFieldAccessField], optional
        :param email: The optional upload email address for this folder.
        :type email: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.email = email


class FolderItemStatusField(str, Enum):
    ACTIVE = 'active'
    TRASHED = 'trashed'
    DELETED = 'deleted'


class Folder(FolderMini):
    def __init__(
        self,
        id: str,
        type: FolderBaseTypeField,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        description: Optional[str] = None,
        size: Optional[int] = None,
        path_collection: Optional[FolderPathCollectionField] = None,
        created_by: Optional[UserMini] = None,
        modified_by: Optional[UserMini] = None,
        trashed_at: Optional[str] = None,
        purged_at: Optional[str] = None,
        content_created_at: Optional[str] = None,
        content_modified_at: Optional[str] = None,
        owned_by: Optional[UserMini] = None,
        shared_link: Optional[FolderSharedLinkField] = None,
        folder_upload_email: Optional[FolderFolderUploadEmailField] = None,
        parent: Optional[FolderMini] = None,
        item_status: Optional[FolderItemStatusField] = None,
        item_collection: Optional[Items] = None,
        sequence_id: Optional[str] = None,
        name: Optional[str] = None,
        etag: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting a folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folders/123`
            the `folder_id` is `123`.
        :type id: str
        :param type: `folder`
        :type type: FolderBaseTypeField
        :param created_at: The date and time when the folder was created. This value may
            be `null` for some folders such as the root folder or the trash
            folder.
        :type created_at: Optional[str], optional
        :param modified_at: The date and time when the folder was last updated. This value may
            be `null` for some folders such as the root folder or the trash
            folder.
        :type modified_at: Optional[str], optional
        :param size: The folder size in bytes.
            Be careful parsing this integer as its
            value can get very large.
        :type size: Optional[int], optional
        :param trashed_at: The time at which this folder was put in the trash.
        :type trashed_at: Optional[str], optional
        :param purged_at: The time at which this folder is expected to be purged
            from the trash.
        :type purged_at: Optional[str], optional
        :param content_created_at: The date and time at which this folder was originally
            created.
        :type content_created_at: Optional[str], optional
        :param content_modified_at: The date and time at which this folder was last updated.
        :type content_modified_at: Optional[str], optional
        :param item_status: Defines if this item has been deleted or not.
            * `active` when the item has is not in the trash
            * `trashed` when the item has been moved to the trash but not deleted
            * `deleted` when the item has been permanently deleted.
        :type item_status: Optional[FolderItemStatusField], optional
        :param name: The name of the folder.
        :type name: Optional[str], optional
        :param etag: The HTTP `etag` of this folder. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the folder if (no) changes have happened.
        :type etag: Optional[str], optional
        """
        super().__init__(
            id=id, type=type, sequence_id=sequence_id, name=name, etag=etag, **kwargs
        )
        self.created_at = created_at
        self.modified_at = modified_at
        self.description = description
        self.size = size
        self.path_collection = path_collection
        self.created_by = created_by
        self.modified_by = modified_by
        self.trashed_at = trashed_at
        self.purged_at = purged_at
        self.content_created_at = content_created_at
        self.content_modified_at = content_modified_at
        self.owned_by = owned_by
        self.shared_link = shared_link
        self.folder_upload_email = folder_upload_email
        self.parent = parent
        self.item_status = item_status
        self.item_collection = item_collection


class SearchResultWithSharedLink(BaseObject):
    def __init__(
        self,
        accessible_via_shared_link: Optional[str] = None,
        item: Optional[Union[File, Folder, WebLink]] = None,
        type: Optional[str] = None,
        **kwargs
    ):
        """
        :param accessible_via_shared_link: The optional shared link through which the user has access to this
            item. This value is only returned for items for which the user has
            recently accessed the file through a shared link. For all other
            items this value will return `null`.
        :type accessible_via_shared_link: Optional[str], optional
        :param type: The result type. The value is always `search_result`.
        :type type: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.accessible_via_shared_link = accessible_via_shared_link
        self.item = item
        self.type = type


class SearchResultsWithSharedLinksTypeField(str, Enum):
    SEARCH_RESULTS_WITH_SHARED_LINKS = 'search_results_with_shared_links'


class SearchResultsWithSharedLinks(BaseObject):
    def __init__(
        self,
        type: SearchResultsWithSharedLinksTypeField,
        total_count: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        entries: Optional[List[SearchResultWithSharedLink]] = None,
        **kwargs
    ):
        """
        :param type: Specifies the response as search result items with shared links
        :type type: SearchResultsWithSharedLinksTypeField
        :param total_count: One greater than the offset of the last entry in the search results.
            The total number of entries in the collection may be less than
            `total_count`.
        :type total_count: Optional[int], optional
        :param limit: The limit that was used for this search. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed.
        :type limit: Optional[int], optional
        :param offset: The 0-based offset of the first entry in this set. This will be the same
            as the `offset` query parameter used.
        :type offset: Optional[int], optional
        :param entries: The search results for the query provided, including the
            additional information about any shared links through
            which the item has been shared with the user.
        :type entries: Optional[List[SearchResultWithSharedLink]], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.total_count = total_count
        self.limit = limit
        self.offset = offset
        self.entries = entries


class SearchResultsTypeField(str, Enum):
    SEARCH_RESULTS_ITEMS = 'search_results_items'


class SearchResults(BaseObject):
    def __init__(
        self,
        type: SearchResultsTypeField,
        total_count: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        entries: Optional[List[Union[File, Folder, WebLink]]] = None,
        **kwargs
    ):
        """
        :param type: Specifies the response as search result items without shared links
        :type type: SearchResultsTypeField
        :param total_count: One greater than the offset of the last entry in the search results.
            The total number of entries in the collection may be less than
            `total_count`.
        :type total_count: Optional[int], optional
        :param limit: The limit that was used for this search. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed.
        :type limit: Optional[int], optional
        :param offset: The 0-based offset of the first entry in this set. This will be the same
            as the `offset` query parameter used.
        :type offset: Optional[int], optional
        :param entries: The search results for the query provided.
        :type entries: Optional[List[Union[File, Folder, WebLink]]], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.total_count = total_count
        self.limit = limit
        self.offset = offset
        self.entries = entries


class RecentItemInteractionTypeField(str, Enum):
    ITEM_PREVIEW = 'item_preview'
    ITEM_UPLOAD = 'item_upload'
    ITEM_COMMENT = 'item_comment'
    ITEM_OPEN = 'item_open'
    ITEM_MODIFY = 'item_modify'


class RecentItem(BaseObject):
    def __init__(
        self,
        type: Optional[str] = None,
        item: Optional[Union[File, Folder, WebLink]] = None,
        interaction_type: Optional[RecentItemInteractionTypeField] = None,
        interacted_at: Optional[str] = None,
        interaction_shared_link: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: `recent_item`
        :type type: Optional[str], optional
        :param interaction_type: The most recent type of access the user performed on
            the item.
        :type interaction_type: Optional[RecentItemInteractionTypeField], optional
        :param interacted_at: The time of the most recent interaction.
        :type interacted_at: Optional[str], optional
        :param interaction_shared_link: If the item was accessed through a shared link it will appear here,
            otherwise this will be null.
        :type interaction_shared_link: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.item = item
        self.interaction_type = interaction_type
        self.interacted_at = interacted_at
        self.interaction_shared_link = interaction_shared_link


class RecentItems(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        prev_marker: Optional[str] = None,
        entries: Optional[List[RecentItem]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[str], optional
        :param entries: A list of recent items
        :type entries: Optional[List[RecentItem]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class MetadataQueryResults(BaseObject):
    def __init__(
        self,
        entries: Optional[List[Union[File, Folder]]] = None,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        **kwargs
    ):
        """
        :param entries: The mini representation of the files and folders that match the search
            terms.
            By default, this endpoint returns only the most basic info about the
            items. To get additional fields for each item, including any of the
            metadata, use the `fields` attribute in the query.
        :type entries: Optional[List[Union[File, Folder]]], optional
        :param limit: The limit that was used for this search. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.entries = entries
        self.limit = limit
        self.next_marker = next_marker


class LegalHoldPolicyAssignment(LegalHoldPolicyAssignmentBase):
    def __init__(
        self,
        legal_hold_policy: Optional[LegalHoldPolicyMini] = None,
        assigned_to: Optional[Union[File, Folder, WebLink]] = None,
        assigned_by: Optional[UserMini] = None,
        assigned_at: Optional[str] = None,
        deleted_at: Optional[str] = None,
        id: Optional[str] = None,
        type: Optional[LegalHoldPolicyAssignmentBaseTypeField] = None,
        **kwargs
    ):
        """
        :param assigned_at: When the legal hold policy assignment object was
            created
        :type assigned_at: Optional[str], optional
        :param deleted_at: When the assignment release request was sent.
            (Because it can take time for an assignment to fully
            delete, this isn't quite the same time that the
            assignment is fully deleted). If null, Assignment
            was not deleted.
        :type deleted_at: Optional[str], optional
        :param id: The unique identifier for this legal hold assignment
        :type id: Optional[str], optional
        :param type: `legal_hold_policy_assignment`
        :type type: Optional[LegalHoldPolicyAssignmentBaseTypeField], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.legal_hold_policy = legal_hold_policy
        self.assigned_to = assigned_to
        self.assigned_by = assigned_by
        self.assigned_at = assigned_at
        self.deleted_at = deleted_at


class FileVersionLegalHoldTypeField(str, Enum):
    FILE_VERSION_LEGAL_HOLD = 'file_version_legal_hold'


class FileVersionLegalHold(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[FileVersionLegalHoldTypeField] = None,
        file_version: Optional[FileVersionMini] = None,
        file: Optional[FileMini] = None,
        legal_hold_policy_assignments: Optional[List[LegalHoldPolicyAssignment]] = None,
        deleted_at: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this file version legal hold
        :type id: Optional[str], optional
        :param type: `file_version_legal_hold`
        :type type: Optional[FileVersionLegalHoldTypeField], optional
        :param legal_hold_policy_assignments: List of assignments contributing to this Hold.
        :type legal_hold_policy_assignments: Optional[List[LegalHoldPolicyAssignment]], optional
        :param deleted_at: Time that this File-Version-Legal-Hold was
            deleted.
        :type deleted_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.file_version = file_version
        self.file = file
        self.legal_hold_policy_assignments = legal_hold_policy_assignments
        self.deleted_at = deleted_at


class FileVersionLegalHolds(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[FileVersionLegalHold]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of file version legal holds
        :type entries: Optional[List[FileVersionLegalHold]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class FolderFullSyncStateField(str, Enum):
    SYNCED = 'synced'
    NOT_SYNCED = 'not_synced'
    PARTIALLY_SYNCED = 'partially_synced'


class FolderFullPermissionsField(BaseObject):
    def __init__(
        self,
        can_delete: bool,
        can_download: bool,
        can_invite_collaborator: bool,
        can_rename: bool,
        can_set_share_access: bool,
        can_share: bool,
        can_upload: Optional[bool] = None,
        **kwargs
    ):
        """
        :param can_delete: Specifies if the current user can delete this item.
        :type can_delete: bool
        :param can_download: Specifies if the current user can download this item.
        :type can_download: bool
        :param can_invite_collaborator: Specifies if the current user can invite new
            users to collaborate on this item, and if the user can
            update the role of a user already collaborated on this
            item.
        :type can_invite_collaborator: bool
        :param can_rename: Specifies if the user can rename this item.
        :type can_rename: bool
        :param can_set_share_access: Specifies if the user can change the access level of an
            existing shared link on this item.
        :type can_set_share_access: bool
        :param can_share: Specifies if the user can create a shared link for this item.
        :type can_share: bool
        :param can_upload: Specifies if the user can upload into this folder.
        :type can_upload: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.can_delete = can_delete
        self.can_download = can_download
        self.can_invite_collaborator = can_invite_collaborator
        self.can_rename = can_rename
        self.can_set_share_access = can_set_share_access
        self.can_share = can_share
        self.can_upload = can_upload


class FolderFullMetadataField(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.extra_data = kwargs


class FolderFullAllowedSharedLinkAccessLevelsField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'


class FolderFullAllowedInviteeRolesField(str, Enum):
    EDITOR = 'editor'
    VIEWER = 'viewer'
    PREVIEWER = 'previewer'
    UPLOADER = 'uploader'
    PREVIEWER_UPLOADER = 'previewer uploader'
    VIEWER_UPLOADER = 'viewer uploader'
    CO_OWNER = 'co-owner'


class FolderFullWatermarkInfoField(BaseObject):
    def __init__(self, is_watermarked: Optional[bool] = None, **kwargs):
        """
        :param is_watermarked: Specifies if this item has a watermark applied.
        :type is_watermarked: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.is_watermarked = is_watermarked


class FolderFullClassificationField(BaseObject):
    def __init__(
        self,
        name: Optional[str] = None,
        definition: Optional[str] = None,
        color: Optional[str] = None,
        **kwargs
    ):
        """
        :param name: The name of the classification
        :type name: Optional[str], optional
        :param definition: An explanation of the meaning of this classification.
        :type definition: Optional[str], optional
        :param color: The color that is used to display the
            classification label in a user-interface. Colors are defined by the admin
            or co-admin who created the classification in the Box web app.
        :type color: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.definition = definition
        self.color = color


class FolderFull(Folder):
    def __init__(
        self,
        id: str,
        type: FolderBaseTypeField,
        sync_state: Optional[FolderFullSyncStateField] = None,
        has_collaborations: Optional[bool] = None,
        permissions: Optional[FolderFullPermissionsField] = None,
        tags: Optional[List[str]] = None,
        can_non_owners_invite: Optional[bool] = None,
        is_externally_owned: Optional[bool] = None,
        metadata: Optional[FolderFullMetadataField] = None,
        is_collaboration_restricted_to_enterprise: Optional[bool] = None,
        allowed_shared_link_access_levels: Optional[
            List[FolderFullAllowedSharedLinkAccessLevelsField]
        ] = None,
        allowed_invitee_roles: Optional[
            List[FolderFullAllowedInviteeRolesField]
        ] = None,
        watermark_info: Optional[FolderFullWatermarkInfoField] = None,
        is_accessible_via_shared_link: Optional[bool] = None,
        can_non_owners_view_collaborators: Optional[bool] = None,
        classification: Optional[FolderFullClassificationField] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        description: Optional[str] = None,
        size: Optional[int] = None,
        path_collection: Optional[FolderPathCollectionField] = None,
        created_by: Optional[UserMini] = None,
        modified_by: Optional[UserMini] = None,
        trashed_at: Optional[str] = None,
        purged_at: Optional[str] = None,
        content_created_at: Optional[str] = None,
        content_modified_at: Optional[str] = None,
        owned_by: Optional[UserMini] = None,
        shared_link: Optional[FolderSharedLinkField] = None,
        folder_upload_email: Optional[FolderFolderUploadEmailField] = None,
        parent: Optional[FolderMini] = None,
        item_status: Optional[FolderItemStatusField] = None,
        item_collection: Optional[Items] = None,
        sequence_id: Optional[str] = None,
        name: Optional[str] = None,
        etag: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting a folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folders/123`
            the `folder_id` is `123`.
        :type id: str
        :param type: `folder`
        :type type: FolderBaseTypeField
        :param has_collaborations: Specifies if this folder has any other collaborators.
        :type has_collaborations: Optional[bool], optional
        :param is_externally_owned: Specifies if this folder is owned by a user outside of the
            authenticated enterprise.
        :type is_externally_owned: Optional[bool], optional
        :param allowed_shared_link_access_levels: A list of access levels that are available
            for this folder.
            For some folders, like the root folder, this will always
            be an empty list as sharing is not allowed at that level.
        :type allowed_shared_link_access_levels: Optional[List[FolderFullAllowedSharedLinkAccessLevelsField]], optional
        :param allowed_invitee_roles: A list of the types of roles that user can be invited at
            when sharing this folder.
        :type allowed_invitee_roles: Optional[List[FolderFullAllowedInviteeRolesField]], optional
        :param is_accessible_via_shared_link: Specifies if the folder can be accessed
            with the direct shared link or a shared link
            to a parent folder.
        :type is_accessible_via_shared_link: Optional[bool], optional
        :param can_non_owners_view_collaborators: Specifies if collaborators who are not owners
            of this folder are restricted from viewing other
            collaborations on this folder.
            It also restricts non-owners from inviting new
            collaborators.
        :type can_non_owners_view_collaborators: Optional[bool], optional
        :param created_at: The date and time when the folder was created. This value may
            be `null` for some folders such as the root folder or the trash
            folder.
        :type created_at: Optional[str], optional
        :param modified_at: The date and time when the folder was last updated. This value may
            be `null` for some folders such as the root folder or the trash
            folder.
        :type modified_at: Optional[str], optional
        :param size: The folder size in bytes.
            Be careful parsing this integer as its
            value can get very large.
        :type size: Optional[int], optional
        :param trashed_at: The time at which this folder was put in the trash.
        :type trashed_at: Optional[str], optional
        :param purged_at: The time at which this folder is expected to be purged
            from the trash.
        :type purged_at: Optional[str], optional
        :param content_created_at: The date and time at which this folder was originally
            created.
        :type content_created_at: Optional[str], optional
        :param content_modified_at: The date and time at which this folder was last updated.
        :type content_modified_at: Optional[str], optional
        :param item_status: Defines if this item has been deleted or not.
            * `active` when the item has is not in the trash
            * `trashed` when the item has been moved to the trash but not deleted
            * `deleted` when the item has been permanently deleted.
        :type item_status: Optional[FolderItemStatusField], optional
        :param name: The name of the folder.
        :type name: Optional[str], optional
        :param etag: The HTTP `etag` of this folder. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the folder if (no) changes have happened.
        :type etag: Optional[str], optional
        """
        super().__init__(
            id=id,
            type=type,
            created_at=created_at,
            modified_at=modified_at,
            description=description,
            size=size,
            path_collection=path_collection,
            created_by=created_by,
            modified_by=modified_by,
            trashed_at=trashed_at,
            purged_at=purged_at,
            content_created_at=content_created_at,
            content_modified_at=content_modified_at,
            owned_by=owned_by,
            shared_link=shared_link,
            folder_upload_email=folder_upload_email,
            parent=parent,
            item_status=item_status,
            item_collection=item_collection,
            sequence_id=sequence_id,
            name=name,
            etag=etag,
            **kwargs
        )
        self.sync_state = sync_state
        self.has_collaborations = has_collaborations
        self.permissions = permissions
        self.tags = tags
        self.can_non_owners_invite = can_non_owners_invite
        self.is_externally_owned = is_externally_owned
        self.metadata = metadata
        self.is_collaboration_restricted_to_enterprise = (
            is_collaboration_restricted_to_enterprise
        )
        self.allowed_shared_link_access_levels = allowed_shared_link_access_levels
        self.allowed_invitee_roles = allowed_invitee_roles
        self.watermark_info = watermark_info
        self.is_accessible_via_shared_link = is_accessible_via_shared_link
        self.can_non_owners_view_collaborators = can_non_owners_view_collaborators
        self.classification = classification


class EventEventTypeField(str, Enum):
    ACCESS_GRANTED = 'ACCESS_GRANTED'
    ACCESS_REVOKED = 'ACCESS_REVOKED'
    ADD_DEVICE_ASSOCIATION = 'ADD_DEVICE_ASSOCIATION'
    ADD_LOGIN_ACTIVITY_DEVICE = 'ADD_LOGIN_ACTIVITY_DEVICE'
    ADMIN_LOGIN = 'ADMIN_LOGIN'
    APPLICATION_CREATED = 'APPLICATION_CREATED'
    APPLICATION_PUBLIC_KEY_ADDED = 'APPLICATION_PUBLIC_KEY_ADDED'
    APPLICATION_PUBLIC_KEY_DELETED = 'APPLICATION_PUBLIC_KEY_DELETED'
    CHANGE_ADMIN_ROLE = 'CHANGE_ADMIN_ROLE'
    CHANGE_FOLDER_PERMISSION = 'CHANGE_FOLDER_PERMISSION'
    COLLABORATION_ACCEPT = 'COLLABORATION_ACCEPT'
    COLLABORATION_EXPIRATION = 'COLLABORATION_EXPIRATION'
    COLLABORATION_INVITE = 'COLLABORATION_INVITE'
    COLLABORATION_REMOVE = 'COLLABORATION_REMOVE'
    COLLABORATION_ROLE_CHANGE = 'COLLABORATION_ROLE_CHANGE'
    COLLAB_ADD_COLLABORATOR = 'COLLAB_ADD_COLLABORATOR'
    COLLAB_INVITE_COLLABORATOR = 'COLLAB_INVITE_COLLABORATOR'
    COLLAB_REMOVE_COLLABORATOR = 'COLLAB_REMOVE_COLLABORATOR'
    COLLAB_ROLE_CHANGE = 'COLLAB_ROLE_CHANGE'
    COMMENT_CREATE = 'COMMENT_CREATE'
    COMMENT_DELETE = 'COMMENT_DELETE'
    CONTENT_ACCESS = 'CONTENT_ACCESS'
    CONTENT_WORKFLOW_ABNORMAL_DOWNLOAD_ACTIVITY = (
        'CONTENT_WORKFLOW_ABNORMAL_DOWNLOAD_ACTIVITY'
    )
    CONTENT_WORKFLOW_AUTOMATION_ADD = 'CONTENT_WORKFLOW_AUTOMATION_ADD'
    CONTENT_WORKFLOW_AUTOMATION_DELETE = 'CONTENT_WORKFLOW_AUTOMATION_DELETE'
    CONTENT_WORKFLOW_POLICY_ADD = 'CONTENT_WORKFLOW_POLICY_ADD'
    CONTENT_WORKFLOW_SHARING_POLICY_VIOLATION = (
        'CONTENT_WORKFLOW_SHARING_POLICY_VIOLATION'
    )
    CONTENT_WORKFLOW_UPLOAD_POLICY_VIOLATION = (
        'CONTENT_WORKFLOW_UPLOAD_POLICY_VIOLATION'
    )
    COPY = 'COPY'
    DATA_RETENTION_CREATE_RETENTION = 'DATA_RETENTION_CREATE_RETENTION'
    DATA_RETENTION_REMOVE_RETENTION = 'DATA_RETENTION_REMOVE_RETENTION'
    DELETE = 'DELETE'
    DELETE_USER = 'DELETE_USER'
    DEVICE_TRUST_CHECK_FAILED = 'DEVICE_TRUST_CHECK_FAILED'
    DOWNLOAD = 'DOWNLOAD'
    EDIT = 'EDIT'
    EDIT_USER = 'EDIT_USER'
    EMAIL_ALIAS_CONFIRM = 'EMAIL_ALIAS_CONFIRM'
    EMAIL_ALIAS_REMOVE = 'EMAIL_ALIAS_REMOVE'
    ENABLE_TWO_FACTOR_AUTH = 'ENABLE_TWO_FACTOR_AUTH'
    ENTERPRISE_APP_AUTHORIZATION_UPDATE = 'ENTERPRISE_APP_AUTHORIZATION_UPDATE'
    FAILED_LOGIN = 'FAILED_LOGIN'
    FILE_MARKED_MALICIOUS = 'FILE_MARKED_MALICIOUS'
    FILE_WATERMARKED_DOWNLOAD = 'FILE_WATERMARKED_DOWNLOAD'
    GROUP_ADD_ITEM = 'GROUP_ADD_ITEM'
    GROUP_ADD_USER = 'GROUP_ADD_USER'
    GROUP_CREATION = 'GROUP_CREATION'
    GROUP_DELETION = 'GROUP_DELETION'
    GROUP_EDITED = 'GROUP_EDITED'
    GROUP_REMOVE_ITEM = 'GROUP_REMOVE_ITEM'
    GROUP_REMOVE_USER = 'GROUP_REMOVE_USER'
    ITEM_COPY = 'ITEM_COPY'
    ITEM_CREATE = 'ITEM_CREATE'
    ITEM_DOWNLOAD = 'ITEM_DOWNLOAD'
    ITEM_MAKE_CURRENT_VERSION = 'ITEM_MAKE_CURRENT_VERSION'
    ITEM_MODIFY = 'ITEM_MODIFY'
    ITEM_MOVE = 'ITEM_MOVE'
    ITEM_OPEN = 'ITEM_OPEN'
    ITEM_PREVIEW = 'ITEM_PREVIEW'
    ITEM_RENAME = 'ITEM_RENAME'
    ITEM_SHARED = 'ITEM_SHARED'
    ITEM_SHARED_CREATE = 'ITEM_SHARED_CREATE'
    ITEM_SHARED_UNSHARE = 'ITEM_SHARED_UNSHARE'
    ITEM_SHARED_UPDATE = 'ITEM_SHARED_UPDATE'
    ITEM_SYNC = 'ITEM_SYNC'
    ITEM_TRASH = 'ITEM_TRASH'
    ITEM_UNDELETE_VIA_TRASH = 'ITEM_UNDELETE_VIA_TRASH'
    ITEM_UNSYNC = 'ITEM_UNSYNC'
    ITEM_UPLOAD = 'ITEM_UPLOAD'
    LEGAL_HOLD_ASSIGNMENT_CREATE = 'LEGAL_HOLD_ASSIGNMENT_CREATE'
    LEGAL_HOLD_ASSIGNMENT_DELETE = 'LEGAL_HOLD_ASSIGNMENT_DELETE'
    LEGAL_HOLD_POLICY_CREATE = 'LEGAL_HOLD_POLICY_CREATE'
    LEGAL_HOLD_POLICY_DELETE = 'LEGAL_HOLD_POLICY_DELETE'
    LEGAL_HOLD_POLICY_UPDATE = 'LEGAL_HOLD_POLICY_UPDATE'
    LOCK = 'LOCK'
    LOCK_CREATE = 'LOCK_CREATE'
    LOCK_DESTROY = 'LOCK_DESTROY'
    LOGIN = 'LOGIN'
    MASTER_INVITE_ACCEPT = 'MASTER_INVITE_ACCEPT'
    MASTER_INVITE_REJECT = 'MASTER_INVITE_REJECT'
    METADATA_INSTANCE_CREATE = 'METADATA_INSTANCE_CREATE'
    METADATA_INSTANCE_DELETE = 'METADATA_INSTANCE_DELETE'
    METADATA_INSTANCE_UPDATE = 'METADATA_INSTANCE_UPDATE'
    METADATA_TEMPLATE_CREATE = 'METADATA_TEMPLATE_CREATE'
    METADATA_TEMPLATE_DELETE = 'METADATA_TEMPLATE_DELETE'
    METADATA_TEMPLATE_UPDATE = 'METADATA_TEMPLATE_UPDATE'
    MOVE = 'MOVE'
    NEW_USER = 'NEW_USER'
    PREVIEW = 'PREVIEW'
    REMOVE_DEVICE_ASSOCIATION = 'REMOVE_DEVICE_ASSOCIATION'
    REMOVE_LOGIN_ACTIVITY_DEVICE = 'REMOVE_LOGIN_ACTIVITY_DEVICE'
    RENAME = 'RENAME'
    RETENTION_POLICY_ASSIGNMENT_ADD = 'RETENTION_POLICY_ASSIGNMENT_ADD'
    SHARE = 'SHARE'
    SHARE_EXPIRATION = 'SHARE_EXPIRATION'
    SHIELD_ALERT = 'SHIELD_ALERT'
    SHIELD_EXTERNAL_COLLAB_ACCESS_BLOCKED = 'SHIELD_EXTERNAL_COLLAB_ACCESS_BLOCKED'
    SHIELD_EXTERNAL_COLLAB_ACCESS_BLOCKED_MISSING_JUSTIFICATION = (
        'SHIELD_EXTERNAL_COLLAB_ACCESS_BLOCKED_MISSING_JUSTIFICATION'
    )
    SHIELD_EXTERNAL_COLLAB_INVITE_BLOCKED = 'SHIELD_EXTERNAL_COLLAB_INVITE_BLOCKED'
    SHIELD_EXTERNAL_COLLAB_INVITE_BLOCKED_MISSING_JUSTIFICATION = (
        'SHIELD_EXTERNAL_COLLAB_INVITE_BLOCKED_MISSING_JUSTIFICATION'
    )
    SHIELD_JUSTIFICATION_APPROVAL = 'SHIELD_JUSTIFICATION_APPROVAL'
    SHIELD_SHARED_LINK_ACCESS_BLOCKED = 'SHIELD_SHARED_LINK_ACCESS_BLOCKED'
    SHIELD_SHARED_LINK_STATUS_RESTRICTED_ON_CREATE = (
        'SHIELD_SHARED_LINK_STATUS_RESTRICTED_ON_CREATE'
    )
    SHIELD_SHARED_LINK_STATUS_RESTRICTED_ON_UPDATE = (
        'SHIELD_SHARED_LINK_STATUS_RESTRICTED_ON_UPDATE'
    )
    SIGN_DOCUMENT_ASSIGNED = 'SIGN_DOCUMENT_ASSIGNED'
    SIGN_DOCUMENT_CANCELLED = 'SIGN_DOCUMENT_CANCELLED'
    SIGN_DOCUMENT_COMPLETED = 'SIGN_DOCUMENT_COMPLETED'
    SIGN_DOCUMENT_CONVERTED = 'SIGN_DOCUMENT_CONVERTED'
    SIGN_DOCUMENT_CREATED = 'SIGN_DOCUMENT_CREATED'
    SIGN_DOCUMENT_DECLINED = 'SIGN_DOCUMENT_DECLINED'
    SIGN_DOCUMENT_EXPIRED = 'SIGN_DOCUMENT_EXPIRED'
    SIGN_DOCUMENT_SIGNED = 'SIGN_DOCUMENT_SIGNED'
    SIGN_DOCUMENT_VIEWED_BY_SIGNED = 'SIGN_DOCUMENT_VIEWED_BY_SIGNED'
    SIGNER_DOWNLOADED = 'SIGNER_DOWNLOADED'
    SIGNER_FORWARDED = 'SIGNER_FORWARDED'
    STORAGE_EXPIRATION = 'STORAGE_EXPIRATION'
    TAG_ITEM_CREATE = 'TAG_ITEM_CREATE'
    TASK_ASSIGNMENT_CREATE = 'TASK_ASSIGNMENT_CREATE'
    TASK_ASSIGNMENT_DELETE = 'TASK_ASSIGNMENT_DELETE'
    TASK_ASSIGNMENT_UPDATE = 'TASK_ASSIGNMENT_UPDATE'
    TASK_CREATE = 'TASK_CREATE'
    TASK_UPDATE = 'TASK_UPDATE'
    TERMS_OF_SERVICE_ACCEPT = 'TERMS_OF_SERVICE_ACCEPT'
    TERMS_OF_SERVICE_REJECT = 'TERMS_OF_SERVICE_REJECT'
    UNDELETE = 'UNDELETE'
    UNLOCK = 'UNLOCK'
    UNSHARE = 'UNSHARE'
    UPDATE_COLLABORATION_EXPIRATION = 'UPDATE_COLLABORATION_EXPIRATION'
    UPDATE_SHARE_EXPIRATION = 'UPDATE_SHARE_EXPIRATION'
    UPLOAD = 'UPLOAD'
    USER_AUTHENTICATE_OAUTH2_ACCESS_TOKEN_CREATE = (
        'USER_AUTHENTICATE_OAUTH2_ACCESS_TOKEN_CREATE'
    )
    WATERMARK_LABEL_CREATE = 'WATERMARK_LABEL_CREATE'
    WATERMARK_LABEL_DELETE = 'WATERMARK_LABEL_DELETE'


class EventAdditionalDetailsField(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Event(BaseObject):
    def __init__(
        self,
        type: Optional[str] = None,
        created_at: Optional[str] = None,
        recorded_at: Optional[str] = None,
        event_id: Optional[str] = None,
        created_by: Optional[UserMini] = None,
        event_type: Optional[EventEventTypeField] = None,
        session_id: Optional[str] = None,
        source: Optional[Union[User, EventSource, File, Folder]] = None,
        additional_details: Optional[EventAdditionalDetailsField] = None,
        **kwargs
    ):
        """
        :param type: `event`
        :type type: Optional[str], optional
        :param created_at: When the event object was created
        :type created_at: Optional[str], optional
        :param recorded_at: When the event object was recorded in database
        :type recorded_at: Optional[str], optional
        :param event_id: The ID of the event object. You can use this to detect duplicate events
        :type event_id: Optional[str], optional
        :param session_id: The session of the user that performed the action. Not all events will
            populate this attribute.
        :type session_id: Optional[str], optional
        :param additional_details: This object provides additional information about the event if available.
            This can include how a user performed an event as well as additional
            information to correlate an event to external KeySafe logs. Not all events
            have an `additional_details` object.  This object is only available in the
            Enterprise Events.
        :type additional_details: Optional[EventAdditionalDetailsField], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.created_at = created_at
        self.recorded_at = recorded_at
        self.event_id = event_id
        self.created_by = created_by
        self.event_type = event_type
        self.session_id = session_id
        self.source = source
        self.additional_details = additional_details


class Events(BaseObject):
    def __init__(
        self,
        chunk_size: Optional[int] = None,
        next_stream_position: Optional[str] = None,
        entries: Optional[List[Event]] = None,
        **kwargs
    ):
        """
        :param chunk_size: The number of events returned in this response.
        :type chunk_size: Optional[int], optional
        :param next_stream_position: The stream position of the start of the next page (chunk)
            of events.
        :type next_stream_position: Optional[str], optional
        :param entries: A list of events
        :type entries: Optional[List[Event]], optional
        """
        super().__init__(**kwargs)
        self.chunk_size = chunk_size
        self.next_stream_position = next_stream_position
        self.entries = entries


class SkillInvocationTypeField(str, Enum):
    SKILL_INVOCATION = 'skill_invocation'


class SkillInvocationSkillFieldTypeField(str, Enum):
    SKILL = 'skill'


class SkillInvocationSkillField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[SkillInvocationSkillFieldTypeField] = None,
        name: Optional[str] = None,
        api_key: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this skill
        :type id: Optional[str], optional
        :param type: `skill`
        :type type: Optional[SkillInvocationSkillFieldTypeField], optional
        :param name: The name of the skill
        :type name: Optional[str], optional
        :param api_key: The client ID of the application
        :type api_key: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name
        self.api_key = api_key


class SkillInvocationTokenFieldReadFieldTokenTypeField(str, Enum):
    BEARER = 'bearer'


class SkillInvocationTokenFieldReadField(BaseObject):
    def __init__(
        self,
        access_token: Optional[str] = None,
        expires_in: Optional[int] = None,
        token_type: Optional[SkillInvocationTokenFieldReadFieldTokenTypeField] = None,
        restricted_to: Optional[str] = None,
        **kwargs
    ):
        """
        :param access_token: The requested access token.
        :type access_token: Optional[str], optional
        :param expires_in: The time in seconds by which this token will expire.
        :type expires_in: Optional[int], optional
        :param token_type: The type of access token returned.
        :type token_type: Optional[SkillInvocationTokenFieldReadFieldTokenTypeField], optional
        :param restricted_to: The permissions that this access token permits,
            providing a list of resources (files, folders, etc)
            and the scopes permitted for each of those resources.
        :type restricted_to: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.restricted_to = restricted_to


class SkillInvocationTokenFieldWriteFieldTokenTypeField(str, Enum):
    BEARER = 'bearer'


class SkillInvocationTokenFieldWriteField(BaseObject):
    def __init__(
        self,
        access_token: Optional[str] = None,
        expires_in: Optional[int] = None,
        token_type: Optional[SkillInvocationTokenFieldWriteFieldTokenTypeField] = None,
        restricted_to: Optional[str] = None,
        **kwargs
    ):
        """
        :param access_token: The requested access token.
        :type access_token: Optional[str], optional
        :param expires_in: The time in seconds by which this token will expire.
        :type expires_in: Optional[int], optional
        :param token_type: The type of access token returned.
        :type token_type: Optional[SkillInvocationTokenFieldWriteFieldTokenTypeField], optional
        :param restricted_to: The permissions that this access token permits,
            providing a list of resources (files, folders, etc)
            and the scopes permitted for each of those resources.
        :type restricted_to: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.restricted_to = restricted_to


class SkillInvocationTokenField(BaseObject):
    def __init__(
        self,
        read: Optional[SkillInvocationTokenFieldReadField] = None,
        write: Optional[SkillInvocationTokenFieldWriteField] = None,
        **kwargs
    ):
        """
        :param read: The basics of an access token
        :type read: Optional[SkillInvocationTokenFieldReadField], optional
        :param write: The basics of an access token
        :type write: Optional[SkillInvocationTokenFieldWriteField], optional
        """
        super().__init__(**kwargs)
        self.read = read
        self.write = write


class SkillInvocationStatusFieldStateField(str, Enum):
    INVOKED = 'invoked'
    PROCESSING = 'processing'
    SUCCESS = 'success'
    TRANSIENT_FAILURE = 'transient_failure'
    PERMANENT_FAILURE = 'permanent_failure'


class SkillInvocationStatusField(BaseObject):
    def __init__(
        self,
        state: Optional[SkillInvocationStatusFieldStateField] = None,
        message: Optional[str] = None,
        error_code: Optional[str] = None,
        additional_info: Optional[str] = None,
        **kwargs
    ):
        """
        :param state: The state of this event.
            * `invoked` - Triggered the skill with event details to start
              applying skill on the file.
            * `processing` - Currently processing.
            * `success` - Completed processing with a success.
            * `transient_failure` - Encountered an issue which can be
              retried.
            * `permanent_failure` -  Encountered a permanent issue and
              retry would not help.
        :type state: Optional[SkillInvocationStatusFieldStateField], optional
        :param message: Status information
        :type message: Optional[str], optional
        :param error_code: Error code information, if error occurred.
        :type error_code: Optional[str], optional
        :param additional_info: Additional status information.
        :type additional_info: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.state = state
        self.message = message
        self.error_code = error_code
        self.additional_info = additional_info


class SkillInvocationEnterpriseFieldTypeField(str, Enum):
    ENTERPRISE = 'enterprise'


class SkillInvocationEnterpriseField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[SkillInvocationEnterpriseFieldTypeField] = None,
        name: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this enterprise.
        :type id: Optional[str], optional
        :param type: `enterprise`
        :type type: Optional[SkillInvocationEnterpriseFieldTypeField], optional
        :param name: The name of the enterprise
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name


class SkillInvocation(BaseObject):
    def __init__(
        self,
        type: Optional[SkillInvocationTypeField] = None,
        id: Optional[str] = None,
        skill: Optional[SkillInvocationSkillField] = None,
        token: Optional[SkillInvocationTokenField] = None,
        status: Optional[SkillInvocationStatusField] = None,
        created_at: Optional[str] = None,
        trigger: Optional[str] = None,
        enterprise: Optional[SkillInvocationEnterpriseField] = None,
        source: Optional[Union[File, Folder]] = None,
        event: Optional[Event] = None,
        **kwargs
    ):
        """
        :param type: `skill_invocation`
        :type type: Optional[SkillInvocationTypeField], optional
        :param id: Unique identifier for the invocation request.
        :type id: Optional[str], optional
        :param token: The read-only and read-write access tokens for this item
        :type token: Optional[SkillInvocationTokenField], optional
        :param status: The details status of this event.
        :type status: Optional[SkillInvocationStatusField], optional
        :param created_at: The time this invocation was created.
        :type created_at: Optional[str], optional
        :param trigger: Action that triggered the invocation
        :type trigger: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id
        self.skill = skill
        self.token = token
        self.status = status
        self.created_at = created_at
        self.trigger = trigger
        self.enterprise = enterprise
        self.source = source
        self.event = event


class CollaborationTypeField(str, Enum):
    COLLABORATION = 'collaboration'


class CollaborationRoleField(str, Enum):
    EDITOR = 'editor'
    VIEWER = 'viewer'
    PREVIEWER = 'previewer'
    UPLOADER = 'uploader'
    PREVIEWER_UPLOADER = 'previewer uploader'
    VIEWER_UPLOADER = 'viewer uploader'
    CO_OWNER = 'co-owner'
    OWNER = 'owner'


class CollaborationStatusField(str, Enum):
    ACCEPTED = 'accepted'
    PENDING = 'pending'
    REJECTED = 'rejected'


class CollaborationAcceptanceRequirementsStatusFieldTermsOfServiceRequirementField(
    BaseObject
):
    def __init__(
        self,
        is_accepted: Optional[bool] = None,
        terms_of_service: Optional[TermsOfServiceBase] = None,
        **kwargs
    ):
        """
        :param is_accepted: Whether or not the terms of service have been accepted.  The
            field is `null` when there is no terms of service required.
        :type is_accepted: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.is_accepted = is_accepted
        self.terms_of_service = terms_of_service


class CollaborationAcceptanceRequirementsStatusFieldStrongPasswordRequirementField(
    BaseObject
):
    def __init__(
        self,
        enterprise_has_strong_password_required_for_external_users: Optional[
            bool
        ] = None,
        user_has_strong_password: Optional[bool] = None,
        **kwargs
    ):
        """
        :param enterprise_has_strong_password_required_for_external_users: Whether or not the enterprise that owns the content requires
            a strong password to collaborate on the content.
        :type enterprise_has_strong_password_required_for_external_users: Optional[bool], optional
        :param user_has_strong_password: Whether or not the user has a strong password set for their
            account. The field is `null` when a strong password is not
            required.
        :type user_has_strong_password: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.enterprise_has_strong_password_required_for_external_users = (
            enterprise_has_strong_password_required_for_external_users
        )
        self.user_has_strong_password = user_has_strong_password


class CollaborationAcceptanceRequirementsStatusFieldTwoFactorAuthenticationRequirementField(
    BaseObject
):
    def __init__(
        self,
        enterprise_has_two_factor_auth_enabled: Optional[bool] = None,
        user_has_two_factor_authentication_enabled: Optional[bool] = None,
        **kwargs
    ):
        """
        :param enterprise_has_two_factor_auth_enabled: Whether or not the enterprise that owns the content requires
            two-factor authentication to be enabled in order to
            collaborate on the content.
        :type enterprise_has_two_factor_auth_enabled: Optional[bool], optional
        :param user_has_two_factor_authentication_enabled: Whether or not the user has two-factor authentication
            enabled. The field is `null` when two-factor
            authentication is not required.
        :type user_has_two_factor_authentication_enabled: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.enterprise_has_two_factor_auth_enabled = (
            enterprise_has_two_factor_auth_enabled
        )
        self.user_has_two_factor_authentication_enabled = (
            user_has_two_factor_authentication_enabled
        )


class CollaborationAcceptanceRequirementsStatusField(BaseObject):
    def __init__(
        self,
        terms_of_service_requirement: Optional[
            CollaborationAcceptanceRequirementsStatusFieldTermsOfServiceRequirementField
        ] = None,
        strong_password_requirement: Optional[
            CollaborationAcceptanceRequirementsStatusFieldStrongPasswordRequirementField
        ] = None,
        two_factor_authentication_requirement: Optional[
            CollaborationAcceptanceRequirementsStatusFieldTwoFactorAuthenticationRequirementField
        ] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.terms_of_service_requirement = terms_of_service_requirement
        self.strong_password_requirement = strong_password_requirement
        self.two_factor_authentication_requirement = (
            two_factor_authentication_requirement
        )


class Collaboration(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[CollaborationTypeField] = None,
        item: Optional[Union[File, Folder, WebLink]] = None,
        accessible_by: Optional[Union[UserCollaborations, GroupMini]] = None,
        invite_email: Optional[str] = None,
        role: Optional[CollaborationRoleField] = None,
        expires_at: Optional[str] = None,
        is_access_only: Optional[bool] = None,
        status: Optional[CollaborationStatusField] = None,
        acknowledged_at: Optional[str] = None,
        created_by: Optional[UserCollaborations] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        acceptance_requirements_status: Optional[
            CollaborationAcceptanceRequirementsStatusField
        ] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this collaboration.
        :type id: Optional[str], optional
        :param type: `collaboration`
        :type type: Optional[CollaborationTypeField], optional
        :param invite_email: The email address used to invite an unregistered collaborator, if
            they are not a registered user.
        :type invite_email: Optional[str], optional
        :param role: The level of access granted.
        :type role: Optional[CollaborationRoleField], optional
        :param expires_at: When the collaboration will expire, or `null` if no expiration
            date is set.
        :type expires_at: Optional[str], optional
        :param is_access_only: If set to `true`, collaborators have access to
            shared items, but such items won't be visible in the
            All Files list. Additionally, collaborators won't
            see the the path to the root folder for the
            shared item.
        :type is_access_only: Optional[bool], optional
        :param status: The status of the collaboration invitation. If the status
            is `pending`, `login` and `name` return an empty string.
        :type status: Optional[CollaborationStatusField], optional
        :param acknowledged_at: When the `status` of the collaboration object changed to
            `accepted` or `rejected`.
        :type acknowledged_at: Optional[str], optional
        :param created_at: When the collaboration object was created.
        :type created_at: Optional[str], optional
        :param modified_at: When the collaboration object was last modified.
        :type modified_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.item = item
        self.accessible_by = accessible_by
        self.invite_email = invite_email
        self.role = role
        self.expires_at = expires_at
        self.is_access_only = is_access_only
        self.status = status
        self.acknowledged_at = acknowledged_at
        self.created_by = created_by
        self.created_at = created_at
        self.modified_at = modified_at
        self.acceptance_requirements_status = acceptance_requirements_status


class CollaborationsOrderFieldDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class CollaborationsOrderField(BaseObject):
    def __init__(
        self,
        by: Optional[str] = None,
        direction: Optional[CollaborationsOrderFieldDirectionField] = None,
        **kwargs
    ):
        """
        :param by: The field to order by
        :type by: Optional[str], optional
        :param direction: The direction to order by, either ascending or descending
        :type direction: Optional[CollaborationsOrderFieldDirectionField], optional
        """
        super().__init__(**kwargs)
        self.by = by
        self.direction = direction


class Collaborations(BaseObject):
    def __init__(
        self,
        total_count: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[List[CollaborationsOrderField]] = None,
        entries: Optional[List[Collaboration]] = None,
        **kwargs
    ):
        """
        :param total_count: One greater than the offset of the last entry in the entire collection.
            The total number of entries in the collection may be less than
            `total_count`.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type total_count: Optional[int], optional
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param offset: The 0-based offset of the first entry in this set. This will be the same
            as the `offset` query parameter.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type offset: Optional[int], optional
        :param order: The order by which items are returned.
            This field is only returned for calls that use offset-based pagination.
            For marker-based paginated APIs, this field will be omitted.
        :type order: Optional[List[CollaborationsOrderField]], optional
        :param entries: A list of collaborations
        :type entries: Optional[List[Collaboration]], optional
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.limit = limit
        self.offset = offset
        self.order = order
        self.entries = entries


class WebhookInvocationTypeField(str, Enum):
    WEBHOOK_EVENT = 'webhook_event'


class WebhookInvocationTriggerField(str, Enum):
    FILE_UPLOADED = 'FILE.UPLOADED'
    FILE_PREVIEWED = 'FILE.PREVIEWED'
    FILE_DOWNLOADED = 'FILE.DOWNLOADED'
    FILE_TRASHED = 'FILE.TRASHED'
    FILE_DELETED = 'FILE.DELETED'
    FILE_RESTORED = 'FILE.RESTORED'
    FILE_COPIED = 'FILE.COPIED'
    FILE_MOVED = 'FILE.MOVED'
    FILE_LOCKED = 'FILE.LOCKED'
    FILE_UNLOCKED = 'FILE.UNLOCKED'
    FILE_RENAMED = 'FILE.RENAMED'
    COMMENT_CREATED = 'COMMENT.CREATED'
    COMMENT_UPDATED = 'COMMENT.UPDATED'
    COMMENT_DELETED = 'COMMENT.DELETED'
    TASK_ASSIGNMENT_CREATED = 'TASK_ASSIGNMENT.CREATED'
    TASK_ASSIGNMENT_UPDATED = 'TASK_ASSIGNMENT.UPDATED'
    METADATA_INSTANCE_CREATED = 'METADATA_INSTANCE.CREATED'
    METADATA_INSTANCE_UPDATED = 'METADATA_INSTANCE.UPDATED'
    METADATA_INSTANCE_DELETED = 'METADATA_INSTANCE.DELETED'
    FOLDER_CREATED = 'FOLDER.CREATED'
    FOLDER_RENAMED = 'FOLDER.RENAMED'
    FOLDER_DOWNLOADED = 'FOLDER.DOWNLOADED'
    FOLDER_RESTORED = 'FOLDER.RESTORED'
    FOLDER_DELETED = 'FOLDER.DELETED'
    FOLDER_COPIED = 'FOLDER.COPIED'
    FOLDER_MOVED = 'FOLDER.MOVED'
    FOLDER_TRASHED = 'FOLDER.TRASHED'
    WEBHOOK_DELETED = 'WEBHOOK.DELETED'
    COLLABORATION_CREATED = 'COLLABORATION.CREATED'
    COLLABORATION_ACCEPTED = 'COLLABORATION.ACCEPTED'
    COLLABORATION_REJECTED = 'COLLABORATION.REJECTED'
    COLLABORATION_REMOVED = 'COLLABORATION.REMOVED'
    COLLABORATION_UPDATED = 'COLLABORATION.UPDATED'
    SHARED_LINK_DELETED = 'SHARED_LINK.DELETED'
    SHARED_LINK_CREATED = 'SHARED_LINK.CREATED'
    SHARED_LINK_UPDATED = 'SHARED_LINK.UPDATED'
    SIGN_REQUEST_COMPLETED = 'SIGN_REQUEST.COMPLETED'
    SIGN_REQUEST_DECLINED = 'SIGN_REQUEST.DECLINED'
    SIGN_REQUEST_EXPIRED = 'SIGN_REQUEST.EXPIRED'
    SIGN_REQUEST_SIGNER_EMAIL_BOUNCED = 'SIGN_REQUEST.SIGNER_EMAIL_BOUNCED'


class WebhookInvocation(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[WebhookInvocationTypeField] = None,
        webhook: Optional[Webhook] = None,
        created_by: Optional[UserMini] = None,
        created_at: Optional[str] = None,
        trigger: Optional[WebhookInvocationTriggerField] = None,
        source: Optional[Union[File, Folder]] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this webhook invocation
        :type id: Optional[str], optional
        :param type: `webhook_event`
        :type type: Optional[WebhookInvocationTypeField], optional
        :param created_at: A timestamp identifying the time that
            the webhook event was triggered.
        :type created_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.webhook = webhook
        self.created_by = created_by
        self.created_at = created_at
        self.trigger = trigger
        self.source = source


class WorkflowMiniTypeField(str, Enum):
    WORKFLOW = 'workflow'


class WorkflowMini(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[WorkflowMiniTypeField] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        is_enabled: Optional[bool] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for the workflow
        :type id: Optional[str], optional
        :param type: `workflow`
        :type type: Optional[WorkflowMiniTypeField], optional
        :param name: The name of the workflow
        :type name: Optional[str], optional
        :param description: The description for a workflow.
        :type description: Optional[str], optional
        :param is_enabled: Specifies if this workflow is enabled
        :type is_enabled: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name
        self.description = description
        self.is_enabled = is_enabled


class WorkflowFlowsFieldTypeField(str, Enum):
    FLOW = 'flow'


class WorkflowFlowsFieldTriggerFieldTypeField(str, Enum):
    TRIGGER = 'trigger'


class WorkflowFlowsFieldTriggerFieldTriggerTypeField(str, Enum):
    WORKFLOW_MANUAL_START = 'WORKFLOW_MANUAL_START'


class WorkflowFlowsFieldTriggerFieldScopeFieldTypeField(str, Enum):
    TRIGGER_SCOPE = 'trigger_scope'


class WorkflowFlowsFieldTriggerFieldScopeFieldObjectFieldTypeField(str, Enum):
    FOLDER = 'folder'


class WorkflowFlowsFieldTriggerFieldScopeFieldObjectField(BaseObject):
    def __init__(
        self,
        type: Optional[
            WorkflowFlowsFieldTriggerFieldScopeFieldObjectFieldTypeField
        ] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: The type of the object
        :type type: Optional[WorkflowFlowsFieldTriggerFieldScopeFieldObjectFieldTypeField], optional
        :param id: The id of the object
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class WorkflowFlowsFieldTriggerFieldScopeField(BaseObject):
    def __init__(
        self,
        type: Optional[WorkflowFlowsFieldTriggerFieldScopeFieldTypeField] = None,
        ref: Optional[str] = None,
        object: Optional[WorkflowFlowsFieldTriggerFieldScopeFieldObjectField] = None,
        **kwargs
    ):
        """
        :param type: The trigger scope's resource type
        :type type: Optional[WorkflowFlowsFieldTriggerFieldScopeFieldTypeField], optional
        :param ref: Indicates the path of the condition value to check
        :type ref: Optional[str], optional
        :param object: The object the `ref` points to
        :type object: Optional[WorkflowFlowsFieldTriggerFieldScopeFieldObjectField], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.ref = ref
        self.object = object


class WorkflowFlowsFieldTriggerField(BaseObject):
    def __init__(
        self,
        type: Optional[WorkflowFlowsFieldTriggerFieldTypeField] = None,
        trigger_type: Optional[WorkflowFlowsFieldTriggerFieldTriggerTypeField] = None,
        scope: Optional[List[WorkflowFlowsFieldTriggerFieldScopeField]] = None,
        **kwargs
    ):
        """
        :param type: The trigger's resource type
        :type type: Optional[WorkflowFlowsFieldTriggerFieldTypeField], optional
        :param trigger_type: The type of trigger selected for this flow
        :type trigger_type: Optional[WorkflowFlowsFieldTriggerFieldTriggerTypeField], optional
        :param scope: List of trigger scopes
        :type scope: Optional[List[WorkflowFlowsFieldTriggerFieldScopeField]], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.trigger_type = trigger_type
        self.scope = scope


class WorkflowFlowsFieldOutcomesFieldTypeField(str, Enum):
    OUTCOME = 'outcome'


class WorkflowFlowsFieldOutcomesFieldActionTypeField(str, Enum):
    ADD_METADATA = 'add_metadata'
    ASSIGN_TASK = 'assign_task'
    COPY_FILE = 'copy_file'
    COPY_FOLDER = 'copy_folder'
    CREATE_FOLDER = 'create_folder'
    DELETE_FILE = 'delete_file'
    DELETE_FOLDER = 'delete_folder'
    LOCK_FILE = 'lock_file'
    MOVE_FILE = 'move_file'
    MOVE_FOLDER = 'move_folder'
    REMOVE_WATERMARK_FILE = 'remove_watermark_file'
    RENAME_FOLDER = 'rename_folder'
    RESTORE_FOLDER = 'restore_folder'
    SHARE_FILE = 'share_file'
    SHARE_FOLDER = 'share_folder'
    UNLOCK_FILE = 'unlock_file'
    UPLOAD_FILE = 'upload_file'
    WAIT_FOR_TASK = 'wait_for_task'
    WATERMARK_FILE = 'watermark_file'
    GO_BACK_TO_STEP = 'go_back_to_step'
    APPLY_FILE_CLASSIFICATION = 'apply_file_classification'
    APPLY_FOLDER_CLASSIFICATION = 'apply_folder_classification'
    SEND_NOTIFICATION = 'send_notification'


class WorkflowFlowsFieldOutcomesFieldIfRejectedFieldTypeField(str, Enum):
    OUTCOME = 'outcome'


class WorkflowFlowsFieldOutcomesFieldIfRejectedFieldActionTypeField(str, Enum):
    ADD_METADATA = 'add_metadata'
    ASSIGN_TASK = 'assign_task'
    COPY_FILE = 'copy_file'
    COPY_FOLDER = 'copy_folder'
    CREATE_FOLDER = 'create_folder'
    DELETE_FILE = 'delete_file'
    DELETE_FOLDER = 'delete_folder'
    LOCK_FILE = 'lock_file'
    MOVE_FILE = 'move_file'
    MOVE_FOLDER = 'move_folder'
    REMOVE_WATERMARK_FILE = 'remove_watermark_file'
    RENAME_FOLDER = 'rename_folder'
    RESTORE_FOLDER = 'restore_folder'
    SHARE_FILE = 'share_file'
    SHARE_FOLDER = 'share_folder'
    UNLOCK_FILE = 'unlock_file'
    UPLOAD_FILE = 'upload_file'
    WAIT_FOR_TASK = 'wait_for_task'
    WATERMARK_FILE = 'watermark_file'
    GO_BACK_TO_STEP = 'go_back_to_step'
    APPLY_FILE_CLASSIFICATION = 'apply_file_classification'
    APPLY_FOLDER_CLASSIFICATION = 'apply_folder_classification'
    SEND_NOTIFICATION = 'send_notification'


class WorkflowFlowsFieldOutcomesFieldIfRejectedField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[WorkflowFlowsFieldOutcomesFieldIfRejectedFieldTypeField] = None,
        name: Optional[str] = None,
        action_type: Optional[
            WorkflowFlowsFieldOutcomesFieldIfRejectedFieldActionTypeField
        ] = None,
        **kwargs
    ):
        """
        :param id: The identifier of the outcome
        :type id: Optional[str], optional
        :param type: The outcomes resource type
        :type type: Optional[WorkflowFlowsFieldOutcomesFieldIfRejectedFieldTypeField], optional
        :param name: The name of the outcome
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name
        self.action_type = action_type


class WorkflowFlowsFieldOutcomesField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[WorkflowFlowsFieldOutcomesFieldTypeField] = None,
        name: Optional[str] = None,
        action_type: Optional[WorkflowFlowsFieldOutcomesFieldActionTypeField] = None,
        if_rejected: Optional[
            List[WorkflowFlowsFieldOutcomesFieldIfRejectedField]
        ] = None,
        **kwargs
    ):
        """
        :param id: The identifier of the outcome
        :type id: Optional[str], optional
        :param type: The outcomes resource type
        :type type: Optional[WorkflowFlowsFieldOutcomesFieldTypeField], optional
        :param name: The name of the outcome
        :type name: Optional[str], optional
        :param if_rejected: If `action_type` is `assign_task` and the task is rejected, returns a
            list of outcomes to complete
        :type if_rejected: Optional[List[WorkflowFlowsFieldOutcomesFieldIfRejectedField]], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name
        self.action_type = action_type
        self.if_rejected = if_rejected


class WorkflowFlowsField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[WorkflowFlowsFieldTypeField] = None,
        trigger: Optional[WorkflowFlowsFieldTriggerField] = None,
        outcomes: Optional[List[WorkflowFlowsFieldOutcomesField]] = None,
        created_at: Optional[str] = None,
        created_by: Optional[UserBase] = None,
        **kwargs
    ):
        """
        :param id: The identifier of the flow
        :type id: Optional[str], optional
        :param type: The flow's resource type
        :type type: Optional[WorkflowFlowsFieldTypeField], optional
        :param created_at: When this flow was created
        :type created_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.trigger = trigger
        self.outcomes = outcomes
        self.created_at = created_at
        self.created_by = created_by


class Workflow(WorkflowMini):
    def __init__(
        self,
        flows: Optional[List[WorkflowFlowsField]] = None,
        id: Optional[str] = None,
        type: Optional[WorkflowMiniTypeField] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        is_enabled: Optional[bool] = None,
        **kwargs
    ):
        """
        :param flows: A list of flows assigned to a workflow.
        :type flows: Optional[List[WorkflowFlowsField]], optional
        :param id: The unique identifier for the workflow
        :type id: Optional[str], optional
        :param type: `workflow`
        :type type: Optional[WorkflowMiniTypeField], optional
        :param name: The name of the workflow
        :type name: Optional[str], optional
        :param description: The description for a workflow.
        :type description: Optional[str], optional
        :param is_enabled: Specifies if this workflow is enabled
        :type is_enabled: Optional[bool], optional
        """
        super().__init__(
            id=id,
            type=type,
            name=name,
            description=description,
            is_enabled=is_enabled,
            **kwargs
        )
        self.flows = flows


class Workflows(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[int] = None,
        prev_marker: Optional[int] = None,
        entries: Optional[List[Workflow]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[int], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[int], optional
        :param entries: A list of workflows
        :type entries: Optional[List[Workflow]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class WorkflowFull(Workflow):
    def __init__(
        self,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        created_by: Optional[UserBase] = None,
        modified_by: Optional[UserBase] = None,
        flows: Optional[List[WorkflowFlowsField]] = None,
        id: Optional[str] = None,
        type: Optional[WorkflowMiniTypeField] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        is_enabled: Optional[bool] = None,
        **kwargs
    ):
        """
        :param created_at: The date and time when the workflow was created on Box
        :type created_at: Optional[str], optional
        :param modified_at: The date and time when the workflow was last updated on Box
        :type modified_at: Optional[str], optional
        :param flows: A list of flows assigned to a workflow.
        :type flows: Optional[List[WorkflowFlowsField]], optional
        :param id: The unique identifier for the workflow
        :type id: Optional[str], optional
        :param type: `workflow`
        :type type: Optional[WorkflowMiniTypeField], optional
        :param name: The name of the workflow
        :type name: Optional[str], optional
        :param description: The description for a workflow.
        :type description: Optional[str], optional
        :param is_enabled: Specifies if this workflow is enabled
        :type is_enabled: Optional[bool], optional
        """
        super().__init__(
            flows=flows,
            id=id,
            type=type,
            name=name,
            description=description,
            is_enabled=is_enabled,
            **kwargs
        )
        self.created_at = created_at
        self.modified_at = modified_at
        self.created_by = created_by
        self.modified_by = modified_by


class ZipDownloadNameConflictsFieldTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'


class ZipDownloadNameConflictsField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[ZipDownloadNameConflictsFieldTypeField] = None,
        original_name: Optional[str] = None,
        download_name: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The identifier of the item
        :type id: Optional[str], optional
        :param type: The type of this item
        :type type: Optional[ZipDownloadNameConflictsFieldTypeField], optional
        :param original_name: The original name of this item
        :type original_name: Optional[str], optional
        :param download_name: The new name of this item as it will appear in the
            downloaded `zip` archive.
        :type download_name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.original_name = original_name
        self.download_name = download_name


class ZipDownload(BaseObject):
    def __init__(
        self,
        download_url: Optional[str] = None,
        status_url: Optional[str] = None,
        expires_at: Optional[str] = None,
        name_conflicts: Optional[List[List[ZipDownloadNameConflictsField]]] = None,
        **kwargs
    ):
        """
        :param download_url: The URL that can be used to download the `zip` archive. A `Get` request to
            this URL will start streaming the items requested. By default, this URL
            is only valid for a few seconds, until the `expires_at` time, unless a
            download is started after which it is valid for the duration of the
            download.
            It is important to note that the domain and path of this URL might change
            between API calls, and therefore it's important to use this URL as-is.
        :type download_url: Optional[str], optional
        :param status_url: The URL that can be used to get the status of the `zip` archive being
            downloaded. A `Get` request to this URL will return the number of files
            in the archive as well as the number of items already downloaded or
            skipped. By default, this URL is only valid for a few seconds, until the
            `expires_at` time, unless a download is started after which the URL is
            valid for 12 hours from the start of the download.
            It is important to note that the domain and path of this URL might change
            between API calls, and therefore it's important to use this URL as-is.
        :type status_url: Optional[str], optional
        :param expires_at: The time and date when this archive will expire. After this time the
            `status_url` and `download_url` will return an error.
            By default, these URLs are only valid for a few seconds, unless a download
            is started after which the `download_url` is valid for the duration of the
            download, and the `status_url` is valid for 12 hours from the start of the
            download.
        :type expires_at: Optional[str], optional
        :param name_conflicts: A list of conflicts that occurred when trying to create the archive. This
            would occur when multiple items have been requested with the
            same name.
            To solve these conflicts, the API will automatically rename an item
            and return a mapping between the original item's name and its new
            name.
            For every conflict, both files will be renamed and therefore this list
            will always be a multiple of 2.
        :type name_conflicts: Optional[List[List[ZipDownloadNameConflictsField]]], optional
        """
        super().__init__(**kwargs)
        self.download_url = download_url
        self.status_url = status_url
        self.expires_at = expires_at
        self.name_conflicts = name_conflicts


class ZipDownloadStatusStateField(str, Enum):
    IN_PROGRESS = 'in_progress'
    FAILED = 'failed'
    SUCCEEDED = 'succeeded'


class ZipDownloadStatus(BaseObject):
    def __init__(
        self,
        total_file_count: Optional[int] = None,
        downloaded_file_count: Optional[int] = None,
        skipped_file_count: Optional[int] = None,
        skipped_folder_count: Optional[int] = None,
        state: Optional[ZipDownloadStatusStateField] = None,
        **kwargs
    ):
        """
        :param total_file_count: The total number of files in the archive.
        :type total_file_count: Optional[int], optional
        :param downloaded_file_count: The number of files that have already been downloaded.
        :type downloaded_file_count: Optional[int], optional
        :param skipped_file_count: The number of files that have been skipped as they could not be
            downloaded. In many cases this is due to permission issues that have
            surfaced between the creation of the request for the archive and the
            archive being downloaded.
        :type skipped_file_count: Optional[int], optional
        :param skipped_folder_count: The number of folders that have been skipped as they could not be
            downloaded. In many cases this is due to permission issues that have
            surfaced between the creation of the request for the archive and the
            archive being downloaded.
        :type skipped_folder_count: Optional[int], optional
        :param state: The state of the archive being downloaded.
        :type state: Optional[ZipDownloadStatusStateField], optional
        """
        super().__init__(**kwargs)
        self.total_file_count = total_file_count
        self.downloaded_file_count = downloaded_file_count
        self.skipped_file_count = skipped_file_count
        self.skipped_folder_count = skipped_folder_count
        self.state = state


class KeywordSkillCardTypeField(str, Enum):
    SKILL_CARD = 'skill_card'


class KeywordSkillCardSkillCardTypeField(str, Enum):
    KEYWORD = 'keyword'


class KeywordSkillCardSkillCardTitleField(BaseObject):
    def __init__(self, message: str, code: Optional[str] = None, **kwargs):
        """
        :param message: The actual title to show in the UI.
        :type message: str
        :param code: An optional identifier for the title.
        :type code: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.message = message
        self.code = code


class KeywordSkillCardSkillFieldTypeField(str, Enum):
    SERVICE = 'service'


class KeywordSkillCardSkillField(BaseObject):
    def __init__(self, type: KeywordSkillCardSkillFieldTypeField, id: str, **kwargs):
        """
        :param type: `service`
        :type type: KeywordSkillCardSkillFieldTypeField
        :param id: A custom identifier that represent the service that
            applied this metadata.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class KeywordSkillCardInvocationFieldTypeField(str, Enum):
    SKILL_INVOCATION = 'skill_invocation'


class KeywordSkillCardInvocationField(BaseObject):
    def __init__(
        self, type: KeywordSkillCardInvocationFieldTypeField, id: str, **kwargs
    ):
        """
        :param type: `skill_invocation`
        :type type: KeywordSkillCardInvocationFieldTypeField
        :param id: A custom identifier that represent the instance of
            the service that applied this metadata. For example,
            if your `image-recognition-service` runs on multiple
            nodes, this field can be used to identify the ID of
            the node that was used to apply the metadata.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class KeywordSkillCardEntriesField(BaseObject):
    def __init__(self, text: Optional[str] = None, **kwargs):
        """
        :param text: The text of the keyword.
        :type text: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.text = text


class KeywordSkillCard(BaseObject):
    def __init__(
        self,
        type: KeywordSkillCardTypeField,
        skill_card_type: KeywordSkillCardSkillCardTypeField,
        skill: KeywordSkillCardSkillField,
        invocation: KeywordSkillCardInvocationField,
        entries: List[KeywordSkillCardEntriesField],
        created_at: Optional[str] = None,
        skill_card_title: Optional[KeywordSkillCardSkillCardTitleField] = None,
        **kwargs
    ):
        """
        :param type: `skill_card`
        :type type: KeywordSkillCardTypeField
        :param skill_card_type: `keyword`
        :type skill_card_type: KeywordSkillCardSkillCardTypeField
        :param skill: The service that applied this metadata.
        :type skill: KeywordSkillCardSkillField
        :param invocation: The invocation of this service, used to track
            which instance of a service applied the metadata.
        :type invocation: KeywordSkillCardInvocationField
        :param entries: An list of entries in the metadata card.
        :type entries: List[KeywordSkillCardEntriesField]
        :param created_at: The optional date and time this card was created at.
        :type created_at: Optional[str], optional
        :param skill_card_title: The title of the card.
        :type skill_card_title: Optional[KeywordSkillCardSkillCardTitleField], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.skill_card_type = skill_card_type
        self.skill = skill
        self.invocation = invocation
        self.entries = entries
        self.created_at = created_at
        self.skill_card_title = skill_card_title


class IntegrationMappingSlackOptions(BaseObject):
    def __init__(self, is_access_management_disabled: Optional[bool] = None, **kwargs):
        """
        :param is_access_management_disabled: Indicates whether or not channel member
            access to the underlying box item
            should be automatically managed.
            Depending on type of channel, access is managed
            through creating collaborations or shared links.
        :type is_access_management_disabled: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.is_access_management_disabled = is_access_management_disabled


class IntegrationMappingPartnerItemSlackTypeField(str, Enum):
    CHANNEL = 'channel'


class IntegrationMappingPartnerItemSlack(BaseObject):
    def __init__(
        self,
        type: IntegrationMappingPartnerItemSlackTypeField,
        id: str,
        slack_workspace_id: Optional[str] = None,
        slack_org_id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: Type of the mapped item referenced in `id`
        :type type: IntegrationMappingPartnerItemSlackTypeField
        :param id: ID of the mapped item (of type referenced in `type`)
        :type id: str
        :param slack_workspace_id: ID of the Slack workspace with which the item is associated. Use this parameter if Box for Slack is installed at a workspace level. Do not use `slack_org_id` at the same time.
        :type slack_workspace_id: Optional[str], optional
        :param slack_org_id: ID of the Slack org with which the item is associated. Use this parameter if Box for Slack is installed at the org level. Do not use `slack_workspace_id` at the same time.
        :type slack_org_id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id
        self.slack_workspace_id = slack_workspace_id
        self.slack_org_id = slack_org_id


class IntegrationMappingTypeField(str, Enum):
    INTEGRATION_MAPPING = 'integration_mapping'


class IntegrationMapping(IntegrationMappingBase):
    def __init__(
        self,
        type: IntegrationMappingTypeField,
        partner_item: Union[IntegrationMappingPartnerItemSlack],
        box_item: FolderMini,
        is_manually_created: Optional[bool] = None,
        options: Optional[IntegrationMappingSlackOptions] = None,
        created_by: Optional[UserIntegrationMappings] = None,
        modified_by: Optional[UserIntegrationMappings] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        id: Optional[str] = None,
        integration_type: Optional[IntegrationMappingBaseIntegrationTypeField] = None,
        **kwargs
    ):
        """
        :param type: Mapping type
        :type type: IntegrationMappingTypeField
        :param partner_item: Mapped item object for Slack
        :type partner_item: Union[IntegrationMappingPartnerItemSlack]
        :param box_item: The Box folder, to which the object from the
            partner app domain (referenced in `partner_item_id`) is mapped
        :type box_item: FolderMini
        :param is_manually_created: Identifies whether the mapping has
            been manually set
            (as opposed to being automatically created)
        :type is_manually_created: Optional[bool], optional
        :param options: Integration mapping options for Slack
        :type options: Optional[IntegrationMappingSlackOptions], optional
        :param created_by: An object representing the user who
            created the integration mapping
        :type created_by: Optional[UserIntegrationMappings], optional
        :param modified_by: The user who
            last modified the integration mapping
        :type modified_by: Optional[UserIntegrationMappings], optional
        :param created_at: When the integration mapping object was created
        :type created_at: Optional[str], optional
        :param modified_at: When the integration mapping object was last modified
        :type modified_at: Optional[str], optional
        :param id: A unique identifier of a folder mapping
            (part of a composite key together
            with `integration_type`)
        :type id: Optional[str], optional
        :param integration_type: Identifies the Box partner app,
            with which the mapping is associated.
            Currently only supports Slack.
            (part of the composite key together with `id`)
        :type integration_type: Optional[IntegrationMappingBaseIntegrationTypeField], optional
        """
        super().__init__(id=id, integration_type=integration_type, **kwargs)
        self.type = type
        self.partner_item = partner_item
        self.box_item = box_item
        self.is_manually_created = is_manually_created
        self.options = options
        self.created_by = created_by
        self.modified_by = modified_by
        self.created_at = created_at
        self.modified_at = modified_at


class IntegrationMappings(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        entries: Optional[List[IntegrationMapping]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        :param entries: A list of integration mappings
        :type entries: Optional[List[IntegrationMapping]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.entries = entries


class IntegrationMappingBoxItemSlackTypeField(str, Enum):
    FOLDER = 'folder'


class IntegrationMappingBoxItemSlack(BaseObject):
    def __init__(
        self, type: IntegrationMappingBoxItemSlackTypeField, id: str, **kwargs
    ):
        """
        :param type: Type of the mapped item referenced in `id`
        :type type: IntegrationMappingBoxItemSlackTypeField
        :param id: ID of the mapped item (of type referenced in `type`)
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class IntegrationMappingSlackCreateRequest(BaseObject):
    def __init__(
        self,
        partner_item: IntegrationMappingPartnerItemSlack,
        box_item: IntegrationMappingBoxItemSlack,
        options: Optional[IntegrationMappingSlackOptions] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.partner_item = partner_item
        self.box_item = box_item
        self.options = options


class TimelineSkillCardTypeField(str, Enum):
    SKILL_CARD = 'skill_card'


class TimelineSkillCardSkillCardTypeField(str, Enum):
    TIMELINE = 'timeline'


class TimelineSkillCardSkillCardTitleField(BaseObject):
    def __init__(self, message: str, code: Optional[str] = None, **kwargs):
        """
        :param message: The actual title to show in the UI.
        :type message: str
        :param code: An optional identifier for the title.
        :type code: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.message = message
        self.code = code


class TimelineSkillCardSkillFieldTypeField(str, Enum):
    SERVICE = 'service'


class TimelineSkillCardSkillField(BaseObject):
    def __init__(self, type: TimelineSkillCardSkillFieldTypeField, id: str, **kwargs):
        """
        :param type: `service`
        :type type: TimelineSkillCardSkillFieldTypeField
        :param id: A custom identifier that represent the service that
            applied this metadata.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class TimelineSkillCardInvocationFieldTypeField(str, Enum):
    SKILL_INVOCATION = 'skill_invocation'


class TimelineSkillCardInvocationField(BaseObject):
    def __init__(
        self, type: TimelineSkillCardInvocationFieldTypeField, id: str, **kwargs
    ):
        """
        :param type: `skill_invocation`
        :type type: TimelineSkillCardInvocationFieldTypeField
        :param id: A custom identifier that represent the instance of
            the service that applied this metadata. For example,
            if your `image-recognition-service` runs on multiple
            nodes, this field can be used to identify the ID of
            the node that was used to apply the metadata.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class TimelineSkillCardEntriesFieldAppearsField(BaseObject):
    def __init__(
        self, start: Optional[int] = None, end: Optional[int] = None, **kwargs
    ):
        """
        :param start: The time in seconds when an
            entry should start appearing on a timeline.
        :type start: Optional[int], optional
        :param end: The time in seconds when an
            entry should stop appearing on a timeline.
        :type end: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.start = start
        self.end = end


class TimelineSkillCardEntriesField(BaseObject):
    def __init__(
        self,
        text: Optional[str] = None,
        appears: Optional[List[TimelineSkillCardEntriesFieldAppearsField]] = None,
        image_url: Optional[str] = None,
        **kwargs
    ):
        """
        :param text: The text of the entry. This would be the display
            name for an item being placed on the timeline, for example the name
            of the person who was detected in a video.
        :type text: Optional[str], optional
        :param appears: Defines a list of timestamps for when this item should appear on the
            timeline.
        :type appears: Optional[List[TimelineSkillCardEntriesFieldAppearsField]], optional
        :param image_url: The image to show on a for an entry that appears
            on a timeline. This image URL is required for every entry.
            The image will be shown in a
            list of items (for example faces), and clicking
            the image will show the user where that entry
            appears during the duration of this entry.
        :type image_url: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.text = text
        self.appears = appears
        self.image_url = image_url


class TimelineSkillCard(BaseObject):
    def __init__(
        self,
        type: TimelineSkillCardTypeField,
        skill_card_type: TimelineSkillCardSkillCardTypeField,
        skill: TimelineSkillCardSkillField,
        invocation: TimelineSkillCardInvocationField,
        entries: List[TimelineSkillCardEntriesField],
        created_at: Optional[str] = None,
        skill_card_title: Optional[TimelineSkillCardSkillCardTitleField] = None,
        duration: Optional[int] = None,
        **kwargs
    ):
        """
        :param type: `skill_card`
        :type type: TimelineSkillCardTypeField
        :param skill_card_type: `timeline`
        :type skill_card_type: TimelineSkillCardSkillCardTypeField
        :param skill: The service that applied this metadata.
        :type skill: TimelineSkillCardSkillField
        :param invocation: The invocation of this service, used to track
            which instance of a service applied the metadata.
        :type invocation: TimelineSkillCardInvocationField
        :param entries: A list of entries on the timeline.
        :type entries: List[TimelineSkillCardEntriesField]
        :param created_at: The optional date and time this card was created at.
        :type created_at: Optional[str], optional
        :param skill_card_title: The title of the card.
        :type skill_card_title: Optional[TimelineSkillCardSkillCardTitleField], optional
        :param duration: An total duration in seconds of the timeline.
        :type duration: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.skill_card_type = skill_card_type
        self.skill = skill
        self.invocation = invocation
        self.entries = entries
        self.created_at = created_at
        self.skill_card_title = skill_card_title
        self.duration = duration


class TranscriptSkillCardTypeField(str, Enum):
    SKILL_CARD = 'skill_card'


class TranscriptSkillCardSkillCardTypeField(str, Enum):
    TRANSCRIPT = 'transcript'


class TranscriptSkillCardSkillCardTitleField(BaseObject):
    def __init__(self, message: str, code: Optional[str] = None, **kwargs):
        """
        :param message: The actual title to show in the UI.
        :type message: str
        :param code: An optional identifier for the title.
        :type code: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.message = message
        self.code = code


class TranscriptSkillCardSkillFieldTypeField(str, Enum):
    SERVICE = 'service'


class TranscriptSkillCardSkillField(BaseObject):
    def __init__(self, type: TranscriptSkillCardSkillFieldTypeField, id: str, **kwargs):
        """
        :param type: `service`
        :type type: TranscriptSkillCardSkillFieldTypeField
        :param id: A custom identifier that represent the service that
            applied this metadata.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class TranscriptSkillCardInvocationFieldTypeField(str, Enum):
    SKILL_INVOCATION = 'skill_invocation'


class TranscriptSkillCardInvocationField(BaseObject):
    def __init__(
        self, type: TranscriptSkillCardInvocationFieldTypeField, id: str, **kwargs
    ):
        """
        :param type: `skill_invocation`
        :type type: TranscriptSkillCardInvocationFieldTypeField
        :param id: A custom identifier that represent the instance of
            the service that applied this metadata. For example,
            if your `image-recognition-service` runs on multiple
            nodes, this field can be used to identify the ID of
            the node that was used to apply the metadata.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class TranscriptSkillCardEntriesFieldAppearsField(BaseObject):
    def __init__(self, start: Optional[int] = None, **kwargs):
        """
        :param start: The time in seconds when an
            entry should start appearing on a timeline.
        :type start: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.start = start


class TranscriptSkillCardEntriesField(BaseObject):
    def __init__(
        self,
        text: Optional[str] = None,
        appears: Optional[List[TranscriptSkillCardEntriesFieldAppearsField]] = None,
        **kwargs
    ):
        """
        :param text: The text of the entry. This would be the transcribed text assigned
            to the entry on the timeline.
        :type text: Optional[str], optional
        :param appears: Defines when a transcribed bit of text appears. This only includes a
            start time and no end time.
        :type appears: Optional[List[TranscriptSkillCardEntriesFieldAppearsField]], optional
        """
        super().__init__(**kwargs)
        self.text = text
        self.appears = appears


class TranscriptSkillCard(BaseObject):
    def __init__(
        self,
        type: TranscriptSkillCardTypeField,
        skill_card_type: TranscriptSkillCardSkillCardTypeField,
        skill: TranscriptSkillCardSkillField,
        invocation: TranscriptSkillCardInvocationField,
        entries: List[TranscriptSkillCardEntriesField],
        created_at: Optional[str] = None,
        skill_card_title: Optional[TranscriptSkillCardSkillCardTitleField] = None,
        duration: Optional[int] = None,
        **kwargs
    ):
        """
        :param type: `skill_card`
        :type type: TranscriptSkillCardTypeField
        :param skill_card_type: `transcript`
        :type skill_card_type: TranscriptSkillCardSkillCardTypeField
        :param skill: The service that applied this metadata.
        :type skill: TranscriptSkillCardSkillField
        :param invocation: The invocation of this service, used to track
            which instance of a service applied the metadata.
        :type invocation: TranscriptSkillCardInvocationField
        :param entries: An list of entries for the card. This represents the individual entries of
            the transcription.
        :type entries: List[TranscriptSkillCardEntriesField]
        :param created_at: The optional date and time this card was created at.
        :type created_at: Optional[str], optional
        :param skill_card_title: The title of the card.
        :type skill_card_title: Optional[TranscriptSkillCardSkillCardTitleField], optional
        :param duration: An optional total duration in seconds.
            Used with a `skill_card_type` of `transcript` or
            `timeline`.
        :type duration: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.skill_card_type = skill_card_type
        self.skill = skill
        self.invocation = invocation
        self.entries = entries
        self.created_at = created_at
        self.skill_card_title = skill_card_title
        self.duration = duration


class StatusSkillCardTypeField(str, Enum):
    SKILL_CARD = 'skill_card'


class StatusSkillCardSkillCardTypeField(str, Enum):
    STATUS = 'status'


class StatusSkillCardSkillCardTitleField(BaseObject):
    def __init__(self, message: str, code: Optional[str] = None, **kwargs):
        """
        :param message: The actual title to show in the UI.
        :type message: str
        :param code: An optional identifier for the title.
        :type code: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.message = message
        self.code = code


class StatusSkillCardStatusFieldCodeField(str, Enum):
    INVOKED = 'invoked'
    PROCESSING = 'processing'
    SUCCESS = 'success'
    TRANSIENT_FAILURE = 'transient_failure'
    PERMANENT_FAILURE = 'permanent_failure'


class StatusSkillCardStatusField(BaseObject):
    def __init__(
        self,
        code: StatusSkillCardStatusFieldCodeField,
        message: Optional[str] = None,
        **kwargs
    ):
        """
        :param code: A code for the status of this Skill invocation. By
            default each of these will have their own accompanied
            messages. These can be adjusted by setting the `message`
            value on this object.
        :type code: StatusSkillCardStatusFieldCodeField
        :param message: A custom message that can be provided with this status.
            This will be shown in the web app to the end user.
        :type message: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message


class StatusSkillCardSkillFieldTypeField(str, Enum):
    SERVICE = 'service'


class StatusSkillCardSkillField(BaseObject):
    def __init__(self, type: StatusSkillCardSkillFieldTypeField, id: str, **kwargs):
        """
        :param type: `service`
        :type type: StatusSkillCardSkillFieldTypeField
        :param id: A custom identifier that represent the service that
            applied this metadata.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class StatusSkillCardInvocationFieldTypeField(str, Enum):
    SKILL_INVOCATION = 'skill_invocation'


class StatusSkillCardInvocationField(BaseObject):
    def __init__(
        self, type: StatusSkillCardInvocationFieldTypeField, id: str, **kwargs
    ):
        """
        :param type: `skill_invocation`
        :type type: StatusSkillCardInvocationFieldTypeField
        :param id: A custom identifier that represent the instance of
            the service that applied this metadata. For example,
            if your `image-recognition-service` runs on multiple
            nodes, this field can be used to identify the ID of
            the node that was used to apply the metadata.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class StatusSkillCard(BaseObject):
    def __init__(
        self,
        type: StatusSkillCardTypeField,
        skill_card_type: StatusSkillCardSkillCardTypeField,
        status: StatusSkillCardStatusField,
        skill: StatusSkillCardSkillField,
        invocation: StatusSkillCardInvocationField,
        created_at: Optional[str] = None,
        skill_card_title: Optional[StatusSkillCardSkillCardTitleField] = None,
        **kwargs
    ):
        """
        :param type: `skill_card`
        :type type: StatusSkillCardTypeField
        :param skill_card_type: `status`
        :type skill_card_type: StatusSkillCardSkillCardTypeField
        :param status: Sets the status of the skill. This can be used to show a message to the user while the Skill is processing the data, or if it was not able to process the file.
        :type status: StatusSkillCardStatusField
        :param skill: The service that applied this metadata.
        :type skill: StatusSkillCardSkillField
        :param invocation: The invocation of this service, used to track
            which instance of a service applied the metadata.
        :type invocation: StatusSkillCardInvocationField
        :param created_at: The optional date and time this card was created at.
        :type created_at: Optional[str], optional
        :param skill_card_title: The title of the card.
        :type skill_card_title: Optional[StatusSkillCardSkillCardTitleField], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.skill_card_type = skill_card_type
        self.status = status
        self.skill = skill
        self.invocation = invocation
        self.created_at = created_at
        self.skill_card_title = skill_card_title


class SkillCardsMetadata(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'can_edit': '$canEdit',
        'id': '$id',
        'parent': '$parent',
        'scope': '$scope',
        'template': '$template',
        'type': '$type',
        'type_version': '$typeVersion',
        'version': '$version',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        '$canEdit': 'can_edit',
        '$id': 'id',
        '$parent': 'parent',
        '$scope': 'scope',
        '$template': 'template',
        '$type': 'type',
        '$typeVersion': 'type_version',
        '$version': 'version',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        can_edit: Optional[bool] = None,
        id: Optional[str] = None,
        parent: Optional[str] = None,
        scope: Optional[str] = None,
        template: Optional[str] = None,
        type: Optional[str] = None,
        type_version: Optional[int] = None,
        version: Optional[int] = None,
        cards: Optional[
            List[
                Union[
                    KeywordSkillCard,
                    TimelineSkillCard,
                    TranscriptSkillCard,
                    StatusSkillCard,
                ]
            ]
        ] = None,
        **kwargs
    ):
        """
        :param can_edit: Whether the user can edit this metadata
        :type can_edit: Optional[bool], optional
        :param id: A UUID to identify the metadata object
        :type id: Optional[str], optional
        :param parent: An ID for the parent folder
        :type parent: Optional[str], optional
        :param scope: An ID for the scope in which this template
            has been applied
        :type scope: Optional[str], optional
        :param template: The name of the template
        :type template: Optional[str], optional
        :param type: A unique identifier for the "type" of this instance. This is an internal
            system property and should not be used by a client application.
        :type type: Optional[str], optional
        :param type_version: The last-known version of the template of the object. This is an internal
            system property and should not be used by a client application.
        :type type_version: Optional[int], optional
        :param version: The version of the metadata object. Starts at 0 and increases every time
            a user-defined property is modified.
        :type version: Optional[int], optional
        :param cards: A list of Box Skill cards that have been applied to this file.
        :type cards: Optional[List[Union[KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]], optional
        """
        super().__init__(**kwargs)
        self.can_edit = can_edit
        self.id = id
        self.parent = parent
        self.scope = scope
        self.template = template
        self.type = type
        self.type_version = type_version
        self.version = version
        self.cards = cards


class SignRequestCreateSignerRoleField(str, Enum):
    SIGNER = 'signer'
    APPROVER = 'approver'
    FINAL_COPY_READER = 'final_copy_reader'


class SignRequestCreateSigner(BaseObject):
    def __init__(
        self,
        email: Optional[str] = None,
        role: Optional[SignRequestCreateSignerRoleField] = None,
        is_in_person: Optional[bool] = None,
        order: Optional[int] = None,
        embed_url_external_user_id: Optional[str] = None,
        redirect_url: Optional[str] = None,
        declined_redirect_url: Optional[str] = None,
        login_required: Optional[bool] = None,
        verification_phone_number: Optional[str] = None,
        password: Optional[str] = None,
        **kwargs
    ):
        """
        :param email: Email address of the signer.
            The email address of the signer is required when making signature requests, except when using templates that are configured to include emails.
        :type email: Optional[str], optional
        :param role: Defines the role of the signer in the sign request. A `signer`
            must sign the document and an `approver` must approve the document. A
            `final_copy_reader` only receives the final signed document and signing
            log.
        :type role: Optional[SignRequestCreateSignerRoleField], optional
        :param is_in_person: Used in combination with an embed URL for a sender. After the
            sender signs, they are redirected to the next `in_person` signer.
        :type is_in_person: Optional[bool], optional
        :param order: Order of the signer
        :type order: Optional[int], optional
        :param embed_url_external_user_id: User ID for the signer in an external application responsible
            for authentication when accessing the embed URL.
        :type embed_url_external_user_id: Optional[str], optional
        :param redirect_url: The URL that a signer will be redirected
            to after signing a document. Defining this URL
            overrides default or global redirect URL
            settings for a specific signer.
            If no declined redirect URL is specified,
            this URL will be used for decline actions as well.
        :type redirect_url: Optional[str], optional
        :param declined_redirect_url: The URL that a signer will be redirect
            to after declining to sign a document.
            Defining this URL overrides default or global
            declined redirect URL settings for a specific signer.
        :type declined_redirect_url: Optional[str], optional
        :param login_required: If set to true, signer will need to login to a Box account
            before signing the request. If the signer does not have
            an existing account, they will have an option to create
            a free Box account.
        :type login_required: Optional[bool], optional
        :param verification_phone_number: If set, this phone number is be used to verify the signer
            via two factor authentication before they are able to sign the document.
        :type verification_phone_number: Optional[str], optional
        :param password: If set, the signer is required to enter the password before they are able
            to sign a document. This field is write only.
        :type password: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.email = email
        self.role = role
        self.is_in_person = is_in_person
        self.order = order
        self.embed_url_external_user_id = embed_url_external_user_id
        self.redirect_url = redirect_url
        self.declined_redirect_url = declined_redirect_url
        self.login_required = login_required
        self.verification_phone_number = verification_phone_number
        self.password = password


class SignRequestPrefillTag(BaseObject):
    def __init__(
        self,
        document_tag_id: Optional[str] = None,
        text_value: Optional[str] = None,
        checkbox_value: Optional[bool] = None,
        date_value: Optional[str] = None,
        **kwargs
    ):
        """
        :param document_tag_id: This references the ID of a specific tag contained in a file of the sign request.
        :type document_tag_id: Optional[str], optional
        :param text_value: Text prefill value
        :type text_value: Optional[str], optional
        :param checkbox_value: Checkbox prefill value
        :type checkbox_value: Optional[bool], optional
        :param date_value: Date prefill value
        :type date_value: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.document_tag_id = document_tag_id
        self.text_value = text_value
        self.checkbox_value = checkbox_value
        self.date_value = date_value


class SignRequestSignerInputTypeField(str, Enum):
    SIGNATURE = 'signature'
    DATE = 'date'
    TEXT = 'text'
    CHECKBOX = 'checkbox'
    RADIO = 'radio'
    DROPDOWN = 'dropdown'


class SignRequestSignerInputContentTypeField(str, Enum):
    SIGNATURE = 'signature'
    INITIAL = 'initial'
    STAMP = 'stamp'
    DATE = 'date'
    CHECKBOX = 'checkbox'
    TEXT = 'text'
    FULL_NAME = 'full_name'
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    COMPANY = 'company'
    TITLE = 'title'
    EMAIL = 'email'
    ATTACHMENT = 'attachment'
    RADIO = 'radio'
    DROPDOWN = 'dropdown'


class SignRequestSignerInput(SignRequestPrefillTag):
    def __init__(
        self,
        page_index: int,
        type: Optional[SignRequestSignerInputTypeField] = None,
        content_type: Optional[SignRequestSignerInputContentTypeField] = None,
        document_tag_id: Optional[str] = None,
        text_value: Optional[str] = None,
        checkbox_value: Optional[bool] = None,
        date_value: Optional[str] = None,
        **kwargs
    ):
        """
        :param page_index: Index of page that the input is on
        :type page_index: int
        :param type: Type of input
        :type type: Optional[SignRequestSignerInputTypeField], optional
        :param content_type: Content type of input
        :type content_type: Optional[SignRequestSignerInputContentTypeField], optional
        :param document_tag_id: This references the ID of a specific tag contained in a file of the sign request.
        :type document_tag_id: Optional[str], optional
        :param text_value: Text prefill value
        :type text_value: Optional[str], optional
        :param checkbox_value: Checkbox prefill value
        :type checkbox_value: Optional[bool], optional
        :param date_value: Date prefill value
        :type date_value: Optional[str], optional
        """
        super().__init__(
            document_tag_id=document_tag_id,
            text_value=text_value,
            checkbox_value=checkbox_value,
            date_value=date_value,
            **kwargs
        )
        self.page_index = page_index
        self.type = type
        self.content_type = content_type


class SignRequestSignerSignerDecisionFieldTypeField(str, Enum):
    SIGNED = 'signed'
    DECLINED = 'declined'


class SignRequestSignerSignerDecisionField(BaseObject):
    def __init__(
        self,
        type: Optional[SignRequestSignerSignerDecisionFieldTypeField] = None,
        finalized_at: Optional[str] = None,
        additional_info: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: Type of decision made by the signer
        :type type: Optional[SignRequestSignerSignerDecisionFieldTypeField], optional
        :param finalized_at: Date and Time that the decision was made
        :type finalized_at: Optional[str], optional
        :param additional_info: Additional info about the decision, such as the decline reason from the signer
        :type additional_info: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.finalized_at = finalized_at
        self.additional_info = additional_info


class SignRequestSigner(SignRequestCreateSigner):
    def __init__(
        self,
        has_viewed_document: Optional[bool] = None,
        signer_decision: Optional[SignRequestSignerSignerDecisionField] = None,
        inputs: Optional[List[SignRequestSignerInput]] = None,
        embed_url: Optional[str] = None,
        iframeable_embed_url: Optional[str] = None,
        email: Optional[str] = None,
        role: Optional[SignRequestCreateSignerRoleField] = None,
        is_in_person: Optional[bool] = None,
        order: Optional[int] = None,
        embed_url_external_user_id: Optional[str] = None,
        redirect_url: Optional[str] = None,
        declined_redirect_url: Optional[str] = None,
        login_required: Optional[bool] = None,
        verification_phone_number: Optional[str] = None,
        password: Optional[str] = None,
        **kwargs
    ):
        """
        :param has_viewed_document: Set to `true` if the signer views the document
        :type has_viewed_document: Optional[bool], optional
        :param signer_decision: Final decision made by the signer
        :type signer_decision: Optional[SignRequestSignerSignerDecisionField], optional
        :param embed_url: URL to direct a signer to for signing
        :type embed_url: Optional[str], optional
        :param iframeable_embed_url: This URL is specifically designed for
            signing documents within an HTML `iframe` tag.
            It will be returned in the response
            only if the `embed_url_external_user_id`
            parameter was passed in the
            `create sign request` call.
        :type iframeable_embed_url: Optional[str], optional
        :param email: Email address of the signer.
            The email address of the signer is required when making signature requests, except when using templates that are configured to include emails.
        :type email: Optional[str], optional
        :param role: Defines the role of the signer in the sign request. A `signer`
            must sign the document and an `approver` must approve the document. A
            `final_copy_reader` only receives the final signed document and signing
            log.
        :type role: Optional[SignRequestCreateSignerRoleField], optional
        :param is_in_person: Used in combination with an embed URL for a sender. After the
            sender signs, they are redirected to the next `in_person` signer.
        :type is_in_person: Optional[bool], optional
        :param order: Order of the signer
        :type order: Optional[int], optional
        :param embed_url_external_user_id: User ID for the signer in an external application responsible
            for authentication when accessing the embed URL.
        :type embed_url_external_user_id: Optional[str], optional
        :param redirect_url: The URL that a signer will be redirected
            to after signing a document. Defining this URL
            overrides default or global redirect URL
            settings for a specific signer.
            If no declined redirect URL is specified,
            this URL will be used for decline actions as well.
        :type redirect_url: Optional[str], optional
        :param declined_redirect_url: The URL that a signer will be redirect
            to after declining to sign a document.
            Defining this URL overrides default or global
            declined redirect URL settings for a specific signer.
        :type declined_redirect_url: Optional[str], optional
        :param login_required: If set to true, signer will need to login to a Box account
            before signing the request. If the signer does not have
            an existing account, they will have an option to create
            a free Box account.
        :type login_required: Optional[bool], optional
        :param verification_phone_number: If set, this phone number is be used to verify the signer
            via two factor authentication before they are able to sign the document.
        :type verification_phone_number: Optional[str], optional
        :param password: If set, the signer is required to enter the password before they are able
            to sign a document. This field is write only.
        :type password: Optional[str], optional
        """
        super().__init__(
            email=email,
            role=role,
            is_in_person=is_in_person,
            order=order,
            embed_url_external_user_id=embed_url_external_user_id,
            redirect_url=redirect_url,
            declined_redirect_url=declined_redirect_url,
            login_required=login_required,
            verification_phone_number=verification_phone_number,
            password=password,
            **kwargs
        )
        self.has_viewed_document = has_viewed_document
        self.signer_decision = signer_decision
        self.inputs = inputs
        self.embed_url = embed_url
        self.iframeable_embed_url = iframeable_embed_url


class SignRequestBase(BaseObject):
    def __init__(
        self,
        parent_folder: FolderMini,
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
        **kwargs
    ):
        """
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
        """
        super().__init__(**kwargs)
        self.parent_folder = parent_folder
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


class SignRequestTypeField(str, Enum):
    SIGN_REQUEST = 'sign-request'


class SignRequestStatusField(str, Enum):
    CONVERTING = 'converting'
    CREATED = 'created'
    SENT = 'sent'
    VIEWED = 'viewed'
    SIGNED = 'signed'
    CANCELLED = 'cancelled'
    DECLINED = 'declined'
    ERROR_CONVERTING = 'error_converting'
    ERROR_SENDING = 'error_sending'
    EXPIRED = 'expired'
    FINALIZING = 'finalizing'
    ERROR_FINALIZING = 'error_finalizing'


class SignRequestSignFilesField(BaseObject):
    def __init__(
        self,
        files: Optional[List[FileMini]] = None,
        is_ready_for_download: Optional[bool] = None,
        **kwargs
    ):
        """
        :param is_ready_for_download: Indicates whether the `sign_files` documents are processing
            and the PDFs may be out of date. A change to any document
            requires processing on all `sign_files`. We
            recommended waiting until processing is finished
            (and this value is true) before downloading the PDFs.
        :type is_ready_for_download: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.files = files
        self.is_ready_for_download = is_ready_for_download


class SignRequest(SignRequestBase):
    def __init__(
        self,
        parent_folder: FolderMini,
        type: Optional[SignRequestTypeField] = None,
        source_files: Optional[List[FileBase]] = None,
        signers: Optional[List[SignRequestSigner]] = None,
        signature_color: Optional[str] = None,
        id: Optional[str] = None,
        prepare_url: Optional[str] = None,
        signing_log: Optional[FileMini] = None,
        status: Optional[SignRequestStatusField] = None,
        sign_files: Optional[SignRequestSignFilesField] = None,
        auto_expire_at: Optional[str] = None,
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
        **kwargs
    ):
        """
        :param type: object type
        :type type: Optional[SignRequestTypeField], optional
        :param source_files: List of files to create a signing document from. This is currently limited to ten files. Only the ID and type fields are required for each file.
        :type source_files: Optional[List[FileBase]], optional
        :param signers: Array of signers for the sign request
        :type signers: Optional[List[SignRequestSigner]], optional
        :param signature_color: Force a specific color for the signature (blue, black, or red).
        :type signature_color: Optional[str], optional
        :param id: Sign request ID
        :type id: Optional[str], optional
        :param prepare_url: This URL is returned if `is_document_preparation_needed` is
            set to `true` in the request. It is used to prepare the sign request
            via UI. The sign request is not sent until preparation is complete.
        :type prepare_url: Optional[str], optional
        :param status: Describes the status of the sign request
        :type status: Optional[SignRequestStatusField], optional
        :param sign_files: List of files that will be signed, which are copies of the original
            source files. A new version of these files are created as signers sign
            and can be downloaded at any point in the signing process.
        :type sign_files: Optional[SignRequestSignFilesField], optional
        :param auto_expire_at: Uses `days_valid` to calculate the date and time, in GMT, the sign request will expire if unsigned.
        :type auto_expire_at: Optional[str], optional
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
        """
        super().__init__(
            parent_folder=parent_folder,
            is_document_preparation_needed=is_document_preparation_needed,
            redirect_url=redirect_url,
            declined_redirect_url=declined_redirect_url,
            are_text_signatures_enabled=are_text_signatures_enabled,
            email_subject=email_subject,
            email_message=email_message,
            are_reminders_enabled=are_reminders_enabled,
            name=name,
            prefill_tags=prefill_tags,
            days_valid=days_valid,
            external_id=external_id,
            is_phone_verification_required_to_view=is_phone_verification_required_to_view,
            template_id=template_id,
            **kwargs
        )
        self.type = type
        self.source_files = source_files
        self.signers = signers
        self.signature_color = signature_color
        self.id = id
        self.prepare_url = prepare_url
        self.signing_log = signing_log
        self.status = status
        self.sign_files = sign_files
        self.auto_expire_at = auto_expire_at


class SignRequests(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        entries: Optional[List[SignRequest]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        :param entries: A list of sign requests
        :type entries: Optional[List[SignRequest]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.entries = entries


class SignRequestCreateRequestSignatureColorField(str, Enum):
    BLUE = 'blue'
    BLACK = 'black'
    RED = 'red'


class SignRequestCreateRequest(SignRequestBase):
    def __init__(
        self,
        signers: List[SignRequestCreateSigner],
        parent_folder: FolderMini,
        source_files: Optional[List[FileBase]] = None,
        signature_color: Optional[SignRequestCreateRequestSignatureColorField] = None,
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
        **kwargs
    ):
        """
        :param signers: Array of signers for the sign request. 35 is the max number of signers permitted.
        :type signers: List[SignRequestCreateSigner]
        :param source_files: List of files to create a signing document from. This is currently limited to ten files. Only the ID and type fields are required for each file.
        :type source_files: Optional[List[FileBase]], optional
        :param signature_color: Force a specific color for the signature (blue, black, or red)
        :type signature_color: Optional[SignRequestCreateRequestSignatureColorField], optional
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
        """
        super().__init__(
            parent_folder=parent_folder,
            is_document_preparation_needed=is_document_preparation_needed,
            redirect_url=redirect_url,
            declined_redirect_url=declined_redirect_url,
            are_text_signatures_enabled=are_text_signatures_enabled,
            email_subject=email_subject,
            email_message=email_message,
            are_reminders_enabled=are_reminders_enabled,
            name=name,
            prefill_tags=prefill_tags,
            days_valid=days_valid,
            external_id=external_id,
            is_phone_verification_required_to_view=is_phone_verification_required_to_view,
            template_id=template_id,
            **kwargs
        )
        self.signers = signers
        self.source_files = source_files
        self.signature_color = signature_color


class TemplateSignerInputTypeField(str, Enum):
    SIGNATURE = 'signature'
    DATE = 'date'
    TEXT = 'text'
    CHECKBOX = 'checkbox'
    ATTACHMENT = 'attachment'
    RADIO = 'radio'
    DROPDOWN = 'dropdown'


class TemplateSignerInputContentTypeField(str, Enum):
    SIGNATURE = 'signature'
    INITIAL = 'initial'
    STAMP = 'stamp'
    DATE = 'date'
    CHECKBOX = 'checkbox'
    TEXT = 'text'
    FULL_NAME = 'full_name'
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    COMPANY = 'company'
    TITLE = 'title'
    EMAIL = 'email'
    ATTACHMENT = 'attachment'
    RADIO = 'radio'
    DROPDOWN = 'dropdown'


class TemplateSignerInputCoordinatesField(BaseObject):
    def __init__(self, x: Optional[float] = None, y: Optional[float] = None, **kwargs):
        """
        :param x: Relative x coordinate to the page the input is on, ranging from 0 to 1.
        :type x: Optional[float], optional
        :param y: Relative y coordinate to the page the input is on, ranging from 0 to 1.
        :type y: Optional[float], optional
        """
        super().__init__(**kwargs)
        self.x = x
        self.y = y


class TemplateSignerInputDimensionsField(BaseObject):
    def __init__(
        self, width: Optional[float] = None, height: Optional[float] = None, **kwargs
    ):
        """
        :param width: Relative width to the page the input is on, ranging from 0 to 1.
        :type width: Optional[float], optional
        :param height: Relative height to the page the input is on, ranging from 0 to 1.
        :type height: Optional[float], optional
        """
        super().__init__(**kwargs)
        self.width = width
        self.height = height


class TemplateSignerInput(SignRequestPrefillTag):
    def __init__(
        self,
        page_index: int,
        type: Optional[TemplateSignerInputTypeField] = None,
        content_type: Optional[TemplateSignerInputContentTypeField] = None,
        is_required: Optional[bool] = None,
        document_id: Optional[str] = None,
        dropdown_choices: Optional[List[str]] = None,
        group_id: Optional[str] = None,
        coordinates: Optional[TemplateSignerInputCoordinatesField] = None,
        dimensions: Optional[TemplateSignerInputDimensionsField] = None,
        label: Optional[str] = None,
        document_tag_id: Optional[str] = None,
        text_value: Optional[str] = None,
        checkbox_value: Optional[bool] = None,
        date_value: Optional[str] = None,
        **kwargs
    ):
        """
        :param page_index: Index of page that the input is on.
        :type page_index: int
        :param type: Type of input
        :type type: Optional[TemplateSignerInputTypeField], optional
        :param content_type: Content type of input
        :type content_type: Optional[TemplateSignerInputContentTypeField], optional
        :param is_required: Whether or not the input is required.
        :type is_required: Optional[bool], optional
        :param document_id: Document identifier.
        :type document_id: Optional[str], optional
        :param dropdown_choices: When the input is of the type `dropdown` this values will be filled with all the dropdown options.
        :type dropdown_choices: Optional[List[str]], optional
        :param group_id: When the input is of type `radio` they can be grouped to gather with this identifier.
        :type group_id: Optional[str], optional
        :param coordinates: Where the input is located on a page.
        :type coordinates: Optional[TemplateSignerInputCoordinatesField], optional
        :param dimensions: The size of the input.
        :type dimensions: Optional[TemplateSignerInputDimensionsField], optional
        :param label: The label field is used especially for text, attachment, radio, and checkbox type inputs.
        :type label: Optional[str], optional
        :param document_tag_id: This references the ID of a specific tag contained in a file of the sign request.
        :type document_tag_id: Optional[str], optional
        :param text_value: Text prefill value
        :type text_value: Optional[str], optional
        :param checkbox_value: Checkbox prefill value
        :type checkbox_value: Optional[bool], optional
        :param date_value: Date prefill value
        :type date_value: Optional[str], optional
        """
        super().__init__(
            document_tag_id=document_tag_id,
            text_value=text_value,
            checkbox_value=checkbox_value,
            date_value=date_value,
            **kwargs
        )
        self.page_index = page_index
        self.type = type
        self.content_type = content_type
        self.is_required = is_required
        self.document_id = document_id
        self.dropdown_choices = dropdown_choices
        self.group_id = group_id
        self.coordinates = coordinates
        self.dimensions = dimensions
        self.label = label


class TemplateSignerRoleField(str, Enum):
    SIGNER = 'signer'
    APPROVER = 'approver'
    FINAL_COPY_READER = 'final_copy_reader'


class TemplateSigner(BaseObject):
    def __init__(
        self,
        inputs: Optional[List[TemplateSignerInput]] = None,
        email: Optional[str] = None,
        role: Optional[TemplateSignerRoleField] = None,
        is_in_person: Optional[bool] = None,
        order: Optional[int] = None,
        **kwargs
    ):
        """
        :param email: Email address of the signer
        :type email: Optional[str], optional
        :param role: Defines the role of the signer in the signature request. A role of
            `signer` needs to sign the document, a role `approver`
            approves the document and
            a `final_copy_reader` role only
            receives the final signed document and signing log.
        :type role: Optional[TemplateSignerRoleField], optional
        :param is_in_person: Used in combination with an embed URL for a sender.
            After the sender signs, they will be
            redirected to the next `in_person` signer.
        :type is_in_person: Optional[bool], optional
        :param order: Order of the signer
        :type order: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.inputs = inputs
        self.email = email
        self.role = role
        self.is_in_person = is_in_person
        self.order = order


class SignTemplateTypeField(str, Enum):
    SIGN_TEMPLATE = 'sign-template'


class SignTemplateAdditionalInfoFieldNonEditableField(str, Enum):
    EMAIL_SUBJECT = 'email_subject'
    EMAIL_MESSAGE = 'email_message'
    NAME = 'name'
    DAYS_VALID = 'days_valid'
    SIGNERS = 'signers'
    SOURCE_FILES = 'source_files'


class SignTemplateAdditionalInfoFieldRequiredFieldSignersField(str, Enum):
    EMAIL = 'email'


class SignTemplateAdditionalInfoFieldRequiredField(BaseObject):
    def __init__(
        self,
        signers: Optional[
            List[List[SignTemplateAdditionalInfoFieldRequiredFieldSignersField]]
        ] = None,
        **kwargs
    ):
        """
        :param signers: Required signer fields.
        :type signers: Optional[List[List[SignTemplateAdditionalInfoFieldRequiredFieldSignersField]]], optional
        """
        super().__init__(**kwargs)
        self.signers = signers


class SignTemplateAdditionalInfoField(BaseObject):
    def __init__(
        self,
        non_editable: Optional[
            List[SignTemplateAdditionalInfoFieldNonEditableField]
        ] = None,
        required: Optional[SignTemplateAdditionalInfoFieldRequiredField] = None,
        **kwargs
    ):
        """
        :param non_editable: Non editable fields.
        :type non_editable: Optional[List[SignTemplateAdditionalInfoFieldNonEditableField]], optional
        :param required: Required fields.
        :type required: Optional[SignTemplateAdditionalInfoFieldRequiredField], optional
        """
        super().__init__(**kwargs)
        self.non_editable = non_editable
        self.required = required


class SignTemplateReadySignLinkField(BaseObject):
    def __init__(
        self,
        url: Optional[str] = None,
        name: Optional[str] = None,
        instructions: Optional[str] = None,
        folder_id: Optional[str] = None,
        is_notification_disabled: Optional[bool] = None,
        is_active: Optional[bool] = None,
        **kwargs
    ):
        """
        :param url: The URL that can be sent to signers.
        :type url: Optional[str], optional
        :param name: Request name.
        :type name: Optional[str], optional
        :param instructions: Extra instructions for all signers.
        :type instructions: Optional[str], optional
        :param folder_id: The destination folder to place final,
            signed document and signing
            log. Only `ID` and `type` fields are required.
            The root folder,
            folder ID `0`, cannot be used.
        :type folder_id: Optional[str], optional
        :param is_notification_disabled: Whether to disable notifications when
            a signer has signed.
        :type is_notification_disabled: Optional[bool], optional
        :param is_active: Whether the ready sign link is enabled or not.
        :type is_active: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.url = url
        self.name = name
        self.instructions = instructions
        self.folder_id = folder_id
        self.is_notification_disabled = is_notification_disabled
        self.is_active = is_active


class SignTemplateCustomBrandingField(BaseObject):
    def __init__(
        self,
        company_name: Optional[str] = None,
        logo_uri: Optional[str] = None,
        branding_color: Optional[str] = None,
        email_footer_text: Optional[str] = None,
        **kwargs
    ):
        """
        :param company_name: Name of the company
        :type company_name: Optional[str], optional
        :param logo_uri: Custom branding logo URI in the form of a base64 image.
        :type logo_uri: Optional[str], optional
        :param branding_color: Custom branding color in hex.
        :type branding_color: Optional[str], optional
        :param email_footer_text: Content of the email footer.
        :type email_footer_text: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.company_name = company_name
        self.logo_uri = logo_uri
        self.branding_color = branding_color
        self.email_footer_text = email_footer_text


class SignTemplate(BaseObject):
    def __init__(
        self,
        type: Optional[SignTemplateTypeField] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        email_subject: Optional[str] = None,
        email_message: Optional[str] = None,
        days_valid: Optional[int] = None,
        parent_folder: Optional[FolderMini] = None,
        source_files: Optional[List[FileMini]] = None,
        are_fields_locked: Optional[bool] = None,
        are_options_locked: Optional[bool] = None,
        are_recipients_locked: Optional[bool] = None,
        are_email_settings_locked: Optional[bool] = None,
        are_files_locked: Optional[bool] = None,
        signers: Optional[List[TemplateSigner]] = None,
        additional_info: Optional[SignTemplateAdditionalInfoField] = None,
        ready_sign_link: Optional[SignTemplateReadySignLinkField] = None,
        custom_branding: Optional[SignTemplateCustomBrandingField] = None,
        **kwargs
    ):
        """
        :param type: object type
        :type type: Optional[SignTemplateTypeField], optional
        :param id: Template identifier.
        :type id: Optional[str], optional
        :param name: The name of the template.
        :type name: Optional[str], optional
        :param email_subject: Subject of signature request email. This is cleaned by sign request. If this field is not passed, a default subject will be used.
        :type email_subject: Optional[str], optional
        :param email_message: Message to include in signature request email. The field is cleaned through sanitization of specific characters. However, some html tags are allowed. Links included in the message are also converted to hyperlinks in the email. The message may contain the following html tags including `a`, `abbr`, `acronym`, `b`, `blockquote`, `code`, `em`, `i`, `ul`, `li`, `ol`, and `strong`. Be aware that when the text to html ratio is too high, the email may end up in spam filters. Custom styles on these tags are not allowed. If this field is not passed, a default message will be used.
        :type email_message: Optional[str], optional
        :param days_valid: Set the number of days after which the created signature request will automatically expire if not completed. By default, we do not apply any expiration date on signature requests, and the signature request does not expire.
        :type days_valid: Optional[int], optional
        :param source_files: List of files to create a signing document from. Only the ID and type fields are required for each file.
        :type source_files: Optional[List[FileMini]], optional
        :param are_fields_locked: Indicates if the template input fields are editable or not.
        :type are_fields_locked: Optional[bool], optional
        :param are_options_locked: Indicates if the template document options are editable or not, for example renaming the document.
        :type are_options_locked: Optional[bool], optional
        :param are_recipients_locked: Indicates if the template signers are editable or not.
        :type are_recipients_locked: Optional[bool], optional
        :param are_email_settings_locked: Indicates if the template email settings are editable or not.
        :type are_email_settings_locked: Optional[bool], optional
        :param are_files_locked: Indicates if the template files are editable or not. This includes deleting or renaming template files.
        :type are_files_locked: Optional[bool], optional
        :param signers: Array of signers for the template.
        :type signers: Optional[List[TemplateSigner]], optional
        :param additional_info: Additional information on which fields are required and which fields are not editable.
        :type additional_info: Optional[SignTemplateAdditionalInfoField], optional
        :param ready_sign_link: Box's ready-sign link feature enables you to create a link to a signature request that you've created from a template. Use this link when you want to post a signature request on a public form — such as an email, social media post, or web page — without knowing who the signers will be. Note: The ready-sign link feature is limited to Enterprise Plus customers and not available to Box Verified Enterprises.
        :type ready_sign_link: Optional[SignTemplateReadySignLinkField], optional
        :param custom_branding: Custom branding applied to notifications
            and signature requests.
        :type custom_branding: Optional[SignTemplateCustomBrandingField], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id
        self.name = name
        self.email_subject = email_subject
        self.email_message = email_message
        self.days_valid = days_valid
        self.parent_folder = parent_folder
        self.source_files = source_files
        self.are_fields_locked = are_fields_locked
        self.are_options_locked = are_options_locked
        self.are_recipients_locked = are_recipients_locked
        self.are_email_settings_locked = are_email_settings_locked
        self.are_files_locked = are_files_locked
        self.signers = signers
        self.additional_info = additional_info
        self.ready_sign_link = ready_sign_link
        self.custom_branding = custom_branding


class SignTemplates(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        prev_marker: Optional[str] = None,
        entries: Optional[List[SignTemplate]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        :param prev_marker: The marker for the start of the previous page of results.
        :type prev_marker: Optional[str], optional
        :param entries: A list of templates.
        :type entries: Optional[List[SignTemplate]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.prev_marker = prev_marker
        self.entries = entries


class ShieldInformationBarrierReportDetailsDetailsField(BaseObject):
    def __init__(self, folder_id: Optional[str] = None, **kwargs):
        """
        :param folder_id: Folder ID for locating this report
        :type folder_id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.folder_id = folder_id


class ShieldInformationBarrierReportDetails(BaseObject):
    def __init__(
        self,
        details: Optional[ShieldInformationBarrierReportDetailsDetailsField] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.details = details


class ShieldInformationBarrierReportStatusField(str, Enum):
    PENDING = 'pending'
    ERROR = 'error'
    DONE = 'done'
    CANCELLED = 'cancelled'


class ShieldInformationBarrierReport(ShieldInformationBarrierReportBase):
    def __init__(
        self,
        shield_information_barrier: Optional[ShieldInformationBarrierReference] = None,
        status: Optional[ShieldInformationBarrierReportStatusField] = None,
        details: Optional[ShieldInformationBarrierReportDetails] = None,
        created_at: Optional[str] = None,
        created_by: Optional[UserBase] = None,
        updated_at: Optional[str] = None,
        id: Optional[str] = None,
        type: Optional[ShieldInformationBarrierReportBaseTypeField] = None,
        **kwargs
    ):
        """
        :param status: Status of the shield information report
        :type status: Optional[ShieldInformationBarrierReportStatusField], optional
        :param created_at: ISO date time string when this
            shield information barrier report object was created.
        :type created_at: Optional[str], optional
        :param updated_at: ISO date time string when this
            shield information barrier report was updated.
        :type updated_at: Optional[str], optional
        :param id: The unique identifier for the shield information barrier report
        :type id: Optional[str], optional
        :param type: The type of the shield information barrier report
        :type type: Optional[ShieldInformationBarrierReportBaseTypeField], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.shield_information_barrier = shield_information_barrier
        self.status = status
        self.details = details
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at


class ShieldInformationBarrierReports(BaseObject):
    def __init__(
        self,
        limit: Optional[int] = None,
        next_marker: Optional[str] = None,
        entries: Optional[List[ShieldInformationBarrierReport]] = None,
        **kwargs
    ):
        """
        :param limit: The limit that was used for these entries. This will be the same as the
            `limit` query parameter unless that value exceeded the maximum value
            allowed. The maximum value varies by API.
        :type limit: Optional[int], optional
        :param next_marker: The marker for the start of the next page of results.
        :type next_marker: Optional[str], optional
        :param entries: A list of shield information
            barrier reports.
        :type entries: Optional[List[ShieldInformationBarrierReport]], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.next_marker = next_marker
        self.entries = entries


class TrackingCodeTypeField(str, Enum):
    TRACKING_CODE = 'tracking_code'


class TrackingCode(BaseObject):
    def __init__(
        self,
        type: Optional[TrackingCodeTypeField] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: `tracking_code`
        :type type: Optional[TrackingCodeTypeField], optional
        :param name: The name of the tracking code, which must be preconfigured in
            the Admin Console
        :type name: Optional[str], optional
        :param value: The value of the tracking code
        :type value: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.name = name
        self.value = value


class UserFullRoleField(str, Enum):
    ADMIN = 'admin'
    COADMIN = 'coadmin'
    USER = 'user'


class UserFullEnterpriseFieldTypeField(str, Enum):
    ENTERPRISE = 'enterprise'


class UserFullEnterpriseField(BaseObject):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[UserFullEnterpriseFieldTypeField] = None,
        name: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this enterprise.
        :type id: Optional[str], optional
        :param type: `enterprise`
        :type type: Optional[UserFullEnterpriseFieldTypeField], optional
        :param name: The name of the enterprise
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name


class UserFull(User):
    def __init__(
        self,
        id: str,
        type: UserBaseTypeField,
        role: Optional[UserFullRoleField] = None,
        tracking_codes: Optional[List[TrackingCode]] = None,
        can_see_managed_users: Optional[bool] = None,
        is_sync_enabled: Optional[bool] = None,
        is_external_collab_restricted: Optional[bool] = None,
        is_exempt_from_device_limits: Optional[bool] = None,
        is_exempt_from_login_verification: Optional[bool] = None,
        enterprise: Optional[UserFullEnterpriseField] = None,
        my_tags: Optional[List[str]] = None,
        hostname: Optional[str] = None,
        is_platform_access_only: Optional[bool] = None,
        external_app_user_id: Optional[str] = None,
        created_at: Optional[str] = None,
        modified_at: Optional[str] = None,
        language: Optional[str] = None,
        timezone: Optional[str] = None,
        space_amount: Optional[int] = None,
        space_used: Optional[int] = None,
        max_upload_size: Optional[int] = None,
        status: Optional[UserStatusField] = None,
        job_title: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None,
        avatar_url: Optional[str] = None,
        notification_email: Optional[UserNotificationEmailField] = None,
        name: Optional[str] = None,
        login: Optional[str] = None,
        **kwargs
    ):
        """
        :param id: The unique identifier for this user
        :type id: str
        :param type: `user`
        :type type: UserBaseTypeField
        :param role: The user’s enterprise role
        :type role: Optional[UserFullRoleField], optional
        :param tracking_codes: Tracking codes allow an admin to generate reports from the
            admin console and assign an attribute to a specific group
            of users. This setting must be enabled for an enterprise
            before it can be used.
        :type tracking_codes: Optional[List[TrackingCode]], optional
        :param can_see_managed_users: Whether the user can see other enterprise users in their contact list
        :type can_see_managed_users: Optional[bool], optional
        :param is_sync_enabled: Whether the user can use Box Sync
        :type is_sync_enabled: Optional[bool], optional
        :param is_external_collab_restricted: Whether the user is allowed to collaborate with users outside their
            enterprise
        :type is_external_collab_restricted: Optional[bool], optional
        :param is_exempt_from_device_limits: Whether to exempt the user from Enterprise device limits
        :type is_exempt_from_device_limits: Optional[bool], optional
        :param is_exempt_from_login_verification: Whether the user must use two-factor authentication
        :type is_exempt_from_login_verification: Optional[bool], optional
        :param my_tags: Tags for all files and folders owned by the user. Values returned
            will only contain tags that were set by the requester.
        :type my_tags: Optional[List[str]], optional
        :param hostname: The root (protocol, subdomain, domain) of any links that need to be
            generated for the user
        :type hostname: Optional[str], optional
        :param is_platform_access_only: Whether the user is an App User
        :type is_platform_access_only: Optional[bool], optional
        :param external_app_user_id: An external identifier for an app user, which can be used to look up
            the user. This can be used to tie user IDs from external identity
            providers to Box users.
        :type external_app_user_id: Optional[str], optional
        :param created_at: When the user object was created
        :type created_at: Optional[str], optional
        :param modified_at: When the user object was last modified
        :type modified_at: Optional[str], optional
        :param language: The language of the user, formatted in modified version of the
            [ISO 639-1](/guides/api-calls/language-codes) format.
        :type language: Optional[str], optional
        :param timezone: The user's timezone
        :type timezone: Optional[str], optional
        :param space_amount: The user’s total available space amount in bytes
        :type space_amount: Optional[int], optional
        :param space_used: The amount of space in use by the user
        :type space_used: Optional[int], optional
        :param max_upload_size: The maximum individual file size in bytes the user can have
        :type max_upload_size: Optional[int], optional
        :param status: The user's account status
        :type status: Optional[UserStatusField], optional
        :param job_title: The user’s job title
        :type job_title: Optional[str], optional
        :param phone: The user’s phone number
        :type phone: Optional[str], optional
        :param address: The user’s address
        :type address: Optional[str], optional
        :param avatar_url: URL of the user’s avatar image
        :type avatar_url: Optional[str], optional
        :param notification_email: An alternate notification email address to which email
            notifications are sent. When it's confirmed, this will be
            the email address to which notifications are sent instead of
            to the primary email address.
        :type notification_email: Optional[UserNotificationEmailField], optional
        :param name: The display name of this user
        :type name: Optional[str], optional
        :param login: The primary email address of this user
        :type login: Optional[str], optional
        """
        super().__init__(
            id=id,
            type=type,
            created_at=created_at,
            modified_at=modified_at,
            language=language,
            timezone=timezone,
            space_amount=space_amount,
            space_used=space_used,
            max_upload_size=max_upload_size,
            status=status,
            job_title=job_title,
            phone=phone,
            address=address,
            avatar_url=avatar_url,
            notification_email=notification_email,
            name=name,
            login=login,
            **kwargs
        )
        self.role = role
        self.tracking_codes = tracking_codes
        self.can_see_managed_users = can_see_managed_users
        self.is_sync_enabled = is_sync_enabled
        self.is_external_collab_restricted = is_external_collab_restricted
        self.is_exempt_from_device_limits = is_exempt_from_device_limits
        self.is_exempt_from_login_verification = is_exempt_from_login_verification
        self.enterprise = enterprise
        self.my_tags = my_tags
        self.hostname = hostname
        self.is_platform_access_only = is_platform_access_only
        self.external_app_user_id = external_app_user_id


class MetadataFieldFilterString(BaseObject):
    pass


class MetadataFieldFilterFloat(BaseObject):
    pass


class MetadataFieldFilterMultiSelect(BaseObject):
    pass


class MetadataFieldFilterFloatRangeMapValue(BaseObject):
    def __init__(
        self, lt: Optional[float] = None, gt: Optional[float] = None, **kwargs
    ):
        """
        :param lt: Specifies the (inclusive) upper bound for the metadata field
            value. The value of a field must be lower than (`lt`) or
            equal to this value for the search query to match this
            template.
        :type lt: Optional[float], optional
        :param gt: Specifies the (inclusive) lower bound for the metadata field
            value. The value of a field must be greater than (`gt`) or
            equal to this value for the search query to match this
            template.
        :type gt: Optional[float], optional
        """
        super().__init__(**kwargs)
        self.lt = lt
        self.gt = gt


class MetadataFieldFilterFloatRange(BaseObject):
    pass


class MetadataFieldFilterDateRangeMapValue(BaseObject):
    def __init__(self, lt: Optional[str] = None, gt: Optional[str] = None, **kwargs):
        """
        :param lt: Specifies the (inclusive) upper bound for the metadata field
            value. The value of a field must be lower than (`lt`) or
            equal to this value for the search query to match this
            template.
        :type lt: Optional[str], optional
        :param gt: Specifies the (inclusive) lower bound for the metadata field
            value. The value of a field must be greater than (`gt`) or
            equal to this value for the search query to match this
            template.
        :type gt: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.lt = lt
        self.gt = gt


class MetadataFieldFilterDateRange(BaseObject):
    pass


class MetadataFilterScopeField(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'
    ENTERPRISE__ENTERPRISE_ID_ = 'enterprise_{enterprise_id}'


class MetadataFilter(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'template_key': 'templateKey',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'templateKey': 'template_key',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        scope: Optional[MetadataFilterScopeField] = None,
        template_key: Optional[str] = None,
        filters: Optional[
            Union[
                MetadataFieldFilterString,
                MetadataFieldFilterFloat,
                MetadataFieldFilterMultiSelect,
                MetadataFieldFilterFloatRange,
                MetadataFieldFilterDateRange,
            ]
        ] = None,
        **kwargs
    ):
        """
        :param scope: Specifies the scope of the template to filter search results by.
            This will be `enterprise_{enterprise_id}` for templates defined
            for use in this enterprise, and `global` for general templates
            that are available to all enterprises using Box.
        :type scope: Optional[MetadataFilterScopeField], optional
        :param template_key: The key of the template to filter search results by.
            In many cases the template key is automatically derived
            of its display name, for example `Contract Template` would
            become `contractTemplate`. In some cases the creator of the
            template will have provided its own template key.
            Please [list the templates for an enterprise][list], or
            get all instances on a [file][file] or [folder][folder]
            to inspect a template's key.
            [list]: e://get-metadata-templates-enterprise
            [file]: e://get-files-id-metadata
            [folder]: e://get-folders-id-metadata
        :type template_key: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.scope = scope
        self.template_key = template_key
        self.filters = filters
