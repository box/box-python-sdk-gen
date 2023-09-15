from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributesArg

from box_sdk_gen.managers.uploads import UploadFileAttributesArgParentField

from box_sdk_gen.schemas import File

from box_sdk_gen.managers.uploads import UploadFileVersionAttributesArg

from box_sdk_gen.schemas import FileVersions

from box_sdk_gen.schemas import FileVersionFull

from box_sdk_gen.managers.file_versions import PromoteFileVersionTypeArg

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.client import BoxClient

from box_sdk_gen.jwt_auth import BoxJWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
)

auth: BoxJWTAuth = BoxJWTAuth(config=jwt_config)

client: BoxClient = BoxClient(auth=auth)


def testCreateListGetRestoreDeleteFileVersion():
    old_name: str = get_uuid()
    new_name: str = get_uuid()
    files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributesArg(
            name=old_name, parent=UploadFileAttributesArgParentField(id='0')
        ),
        file=generate_byte_stream(10),
    )
    file: File = files.entries[0]
    assert file.name == old_name
    assert file.size == 10
    new_files: Files = client.uploads.upload_file_version(
        file_id=file.id,
        attributes=UploadFileVersionAttributesArg(name=new_name),
        file=generate_byte_stream(20),
    )
    new_file: File = new_files.entries[0]
    assert new_file.name == new_name
    assert new_file.size == 20
    file_versions: FileVersions = client.file_versions.get_file_versions(
        file_id=file.id
    )
    assert file_versions.total_count == 1
    file_version: FileVersionFull = client.file_versions.get_file_version_by_id(
        file_id=file.id, file_version_id=file_versions.entries[0].id
    )
    assert file_version.id == file_versions.entries[0].id
    client.file_versions.promote_file_version(
        file_id=file.id,
        id=file_versions.entries[0].id,
        type=PromoteFileVersionTypeArg.FILE_VERSION.value,
    )
    file_restored: FileFull = client.files.get_file_by_id(file_id=file.id)
    assert file_restored.name == old_name
    assert file_restored.size == 10
    file_versions_restored: FileVersions = client.file_versions.get_file_versions(
        file_id=file.id
    )
    client.file_versions.delete_file_version_by_id(
        file_id=file.id, file_version_id=file_versions_restored.entries[0].id
    )
    client.file_versions.get_file_versions(file_id=file.id)
    client.files.delete_file_by_id(file_id=file.id)
