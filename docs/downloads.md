# Downloads

Downloads module is used to download files from Box.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Download a File](#download-a-file)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Download a File

To get the entire contents of the file as stream of bytes, call `download_file` method.
This method returns a `ByteStream` object, which is an implementation of `io.BufferedIOBase`, what allows
reading downloaded file as a stream. Thanks to that, the file parts will be downloaded just when needed and
it won;t be necessary to store the entire file content in-memory.

To get the full content of the file in `bytes` format just call `read()` method on returned object.

```python
from box_sdk_gen import ByteStream

file_content_stream: ByteStream = client.downloads.download_file(file_id='123456789')
print('File content: ', file_content_stream.read())
```

To save downloaded file to your local disk you can use e.g. `shutil.copyfileobj()` method:

<!-- sample get_files_id_content -->

```python
import shutil
from box_sdk_gen import ByteStream

file_content_stream: ByteStream = client.downloads.download_file(file_id='123456789')
with open('file.pdf', 'wb') as f:
    shutil.copyfileobj(file_content_stream, f)
print('File was successfully downloaded as "file.pdf"')
```
