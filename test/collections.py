from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import Collections

from box_sdk_gen.schemas import Collection

from box_sdk_gen.schemas import Items

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParent

from box_sdk_gen.managers.folders import UpdateFolderByIdCollections

from box_sdk_gen.internal.utils import get_uuid

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testCollections():
    collections: Collections = client.collections.get_collections()
    favourite_collection: Collection = collections.entries[0]
    collection_items: Items = client.collections.get_collection_items(
        collection_id=favourite_collection.id
    )
    folder: FolderFull = client.folders.create_folder(
        name=get_uuid(), parent=CreateFolderParent(id='0')
    )
    client.folders.update_folder_by_id(
        folder_id=folder.id,
        collections=[UpdateFolderByIdCollections(id=favourite_collection.id)],
    )
    collection_items_after_update: Items = client.collections.get_collection_items(
        collection_id=favourite_collection.id
    )
    assert (
        len(collection_items_after_update.entries) == len(collection_items.entries) + 1
    )
    client.folders.update_folder_by_id(folder_id=folder.id, collections=[])
    collection_items_after_remove: Items = client.collections.get_collection_items(
        collection_id=favourite_collection.id
    )
    assert len(collection_items_after_remove.entries) == len(collection_items.entries)
    client.folders.delete_folder_by_id(folder_id=folder.id)
