# Folders

Folder objects represent a folder from a user's account. They can be used to
iterate through a folder's contents and perform other common folder operations (move, copy, delete, etc.).

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Get Information About a Folder](#get-information-about-a-folder)
  - [Get the User's Root Folder Information](#get-the-users-root-folder-information)
  - [Getting additional fields](#getting-additional-fields)
- [Get the Items in a Folder](#get-the-items-in-a-folder)
- [Create a Folder](#create-a-folder)
- [Update a Folder](#update-a-folder)
- [Copy a Folder](#copy-a-folder)
- [Move a Folder](#move-a-folder)
- [Rename a Folder](#rename-a-folder)
- [Delete a Folder](#delete-a-folder)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Get Information About a Folder

To retrieve information about a folder, call:

```python
from box_sdk.schemas import FolderFull

folder: FolderFull = client.folders.get_folder_by_id(folder_id='12345')
print(f'Folder with id {folder.id} has name {folder.name}')
```

`get_folder_by_id` method returns a new `FolderFull` object with fields populated by data from the API.
The default response object will contain only fields specified in `Folder` class.

## Get the User's Root Folder Information

To get the current user's root folder, call `get_folder_by_id` with `folder_id` set to '0'.

```python
root_folder = client.folders.get_folder_by_id(folder_id='0')
```

## Getting additional fields

If you want the response object to contain additional fields that are not return by default, you should pass a list of
such fields in a comma-separated string

```python
from box_sdk.schemas import FolderFull

folder: FolderFull = client.folders.get_folder_by_id(folder_id='12345', fields='has_collaborations,tags')
```

NOTE: Be aware that specifying `fields` parameter will have the effect that none of the standard fields
are returned in the response unless explicitly specified, instead only fields defined in `FolderBase`
are returned, additional to the fields requested.

# Get the Items in a Folder

To retrieve the items in a folder, call `get_folder_items` method. It returns a `Items` object
that exposes list of items inside a folder with field `entries`.

```python
from box_sdk.schemas import Items

items: Items = client.folders.get_folder_items('12345')
for item in items.entries:
    print(f'{item.type.capitalize()} {item.id} is named "{item.name}"')
```

# Create a Folder

A folder can be created by calling `create_folder` method with required request body parameters.
This method returns a new `FolderFull` representing the created subfolder.

```python
from box_sdk.managers.folders import CreateFolderParentArg

subfolder = client.folders.create_folder(name='New Folder Name', parent=CreateFolderParentArg(id='0'))
print(f'Created subfolder with ID {subfolder.id}')
```

# Update a Folder

To update a folder's information, call `update_folder_by_id` method with new values of properties
to update on the folder. This method returns an updated `FolderFull` object.

<!-- sample put_folders_id -->

```python
updated_folder = client.folders.update_folder_by_id(
  folder_id='12345',
  name='Updated folder name',
  description='Updated description'
)
print(f'Folder with ID {updated_folder.id} new name: {updated_folder.name}')
```

# Copy a Folder

A folder can be copied into a new parent folder by calling `copy_folder` with the
destination folder and an optional new name for the file in case there is a name conflict in the destination folder.
This method returns a new `FolderFull` object representing the copy of the folder in the destination folder.

<!-- sample post_folders_id_copy -->

```python
from box_sdk.managers.folders import CopyFolderParentArg

folder_id = '22222'
destination_folder_id = '44444'

folder_copy = client.folders.copy_folder(
  folder_id=folder_id,
  parent=CopyFolderParentArg(id=destination_folder_id),
  name='Copied folder name'
)

print(f'Folder "{folder_copy.name}" has been copied into folder "{folder_copy.parent.name}"')
```

# Move a Folder

To move a folder from one parent folder into another, call `update_folder_by_id` and pass `parent` field to specify
destination folder to move the folder into. You can optionally provide a `name` parameter to automatically rename the
folder in case of a name conflict in the destination folder. This method returns the updated `FolderFull` object.

```python
from box_sdk.managers.folders import CopyFolderParentArg

folder_id = '11111'
destination_folder_id = '44444'

moved_folder = client.folders.update_folder_by_id(
  folder_id=folder_id,
  parent=CopyFolderParentArg(id=destination_folder_id),
  name='Moved folder new name'
)
print(f'Folder "{moved_folder.name}" has been moved into folder "{moved_folder.parent.name}"')
```

# Rename a Folder

A folder can be renamed by calling `update_folder_by_id` method and passing a new folder name.
This method returns the updated `FolderFull` object with a new name.

```python
updated_folder = client.folders.update_folder_by_id(
  folder_id=folder_id,
  name='Updated folder name'
)

print(f'Folder "{updated_folder.id}" has a new name "{updated_folder.name}"')
```

# Delete a Folder

Calling the `delete_folder_by_id` method will delete the folder. Depending on enterprise settings,
this will either move the folder to the user's trash or permanently delete the folder.

```python
client.folders.delete_folder_by_id('12345')
```

By default, the method will not delete the folder when folder is not empty. To delete the folder with all its content
set the `recursive` parameter to `True`.

```python
client.folders.delete_folder_by_id(
    folder_id='12345',
    recursive=True
)
print('Folder with id: 12345 was successfully deleted')
```
