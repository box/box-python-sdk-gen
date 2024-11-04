from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas.collections import Collections

from box_sdk_gen.schemas.collection import Collection

from box_sdk_gen.schemas.items import Items

from box_sdk_gen.schemas.folder_full import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParent

from box_sdk_gen.managers.folders import UpdateFolderByIdCollections

from box_sdk_gen.internal.utils import get_uuid

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testCollections():
    collections: Collections = client.collections.get_collections()
    favourite_collection: Collection = client.collections.get_collection_by_id(
        collections.entries[0].id
    )
    assert to_string(favourite_collection.type) == 'collection'
    assert to_string(favourite_collection.collection_type) == 'favorites'
    collection_items: Items = client.collections.get_collection_items(
        favourite_collection.id
    )
    folder: FolderFull = client.folders.create_folder(
        get_uuid(), CreateFolderParent(id='0')
    )
    client.folders.update_folder_by_id(
        folder.id, collections=[UpdateFolderByIdCollections(id=favourite_collection.id)]
    )
    collection_items_after_update: Items = client.collections.get_collection_items(
        favourite_collection.id
    )
    assert (
        len(collection_items_after_update.entries) == len(collection_items.entries) + 1
    )
    client.folders.update_folder_by_id(folder.id, collections=[])
    collection_items_after_remove: Items = client.collections.get_collection_items(
        favourite_collection.id
    )
    assert len(collection_items_after_remove.entries) == len(collection_items.entries)
    client.folders.delete_folder_by_id(folder.id)
