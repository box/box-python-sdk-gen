from typing import Union

from box_sdk_gen.utils import to_string

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import MetadataTemplate

from box_sdk_gen.managers.metadata_templates import CreateMetadataTemplateFieldsArg

from box_sdk_gen.managers.metadata_templates import (
    CreateMetadataTemplateFieldsArgTypeField,
)

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributesArg

from box_sdk_gen.managers.uploads import UploadFileAttributesArgParentField

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.schemas import MetadataFull

from box_sdk_gen.managers.file_metadata import CreateFileMetadataByIdScopeArg

from box_sdk_gen.schemas import MetadataQueryResults

from box_sdk_gen.managers.metadata_templates import DeleteMetadataTemplateScopeArg

from box_sdk_gen.schemas import MetadataQueryIndices

from box_sdk_gen.managers.search import GetMetadataQueryIndicesScopeArg

from box_sdk_gen.managers.search import GetSearchTrashContentArg

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_stream

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testCreateMetaDataQueryExecuteRead():
    template_key: str = ''.join(['key', get_uuid()])
    template: MetadataTemplate = client.metadata_templates.create_metadata_template(
        scope='enterprise',
        template_key=template_key,
        display_name=template_key,
        fields=[
            CreateMetadataTemplateFieldsArg(
                type=CreateMetadataTemplateFieldsArgTypeField.FLOAT.value,
                key='testName',
                display_name='testName',
            )
        ],
    )
    assert template.template_key == template_key
    files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributesArg(
            name=get_uuid(), parent=UploadFileAttributesArgParentField(id='0')
        ),
        file=generate_byte_stream(10),
    )
    file: FileFull = files.entries[0]
    metadata: MetadataFull = client.file_metadata.create_file_metadata_by_id(
        file_id=file.id,
        scope=CreateFileMetadataByIdScopeArg.ENTERPRISE.value,
        template_key=template_key,
        request_body={'testName': 1},
    )
    assert metadata.template == template_key
    assert metadata.scope == template.scope
    search_from: str = ''.join([template.scope, '.', template.template_key])
    query: MetadataQueryResults = client.search.create_metadata_query_execute_read(
        from_=search_from,
        query='testName >= :value',
        query_params={'value': '0.0'},
        ancestor_folder_id='0',
    )
    assert len(query.entries) >= 0
    client.metadata_templates.delete_metadata_template(
        scope=DeleteMetadataTemplateScopeArg.ENTERPRISE.value,
        template_key=template.template_key,
    )
    client.files.delete_file_by_id(file_id=file.id)


def testGetMetadataQueryIndices():
    template_key: str = ''.join(['key', get_uuid()])
    template: MetadataTemplate = client.metadata_templates.create_metadata_template(
        scope='enterprise',
        template_key=template_key,
        display_name=template_key,
        fields=[
            CreateMetadataTemplateFieldsArg(
                type=CreateMetadataTemplateFieldsArgTypeField.STRING.value,
                key='testName',
                display_name='testName',
            )
        ],
    )
    assert template.template_key == template_key
    indices: MetadataQueryIndices = client.search.get_metadata_query_indices(
        scope=GetMetadataQueryIndicesScopeArg.ENTERPRISE.value,
        template_key=template_key,
    )
    assert len(indices.entries) >= 0
    client.metadata_templates.delete_metadata_template(
        scope=DeleteMetadataTemplateScopeArg.ENTERPRISE.value,
        template_key=template.template_key,
    )


def testGetSearch():
    keyword: str = 'test'
    search: Union[SearchResults, SearchResultsWithSharedLinks] = (
        client.search.get_search(
            query=keyword,
            ancestor_folder_ids=['0'],
            trash_content=GetSearchTrashContentArg.NON_TRASHED_ONLY.value,
        )
    )
    assert len(search.entries) >= 0
    assert to_string(search.type) == 'search_results_items'
    search_with_shared_link: Union[SearchResults, SearchResultsWithSharedLinks] = (
        client.search.get_search(
            query=keyword,
            ancestor_folder_ids=['0'],
            trash_content=GetSearchTrashContentArg.NON_TRASHED_ONLY.value,
            include_recent_shared_links=True,
        )
    )
    assert len(search_with_shared_link.entries) >= 0
    assert to_string(search_with_shared_link.type) == 'search_results_with_shared_links'
