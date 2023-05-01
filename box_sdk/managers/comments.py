from typing import Optional

from box_sdk.base_object import BaseObject

from enum import Enum

from typing import Union

import json

from box_sdk.schemas import Comments

from box_sdk.schemas import ClientError

from box_sdk.schemas import CommentFull

from box_sdk.schemas import Comment

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetFileCommentsOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.limit = limit
        self.offset = offset

class GetCommentByIdOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class UpdateCommentByIdRequestBodyArg(BaseObject):
    def __init__(self, message: Optional[str] = None, **kwargs):
        """
        :param message: The text of the comment to update
        :type message: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.message = message

class UpdateCommentByIdOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class CreateCommentRequestBodyArgItemFieldTypeField(str, Enum):
    FILE = 'file'
    COMMENT = 'comment'

class CreateCommentRequestBodyArgItemField(BaseObject):
    def __init__(self, id: str, type: CreateCommentRequestBodyArgItemFieldTypeField, **kwargs):
        """
        :param id: The ID of the item
        :type id: str
        :param type: The type of the item that this comment will be placed on.
        :type type: CreateCommentRequestBodyArgItemFieldTypeField
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class CreateCommentRequestBodyArg(BaseObject):
    def __init__(self, message: str, tagged_message: Optional[str] = None, item: Optional[CreateCommentRequestBodyArgItemField] = None, **kwargs):
        """
        :param message: The text of the comment.
            To mention a user, use the `tagged_message`
            parameter instead.
        :type message: str
        :param tagged_message: The text of the comment, including `@[user_id:name]`
            somewhere in the message to mention another user, which
            will send them an email notification, letting them know
            they have been mentioned.
            The `user_id` is the target user's ID, where the `name`
            can be any custom phrase. In the Box UI this name will
            link to the user's profile.
            If you are not mentioning another user, use `message`
            instead.
        :type tagged_message: Optional[str], optional
        :param item: The item to attach the comment to.
        :type item: Optional[CreateCommentRequestBodyArgItemField], optional
        """
        super().__init__(**kwargs)
        self.message = message
        self.tagged_message = tagged_message
        self.item = item

class CreateCommentOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class CommentsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_file_comments(self, file_id: str, options: GetFileCommentsOptionsArg = None) -> Comments:
        """
        Retrieves a list of comments for a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        if options is None:
            options = GetFileCommentsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/comments']), FetchOptions(method='GET', params={'fields': options.fields, 'limit': options.limit, 'offset': options.offset}, auth=self.auth))
        return Comments.from_dict(json.loads(response.text))
    def get_comment_by_id(self, comment_id: str, options: GetCommentByIdOptionsArg = None) -> CommentFull:
        """
        Retrieves the message and metadata for a specific comment, as well
        
        as information on the user who created the comment.

        :param comment_id: The ID of the comment.
            Example: "12345"
        :type comment_id: str
        """
        if options is None:
            options = GetCommentByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/comments/', comment_id]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return CommentFull.from_dict(json.loads(response.text))
    def update_comment_by_id(self, comment_id: str, request_body: UpdateCommentByIdRequestBodyArg, options: UpdateCommentByIdOptionsArg = None) -> CommentFull:
        """
        Update the message of a comment.
        :param comment_id: The ID of the comment.
            Example: "12345"
        :type comment_id: str
        """
        if options is None:
            options = UpdateCommentByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/comments/', comment_id]), FetchOptions(method='PUT', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return CommentFull.from_dict(json.loads(response.text))
    def delete_comment_by_id(self, comment_id: str):
        """
        Permanently deletes a comment.
        :param comment_id: The ID of the comment.
            Example: "12345"
        :type comment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/comments/', comment_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def create_comment(self, request_body: CreateCommentRequestBodyArg, options: CreateCommentOptionsArg = None) -> Comment:
        """
        Adds a comment by the user to a specific file, or
        
        as a reply to an other comment.

        """
        if options is None:
            options = CreateCommentOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/comments']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return Comment.from_dict(json.loads(response.text))