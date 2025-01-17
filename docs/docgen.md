# DocgenManager

- [Get Box Doc Gen job by ID](#get-box-doc-gen-job-by-id)
- [List all Box Doc Gen jobs](#list-all-box-doc-gen-jobs)
- [Get Box Doc Gen jobs in a batch with a specific ID](#get-box-doc-gen-jobs-in-a-batch-with-a-specific-id)
- [Generate document using a Box Doc Gen template](#generate-document-using-a-box-doc-gen-template)

## Get Box Doc Gen job by ID

Get details of the Box Doc Gen job.

This operation is performed by calling function `get_docgen_job_by_id_v2025_r0`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-docgen-jobs-id-v2025.0/).

<!-- sample get_docgen_jobs_id_v2025.0 -->

```python
client.docgen.get_docgen_job_by_id_v2025_r0(docgen_jobs.entries[0].id)
```

### Arguments

- job_id `str`
  - Box Doc Gen job ID. Example: 123
- box_version `BoxVersionHeaderV2025R0`
  - Version header
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `DocGenJobV2025R0`.

Details of the Box Doc Gen job.

## List all Box Doc Gen jobs

Lists all Box Doc Gen jobs for a user.

This operation is performed by calling function `get_docgen_jobs_v2025_r0`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-docgen-jobs-v2025.0/).

<!-- sample get_docgen_jobs_v2025.0 -->

```python
client.docgen.get_docgen_jobs_v2025_r0()
```

### Arguments

- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination. This requires `usemarker` to be set to `true`.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- box_version `BoxVersionHeaderV2025R0`
  - Version header
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `DocGenJobsFullV2025R0`.

A list of Box Doc Gen jobs.

## Get Box Doc Gen jobs in a batch with a specific ID

Lists Box Doc Gen jobs in a batch

This operation is performed by calling function `get_docgen_batch_job_by_id_v2025_r0`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-docgen-batch-jobs-id-v2025.0/).

<!-- sample get_docgen_batch_jobs_id_v2025.0 -->

```python
client.docgen.get_docgen_batch_job_by_id_v2025_r0(docgen_batch.id)
```

### Arguments

- batch_id `str`
  - Box Doc Gen batch ID. Example: 123
- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination. This requires `usemarker` to be set to `true`.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- box_version `BoxVersionHeaderV2025R0`
  - Version header
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `DocGenJobsV2025R0`.

Returns a list of Box Doc Gen jobs in a Box Doc Gen batch.

## Generate document using a Box Doc Gen template

Generates a document using a Box Doc Gen template.

This operation is performed by calling function `create_docgen_batch_v2025_r0`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-docgen-batches-v2025.0/).

<!-- sample post_docgen_batches_v2025.0 -->

```python
client.docgen.create_docgen_batch_v2025_r0(
    FileReferenceV2025R0(id=uploaded_file.id),
    "api",
    CreateDocgenBatchV2025R0DestinationFolder(id=folder.id),
    "pdf",
    [
        DocGenDocumentGenerationDataV2025R0(
            generated_file_name="test", user_input={"abc": "xyz"}
        )
    ],
)
```

### Arguments

- file `FileReferenceV2025R0`
  -
- file_version `Optional[FileVersionBaseV2025R0]`
  -
- input_source `str`
  - Source of input. The value has to be `api` for all the API-based document generation requests.
- destination_folder `CreateDocgenBatchV2025R0DestinationFolder`
  -
- output_type `str`
  - Type of the output file.
- document_generation_data `List[DocGenDocumentGenerationDataV2025R0]`
  -
- box_version `BoxVersionHeaderV2025R0`
  - Version header
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `DocGenBatchBaseV2025R0`.

The created Batch ID.
