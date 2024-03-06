from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.schemas import SignRequest

from box_sdk_gen.schemas import FileBase

from box_sdk_gen.schemas import FileBaseTypeField

from box_sdk_gen.schemas import SignRequestCreateSigner

from box_sdk_gen.schemas import FolderMini

from box_sdk_gen.schemas import FolderBaseTypeField

from box_sdk_gen.schemas import SignRequests

from box_sdk_gen.internal.utils import get_uuid

from test.commons import upload_new_file

from test.commons import create_new_folder

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testCreateGetCancelAndListSignRequest():
    signer_email: str = ''.join([get_uuid(), '@box.com'])
    file_to_sign: FileFull = upload_new_file()
    destination_folder: FolderFull = create_new_folder()
    created_sign_request: SignRequest = client.sign_requests.create_sign_request(
        [SignRequestCreateSigner(email=signer_email)],
        source_files=[FileBase(id=file_to_sign.id, type=FileBaseTypeField.FILE.value)],
        parent_folder=FolderMini(
            id=destination_folder.id, type=FolderBaseTypeField.FOLDER.value
        ),
    )
    assert created_sign_request.sign_files.files[0].name == file_to_sign.name
    assert created_sign_request.signers[1].email == signer_email
    assert created_sign_request.parent_folder.id == destination_folder.id
    new_sign_request: SignRequest = client.sign_requests.get_sign_request_by_id(
        created_sign_request.id
    )
    assert new_sign_request.sign_files.files[0].name == file_to_sign.name
    assert new_sign_request.signers[1].email == signer_email
    assert new_sign_request.parent_folder.id == destination_folder.id
    cancelled_sign_request: SignRequest = client.sign_requests.cancel_sign_request(
        created_sign_request.id
    )
    assert to_string(cancelled_sign_request.status) == 'cancelled'
    sign_requests: SignRequests = client.sign_requests.get_sign_requests()
    assert to_string(sign_requests.entries[0].type) == 'sign-request'
    client.folders.delete_folder_by_id(destination_folder.id, recursive=True)
    client.files.delete_file_by_id(file_to_sign.id)


def testCreateSignRequestWithSignerGroupId():
    signer_1_email: str = ''.join([get_uuid(), '@box.com'])
    signer_2_email: str = ''.join([get_uuid(), '@box.com'])
    file_to_sign: FileFull = upload_new_file()
    destination_folder: FolderFull = create_new_folder()
    created_sign_request: SignRequest = client.sign_requests.create_sign_request(
        [
            SignRequestCreateSigner(email=signer_1_email, signer_group_id='user'),
            SignRequestCreateSigner(email=signer_2_email, signer_group_id='user'),
        ],
        source_files=[FileBase(id=file_to_sign.id, type=FileBaseTypeField.FILE.value)],
        parent_folder=FolderMini(
            id=destination_folder.id, type=FolderBaseTypeField.FOLDER.value
        ),
    )
    assert len(created_sign_request.signers) == 3
    assert (
        created_sign_request.signers[1].signer_group_id
        == created_sign_request.signers[2].signer_group_id
    )
    client.folders.delete_folder_by_id(destination_folder.id, recursive=True)
    client.files.delete_file_by_id(file_to_sign.id)
