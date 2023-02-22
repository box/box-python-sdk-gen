from enum import Enum

from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

import json

from fetch import fetch, FetchOptions, FetchResponse

from schemas import MetadataQueryResults

from schemas import ClientError

from schemas import MetadataQuery

from schemas import MetadataQueryIndices

from schemas import SearchResults

from schemas import SearchResultsWithSharedLinks

from schemas import MetadataFilter

class GetMetadataQueryIndicesScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'

class GetSearchOptionsArgScopeField(str, Enum):
    USER_CONTENT = 'user_content'
    ENTERPRISE_CONTENT = 'enterprise_content'

class GetSearchOptionsArgTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'
    WEB_LINK = 'web_link'

class GetSearchOptionsArgTrashContentField(str, Enum):
    NON_TRASHED_ONLY = 'non_trashed_only'
    TRASHED_ONLY = 'trashed_only'

class GetSearchOptionsArgSortField(str, Enum):
    MODIFIED_AT = 'modified_at'
    RELEVANCE = 'relevance'

class GetSearchOptionsArgDirectionField(str, Enum):
    DESC = 'DESC'
    ASC = 'ASC'

class GetSearchOptionsArg(BaseObject):
    def __init__(self, query: Union[None, str] = None, scope: Union[None, GetSearchOptionsArgScopeField] = None, fileExtensions: Union[None, str] = None, createdAtRange: Union[None, str] = None, updatedAtRange: Union[None, str] = None, sizeRange: Union[None, str] = None, ownerUserIds: Union[None, str] = None, recentUpdaterUserIds: Union[None, str] = None, ancestorFolderIds: Union[None, str] = None, contentTypes: Union[None, str] = None, type: Union[None, GetSearchOptionsArgTypeField] = None, trashContent: Union[None, GetSearchOptionsArgTrashContentField] = None, mdfilters: Union[None, str] = None, sort: Union[None, GetSearchOptionsArgSortField] = None, direction: Union[None, GetSearchOptionsArgDirectionField] = None, limit: Union[None, int] = None, includeRecentSharedLinks: Union[None, bool] = None, fields: Union[None, str] = None, offset: Union[None, int] = None, **kwargs):
        """
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
            Please note that we do not support lower case (that is,
            `and`, `or`, and `not`) or mixed case (that is, `And`, `Or`, and `Not`)
            operators.
            This field is required unless the `mdfilters` parameter is defined.
        :type query: Union[None, str], optional
        :param scope: Limits the search results to either the files that the user has
            access to, or to files available to the entire enterprise.
            The scope defaults to `user_content`, which limits the search
            results to content that is available to the currently authenticated
            user.
            The `enterprise_content` can be requested by an admin through our
            support channels. Once this scope has been enabled for a user, it
            will allow that use to query for content across the entire
            enterprise and not only the content that they have access to.
        :type scope: Union[None, GetSearchOptionsArgScopeField], optional
        :param fileExtensions: Limits the search results to any files that match any of the provided
            file extensions. This list is a comma-separated list of file extensions
            without the dots.
        :type fileExtensions: Union[None, str], optional
        :param createdAtRange: Limits the search results to any items created within
            a given date range.
            Date ranges are defined as comma separated RFC3339
            timestamps.
            If the the start date is omitted (`,2014-05-17T13:35:01-07:00`)
            anything created before the end date will be returned.
            If the end date is omitted (`2014-05-15T13:35:01-07:00,`) the
            current date will be used as the end date instead.
        :type createdAtRange: Union[None, str], optional
        :param updatedAtRange: Limits the search results to any items updated within
            a given date range.
            Date ranges are defined as comma separated RFC3339
            timestamps.
            If the start date is omitted (`,2014-05-17T13:35:01-07:00`)
            anything updated before the end date will be returned.
            If the end date is omitted (`2014-05-15T13:35:01-07:00,`) the
            current date will be used as the end date instead.
        :type updatedAtRange: Union[None, str], optional
        :param sizeRange: Limits the search results to any items with a size within
            a given file size range. This applied to files and folders.
            Size ranges are defined as comma separated list of a lower
            and upper byte size limit (inclusive).
            The upper and lower bound can be omitted to create open ranges.
        :type sizeRange: Union[None, str], optional
        :param ownerUserIds: Limits the search results to any items that are owned
            by the given list of owners, defined as a list of comma separated
            user IDs.
            Please note that the items still need to be owned or shared with
            the currently authenticated user for them to show up in the search
            results. If the user does not have access to any files owned by any of
            the users an empty result set will be returned.
            To search across an entire enterprise, we recommend using the
            `enterprise_content` scope parameter which can be requested with our
            support team.
        :type ownerUserIds: Union[None, str], optional
        :param recentUpdaterUserIds: Limits the search results to any items that have been updated
            by the given list of users, defined as a list of comma separated
            user IDs.
            Please note that the items still need to be owned or shared with
            the currently authenticated user for them to show up in the search
            results. If the user does not have access to any files owned by any of
            the users an empty result set will be returned.
            This feature only searches back to the last 10 versions of an item.
        :type recentUpdaterUserIds: Union[None, str], optional
        :param ancestorFolderIds: Limits the search results to items within the given
            list of folders, defined as a comma separated lists
            of folder IDs.
            Search results will also include items within any subfolders
            of those ancestor folders.
            Please note that the folders still need to be owned or shared with
            the currently authenticated user. If the folder is not accessible by this
            user, or it does not exist, a `HTTP 404` error code will be returned
            instead.
            To search across an entire enterprise, we recommend using the
            `enterprise_content` scope parameter which can be requested with our
            support team.
        :type ancestorFolderIds: Union[None, str], optional
        :param contentTypes: Limits the search results to any items that match the search query
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
        :type contentTypes: Union[None, str], optional
        :param type: Limits the search results to any items of this type. This
            parameter only takes one value. By default the API returns
            items that match any of these types.
            * `file` - Limits the search results to files
            * `folder` - Limits the search results to folders
            * `web_link` - Limits the search results to web links, also known
               as bookmarks
        :type type: Union[None, GetSearchOptionsArgTypeField], optional
        :param trashContent: Determines if the search should look in the trash for items.
            By default, this API only returns search results for items
            not currently in the trash (`non_trashed_only`).
            * `trashed_only` - Only searches for items currently in the trash
            * `non_trashed_only` - Only searches for items currently not in
              the trash
        :type trashContent: Union[None, GetSearchOptionsArgTrashContentField], optional
        :param mdfilters: Limits the search results to any items for which the metadata matches
            the provided filter.
            This parameter contains a list of 1 metadata template to filter
            the search results by. This list can currently only
            contain one entry, though this might be expanded in the future.
            This parameter is required unless the `query` parameter is provided.
        :type mdfilters: Union[None, str], optional
        :param sort: Defines the order in which search results are returned. This API
            defaults to returning items by relevance unless this parameter is
            explicitly specified.
            * `relevance` (default) returns the results sorted by relevance to the
            query search term. The relevance is based on the occurrence of the search
            term in the items name, description, content, and additional properties.
            * `modified_at` returns the results ordered in descending order by date
            at which the item was last modified.
        :type sort: Union[None, GetSearchOptionsArgSortField], optional
        :param direction: Defines the direction in which search results are ordered. This API
            defaults to returning items in descending (`DESC`) order unless this
            parameter is explicitly specified.
            When results are sorted by `relevance` the ordering is locked to returning
            items in descending order of relevance, and this parameter is ignored.
        :type direction: Union[None, GetSearchOptionsArgDirectionField], optional
        :param limit: Defines the maximum number of items to return as part of a page of
            results.
        :type limit: Union[None, int], optional
        :param includeRecentSharedLinks: Defines whether the search results should include any items
            that the user recently accessed through a shared link.
            Please note that when this parameter has been set to true,
            the format of the response of this API changes to return
            a list of [Search Results with
            Shared Links](r://search_results_with_shared_links)
        :type includeRecentSharedLinks: Union[None, bool], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.query = query
        self.scope = scope
        self.fileExtensions = fileExtensions
        self.createdAtRange = createdAtRange
        self.updatedAtRange = updatedAtRange
        self.sizeRange = sizeRange
        self.ownerUserIds = ownerUserIds
        self.recentUpdaterUserIds = recentUpdaterUserIds
        self.ancestorFolderIds = ancestorFolderIds
        self.contentTypes = contentTypes
        self.type = type
        self.trashContent = trashContent
        self.mdfilters = mdfilters
        self.sort = sort
        self.direction = direction
        self.limit = limit
        self.includeRecentSharedLinks = includeRecentSharedLinks
        self.fields = fields
        self.offset = offset

class SearchManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def postMetadataQueriesExecuteRead(self, requestBody: MetadataQuery) -> MetadataQueryResults:
        """
        Create a search using SQL-like syntax to return items that match specific
        
        metadata.

        
        By default, this endpoint returns only the most basic info about the items for

        
        which the query matches. To get additional fields for each item, including any

        
        of the metadata, use the `fields` attribute in the query.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_queries/execute_read']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return MetadataQueryResults.from_dict(json.loads(response.text))
    def getMetadataQueryIndices(self, scope: GetMetadataQueryIndicesScopeArg, templateKey: str) -> MetadataQueryIndices:
        """
        Retrieves the metadata query indices for a given scope and template key.
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: GetMetadataQueryIndicesScopeArg
        :param templateKey: The name of the metadata template
            Example: "properties"
        :type templateKey: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/metadata_query_indices']), FetchOptions(method='GET', params={'scope': scope, 'template_key': templateKey}, auth=self.auth))
        return MetadataQueryIndices.from_dict(json.loads(response.text))
    def getSearch(self, options: GetSearchOptionsArg = None) -> None:
        """
        Searches for files, folders, web links, and shared files across the
        
        users content or across the entire enterprise.

        """
        if options is None:
            options = GetSearchOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/search']), FetchOptions(method='GET', params={'query': options.query, 'scope': options.scope, 'file_extensions': options.fileExtensions, 'created_at_range': options.createdAtRange, 'updated_at_range': options.updatedAtRange, 'size_range': options.sizeRange, 'owner_user_ids': options.ownerUserIds, 'recent_updater_user_ids': options.recentUpdaterUserIds, 'ancestor_folder_ids': options.ancestorFolderIds, 'content_types': options.contentTypes, 'type': options.type, 'trash_content': options.trashContent, 'mdfilters': options.mdfilters, 'sort': options.sort, 'direction': options.direction, 'limit': options.limit, 'include_recent_shared_links': options.includeRecentSharedLinks, 'fields': options.fields, 'offset': options.offset}, auth=self.auth))
        return None