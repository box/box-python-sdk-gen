import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParentArg

from box_sdk_gen.schemas import Watermark

from box_sdk_gen.managers.folder_watermarks import UpdateFolderWatermarkWatermarkArg

from box_sdk_gen.managers.folder_watermarks import (
    UpdateFolderWatermarkWatermarkArgImprintField,
)

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testCreateGetDeleteFolderWatermark():
    folder_name: str = get_uuid()
    folder: FolderFull = client.folders.create_folder(
        name=folder_name, parent=CreateFolderParentArg(id='0')
    )
    created_watermark: Watermark = client.folder_watermarks.update_folder_watermark(
        folder_id=folder.id,
        watermark=UpdateFolderWatermarkWatermarkArg(
            imprint=UpdateFolderWatermarkWatermarkArgImprintField.DEFAULT.value
        ),
    )
    watermark: Watermark = client.folder_watermarks.get_folder_watermark(
        folder_id=folder.id
    )
    client.folder_watermarks.delete_folder_watermark(folder_id=folder.id)
    with pytest.raises(Exception):
        client.folder_watermarks.get_folder_watermark(folder_id=folder.id)
    client.folders.delete_folder_by_id(folder_id=folder.id)
