from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParentArg

from box_sdk_gen.schemas import File

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributesArg

from box_sdk_gen.managers.uploads import UploadFileAttributesArgParentField

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.client import BoxClient

from box_sdk_gen.jwt_auth import BoxJWTAuth

from box_sdk_gen.jwt_auth import JWTConfig


def get_jwt_auth() -> BoxJWTAuth:
    jwt_config: JWTConfig = JWTConfig.from_config_json_string(
        decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
    )
    auth: BoxJWTAuth = BoxJWTAuth(config=jwt_config)
    return auth


def get_default_client_as_user(user_id: str) -> BoxClient:
    auth: BoxJWTAuth = get_jwt_auth()
    auth.as_user(user_id)
    return BoxClient(auth=auth)


def get_default_client() -> BoxClient:
    client: BoxClient = BoxClient(auth=get_jwt_auth())
    return client


def create_new_folder() -> FolderFull:
    client: BoxClient = get_default_client()
    new_folder_name: str = get_uuid()
    return client.folders.create_folder(
        name=new_folder_name, parent=CreateFolderParentArg(id='0')
    )


def upload_new_file() -> File:
    client: BoxClient = get_default_client()
    new_file_name: str = ''.join([get_uuid(), '.pdf'])
    file_content_stream: ByteStream = generate_byte_stream(1024 * 1024)
    uploaded_files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributesArg(
            name=new_file_name, parent=UploadFileAttributesArgParentField(id='0')
        ),
        file=file_content_stream,
    )
    return uploaded_files.entries[0]
