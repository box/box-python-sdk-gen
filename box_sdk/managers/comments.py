from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

import json

from box_sdk.schemas import Comments

from box_sdk.schemas import ClientError

from box_sdk.schemas import Comment

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetFilesIdCommentsOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, limit: Union[None, int] = None, offset: Union[None, int] = None, **kwargs):
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
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.limit = limit
        self.offset = offset

class GetCommentsIdOptionsArg(BaseObject):
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

class PutCommentsIdRequestBodyArg(BaseObject):
    def __init__(self, message: Union[None, str] = None, **kwargs):
        """
        :param message: The text of the comment to update
        :type message: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.message = message

class PutCommentsIdOptionsArg(BaseObject):
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

class PostCommentsRequestBodyArgItemFieldTypeField(str, Enum):
    FILE = 'file'
    COMMENT = 'comment'

class PostCommentsRequestBodyArgItemField(BaseObject):
    def __init__(self, id: str, type: PostCommentsRequestBodyArgItemFieldTypeField, **kwargs):
        """
        :param id: The ID of the item
        :type id: str
        :param type: The type of the item that this comment will be placed on.
        :type type: PostCommentsRequestBodyArgItemFieldTypeField
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class PostCommentsRequestBodyArg(BaseObject):
    def __init__(self, message: str, tagged_message: Union[None, str] = None, item: Union[None, PostCommentsRequestBodyArgItemField] = None, **kwargs):
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
        :type tagged_message: Union[None, str], optional
        :param item: The item to attach the comment to.
        :type item: Union[None, PostCommentsRequestBodyArgItemField], optional
        """
        super().__init__(**kwargs)
        self.message = message
        self.tagged_message = tagged_message
        self.item = item

class PostCommentsOptionsArg(BaseObject):
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

class CommentsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_files_id_comments(self, file_id: str, options: GetFilesIdCommentsOptionsArg = None) -> Comments:
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
            options = GetFilesIdCommentsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/comments']), FetchOptions(method='GET', params={'fields': options.fields, 'limit': options.limit, 'offset': options.offset}, auth=self.auth))
        return Comments.from_dict(json.loads(response.text))
    def get_comments_id(self, comment_id: str, options: GetCommentsIdOptionsArg = None) -> Comment:
        """
        Retrieves the message and metadata for a specific comment, as well
        
        as information on the user who created the comment.

        :param comment_id: The ID of the comment.
            Example: "12345"
        :type comment_id: str
        """
        if options is None:
            options = GetCommentsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/comments/', comment_id]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return Comment.from_dict(json.loads(response.text))
    def put_comments_id(self, comment_id: str, request_body: PutCommentsIdRequestBodyArg, options: PutCommentsIdOptionsArg = None) -> Comment:
        """
        Update the message of a comment.
        :param comment_id: The ID of the comment.
            Example: "12345"
        :type comment_id: str
        """
        if options is None:
            options = PutCommentsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/comments/', comment_id]), FetchOptions(method='PUT', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), auth=self.auth))
        return Comment.from_dict(json.loads(response.text))
    def delete_comments_id(self, comment_id: str):
        """
        Permanently deletes a comment.
        :param comment_id: The ID of the comment.
            Example: "12345"
        :type comment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/comments/', comment_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def post_comments(self, request_body: PostCommentsRequestBodyArg, options: PostCommentsOptionsArg = None) -> Comment:
        """
        Adds a comment by the user to a specific file, or
        
        as a reply to an other comment.

        """
        if options is None:
            options = PostCommentsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/comments']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), auth=self.auth))
        return Comment.from_dict(json.loads(response.text))