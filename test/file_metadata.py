from typing import Dict

import pytest

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributesArg

from box_sdk_gen.managers.uploads import UploadFileAttributesArgParentField

from box_sdk_gen.schemas import Metadatas

from box_sdk_gen.schemas import Metadata

from box_sdk_gen.schemas import MetadataFull

from box_sdk_gen.managers.file_metadata import UpdateFileMetadataByIdRequestBodyArg

from box_sdk_gen.managers.file_metadata import (
    UpdateFileMetadataByIdRequestBodyArgOpField,
)

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import BoxClient

from box_sdk_gen.jwt_auth import BoxJWTAuth

from box_sdk_gen.jwt_auth import JWTConfig


def testFileMetadata():
    client: BoxClient = BoxClient(
        auth=BoxJWTAuth(
            config=JWTConfig.from_config_json_string(
                decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
            )
        )
    )
    uploaded_files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributesArg(
            name=get_uuid(), parent=UploadFileAttributesArgParentField(id='0')
        ),
        file=generate_byte_stream(256),
    )
    file_id: str = uploaded_files.entries[0].id
    file_metadata: Metadatas = client.file_metadata.get_file_metadata(file_id=file_id)
    assert len(file_metadata.entries) == 0
    scope: str = 'global'
    template: str = 'properties'
    data: Dict[str, str] = {'abc': 'xyz'}
    created_metadata: Metadata = client.file_metadata.create_file_metadata_by_id(
        file_id=file_id, scope=scope, template_key=template, request_body=data
    )
    assert created_metadata.template == template
    assert created_metadata.scope == scope
    assert created_metadata.version == 0
    received_metadata: MetadataFull = client.file_metadata.get_file_metadata_by_id(
        file_id=file_id, scope=scope, template_key=template
    )
    assert received_metadata.extra_data['abc'] == data['abc']
    new_value: str = 'bar'
    updated_metadata: Metadata = client.file_metadata.update_file_metadata_by_id(
        file_id=file_id,
        scope=scope,
        template_key=template,
        request_body=[
            UpdateFileMetadataByIdRequestBodyArg(
                op=UpdateFileMetadataByIdRequestBodyArgOpField.REPLACE.value,
                path='/abc',
                value=new_value,
            )
        ],
    )
    received_updated_metadata: MetadataFull = (
        client.file_metadata.get_file_metadata_by_id(
            file_id=file_id, scope=scope, template_key=template
        )
    )
    assert received_updated_metadata.extra_data['abc'] == new_value
    client.file_metadata.delete_file_metadata_by_id(
        file_id=file_id, scope=scope, template_key=template
    )
    with pytest.raises(Exception):
        client.file_metadata.get_file_metadata_by_id(
            file_id=file_id, scope=scope, template_key=template
        )
    client.files.delete_file_by_id(file_id=file_id)
