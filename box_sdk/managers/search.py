from box_sdk.base_object import BaseObject

from enum import Enum

from typing import Optional

from typing import List

from typing import Union

from typing import Dict

import json

from box_sdk.schemas import MetadataQueryResults

from box_sdk.schemas import ClientError

from box_sdk.schemas import MetadataQuery

from box_sdk.schemas import MetadataQueryIndices

from box_sdk.schemas import SearchResults

from box_sdk.schemas import SearchResultsWithSharedLinks

from box_sdk.schemas import MetadataFilter

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import prepare_params

from box_sdk.utils import to_string

from box_sdk.utils import ByteStream

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateMetadataQueryExecuteReadQueryParamsArg(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class GetMetadataQueryIndicesScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class GetSearchScopeArg(str, Enum):
    USER_CONTENT = 'user_content'
    ENTERPRISE_CONTENT = 'enterprise_content'

class GetSearchTypeArg(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'
    WEB_LINK = 'web_link'

class GetSearchTrashContentArg(str, Enum):
    NON_TRASHED_ONLY = 'non_trashed_only'
    TRASHED_ONLY = 'trashed_only'
    ALL_ITEMS = 'all_items'

class GetSearchSortArg(str, Enum):
    MODIFIED_AT = 'modified_at'
    RELEVANCE = 'relevance'

class GetSearchDirectionArg(str, Enum):
    DESC = 'DESC'
    ASC = 'ASC'

class SearchManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def create_metadata_query_execute_read(self, from_: str, ancestor_folder_id: str, query: Optional[str] = None, query_params: Optional[CreateMetadataQueryExecuteReadQueryParamsArg] = None, order_by: Optional[List] = None, limit: Optional[int] = None, marker: Optional[str] = None, fields: Optional[List[str]] = None, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> MetadataQueryResults:
        """
        Create a search using SQL-like syntax to return items that match specific
        
        metadata.

        
        By default, this endpoint returns only the most basic info about the items for

        
        which the query matches. To get additional fields for each item, including any

        
        of the metadata, use the `fields` attribute in the query.

        :param from_: Specifies the template used in the query. Must be in the form
            `scope.templateKey`. Not all templates can be used in this field,
            most notably the built-in, Box-provided classification templates
            can not be used in a query.
        :type from_: str
        :param ancestor_folder_id: The ID of the folder that you are restricting the query to. A
            value of zero will return results from all folders you have access
            to. A non-zero value will only return results found in the folder
            corresponding to the ID or in any of its subfolders.
        :type ancestor_folder_id: str
        :param query: The query to perform. A query is a logical expression that is very similar
            to a SQL `SELECT` statement. Values in the search query can be turned into
            parameters specified in the `query_param` arguments list to prevent having
            to manually insert search values into the query string.
            For example, a value of `:amount` would represent the `amount` value in
            `query_params` object.
        :type query: Optional[str], optional
        :param query_params: Set of arguments corresponding to the parameters specified in the
            `query`. The type of each parameter used in the `query_params` must match
            the type of the corresponding metadata template field.
        :type query_params: Optional[CreateMetadataQueryExecuteReadQueryParamsArg], optional
        :param order_by: A list of template fields and directions to sort the metadata query
            results by.
            The ordering `direction` must be the same for each item in the array.
        :type order_by: Optional[List], optional
        :param limit: A value between 0 and 100 that indicates the maximum number of results
            to return for a single request. This only specifies a maximum
            boundary and will not guarantee the minimum number of results
            returned.
        :type limit: Optional[int], optional
        :param marker: Marker to use for requesting the next page.
        :type marker: Optional[str], optional
        :param fields: By default, this endpoint returns only the most basic info about the items for
            which the query matches. This attribute can be used to specify a list of
            additional attributes to return for any item, including its metadata.
            This attribute takes a list of item fields, metadata template identifiers,
            or metadata template field identifiers.
            For example:
            * `created_by` will add the details of the user who created the item to
            the response.
            * `metadata.<scope>.<templateKey>` will return the mini-representation
            of the metadata instance identified by the `scope` and `templateKey`.
            * `metadata.<scope>.<templateKey>.<field>` will return all the mini-representation
            of the metadata instance identified by the `scope` and `templateKey` plus
            the field specified by the `field` name. Multiple fields for the same
            `scope` and `templateKey` can be defined.
        :type fields: Optional[List[str]], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: MetadataQuery = MetadataQuery(from_=from_, query=query, query_params=query_params, ancestor_folder_id=ancestor_folder_id, order_by=order_by, limit=limit, marker=marker, fields=fields)
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_queries/execute_read']), FetchOptions(method='POST', headers=headers_map, body=json.dumps(request_body.to_dict()), content_type='application/json', response_format='json', auth=self.auth, network_session=self.network_session))
        return MetadataQueryResults.from_dict(json.loads(response.text))
    def get_metadata_query_indices(self, scope: GetMetadataQueryIndicesScopeArg, template_key: str, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> MetadataQueryIndices:
        """
        Retrieves the metadata query indices for a given scope and template key.
        :param scope: The scope of the metadata template
        :type scope: GetMetadataQueryIndicesScopeArg
        :param template_key: The name of the metadata template
        :type template_key: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({'scope': to_string(scope), 'template_key': to_string(template_key)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_query_indices']), FetchOptions(method='GET', params=query_params_map, headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return MetadataQueryIndices.from_dict(json.loads(response.text))
    def get_search(self, query: Optional[str] = None, scope: Optional[GetSearchScopeArg] = None, file_extensions: Optional[str] = None, created_at_range: Optional[str] = None, updated_at_range: Optional[str] = None, size_range: Optional[str] = None, owner_user_ids: Optional[str] = None, recent_updater_user_ids: Optional[str] = None, ancestor_folder_ids: Optional[str] = None, content_types: Optional[str] = None, type: Optional[GetSearchTypeArg] = None, trash_content: Optional[GetSearchTrashContentArg] = None, mdfilters: Optional[str] = None, sort: Optional[GetSearchSortArg] = None, direction: Optional[GetSearchDirectionArg] = None, limit: Optional[int] = None, include_recent_shared_links: Optional[bool] = None, fields: Optional[str] = None, offset: Optional[int] = None, deleted_user_ids: Optional[str] = None, deleted_at_range: Optional[str] = None, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> None:
        """
        Searches for files, folders, web links, and shared files across the
        
        users content or across the entire enterprise.

        :param query: The string to search for. This query is matched against item names,
            descriptions, text content of files, and various other fields of
            the different item types.
            This parameter supports a variety of operators to further refine
            the results returns.
            * `""` - by wrapping a query in double quotes only exact matches are
              returned by the API. Exact searches do not return search matches
              based on specific character sequences. Instead, they return
              matches based on phrases, that is, word sequences. For example:
              A search for `"Blue-Box"` may return search results including
              the sequence `"blue.box"`, `"Blue Box"`, and `"Blue-Box"`;
              any item containing the words `Blue` and `Box` consecutively, in
              the order specified.
            * `AND` - returns items that contain both the search terms. For
              example, a search for `marketing AND BoxWorks` returns items
              that have both `marketing` and `BoxWorks` within its text in any order.
              It does not return a result that only has `BoxWorks` in its text.
            * `OR` - returns items that contain either of the search terms. For
              example, a search for `marketing OR BoxWorks` returns a result that
              has either `marketing` or `BoxWorks` within its text. Using this
              operator is not necessary as we implicitly interpret multi-word
              queries as `OR` unless another supported boolean term is used.
            * `NOT` - returns items that do not contain the search term provided.
              For example, a search for `marketing AND NOT BoxWorks` returns a result
              that has only `marketing` within its text. Results containing
              `BoxWorks` are omitted.
            We do not support lower case (that is,
            `and`, `or`, and `not`) or mixed case (that is, `And`, `Or`, and `Not`)
            operators.
            This field is required unless the `mdfilters` parameter is defined.
        :type query: Optional[str], optional
        :param scope: Limits the search results to either the files that the user has
            access to, or to files available to the entire enterprise.
            The scope defaults to `user_content`, which limits the search
            results to content that is available to the currently authenticated
            user.
            The `enterprise_content` can be requested by an admin through our
            support channels. Once this scope has been enabled for a user, it
            will allow that use to query for content across the entire
            enterprise and not only the content that they have access to.
        :type scope: Optional[GetSearchScopeArg], optional
        :param file_extensions: Limits the search results to any files that match any of the provided
            file extensions. This list is a comma-separated list of file extensions
            without the dots.
        :type file_extensions: Optional[str], optional
        :param created_at_range: Limits the search results to any items created within
            a given date range.
            Date ranges are defined as comma separated RFC3339
            timestamps.
            If the the start date is omitted (`,2014-05-17T13:35:01-07:00`)
            anything created before the end date will be returned.
            If the end date is omitted (`2014-05-15T13:35:01-07:00,`) the
            current date will be used as the end date instead.
        :type created_at_range: Optional[str], optional
        :param updated_at_range: Limits the search results to any items updated within
            a given date range.
            Date ranges are defined as comma separated RFC3339
            timestamps.
            If the start date is omitted (`,2014-05-17T13:35:01-07:00`)
            anything updated before the end date will be returned.
            If the end date is omitted (`2014-05-15T13:35:01-07:00,`) the
            current date will be used as the end date instead.
        :type updated_at_range: Optional[str], optional
        :param size_range: Limits the search results to any items with a size within
            a given file size range. This applied to files and folders.
            Size ranges are defined as comma separated list of a lower
            and upper byte size limit (inclusive).
            The upper and lower bound can be omitted to create open ranges.
        :type size_range: Optional[str], optional
        :param owner_user_ids: Limits the search results to any items that are owned
            by the given list of owners, defined as a list of comma separated
            user IDs.
            The items still need to be owned or shared with
            the currently authenticated user for them to show up in the search
            results. If the user does not have access to any files owned by any of
            the users an empty result set will be returned.
            To search across an entire enterprise, we recommend using the
            `enterprise_content` scope parameter which can be requested with our
            support team.
        :type owner_user_ids: Optional[str], optional
        :param recent_updater_user_ids: Limits the search results to any items that have been updated
            by the given list of users, defined as a list of comma separated
            user IDs.
            The items still need to be owned or shared with
            the currently authenticated user for them to show up in the search
            results. If the user does not have access to any files owned by any of
            the users an empty result set will be returned.
            This feature only searches back to the last 10 versions of an item.
        :type recent_updater_user_ids: Optional[str], optional
        :param ancestor_folder_ids: Limits the search results to items within the given
            list of folders, defined as a comma separated lists
            of folder IDs.
            Search results will also include items within any subfolders
            of those ancestor folders.
            The folders still need to be owned or shared with
            the currently authenticated user. If the folder is not accessible by this
            user, or it does not exist, a `HTTP 404` error code will be returned
            instead.
            To search across an entire enterprise, we recommend using the
            `enterprise_content` scope parameter which can be requested with our
            support team.
        :type ancestor_folder_ids: Optional[str], optional
        :param content_types: Limits the search results to any items that match the search query
            for a specific part of the file, for example the file description.
            Content types are defined as a comma separated lists
            of Box recognized content types. The allowed content types are as follows.
            * `name` - The name of the item, as defined by its `name` field.
            * `description` - The description of the item, as defined by its
              `description` field.
            * `file_content` - The actual content of the file.
            * `comments` - The content of any of the comments on a file or
               folder.
            * `tags` - Any tags that are applied to an item, as defined by its
               `tags` field.
        :type content_types: Optional[str], optional
        :param type: Limits the search results to any items of this type. This
            parameter only takes one value. By default the API returns
            items that match any of these types.
            * `file` - Limits the search results to files
            * `folder` - Limits the search results to folders
            * `web_link` - Limits the search results to web links, also known
               as bookmarks
        :type type: Optional[GetSearchTypeArg], optional
        :param trash_content: Determines if the search should look in the trash for items.
            By default, this API only returns search results for items
            not currently in the trash (`non_trashed_only`).
            * `trashed_only` - Only searches for items currently in the trash
            * `non_trashed_only` - Only searches for items currently not in
              the trash
            * `all_items` - Searches for both trashed and non-trashed items.
        :type trash_content: Optional[GetSearchTrashContentArg], optional
        :param mdfilters: Limits the search results to any items for which the metadata matches
            the provided filter.
            This parameter contains a list of 1 metadata template to filter
            the search results by. This list can currently only
            contain one entry, though this might be expanded in the future.
            This parameter is required unless the `query` parameter is provided.
        :type mdfilters: Optional[str], optional
        :param sort: Defines the order in which search results are returned. This API
            defaults to returning items by relevance unless this parameter is
            explicitly specified.
            * `relevance` (default) returns the results sorted by relevance to the
            query search term. The relevance is based on the occurrence of the search
            term in the items name, description, content, and additional properties.
            * `modified_at` returns the results ordered in descending order by date
            at which the item was last modified.
        :type sort: Optional[GetSearchSortArg], optional
        :param direction: Defines the direction in which search results are ordered. This API
            defaults to returning items in descending (`DESC`) order unless this
            parameter is explicitly specified.
            When results are sorted by `relevance` the ordering is locked to returning
            items in descending order of relevance, and this parameter is ignored.
        :type direction: Optional[GetSearchDirectionArg], optional
        :param limit: Defines the maximum number of items to return as part of a page of
            results.
        :type limit: Optional[int], optional
        :param include_recent_shared_links: Defines whether the search results should include any items
            that the user recently accessed through a shared link.
            When this parameter has been set to true,
            the format of the response of this API changes to return
            a list of [Search Results with
            Shared Links](r://search_results_with_shared_links)
        :type include_recent_shared_links: Optional[bool], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        :param deleted_user_ids: Limits the search results to items that were deleted by the given
            list of users, defined as a list of comma separated user IDs.
            The `trash_content` parameter needs to be set to `trashed_only`.
            If searching in trash is not performed, an empty result set
            is returned. The items need to be owned or shared with
            the currently authenticated user for them to show up in the search
            results.
            If the user does not have access to any files owned by
            any of the users, an empty result set is returned.
            Data available from 2023-02-01 onwards.
        :type deleted_user_ids: Optional[str], optional
        :param deleted_at_range: Limits the search results to any items deleted within a given
            date range.
            Date ranges are defined as comma separated RFC3339 timestamps.
            If the the start date is omitted (`2014-05-17T13:35:01-07:00`),
            anything deleted before the end date will be returned.
            If the end date is omitted (`2014-05-15T13:35:01-07:00`),
            the current date will be used as the end date instead.
            The `trash_content` parameter needs to be set to `trashed_only`.
            If searching in trash is not performed, then an empty result
            is returned.
            Data available from 2023-02-01 onwards.
        :type deleted_at_range: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({'query': to_string(query), 'scope': to_string(scope), 'file_extensions': to_string(file_extensions), 'created_at_range': to_string(created_at_range), 'updated_at_range': to_string(updated_at_range), 'size_range': to_string(size_range), 'owner_user_ids': to_string(owner_user_ids), 'recent_updater_user_ids': to_string(recent_updater_user_ids), 'ancestor_folder_ids': to_string(ancestor_folder_ids), 'content_types': to_string(content_types), 'type': to_string(type), 'trash_content': to_string(trash_content), 'mdfilters': to_string(mdfilters), 'sort': to_string(sort), 'direction': to_string(direction), 'limit': to_string(limit), 'include_recent_shared_links': to_string(include_recent_shared_links), 'fields': to_string(fields), 'offset': to_string(offset), 'deleted_user_ids': to_string(deleted_user_ids), 'deleted_at_range': to_string(deleted_at_range)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/search']), FetchOptions(method='GET', params=query_params_map, headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return None