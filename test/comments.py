import pytest

from box_sdk.managers.uploads import UploadFileAttributesArg

from box_sdk.managers.uploads import UploadFileAttributesArgParentField

from box_sdk.managers.comments import CreateCommentItemArg

from box_sdk.managers.comments import CreateCommentItemArgTypeField

from box_sdk.utils import decode_base_64

from box_sdk.utils import generate_byte_stream

from box_sdk.utils import get_env_var

from box_sdk.utils import get_uuid

from box_sdk.client import Client

from box_sdk.jwt_auth import JWTAuth

from box_sdk.jwt_auth import JWTConfig

def comments():
    jwt_config: JWTConfig = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))
    auth: JWTAuth = JWTAuth(config=jwt_config)
    client: Client = Client(auth=auth)
    file_size: int = 256
    file_name: str = get_uuid()
    file_byte_stream: ByteStream = generate_byte_stream(file_size)
    parent_id: str = '0'
    uploaded_files: Files = client.uploads.upload_file(attributes=UploadFileAttributesArg(name=file_name, parent=UploadFileAttributesArgParentField(id=parent_id)), file=file_byte_stream)
    file_id: Files = uploaded_files.entries[0].id
    comments: Comments = client.comments.get_file_comments(file_id=file_id)
    assert comments.total_count == 0
    message: str = 'Hello there!'
    new_comment: Comment = client.comments.create_comment(message=message, item=CreateCommentItemArg(id=file_id, type=CreateCommentItemArgTypeField.FILE.value))
    assert new_comment.message == message
    assert new_comment.is_reply_comment == False
    assert new_comment.item.id == file_id
    new_reply_comment: Comment = client.comments.create_comment(message=message, item=CreateCommentItemArg(id=new_comment.id, type=CreateCommentItemArgTypeField.COMMENT.value))
    assert new_reply_comment.message == message
    assert new_reply_comment.is_reply_comment == True
    new_message: str = 'Hi!'
    client.comments.update_comment_by_id(comment_id=new_reply_comment.id, message=new_message)
    new_comments: Comments = client.comments.get_file_comments(file_id=file_id)
    assert new_comments.total_count == 2
    assert new_comments.entries[1].message == new_message
    assert not client.comments.get_comment_by_id(comment_id=new_comment.id) == None
    client.comments.delete_comment_by_id(new_comment.id)
    with pytest.raises(Exception):
        client.comments.get_comment_by_id(comment_id=new_comment.id)
    client.files.delete_file_by_id(file_id=file_id)