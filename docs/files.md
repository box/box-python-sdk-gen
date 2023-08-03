# Files

File objects represent individual files in Box. They can be used to download a
file's contents, upload new versions, and perform other common file operations
(move, copy, delete, etc.).

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Get a File's Information](#get-a-files-information)
  - [Getting additional fields](#getting-additional-fields)
- [Update a File's Information](#update-a-files-information)
- [Copy a File](#copy-a-file)
- [Delete a File](#delete-a-file)
- [Restore a File from Trash](#restore-a-file-from-trash)
- [Get Thumbnail](#get-thumbnail)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Get a File's Information

To retreive information about a File, call `get_file_by_id` method. This method returns a `File` object which contains information about the file.

<!-- sample get_files_id -->

```python
from box_sdk_gen.schemas import FileFull

file: FileFull = client.files.get_file_by_id(file_id='123456789')
print(f'File with id {file.id} has name {file.name}')
```

### Getting additional fields

If you want the response object to contain additional fields that are not return by default, you should pass a list of
such fields in a comma-separated string

```python
from box_sdk_gen.schemas import FileFull

file: FileFull = client.files.get_file_by_id(file_id='12345', fields='is_externally_owned,has_collaborations')
```

NOTE: Be aware that specifying `fields` parameter will have the effect that none of the standard fields
are returned in the response unless explicitly specified, instead only fields defined in `FileBase`
are returned, additional to the fields requested.

## Update a File's Information

To update a file's information, call `update_file_by_id` method. This method returns a `File` object which contains information about the file.

<!-- sample put_files_id -->

```python
from box_sdk_gen.schemas import FileFull

file: FileFull = client.files.update_file_by_id(file_id='123', name='test.txt', description='Test file')
print(f'File with id {file.id} has new name {file.name}')
```

## Copy a File

To copy a file to a new location, call `copy_file` method.
You need to specify the `parent` field in the request body, which is the destination folder and optionally the `name` field which is the new name of the file.
This method returns a `File` object which contains information about the copied file.

<!-- sample post_files_id_copy -->

```python
from box_sdk_gen.managers.files import CopyFileParentArg
from box_sdk_gen.schemas import FileFull


file: FileFull = client.files.copy_file(
    file_id='123456789',
    parent=CopyFileParentArg(id='0'),
    name='test_copy.txt'
)
print(f'File copied with id {file.id}, name {file.name}')
```

## Delete a File

To delete a file, call `delete_file_by_id` method. If the file is successfully deleted, this method returns `None`. Otherwise, it raises an exception.

<!-- sample delete_files_id -->

```python
client.files.delete_file_by_id(file_id='123456789')
```

## Restore a File from Trash

To restore a file from trash, call `restore_file_from_trash` method.
This method returns a `TrashFileRestored` object which contains information about the restored file.

<!-- sample post_files_id -->

```python
from box_sdk_gen.schemas import TrashFileRestored

file: TrashFileRestored = client.files.restore_file_from_trash(file_id='123456789')
print(f'File restored with id {file.id}, name {file.name}')
```

## Get Thumbnail

To retrieve a thumbnail for a file, call `get_file_thumbnail_by_id` method. This method returns a `ByteStream` object,
which is an implementation of `io.BufferedIOBase`, which contains the thumbnail data in the specified format.

Optionally, you can specify the information about the thumbnail you want to retrieve,
including the `max_height`, `max_width`, `min_height`, `min_width`.

To save downloaded thumbnail to your local disk you can use e.g. `shutil.copyfileobj()` method:

<!-- sample get_files_id_thumbnail_id -->

```python
import shutil
from box_sdk_gen.managers.files import GetFileThumbnailByIdExtensionArg
from box_sdk_gen.utils import ByteStream

thumbnail: ByteStream = client.files.get_file_thumbnail_by_id(
    file_id='1199932968894',
    extension=GetFileThumbnailByIdExtensionArg.PNG,
    min_height=256,
    min_width=256,
    max_height=256,
    max_width=256,
)
with open('thumbnail.png', 'wb') as f:
    shutil.copyfileobj(thumbnail, f)
```
