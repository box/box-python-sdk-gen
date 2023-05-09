from box_sdk.utils import decode_base_64

from box_sdk.utils import get_env_var

from box_sdk.utils import get_uuid

from box_sdk.utils import generate_byte_stream

from box_sdk.managers.uploads import UploadFileRequestBodyArg

from box_sdk.managers.uploads import UploadFileRequestBodyArgAttributesField

from box_sdk.managers.uploads import UploadFileRequestBodyArgAttributesFieldParentField

from box_sdk.managers.folders import CreateFolderRequestBodyArg

from box_sdk.managers.folders import CreateFolderRequestBodyArgParentField

from box_sdk.client import Client

from box_sdk.jwt_auth import JWTAuth

from box_sdk.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def upload_new_file():
    new_file_name: str = ''.join([get_uuid(), '.pdf'])
    file_content_stream = generate_byte_stream()
    uploaded_files = client.uploads.upload_file(UploadFileRequestBodyArg(attributes=UploadFileRequestBodyArgAttributesField(name=new_file_name, parent=UploadFileRequestBodyArgAttributesFieldParentField(id='0')), file=file_content_stream))
    return uploaded_files.entries[0]

def create_new_folder():
    new_folder_name = get_uuid()
    return client.folders.create_folder(CreateFolderRequestBodyArg(name=new_folder_name, parent=CreateFolderRequestBodyArgParentField(id='0')))