from box_sdk_gen.schemas import Collections

from box_sdk_gen.schemas import Collection

from box_sdk_gen.schemas import Items

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParentArg

from box_sdk_gen.managers.folders import UpdateFolderByIdCollectionsArg

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import BoxClient

from box_sdk_gen.jwt_auth import BoxJWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
)

auth: BoxJWTAuth = BoxJWTAuth(config=jwt_config)

client: BoxClient = BoxClient(auth=auth)


def testCollections():
    collections: Collections = client.collections.get_collections()
    favourite_collection: Collection = collections.entries[0]
    collection_items: Items = client.collections.get_collection_items(
        collection_id=favourite_collection.id
    )
    folder: FolderFull = client.folders.create_folder(
        name=get_uuid(), parent=CreateFolderParentArg(id='0')
    )
    client.folders.update_folder_by_id(
        folder_id=folder.id,
        collections=[UpdateFolderByIdCollectionsArg(id=favourite_collection.id)],
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
