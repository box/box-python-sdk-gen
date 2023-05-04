# Downloads

Downloads module is used to download files from Box.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Download a File](#download-a-file)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Download a File

To get the entire contents of the file as `bytes`, call `download_file` method.
This method returns a `bytes` object which contains the file content.

<!-- sample get_files_id_content -->

```python
file_content: bytes = client.downloads.download_file(file_id='123456789')
with open('file.pdf', 'wb') as f:
    f.write(file_content)
print('File was successfully downloaded as "file.pdf"')
```

Additionally, only a part of the file can be downloaded by specifying a byte range.

```python
from box_sdk.managers.downloads import DownloadFileOptionsArg

options = DownloadFileOptionsArg(range='bytes=0-100')
file_content: bytes = client.downloads.download_file(file_id='123456789', options=options)
print('File content size: ', len(file_content))
```
