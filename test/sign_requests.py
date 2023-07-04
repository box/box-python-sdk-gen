from box_sdk.schemas import FileBaseTypeField

from box_sdk.schemas import FolderBaseTypeField

from box_sdk.utils import decode_base_64

from box_sdk.utils import get_env_var

from box_sdk.utils import get_uuid

from test.commons import upload_new_file

from test.commons import create_new_folder

from box_sdk.schemas import SignRequestCreateRequest

from box_sdk.schemas import SignRequestCreateSigner

from box_sdk.schemas import FolderMini

from box_sdk.schemas import FileBase

from box_sdk.client import Client

from box_sdk.jwt_auth import JWTAuth

from box_sdk.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def test_create_get_cancel_and_list_sign_request():
    signer_email: str = ''.join([get_uuid(), '@box.com'])
    file_to_sign = upload_new_file()
    destination_folder = create_new_folder()
    created_sign_request: SignRequest = client.sign_requests.create_sign_request(source_files=[FileBase(id=file_to_sign.id, type=FileBaseTypeField.FILE.value)], signers=[SignRequestCreateSigner(email=signer_email)], parent_folder=FolderMini(id=destination_folder.id, type=FolderBaseTypeField.FOLDER.value))
    assert created_sign_request.sign_files.files[0].name == file_to_sign.name
    assert created_sign_request.signers[1].email == signer_email
    assert created_sign_request.parent_folder.id == destination_folder.id
    new_sign_request: SignRequest = client.sign_requests.get_sign_request_by_id(created_sign_request.id)
    assert new_sign_request.sign_files.files[0].name == file_to_sign.name
    assert new_sign_request.signers[1].email == signer_email
    assert new_sign_request.parent_folder.id == destination_folder.id
    cancelled_sign_request: SignRequest = client.sign_requests.cancel_sign_request(created_sign_request.id)
    assert cancelled_sign_request.status == 'cancelled'
    sign_requests: SignRequests = client.sign_requests.get_sign_requests()
    assert sign_requests.entries[0].type == 'sign-request'
    client.folders.delete_folder_by_id(folder_id=destination_folder.id, recursive=True)
    client.files.delete_file_by_id(file_id=file_to_sign.id)