# Uploads

Uploads module is used to upload files to Box. It supports uploading files from a readable stream. For now, it only supports uploading small files without chunked upload.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Upload a File](#upload-a-file)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Upload a File

To upload a small file from a readable stream, call `upload_file` method.
This method returns a `Files` object which contains information about the uploaded files.

<!-- sample post_files_content -->

```python
from box_sdk_gen import UploadFileAttributesArg, UploadFileAttributesArgParentField

attrs = UploadFileAttributesArg(
    name='filename.txt',
    parent=UploadFileAttributesArgParentField(id='0')
)
files: File = client.uploads.upload_file(attributes=attrs, file=open('filename.txt', 'rb'))
file = files.entries[0]
print(f'File uploaded with id {file.id}, name {file.name}')
```
