from typing import Union

from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import MetadataTemplate

from box_sdk_gen.managers.metadata_templates import CreateMetadataTemplateFields

from box_sdk_gen.managers.metadata_templates import (
    CreateMetadataTemplateFieldsTypeField,
)

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributes

from box_sdk_gen.managers.uploads import UploadFileAttributesParentField

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.schemas import MetadataFull

from box_sdk_gen.managers.file_metadata import CreateFileMetadataByIdScope

from box_sdk_gen.schemas import MetadataQueryResults

from box_sdk_gen.managers.metadata_templates import DeleteMetadataTemplateScope

from box_sdk_gen.schemas import SearchResults

from box_sdk_gen.schemas import SearchResultsWithSharedLinks

from box_sdk_gen.managers.search import SearchForContentTrashContent

from box_sdk_gen.managers.metadata_templates import (
    CreateMetadataTemplateFieldsOptionsField,
)

from box_sdk_gen.schemas import MetadataFilter

from box_sdk_gen.schemas import MetadataFilterScopeField

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import generate_byte_stream

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testCreateMetaDataQueryExecuteRead():
    template_key: str = ''.join(['key', get_uuid()])
    template: MetadataTemplate = client.metadata_templates.create_metadata_template(
        'enterprise',
        template_key,
        template_key=template_key,
        fields=[
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.FLOAT.value,
                key='testName',
                display_name='testName',
            )
        ],
    )
    assert template.template_key == template_key
    files: Files = client.uploads.upload_file(
        UploadFileAttributes(
            name=get_uuid(), parent=UploadFileAttributesParentField(id='0')
        ),
        generate_byte_stream(10),
    )
    file: FileFull = files.entries[0]
    metadata: MetadataFull = client.file_metadata.create_file_metadata_by_id(
        file.id,
        CreateFileMetadataByIdScope.ENTERPRISE.value,
        template_key,
        {'testName': 1},
    )
    assert metadata.template == template_key
    assert metadata.scope == template.scope
    search_from: str = ''.join([template.scope, '.', template.template_key])
    query: MetadataQueryResults = client.search.search_by_metadata_query(
        search_from, '0', query='testName >= :value', query_params={'value': '0.0'}
    )
    assert len(query.entries) >= 0
    client.metadata_templates.delete_metadata_template(
        DeleteMetadataTemplateScope.ENTERPRISE.value, template.template_key
    )
    client.files.delete_file_by_id(file.id)


def testGetSearch():
    keyword: str = 'test'
    search: Union[SearchResults, SearchResultsWithSharedLinks] = (
        client.search.search_for_content(
            query=keyword,
            ancestor_folder_ids=['0'],
            trash_content=SearchForContentTrashContent.NON_TRASHED_ONLY.value,
        )
    )
    assert len(search.entries) >= 0
    assert to_string(search.type) == 'search_results_items'
    search_with_shared_link: Union[SearchResults, SearchResultsWithSharedLinks] = (
        client.search.search_for_content(
            query=keyword,
            ancestor_folder_ids=['0'],
            trash_content=SearchForContentTrashContent.NON_TRASHED_ONLY.value,
            include_recent_shared_links=True,
        )
    )
    assert len(search_with_shared_link.entries) >= 0
    assert to_string(search_with_shared_link.type) == 'search_results_with_shared_links'


def testMetadataFilters():
    template_key: str = ''.join(['key', get_uuid()])
    template: MetadataTemplate = client.metadata_templates.create_metadata_template(
        'enterprise',
        template_key,
        template_key=template_key,
        fields=[
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.FLOAT.value,
                key='floatField',
                display_name='floatField',
            ),
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.STRING.value,
                key='stringField',
                display_name='stringField',
            ),
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.DATE.value,
                key='dateField',
                display_name='dateField',
            ),
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.ENUM.value,
                key='enumField',
                display_name='enumField',
                options=[
                    CreateMetadataTemplateFieldsOptionsField(key='enumValue1'),
                    CreateMetadataTemplateFieldsOptionsField(key='enumValue2'),
                ],
            ),
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.MULTISELECT.value,
                key='multiSelectField',
                display_name='multiSelectField',
                options=[
                    CreateMetadataTemplateFieldsOptionsField(key='multiSelectValue1'),
                    CreateMetadataTemplateFieldsOptionsField(key='multiSelectValue2'),
                ],
            ),
        ],
    )
    files: Files = client.uploads.upload_file(
        UploadFileAttributes(
            name=get_uuid(), parent=UploadFileAttributesParentField(id='0')
        ),
        generate_byte_stream(10),
    )
    file: FileFull = files.entries[0]
    metadata: MetadataFull = client.file_metadata.create_file_metadata_by_id(
        file.id,
        CreateFileMetadataByIdScope.ENTERPRISE.value,
        template_key,
        {
            'floatField': 10,
            'stringField': 'stringValue',
            'dateField': '2035-01-02T00:00:00Z',
            'enumField': 'enumValue2',
            'multiSelectField': ['multiSelectValue1', 'multiSelectValue2'],
        },
    )
    string_query: Union[SearchResults, SearchResultsWithSharedLinks] = (
        client.search.search_for_content(
            ancestor_folder_ids=['0'],
            mdfilters=[
                MetadataFilter(
                    filters={'stringField': 'stringValue'},
                    scope=MetadataFilterScopeField.ENTERPRISE.value,
                    template_key=template_key,
                )
            ],
        )
    )
    assert len(string_query.entries) >= 0
    enum_query: Union[SearchResults, SearchResultsWithSharedLinks] = (
        client.search.search_for_content(
            ancestor_folder_ids=['0'],
            mdfilters=[
                MetadataFilter(
                    filters={'enumField': 'enumValue2'},
                    scope=MetadataFilterScopeField.ENTERPRISE.value,
                    template_key=template_key,
                )
            ],
        )
    )
    assert len(enum_query.entries) >= 0
    multi_select_query: Union[SearchResults, SearchResultsWithSharedLinks] = (
        client.search.search_for_content(
            ancestor_folder_ids=['0'],
            mdfilters=[
                MetadataFilter(
                    filters={
                        'multiSelectField': ['multiSelectValue1', 'multiSelectValue2']
                    },
                    scope=MetadataFilterScopeField.ENTERPRISE.value,
                    template_key=template_key,
                )
            ],
        )
    )
    assert len(multi_select_query.entries) >= 0
    client.metadata_templates.delete_metadata_template(
        DeleteMetadataTemplateScope.ENTERPRISE.value, template.template_key
    )
    client.files.delete_file_by_id(file.id)
