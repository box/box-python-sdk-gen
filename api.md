# API Reference

> [!CAUTION]
> **`box-python-sdk-gen` is deprecated and no longer maintained.** As of September 17, 2025, it receives no new features, bug fixes, or security patches. Do not use it for new projects.
>
> Use [`box-python-sdk`](https://github.com/box/box-python-sdk) v10+ instead: `pip install "boxsdk>=10"`. `box-python-sdk` v10 includes every manager listed below, plus newer ones.
> To migrate existing code, see the [migration guide](https://github.com/box/box-python-sdk/blob/main/migration-guides/from-box-python-sdk-gen-v1-to-box-python-sdk.md).

This file lists every manager and method exposed on `BoxClient`. For setup, authentication, and usage examples, see [README.md](README.md). Each section links to a page in [docs/](docs/README.md) with code samples. Parameters marked `?` are optional.

# Client

See [docs/client.md](docs/client.md) and [docs/configuration.md](docs/configuration.md).

Methods:

- <code>client.<a href="./box_sdk_gen/client.py">make_request</a>(fetch_options) -> FetchResponse</code>
- <code>client.<a href="./box_sdk_gen/client.py">with_as_user_header</a>(user_id) -> BoxClient</code>
- <code>client.<a href="./box_sdk_gen/client.py">with_suppressed_notifications</a>() -> BoxClient</code>
- <code>client.<a href="./box_sdk_gen/client.py">with_extra_headers</a>(extra_headers?) -> BoxClient</code>
- <code>client.<a href="./box_sdk_gen/client.py">with_custom_base_urls</a>(base_urls) -> BoxClient</code>
- <code>client.<a href="./box_sdk_gen/client.py">with_proxy</a>(config) -> BoxClient</code>

# Authorization

Examples: [docs/authorization.md](docs/authorization.md)

Methods:

- <code title="get /authorize">client.authorization.<a href="./box_sdk_gen/managers/authorization.py">authorize_user</a>(response_type, client_id, redirect_uri?, state?, scope?, extra_headers?) -> None</code>
- <code title="post /oauth2/token">client.authorization.<a href="./box_sdk_gen/managers/authorization.py">request_access_token</a>(grant_type, client_id?, client_secret?, code?, refresh_token?, assertion?, subject_token?, subject_token_type?, actor_token?, actor_token_type?, scope?, resource?, box_subject_type?, box_subject_id?, box_shared_link?, extra_headers?) -> AccessToken</code>
- <code title="post /oauth2/token">client.authorization.<a href="./box_sdk_gen/managers/authorization.py">refresh_access_token</a>(client_id, client_secret, refresh_token, grant_type?, extra_headers?) -> AccessToken</code>
- <code title="post /oauth2/revoke">client.authorization.<a href="./box_sdk_gen/managers/authorization.py">revoke_access_token</a>(client_id?, client_secret?, token?, extra_headers?) -> None</code>

# Files

Examples: [docs/files.md](docs/files.md)

Methods:

- <code title="get /2.0/files/{file_id}">client.files.<a href="./box_sdk_gen/managers/files.py">get_file_by_id</a>(file_id, fields?, if_none_match?, boxapi?, x_rep_hints?, extra_headers?) -> FileFull</code>
- <code title="put /2.0/files/{file_id}">client.files.<a href="./box_sdk_gen/managers/files.py">update_file_by_id</a>(file_id, name?, description?, parent?, shared_link?, lock?, disposition_at?, permissions?, collections?, tags?, fields?, if_match?, extra_headers?) -> FileFull</code>
- <code title="delete /2.0/files/{file_id}">client.files.<a href="./box_sdk_gen/managers/files.py">delete_file_by_id</a>(file_id, if_match?, extra_headers?) -> None</code>
- <code title="post /2.0/files/{file_id}/copy">client.files.<a href="./box_sdk_gen/managers/files.py">copy_file</a>(file_id, parent, name?, version?, fields?, extra_headers?) -> FileFull</code>
- <code title="get /2.0/files/{file_id}/thumbnail.{extension}">client.files.<a href="./box_sdk_gen/managers/files.py">get_file_thumbnail_url</a>(file_id, extension, min_height?, min_width?, max_height?, max_width?, extra_headers?) -> str</code>
- <code title="get /2.0/files/{file_id}/thumbnail.{extension}">client.files.<a href="./box_sdk_gen/managers/files.py">get_file_thumbnail_by_id</a>(file_id, extension, min_height?, min_width?, max_height?, max_width?, extra_headers?) -> Optional[ByteStream]</code>

# Trashed files

Examples: [docs/trashed_files.md](docs/trashed_files.md)

Methods:

- <code title="post /2.0/files/{file_id}">client.trashed_files.<a href="./box_sdk_gen/managers/trashed_files.py">restore_file_from_trash</a>(file_id, name?, parent?, fields?, extra_headers?) -> TrashFileRestored</code>
- <code title="get /2.0/files/{file_id}/trash">client.trashed_files.<a href="./box_sdk_gen/managers/trashed_files.py">get_trashed_file_by_id</a>(file_id, fields?, extra_headers?) -> TrashFile</code>
- <code title="delete /2.0/files/{file_id}/trash">client.trashed_files.<a href="./box_sdk_gen/managers/trashed_files.py">delete_trashed_file_by_id</a>(file_id, extra_headers?) -> None</code>

# App item associations

Examples: [docs/app_item_associations.md](docs/app_item_associations.md)

Methods:

- <code title="get /2.0/files/{file_id}/app_item_associations">client.app_item_associations.<a href="./box_sdk_gen/managers/app_item_associations.py">get_file_app_item_associations</a>(file_id, limit?, marker?, application_type?, extra_headers?) -> AppItemAssociations</code>
- <code title="get /2.0/folders/{folder_id}/app_item_associations">client.app_item_associations.<a href="./box_sdk_gen/managers/app_item_associations.py">get_folder_app_item_associations</a>(folder_id, limit?, marker?, application_type?, extra_headers?) -> AppItemAssociations</code>

# Downloads

Examples: [docs/downloads.md](docs/downloads.md)

Methods:

- <code title="get /2.0/files/{file_id}/content">client.downloads.<a href="./box_sdk_gen/managers/downloads.py">get_download_file_url</a>(file_id, version?, access_token?, range?, boxapi?, extra_headers?) -> str</code>
- <code title="get /2.0/files/{file_id}/content">client.downloads.<a href="./box_sdk_gen/managers/downloads.py">download_file</a>(file_id, version?, access_token?, range?, boxapi?, extra_headers?) -> Optional[ByteStream]</code>
- <code>client.downloads.<a href="./box_sdk_gen/managers/downloads.py">download_file_to_output_stream</a>(file_id, output_stream, version?, access_token?, range?, boxapi?, extra_headers?) -> None</code>

# Uploads

Examples: [docs/uploads.md](docs/uploads.md)

Methods:

- <code title="post /2.0/files/{file_id}/content">client.uploads.<a href="./box_sdk_gen/managers/uploads.py">upload_file_version</a>(file_id, attributes, file, file_file_name?, file_content_type?, fields?, if_match?, content_md_5?, extra_headers?) -> Files</code>
- <code title="options /2.0/files/content">client.uploads.<a href="./box_sdk_gen/managers/uploads.py">preflight_file_upload_check</a>(name?, size?, parent?, extra_headers?) -> UploadUrl</code>
- <code title="post /2.0/files/content">client.uploads.<a href="./box_sdk_gen/managers/uploads.py">upload_file</a>(attributes, file, file_file_name?, file_content_type?, fields?, content_md_5?, extra_headers?) -> Files</code>
- <code>client.uploads.<a href="./box_sdk_gen/managers/uploads.py">upload_with_preflight_check</a>(attributes, file, file_file_name?, file_content_type?, fields?, content_md_5?, extra_headers?) -> Files</code>

# Chunked uploads

Examples: [docs/chunked_uploads.md](docs/chunked_uploads.md)

Methods:

- <code title="post /2.0/files/upload_sessions">client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">create_file_upload_session</a>(folder_id, file_size, file_name, extra_headers?) -> UploadSession</code>
- <code title="post /2.0/files/{file_id}/upload_sessions">client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">create_file_upload_session_for_existing_file</a>(file_id, file_size, file_name?, extra_headers?) -> UploadSession</code>
- <code>client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">get_file_upload_session_by_url</a>(url, extra_headers?) -> UploadSession</code>
- <code title="get /2.0/files/upload_sessions/{upload_session_id}">client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">get_file_upload_session_by_id</a>(upload_session_id, extra_headers?) -> UploadSession</code>
- <code>client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">upload_file_part_by_url</a>(url, request_body, digest, content_range, extra_headers?) -> UploadedPart</code>
- <code title="put /2.0/files/upload_sessions/{upload_session_id}">client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">upload_file_part</a>(upload_session_id, request_body, digest, content_range, extra_headers?) -> UploadedPart</code>
- <code>client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">delete_file_upload_session_by_url</a>(url, extra_headers?) -> None</code>
- <code title="delete /2.0/files/upload_sessions/{upload_session_id}">client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">delete_file_upload_session_by_id</a>(upload_session_id, extra_headers?) -> None</code>
- <code>client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">get_file_upload_session_parts_by_url</a>(url, offset?, limit?, extra_headers?) -> UploadParts</code>
- <code title="get /2.0/files/upload_sessions/{upload_session_id}/parts">client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">get_file_upload_session_parts</a>(upload_session_id, offset?, limit?, extra_headers?) -> UploadParts</code>
- <code>client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">create_file_upload_session_commit_by_url</a>(url, parts, digest, if_match?, if_none_match?, extra_headers?) -> Optional[Files]</code>
- <code title="post /2.0/files/upload_sessions/{upload_session_id}/commit">client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">create_file_upload_session_commit</a>(upload_session_id, parts, digest, if_match?, if_none_match?, extra_headers?) -> Optional[Files]</code>
- <code>client.chunked_uploads.<a href="./box_sdk_gen/managers/chunked_uploads.py">upload_big_file</a>(file, file_name, file_size, parent_folder_id) -> FileFull</code>

# List collaborations

Examples: [docs/list_collaborations.md](docs/list_collaborations.md)

Methods:

- <code title="get /2.0/files/{file_id}/collaborations">client.list_collaborations.<a href="./box_sdk_gen/managers/list_collaborations.py">get_file_collaborations</a>(file_id, fields?, limit?, marker?, extra_headers?) -> Collaborations</code>
- <code title="get /2.0/folders/{folder_id}/collaborations">client.list_collaborations.<a href="./box_sdk_gen/managers/list_collaborations.py">get_folder_collaborations</a>(folder_id, fields?, limit?, marker?, extra_headers?) -> Collaborations</code>
- <code title="get /2.0/collaborations">client.list_collaborations.<a href="./box_sdk_gen/managers/list_collaborations.py">get_collaborations</a>(status, fields?, offset?, limit?, extra_headers?) -> CollaborationsOffsetPaginated</code>
- <code title="get /2.0/groups/{group_id}/collaborations">client.list_collaborations.<a href="./box_sdk_gen/managers/list_collaborations.py">get_group_collaborations</a>(group_id, limit?, offset?, extra_headers?) -> CollaborationsOffsetPaginated</code>

# Comments

Examples: [docs/comments.md](docs/comments.md)

Methods:

- <code title="get /2.0/files/{file_id}/comments">client.comments.<a href="./box_sdk_gen/managers/comments.py">get_file_comments</a>(file_id, fields?, limit?, offset?, extra_headers?) -> Comments</code>
- <code title="get /2.0/comments/{comment_id}">client.comments.<a href="./box_sdk_gen/managers/comments.py">get_comment_by_id</a>(comment_id, fields?, extra_headers?) -> CommentFull</code>
- <code title="put /2.0/comments/{comment_id}">client.comments.<a href="./box_sdk_gen/managers/comments.py">update_comment_by_id</a>(comment_id, message?, fields?, extra_headers?) -> CommentFull</code>
- <code title="delete /2.0/comments/{comment_id}">client.comments.<a href="./box_sdk_gen/managers/comments.py">delete_comment_by_id</a>(comment_id, extra_headers?) -> None</code>
- <code title="post /2.0/comments">client.comments.<a href="./box_sdk_gen/managers/comments.py">create_comment</a>(message, item, tagged_message?, fields?, extra_headers?) -> CommentFull</code>

# Tasks

Examples: [docs/tasks.md](docs/tasks.md)

Methods:

- <code title="get /2.0/files/{file_id}/tasks">client.tasks.<a href="./box_sdk_gen/managers/tasks.py">get_file_tasks</a>(file_id, extra_headers?) -> Tasks</code>
- <code title="post /2.0/tasks">client.tasks.<a href="./box_sdk_gen/managers/tasks.py">create_task</a>(item, action?, message?, due_at?, completion_rule?, extra_headers?) -> Task</code>
- <code title="get /2.0/tasks/{task_id}">client.tasks.<a href="./box_sdk_gen/managers/tasks.py">get_task_by_id</a>(task_id, extra_headers?) -> Task</code>
- <code title="put /2.0/tasks/{task_id}">client.tasks.<a href="./box_sdk_gen/managers/tasks.py">update_task_by_id</a>(task_id, action?, message?, due_at?, completion_rule?, extra_headers?) -> Task</code>
- <code title="delete /2.0/tasks/{task_id}">client.tasks.<a href="./box_sdk_gen/managers/tasks.py">delete_task_by_id</a>(task_id, extra_headers?) -> None</code>

# File versions

Examples: [docs/file_versions.md](docs/file_versions.md)

Methods:

- <code title="get /2.0/files/{file_id}/versions">client.file_versions.<a href="./box_sdk_gen/managers/file_versions.py">get_file_versions</a>(file_id, fields?, limit?, offset?, extra_headers?) -> FileVersions</code>
- <code title="get /2.0/files/{file_id}/versions/{file_version_id}">client.file_versions.<a href="./box_sdk_gen/managers/file_versions.py">get_file_version_by_id</a>(file_id, file_version_id, fields?, extra_headers?) -> FileVersionFull</code>
- <code title="delete /2.0/files/{file_id}/versions/{file_version_id}">client.file_versions.<a href="./box_sdk_gen/managers/file_versions.py">delete_file_version_by_id</a>(file_id, file_version_id, if_match?, extra_headers?) -> None</code>
- <code title="put /2.0/files/{file_id}/versions/{file_version_id}">client.file_versions.<a href="./box_sdk_gen/managers/file_versions.py">update_file_version_by_id</a>(file_id, file_version_id, trashed_at?, extra_headers?) -> FileVersionFull</code>
- <code title="post /2.0/files/{file_id}/versions/current">client.file_versions.<a href="./box_sdk_gen/managers/file_versions.py">promote_file_version</a>(file_id, id?, type?, fields?, extra_headers?) -> FileVersionFull</code>

# File metadata

Examples: [docs/file_metadata.md](docs/file_metadata.md)

Methods:

- <code title="get /2.0/files/{file_id}/metadata">client.file_metadata.<a href="./box_sdk_gen/managers/file_metadata.py">get_file_metadata</a>(file_id, extra_headers?) -> Metadatas</code>
- <code title="get /2.0/files/{file_id}/metadata/{scope}/{template_key}">client.file_metadata.<a href="./box_sdk_gen/managers/file_metadata.py">get_file_metadata_by_id</a>(file_id, scope, template_key, extra_headers?) -> MetadataFull</code>
- <code title="post /2.0/files/{file_id}/metadata/{scope}/{template_key}">client.file_metadata.<a href="./box_sdk_gen/managers/file_metadata.py">create_file_metadata_by_id</a>(file_id, scope, template_key, request_body, extra_headers?) -> MetadataFull</code>
- <code title="put /2.0/files/{file_id}/metadata/{scope}/{template_key}">client.file_metadata.<a href="./box_sdk_gen/managers/file_metadata.py">update_file_metadata_by_id</a>(file_id, scope, template_key, request_body, extra_headers?) -> MetadataFull</code>
- <code title="delete /2.0/files/{file_id}/metadata/{scope}/{template_key}">client.file_metadata.<a href="./box_sdk_gen/managers/file_metadata.py">delete_file_metadata_by_id</a>(file_id, scope, template_key, extra_headers?) -> None</code>

# File classifications

Examples: [docs/file_classifications.md](docs/file_classifications.md)

Methods:

- <code title="get /2.0/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo">client.file_classifications.<a href="./box_sdk_gen/managers/file_classifications.py">get_classification_on_file</a>(file_id, extra_headers?) -> Classification</code>
- <code title="post /2.0/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo">client.file_classifications.<a href="./box_sdk_gen/managers/file_classifications.py">add_classification_to_file</a>(file_id, box_security_classification_key?, extra_headers?) -> Classification</code>
- <code title="put /2.0/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo">client.file_classifications.<a href="./box_sdk_gen/managers/file_classifications.py">update_classification_on_file</a>(file_id, request_body, extra_headers?) -> Classification</code>
- <code title="delete /2.0/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo">client.file_classifications.<a href="./box_sdk_gen/managers/file_classifications.py">delete_classification_from_file</a>(file_id, extra_headers?) -> None</code>

# Skills

Examples: [docs/skills.md](docs/skills.md)

Methods:

- <code title="get /2.0/files/{file_id}/metadata/global/boxSkillsCards">client.skills.<a href="./box_sdk_gen/managers/skills.py">get_box_skill_cards_on_file</a>(file_id, extra_headers?) -> SkillCardsMetadata</code>
- <code title="post /2.0/files/{file_id}/metadata/global/boxSkillsCards">client.skills.<a href="./box_sdk_gen/managers/skills.py">create_box_skill_cards_on_file</a>(file_id, cards, extra_headers?) -> SkillCardsMetadata</code>
- <code title="put /2.0/files/{file_id}/metadata/global/boxSkillsCards">client.skills.<a href="./box_sdk_gen/managers/skills.py">update_box_skill_cards_on_file</a>(file_id, request_body, extra_headers?) -> SkillCardsMetadata</code>
- <code title="delete /2.0/files/{file_id}/metadata/global/boxSkillsCards">client.skills.<a href="./box_sdk_gen/managers/skills.py">delete_box_skill_cards_from_file</a>(file_id, extra_headers?) -> None</code>
- <code title="put /2.0/skill_invocations/{skill_id}">client.skills.<a href="./box_sdk_gen/managers/skills.py">update_all_skill_cards_on_file</a>(skill_id, status, metadata, file, file_version?, usage?, extra_headers?) -> None</code>

# File watermarks

Examples: [docs/file_watermarks.md](docs/file_watermarks.md)

Methods:

- <code title="get /2.0/files/{file_id}/watermark">client.file_watermarks.<a href="./box_sdk_gen/managers/file_watermarks.py">get_file_watermark</a>(file_id, extra_headers?) -> Watermark</code>
- <code title="put /2.0/files/{file_id}/watermark">client.file_watermarks.<a href="./box_sdk_gen/managers/file_watermarks.py">update_file_watermark</a>(file_id, watermark, extra_headers?) -> Watermark</code>
- <code title="delete /2.0/files/{file_id}/watermark">client.file_watermarks.<a href="./box_sdk_gen/managers/file_watermarks.py">delete_file_watermark</a>(file_id, extra_headers?) -> None</code>

# File requests

Examples: [docs/file_requests.md](docs/file_requests.md)

Methods:

- <code title="get /2.0/file_requests/{file_request_id}">client.file_requests.<a href="./box_sdk_gen/managers/file_requests.py">get_file_request_by_id</a>(file_request_id, extra_headers?) -> FileRequest</code>
- <code title="put /2.0/file_requests/{file_request_id}">client.file_requests.<a href="./box_sdk_gen/managers/file_requests.py">update_file_request_by_id</a>(file_request_id, title?, description?, status?, is_email_required?, is_description_required?, expires_at?, if_match?, extra_headers?) -> FileRequest</code>
- <code title="delete /2.0/file_requests/{file_request_id}">client.file_requests.<a href="./box_sdk_gen/managers/file_requests.py">delete_file_request_by_id</a>(file_request_id, extra_headers?) -> None</code>
- <code title="post /2.0/file_requests/{file_request_id}/copy">client.file_requests.<a href="./box_sdk_gen/managers/file_requests.py">create_file_request_copy</a>(file_request_id, folder, title?, description?, status?, is_email_required?, is_description_required?, expires_at?, extra_headers?) -> FileRequest</code>

# Folders

Examples: [docs/folders.md](docs/folders.md)

Methods:

- <code title="get /2.0/folders/{folder_id}">client.folders.<a href="./box_sdk_gen/managers/folders.py">get_folder_by_id</a>(folder_id, fields?, sort?, direction?, offset?, limit?, if_none_match?, boxapi?, extra_headers?) -> FolderFull</code>
- <code title="put /2.0/folders/{folder_id}">client.folders.<a href="./box_sdk_gen/managers/folders.py">update_folder_by_id</a>(folder_id, name?, description?, sync_state?, can_non_owners_invite?, parent?, shared_link?, folder_upload_email?, tags?, is_collaboration_restricted_to_enterprise?, collections?, can_non_owners_view_collaborators?, fields?, if_match?, extra_headers?) -> FolderFull</code>
- <code title="delete /2.0/folders/{folder_id}">client.folders.<a href="./box_sdk_gen/managers/folders.py">delete_folder_by_id</a>(folder_id, recursive?, if_match?, extra_headers?) -> None</code>
- <code title="get /2.0/folders/{folder_id}/items">client.folders.<a href="./box_sdk_gen/managers/folders.py">get_folder_items</a>(folder_id, fields?, usemarker?, marker?, offset?, limit?, sort?, direction?, boxapi?, extra_headers?) -> Items</code>
- <code title="post /2.0/folders">client.folders.<a href="./box_sdk_gen/managers/folders.py">create_folder</a>(name, parent, folder_upload_email?, sync_state?, fields?, extra_headers?) -> FolderFull</code>
- <code title="post /2.0/folders/{folder_id}/copy">client.folders.<a href="./box_sdk_gen/managers/folders.py">copy_folder</a>(folder_id, parent, name?, fields?, extra_headers?) -> FolderFull</code>

# Trashed folders

Examples: [docs/trashed_folders.md](docs/trashed_folders.md)

Methods:

- <code title="post /2.0/folders/{folder_id}">client.trashed_folders.<a href="./box_sdk_gen/managers/trashed_folders.py">restore_folder_from_trash</a>(folder_id, name?, parent?, fields?, extra_headers?) -> TrashFolderRestored</code>
- <code title="get /2.0/folders/{folder_id}/trash">client.trashed_folders.<a href="./box_sdk_gen/managers/trashed_folders.py">get_trashed_folder_by_id</a>(folder_id, fields?, extra_headers?) -> TrashFolder</code>
- <code title="delete /2.0/folders/{folder_id}/trash">client.trashed_folders.<a href="./box_sdk_gen/managers/trashed_folders.py">delete_trashed_folder_by_id</a>(folder_id, extra_headers?) -> None</code>

# Folder metadata

Examples: [docs/folder_metadata.md](docs/folder_metadata.md)

Methods:

- <code title="get /2.0/folders/{folder_id}/metadata">client.folder_metadata.<a href="./box_sdk_gen/managers/folder_metadata.py">get_folder_metadata</a>(folder_id, extra_headers?) -> Metadatas</code>
- <code title="get /2.0/folders/{folder_id}/metadata/{scope}/{template_key}">client.folder_metadata.<a href="./box_sdk_gen/managers/folder_metadata.py">get_folder_metadata_by_id</a>(folder_id, scope, template_key, extra_headers?) -> MetadataFull</code>
- <code title="post /2.0/folders/{folder_id}/metadata/{scope}/{template_key}">client.folder_metadata.<a href="./box_sdk_gen/managers/folder_metadata.py">create_folder_metadata_by_id</a>(folder_id, scope, template_key, request_body, extra_headers?) -> MetadataFull</code>
- <code title="put /2.0/folders/{folder_id}/metadata/{scope}/{template_key}">client.folder_metadata.<a href="./box_sdk_gen/managers/folder_metadata.py">update_folder_metadata_by_id</a>(folder_id, scope, template_key, request_body, extra_headers?) -> MetadataFull</code>
- <code title="delete /2.0/folders/{folder_id}/metadata/{scope}/{template_key}">client.folder_metadata.<a href="./box_sdk_gen/managers/folder_metadata.py">delete_folder_metadata_by_id</a>(folder_id, scope, template_key, extra_headers?) -> None</code>

# Folder classifications

Examples: [docs/folder_classifications.md](docs/folder_classifications.md)

Methods:

- <code title="get /2.0/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo">client.folder_classifications.<a href="./box_sdk_gen/managers/folder_classifications.py">get_classification_on_folder</a>(folder_id, extra_headers?) -> Classification</code>
- <code title="post /2.0/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo">client.folder_classifications.<a href="./box_sdk_gen/managers/folder_classifications.py">add_classification_to_folder</a>(folder_id, box_security_classification_key?, extra_headers?) -> Classification</code>
- <code title="put /2.0/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo">client.folder_classifications.<a href="./box_sdk_gen/managers/folder_classifications.py">update_classification_on_folder</a>(folder_id, request_body, extra_headers?) -> Classification</code>
- <code title="delete /2.0/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo">client.folder_classifications.<a href="./box_sdk_gen/managers/folder_classifications.py">delete_classification_from_folder</a>(folder_id, extra_headers?) -> None</code>

# Trashed items

Examples: [docs/trashed_items.md](docs/trashed_items.md)

Methods:

- <code title="get /2.0/folders/trash/items">client.trashed_items.<a href="./box_sdk_gen/managers/trashed_items.py">get_trashed_items</a>(fields?, limit?, offset?, usemarker?, marker?, direction?, sort?, extra_headers?) -> Items</code>

# Folder watermarks

Examples: [docs/folder_watermarks.md](docs/folder_watermarks.md)

Methods:

- <code title="get /2.0/folders/{folder_id}/watermark">client.folder_watermarks.<a href="./box_sdk_gen/managers/folder_watermarks.py">get_folder_watermark</a>(folder_id, extra_headers?) -> Watermark</code>
- <code title="put /2.0/folders/{folder_id}/watermark">client.folder_watermarks.<a href="./box_sdk_gen/managers/folder_watermarks.py">update_folder_watermark</a>(folder_id, watermark, extra_headers?) -> Watermark</code>
- <code title="delete /2.0/folders/{folder_id}/watermark">client.folder_watermarks.<a href="./box_sdk_gen/managers/folder_watermarks.py">delete_folder_watermark</a>(folder_id, extra_headers?) -> None</code>

# Folder locks

Examples: [docs/folder_locks.md](docs/folder_locks.md)

Methods:

- <code title="get /2.0/folder_locks">client.folder_locks.<a href="./box_sdk_gen/managers/folder_locks.py">get_folder_locks</a>(folder_id, extra_headers?) -> FolderLocks</code>
- <code title="post /2.0/folder_locks">client.folder_locks.<a href="./box_sdk_gen/managers/folder_locks.py">create_folder_lock</a>(folder, locked_operations?, extra_headers?) -> FolderLock</code>
- <code title="delete /2.0/folder_locks/{folder_lock_id}">client.folder_locks.<a href="./box_sdk_gen/managers/folder_locks.py">delete_folder_lock_by_id</a>(folder_lock_id, extra_headers?) -> None</code>

# Metadata templates

Examples: [docs/metadata_templates.md](docs/metadata_templates.md)

Methods:

- <code title="get /2.0/metadata_templates">client.metadata_templates.<a href="./box_sdk_gen/managers/metadata_templates.py">get_metadata_templates_by_instance_id</a>(metadata_instance_id, marker?, limit?, extra_headers?) -> MetadataTemplates</code>
- <code title="get /2.0/metadata_templates/{scope}/{template_key}/schema">client.metadata_templates.<a href="./box_sdk_gen/managers/metadata_templates.py">get_metadata_template</a>(scope, template_key, extra_headers?) -> MetadataTemplate</code>
- <code title="put /2.0/metadata_templates/{scope}/{template_key}/schema">client.metadata_templates.<a href="./box_sdk_gen/managers/metadata_templates.py">update_metadata_template</a>(scope, template_key, request_body, extra_headers?) -> MetadataTemplate</code>
- <code title="delete /2.0/metadata_templates/{scope}/{template_key}/schema">client.metadata_templates.<a href="./box_sdk_gen/managers/metadata_templates.py">delete_metadata_template</a>(scope, template_key, extra_headers?) -> None</code>
- <code title="get /2.0/metadata_templates/{template_id}">client.metadata_templates.<a href="./box_sdk_gen/managers/metadata_templates.py">get_metadata_template_by_id</a>(template_id, extra_headers?) -> MetadataTemplate</code>
- <code title="get /2.0/metadata_templates/global">client.metadata_templates.<a href="./box_sdk_gen/managers/metadata_templates.py">get_global_metadata_templates</a>(marker?, limit?, extra_headers?) -> MetadataTemplates</code>
- <code title="get /2.0/metadata_templates/enterprise">client.metadata_templates.<a href="./box_sdk_gen/managers/metadata_templates.py">get_enterprise_metadata_templates</a>(marker?, limit?, extra_headers?) -> MetadataTemplates</code>
- <code title="post /2.0/metadata_templates/schema">client.metadata_templates.<a href="./box_sdk_gen/managers/metadata_templates.py">create_metadata_template</a>(scope, display_name, template_key?, hidden?, fields?, copy_instance_on_item_copy?, extra_headers?) -> MetadataTemplate</code>

# Classifications

Examples: [docs/classifications.md](docs/classifications.md)

Methods:

- <code title="get /2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema">client.classifications.<a href="./box_sdk_gen/managers/classifications.py">get_classification_template</a>(extra_headers?) -> ClassificationTemplate</code>
- <code title="put /2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema">client.classifications.<a href="./box_sdk_gen/managers/classifications.py">add_classification</a>(request_body, extra_headers?) -> ClassificationTemplate</code>
- <code title="put /2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema">client.classifications.<a href="./box_sdk_gen/managers/classifications.py">update_classification</a>(request_body, extra_headers?) -> ClassificationTemplate</code>
- <code title="post /2.0/metadata_templates/schema">client.classifications.<a href="./box_sdk_gen/managers/classifications.py">create_classification_template</a>(fields, scope?, template_key?, display_name?, hidden?, copy_instance_on_item_copy?, extra_headers?) -> ClassificationTemplate</code>

# Metadata cascade policies

Examples: [docs/metadata_cascade_policies.md](docs/metadata_cascade_policies.md)

Methods:

- <code title="get /2.0/metadata_cascade_policies">client.metadata_cascade_policies.<a href="./box_sdk_gen/managers/metadata_cascade_policies.py">get_metadata_cascade_policies</a>(folder_id, owner_enterprise_id?, marker?, offset?, extra_headers?) -> MetadataCascadePolicies</code>
- <code title="post /2.0/metadata_cascade_policies">client.metadata_cascade_policies.<a href="./box_sdk_gen/managers/metadata_cascade_policies.py">create_metadata_cascade_policy</a>(folder_id, scope, template_key, extra_headers?) -> MetadataCascadePolicy</code>
- <code title="get /2.0/metadata_cascade_policies/{metadata_cascade_policy_id}">client.metadata_cascade_policies.<a href="./box_sdk_gen/managers/metadata_cascade_policies.py">get_metadata_cascade_policy_by_id</a>(metadata_cascade_policy_id, extra_headers?) -> MetadataCascadePolicy</code>
- <code title="delete /2.0/metadata_cascade_policies/{metadata_cascade_policy_id}">client.metadata_cascade_policies.<a href="./box_sdk_gen/managers/metadata_cascade_policies.py">delete_metadata_cascade_policy_by_id</a>(metadata_cascade_policy_id, extra_headers?) -> None</code>
- <code title="post /2.0/metadata_cascade_policies/{metadata_cascade_policy_id}/apply">client.metadata_cascade_policies.<a href="./box_sdk_gen/managers/metadata_cascade_policies.py">apply_metadata_cascade_policy</a>(metadata_cascade_policy_id, conflict_resolution, extra_headers?) -> None</code>

# Search

Examples: [docs/search.md](docs/search.md)

Methods:

- <code title="post /2.0/metadata_queries/execute_read">client.search.<a href="./box_sdk_gen/managers/search.py">search_by_metadata_query</a>(from_, ancestor_folder_id, query?, query_params?, order_by?, limit?, marker?, fields?, extra_headers?) -> MetadataQueryResults</code>
- <code title="get /2.0/search">client.search.<a href="./box_sdk_gen/managers/search.py">search_for_content</a>(query?, scope?, file_extensions?, created_at_range?, updated_at_range?, size_range?, owner_user_ids?, recent_updater_user_ids?, ancestor_folder_ids?, content_types?, type?, trash_content?, mdfilters?, sort?, direction?, limit?, include_recent_shared_links?, fields?, offset?, deleted_user_ids?, deleted_at_range?, extra_headers?) -> Union[SearchResults, SearchResultsWithSharedLinks]</code>

# User collaborations

Examples: [docs/user_collaborations.md](docs/user_collaborations.md)

Methods:

- <code title="get /2.0/collaborations/{collaboration_id}">client.user_collaborations.<a href="./box_sdk_gen/managers/user_collaborations.py">get_collaboration_by_id</a>(collaboration_id, fields?, extra_headers?) -> Collaboration</code>
- <code title="put /2.0/collaborations/{collaboration_id}">client.user_collaborations.<a href="./box_sdk_gen/managers/user_collaborations.py">update_collaboration_by_id</a>(collaboration_id, role, status?, expires_at?, can_view_path?, extra_headers?) -> Optional[Collaboration]</code>
- <code title="delete /2.0/collaborations/{collaboration_id}">client.user_collaborations.<a href="./box_sdk_gen/managers/user_collaborations.py">delete_collaboration_by_id</a>(collaboration_id, extra_headers?) -> None</code>
- <code title="post /2.0/collaborations">client.user_collaborations.<a href="./box_sdk_gen/managers/user_collaborations.py">create_collaboration</a>(item, accessible_by, role, is_access_only?, can_view_path?, expires_at?, fields?, notify?, extra_headers?) -> Collaboration</code>

# Task assignments

Examples: [docs/task_assignments.md](docs/task_assignments.md)

Methods:

- <code title="get /2.0/tasks/{task_id}/assignments">client.task_assignments.<a href="./box_sdk_gen/managers/task_assignments.py">get_task_assignments</a>(task_id, extra_headers?) -> TaskAssignments</code>
- <code title="post /2.0/task_assignments">client.task_assignments.<a href="./box_sdk_gen/managers/task_assignments.py">create_task_assignment</a>(task, assign_to, extra_headers?) -> TaskAssignment</code>
- <code title="get /2.0/task_assignments/{task_assignment_id}">client.task_assignments.<a href="./box_sdk_gen/managers/task_assignments.py">get_task_assignment_by_id</a>(task_assignment_id, extra_headers?) -> TaskAssignment</code>
- <code title="put /2.0/task_assignments/{task_assignment_id}">client.task_assignments.<a href="./box_sdk_gen/managers/task_assignments.py">update_task_assignment_by_id</a>(task_assignment_id, message?, resolution_state?, extra_headers?) -> TaskAssignment</code>
- <code title="delete /2.0/task_assignments/{task_assignment_id}">client.task_assignments.<a href="./box_sdk_gen/managers/task_assignments.py">delete_task_assignment_by_id</a>(task_assignment_id, extra_headers?) -> None</code>

# Shared links files

Examples: [docs/shared_links_files.md](docs/shared_links_files.md)

Methods:

- <code title="get /2.0/shared_items">client.shared_links_files.<a href="./box_sdk_gen/managers/shared_links_files.py">find_file_for_shared_link</a>(boxapi, fields?, if_none_match?, extra_headers?) -> FileFull</code>
- <code title="get /2.0/files/{file_id}">client.shared_links_files.<a href="./box_sdk_gen/managers/shared_links_files.py">get_shared_link_for_file</a>(file_id, fields, extra_headers?) -> FileFull</code>
- <code title="put /2.0/files/{file_id}">client.shared_links_files.<a href="./box_sdk_gen/managers/shared_links_files.py">add_share_link_to_file</a>(file_id, fields, shared_link?, extra_headers?) -> FileFull</code>
- <code title="put /2.0/files/{file_id}">client.shared_links_files.<a href="./box_sdk_gen/managers/shared_links_files.py">update_shared_link_on_file</a>(file_id, fields, shared_link?, extra_headers?) -> FileFull</code>
- <code title="put /2.0/files/{file_id}">client.shared_links_files.<a href="./box_sdk_gen/managers/shared_links_files.py">remove_shared_link_from_file</a>(file_id, fields, shared_link?, extra_headers?) -> FileFull</code>

# Shared links folders

Examples: [docs/shared_links_folders.md](docs/shared_links_folders.md)

Methods:

- <code title="get /2.0/shared_items">client.shared_links_folders.<a href="./box_sdk_gen/managers/shared_links_folders.py">find_folder_for_shared_link</a>(boxapi, fields?, if_none_match?, extra_headers?) -> FolderFull</code>
- <code title="get /2.0/folders/{folder_id}">client.shared_links_folders.<a href="./box_sdk_gen/managers/shared_links_folders.py">get_shared_link_for_folder</a>(folder_id, fields, extra_headers?) -> FolderFull</code>
- <code title="put /2.0/folders/{folder_id}">client.shared_links_folders.<a href="./box_sdk_gen/managers/shared_links_folders.py">add_share_link_to_folder</a>(folder_id, fields, shared_link?, extra_headers?) -> FolderFull</code>
- <code title="put /2.0/folders/{folder_id}">client.shared_links_folders.<a href="./box_sdk_gen/managers/shared_links_folders.py">update_shared_link_on_folder</a>(folder_id, fields, shared_link?, extra_headers?) -> FolderFull</code>
- <code title="put /2.0/folders/{folder_id}">client.shared_links_folders.<a href="./box_sdk_gen/managers/shared_links_folders.py">remove_shared_link_from_folder</a>(folder_id, fields, shared_link?, extra_headers?) -> FolderFull</code>

# Web links

Examples: [docs/web_links.md](docs/web_links.md)

Methods:

- <code title="post /2.0/web_links">client.web_links.<a href="./box_sdk_gen/managers/web_links.py">create_web_link</a>(url, parent, name?, description?, extra_headers?) -> WebLink</code>
- <code title="get /2.0/web_links/{web_link_id}">client.web_links.<a href="./box_sdk_gen/managers/web_links.py">get_web_link_by_id</a>(web_link_id, boxapi?, extra_headers?) -> WebLink</code>
- <code title="put /2.0/web_links/{web_link_id}">client.web_links.<a href="./box_sdk_gen/managers/web_links.py">update_web_link_by_id</a>(web_link_id, url?, parent?, name?, description?, shared_link?, extra_headers?) -> WebLink</code>
- <code title="delete /2.0/web_links/{web_link_id}">client.web_links.<a href="./box_sdk_gen/managers/web_links.py">delete_web_link_by_id</a>(web_link_id, extra_headers?) -> None</code>

# Trashed web links

Examples: [docs/trashed_web_links.md](docs/trashed_web_links.md)

Methods:

- <code title="post /2.0/web_links/{web_link_id}">client.trashed_web_links.<a href="./box_sdk_gen/managers/trashed_web_links.py">restore_weblink_from_trash</a>(web_link_id, name?, parent?, fields?, extra_headers?) -> TrashWebLinkRestored</code>
- <code title="get /2.0/web_links/{web_link_id}/trash">client.trashed_web_links.<a href="./box_sdk_gen/managers/trashed_web_links.py">get_trashed_web_link_by_id</a>(web_link_id, fields?, extra_headers?) -> TrashWebLink</code>
- <code title="delete /2.0/web_links/{web_link_id}/trash">client.trashed_web_links.<a href="./box_sdk_gen/managers/trashed_web_links.py">delete_trashed_web_link_by_id</a>(web_link_id, extra_headers?) -> None</code>

# Shared links web links

Examples: [docs/shared_links_web_links.md](docs/shared_links_web_links.md)

Methods:

- <code title="get /2.0/shared_items">client.shared_links_web_links.<a href="./box_sdk_gen/managers/shared_links_web_links.py">find_web_link_for_shared_link</a>(boxapi, fields?, if_none_match?, extra_headers?) -> WebLink</code>
- <code title="get /2.0/web_links/{web_link_id}">client.shared_links_web_links.<a href="./box_sdk_gen/managers/shared_links_web_links.py">get_shared_link_for_web_link</a>(web_link_id, fields, extra_headers?) -> WebLink</code>
- <code title="put /2.0/web_links/{web_link_id}">client.shared_links_web_links.<a href="./box_sdk_gen/managers/shared_links_web_links.py">add_share_link_to_web_link</a>(web_link_id, fields, shared_link?, extra_headers?) -> WebLink</code>
- <code title="put /2.0/web_links/{web_link_id}">client.shared_links_web_links.<a href="./box_sdk_gen/managers/shared_links_web_links.py">update_shared_link_on_web_link</a>(web_link_id, fields, shared_link?, extra_headers?) -> WebLink</code>
- <code title="put /2.0/web_links/{web_link_id}">client.shared_links_web_links.<a href="./box_sdk_gen/managers/shared_links_web_links.py">remove_shared_link_from_web_link</a>(web_link_id, fields, shared_link?, extra_headers?) -> WebLink</code>

# Shared links app items

Examples: [docs/shared_links_app_items.md](docs/shared_links_app_items.md)

Methods:

- <code title="get /2.0/shared_items">client.shared_links_app_items.<a href="./box_sdk_gen/managers/shared_links_app_items.py">find_app_item_for_shared_link</a>(boxapi, extra_headers?) -> AppItem</code>

# Users

Examples: [docs/users.md](docs/users.md)

Methods:

- <code title="get /2.0/users">client.users.<a href="./box_sdk_gen/managers/users.py">get_users</a>(filter_term?, user_type?, external_app_user_id?, fields?, offset?, limit?, usemarker?, marker?, extra_headers?) -> Users</code>
- <code title="post /2.0/users">client.users.<a href="./box_sdk_gen/managers/users.py">create_user</a>(name, login?, is_platform_access_only?, role?, language?, is_sync_enabled?, job_title?, phone?, address?, space_amount?, tracking_codes?, can_see_managed_users?, timezone?, is_external_collab_restricted?, is_exempt_from_device_limits?, is_exempt_from_login_verification?, status?, external_app_user_id?, fields?, extra_headers?) -> UserFull</code>
- <code title="get /2.0/users/me">client.users.<a href="./box_sdk_gen/managers/users.py">get_user_me</a>(fields?, extra_headers?) -> UserFull</code>
- <code title="get /2.0/users/{user_id}">client.users.<a href="./box_sdk_gen/managers/users.py">get_user_by_id</a>(user_id, fields?, extra_headers?) -> UserFull</code>
- <code title="put /2.0/users/{user_id}">client.users.<a href="./box_sdk_gen/managers/users.py">update_user_by_id</a>(user_id, enterprise?, notify?, name?, login?, role?, language?, is_sync_enabled?, job_title?, phone?, address?, tracking_codes?, can_see_managed_users?, timezone?, is_external_collab_restricted?, is_exempt_from_device_limits?, is_exempt_from_login_verification?, is_password_reset_required?, status?, space_amount?, notification_email?, external_app_user_id?, fields?, extra_headers?) -> UserFull</code>
- <code title="delete /2.0/users/{user_id}">client.users.<a href="./box_sdk_gen/managers/users.py">delete_user_by_id</a>(user_id, notify?, force?, extra_headers?) -> None</code>

# Session termination

Examples: [docs/session_termination.md](docs/session_termination.md)

Methods:

- <code title="post /2.0/users/terminate_sessions">client.session_termination.<a href="./box_sdk_gen/managers/session_termination.py">terminate_users_sessions</a>(user_ids, user_logins, extra_headers?) -> SessionTerminationMessage</code>
- <code title="post /2.0/groups/terminate_sessions">client.session_termination.<a href="./box_sdk_gen/managers/session_termination.py">terminate_groups_sessions</a>(group_ids, extra_headers?) -> SessionTerminationMessage</code>

# Avatars

Examples: [docs/avatars.md](docs/avatars.md)

Methods:

- <code title="get /2.0/users/{user_id}/avatar">client.avatars.<a href="./box_sdk_gen/managers/avatars.py">get_user_avatar</a>(user_id, extra_headers?) -> ByteStream</code>
- <code title="post /2.0/users/{user_id}/avatar">client.avatars.<a href="./box_sdk_gen/managers/avatars.py">create_user_avatar</a>(user_id, pic, pic_file_name?, pic_content_type?, extra_headers?) -> UserAvatar</code>
- <code title="delete /2.0/users/{user_id}/avatar">client.avatars.<a href="./box_sdk_gen/managers/avatars.py">delete_user_avatar</a>(user_id, extra_headers?) -> None</code>

# Transfer

Examples: [docs/transfer.md](docs/transfer.md)

Methods:

- <code title="put /2.0/users/{user_id}/folders/0">client.transfer.<a href="./box_sdk_gen/managers/transfer.py">transfer_owned_folder</a>(user_id, owned_by, fields?, notify?, extra_headers?) -> FolderFull</code>

# Email aliases

Examples: [docs/email_aliases.md](docs/email_aliases.md)

Methods:

- <code title="get /2.0/users/{user_id}/email_aliases">client.email_aliases.<a href="./box_sdk_gen/managers/email_aliases.py">get_user_email_aliases</a>(user_id, extra_headers?) -> EmailAliases</code>
- <code title="post /2.0/users/{user_id}/email_aliases">client.email_aliases.<a href="./box_sdk_gen/managers/email_aliases.py">create_user_email_alias</a>(user_id, email, extra_headers?) -> EmailAlias</code>
- <code title="delete /2.0/users/{user_id}/email_aliases/{email_alias_id}">client.email_aliases.<a href="./box_sdk_gen/managers/email_aliases.py">delete_user_email_alias_by_id</a>(user_id, email_alias_id, extra_headers?) -> None</code>

# Memberships

Examples: [docs/memberships.md](docs/memberships.md)

Methods:

- <code title="get /2.0/users/{user_id}/memberships">client.memberships.<a href="./box_sdk_gen/managers/memberships.py">get_user_memberships</a>(user_id, limit?, offset?, extra_headers?) -> GroupMemberships</code>
- <code title="get /2.0/groups/{group_id}/memberships">client.memberships.<a href="./box_sdk_gen/managers/memberships.py">get_group_memberships</a>(group_id, limit?, offset?, extra_headers?) -> GroupMemberships</code>
- <code title="post /2.0/group_memberships">client.memberships.<a href="./box_sdk_gen/managers/memberships.py">create_group_membership</a>(user, group, role?, configurable_permissions?, fields?, extra_headers?) -> GroupMembership</code>
- <code title="get /2.0/group_memberships/{group_membership_id}">client.memberships.<a href="./box_sdk_gen/managers/memberships.py">get_group_membership_by_id</a>(group_membership_id, fields?, extra_headers?) -> GroupMembership</code>
- <code title="put /2.0/group_memberships/{group_membership_id}">client.memberships.<a href="./box_sdk_gen/managers/memberships.py">update_group_membership_by_id</a>(group_membership_id, role?, configurable_permissions?, fields?, extra_headers?) -> GroupMembership</code>
- <code title="delete /2.0/group_memberships/{group_membership_id}">client.memberships.<a href="./box_sdk_gen/managers/memberships.py">delete_group_membership_by_id</a>(group_membership_id, extra_headers?) -> None</code>

# Invites

Examples: [docs/invites.md](docs/invites.md)

Methods:

- <code title="post /2.0/invites">client.invites.<a href="./box_sdk_gen/managers/invites.py">create_invite</a>(enterprise, actionable_by, fields?, extra_headers?) -> Invite</code>
- <code title="get /2.0/invites/{invite_id}">client.invites.<a href="./box_sdk_gen/managers/invites.py">get_invite_by_id</a>(invite_id, fields?, extra_headers?) -> Invite</code>

# Groups

Examples: [docs/groups.md](docs/groups.md)

Methods:

- <code title="get /2.0/groups">client.groups.<a href="./box_sdk_gen/managers/groups.py">get_groups</a>(filter_term?, fields?, limit?, offset?, extra_headers?) -> Groups</code>
- <code title="post /2.0/groups">client.groups.<a href="./box_sdk_gen/managers/groups.py">create_group</a>(name, provenance?, external_sync_identifier?, description?, invitability_level?, member_viewability_level?, fields?, extra_headers?) -> GroupFull</code>
- <code title="get /2.0/groups/{group_id}">client.groups.<a href="./box_sdk_gen/managers/groups.py">get_group_by_id</a>(group_id, fields?, extra_headers?) -> GroupFull</code>
- <code title="put /2.0/groups/{group_id}">client.groups.<a href="./box_sdk_gen/managers/groups.py">update_group_by_id</a>(group_id, name?, provenance?, external_sync_identifier?, description?, invitability_level?, member_viewability_level?, fields?, extra_headers?) -> GroupFull</code>
- <code title="delete /2.0/groups/{group_id}">client.groups.<a href="./box_sdk_gen/managers/groups.py">delete_group_by_id</a>(group_id, extra_headers?) -> None</code>

# Webhooks

Examples: [docs/webhooks.md](docs/webhooks.md)

Methods:

- <code title="get /2.0/webhooks">client.webhooks.<a href="./box_sdk_gen/managers/webhooks.py">get_webhooks</a>(marker?, limit?, extra_headers?) -> Webhooks</code>
- <code title="post /2.0/webhooks">client.webhooks.<a href="./box_sdk_gen/managers/webhooks.py">create_webhook</a>(target, address, triggers, extra_headers?) -> Webhook</code>
- <code title="get /2.0/webhooks/{webhook_id}">client.webhooks.<a href="./box_sdk_gen/managers/webhooks.py">get_webhook_by_id</a>(webhook_id, extra_headers?) -> Webhook</code>
- <code title="put /2.0/webhooks/{webhook_id}">client.webhooks.<a href="./box_sdk_gen/managers/webhooks.py">update_webhook_by_id</a>(webhook_id, target?, address?, triggers?, extra_headers?) -> Webhook</code>
- <code title="delete /2.0/webhooks/{webhook_id}">client.webhooks.<a href="./box_sdk_gen/managers/webhooks.py">delete_webhook_by_id</a>(webhook_id, extra_headers?) -> None</code>
- <code>client.webhooks.<a href="./box_sdk_gen/managers/webhooks.py">validate_message</a>(body, headers, primary_key, secondary_key?, max_age?) -> bool</code>

# Events

Examples: [docs/events.md](docs/events.md)

Methods:

- <code title="options /2.0/events">client.events.<a href="./box_sdk_gen/managers/events.py">get_events_with_long_polling</a>(extra_headers?) -> RealtimeServers</code>
- <code title="get /2.0/events">client.events.<a href="./box_sdk_gen/managers/events.py">get_events</a>(stream_type?, stream_position?, limit?, event_type?, created_after?, created_before?, extra_headers?) -> Events</code>
- <code>client.events.<a href="./box_sdk_gen/managers/events.py">get_event_stream</a>(query_params?, headers?) -> EventStream</code>

# Collections

Examples: [docs/collections.md](docs/collections.md)

Methods:

- <code title="get /2.0/collections">client.collections.<a href="./box_sdk_gen/managers/collections.py">get_collections</a>(fields?, offset?, limit?, extra_headers?) -> Collections</code>
- <code title="get /2.0/collections/{collection_id}/items">client.collections.<a href="./box_sdk_gen/managers/collections.py">get_collection_items</a>(collection_id, fields?, offset?, limit?, extra_headers?) -> ItemsOffsetPaginated</code>
- <code title="get /2.0/collections/{collection_id}">client.collections.<a href="./box_sdk_gen/managers/collections.py">get_collection_by_id</a>(collection_id, extra_headers?) -> Collection</code>

# Recent items

Examples: [docs/recent_items.md](docs/recent_items.md)

Methods:

- <code title="get /2.0/recent_items">client.recent_items.<a href="./box_sdk_gen/managers/recent_items.py">get_recent_items</a>(fields?, limit?, marker?, extra_headers?) -> RecentItems</code>

# Retention policies

Examples: [docs/retention_policies.md](docs/retention_policies.md)

Methods:

- <code title="get /2.0/retention_policies">client.retention_policies.<a href="./box_sdk_gen/managers/retention_policies.py">get_retention_policies</a>(policy_name?, policy_type?, created_by_user_id?, fields?, limit?, marker?, extra_headers?) -> RetentionPolicies</code>
- <code title="post /2.0/retention_policies">client.retention_policies.<a href="./box_sdk_gen/managers/retention_policies.py">create_retention_policy</a>(policy_name, policy_type, disposition_action, description?, retention_length?, retention_type?, can_owner_extend_retention?, are_owners_notified?, custom_notification_recipients?, extra_headers?) -> RetentionPolicy</code>
- <code title="get /2.0/retention_policies/{retention_policy_id}">client.retention_policies.<a href="./box_sdk_gen/managers/retention_policies.py">get_retention_policy_by_id</a>(retention_policy_id, fields?, extra_headers?) -> RetentionPolicy</code>
- <code title="put /2.0/retention_policies/{retention_policy_id}">client.retention_policies.<a href="./box_sdk_gen/managers/retention_policies.py">update_retention_policy_by_id</a>(retention_policy_id, policy_name?, description?, disposition_action?, retention_type?, retention_length?, status?, can_owner_extend_retention?, are_owners_notified?, custom_notification_recipients?, extra_headers?) -> RetentionPolicy</code>
- <code title="delete /2.0/retention_policies/{retention_policy_id}">client.retention_policies.<a href="./box_sdk_gen/managers/retention_policies.py">delete_retention_policy_by_id</a>(retention_policy_id, extra_headers?) -> None</code>

# Retention policy assignments

Examples: [docs/retention_policy_assignments.md](docs/retention_policy_assignments.md)

Methods:

- <code title="get /2.0/retention_policies/{retention_policy_id}/assignments">client.retention_policy_assignments.<a href="./box_sdk_gen/managers/retention_policy_assignments.py">get_retention_policy_assignments</a>(retention_policy_id, type?, fields?, marker?, limit?, extra_headers?) -> RetentionPolicyAssignments</code>
- <code title="post /2.0/retention_policy_assignments">client.retention_policy_assignments.<a href="./box_sdk_gen/managers/retention_policy_assignments.py">create_retention_policy_assignment</a>(policy_id, assign_to, filter_fields?, start_date_field?, extra_headers?) -> RetentionPolicyAssignment</code>
- <code title="get /2.0/retention_policy_assignments/{retention_policy_assignment_id}">client.retention_policy_assignments.<a href="./box_sdk_gen/managers/retention_policy_assignments.py">get_retention_policy_assignment_by_id</a>(retention_policy_assignment_id, fields?, extra_headers?) -> RetentionPolicyAssignment</code>
- <code title="delete /2.0/retention_policy_assignments/{retention_policy_assignment_id}">client.retention_policy_assignments.<a href="./box_sdk_gen/managers/retention_policy_assignments.py">delete_retention_policy_assignment_by_id</a>(retention_policy_assignment_id, extra_headers?) -> None</code>
- <code title="get /2.0/retention_policy_assignments/{retention_policy_assignment_id}/files_under_retention">client.retention_policy_assignments.<a href="./box_sdk_gen/managers/retention_policy_assignments.py">get_files_under_retention_policy_assignment</a>(retention_policy_assignment_id, marker?, limit?, extra_headers?) -> FilesUnderRetention</code>

# Legal hold policies

Examples: [docs/legal_hold_policies.md](docs/legal_hold_policies.md)

Methods:

- <code title="get /2.0/legal_hold_policies">client.legal_hold_policies.<a href="./box_sdk_gen/managers/legal_hold_policies.py">get_legal_hold_policies</a>(policy_name?, fields?, marker?, limit?, extra_headers?) -> LegalHoldPolicies</code>
- <code title="post /2.0/legal_hold_policies">client.legal_hold_policies.<a href="./box_sdk_gen/managers/legal_hold_policies.py">create_legal_hold_policy</a>(policy_name, description?, filter_started_at?, filter_ended_at?, is_ongoing?, extra_headers?) -> LegalHoldPolicy</code>
- <code title="get /2.0/legal_hold_policies/{legal_hold_policy_id}">client.legal_hold_policies.<a href="./box_sdk_gen/managers/legal_hold_policies.py">get_legal_hold_policy_by_id</a>(legal_hold_policy_id, extra_headers?) -> LegalHoldPolicy</code>
- <code title="put /2.0/legal_hold_policies/{legal_hold_policy_id}">client.legal_hold_policies.<a href="./box_sdk_gen/managers/legal_hold_policies.py">update_legal_hold_policy_by_id</a>(legal_hold_policy_id, policy_name?, description?, release_notes?, extra_headers?) -> LegalHoldPolicy</code>
- <code title="delete /2.0/legal_hold_policies/{legal_hold_policy_id}">client.legal_hold_policies.<a href="./box_sdk_gen/managers/legal_hold_policies.py">delete_legal_hold_policy_by_id</a>(legal_hold_policy_id, extra_headers?) -> None</code>

# Legal hold policy assignments

Examples: [docs/legal_hold_policy_assignments.md](docs/legal_hold_policy_assignments.md)

Methods:

- <code title="get /2.0/legal_hold_policy_assignments">client.legal_hold_policy_assignments.<a href="./box_sdk_gen/managers/legal_hold_policy_assignments.py">get_legal_hold_policy_assignments</a>(policy_id, assign_to_type?, assign_to_id?, marker?, limit?, fields?, extra_headers?) -> LegalHoldPolicyAssignments</code>
- <code title="post /2.0/legal_hold_policy_assignments">client.legal_hold_policy_assignments.<a href="./box_sdk_gen/managers/legal_hold_policy_assignments.py">create_legal_hold_policy_assignment</a>(policy_id, assign_to, extra_headers?) -> LegalHoldPolicyAssignment</code>
- <code title="get /2.0/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}">client.legal_hold_policy_assignments.<a href="./box_sdk_gen/managers/legal_hold_policy_assignments.py">get_legal_hold_policy_assignment_by_id</a>(legal_hold_policy_assignment_id, extra_headers?) -> LegalHoldPolicyAssignment</code>
- <code title="delete /2.0/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}">client.legal_hold_policy_assignments.<a href="./box_sdk_gen/managers/legal_hold_policy_assignments.py">delete_legal_hold_policy_assignment_by_id</a>(legal_hold_policy_assignment_id, extra_headers?) -> None</code>
- <code title="get /2.0/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/files_on_hold">client.legal_hold_policy_assignments.<a href="./box_sdk_gen/managers/legal_hold_policy_assignments.py">get_legal_hold_policy_assignment_file_on_hold</a>(legal_hold_policy_assignment_id, marker?, limit?, fields?, extra_headers?) -> FilesOnHold</code>

# File version retentions

Examples: [docs/file_version_retentions.md](docs/file_version_retentions.md)

Methods:

- <code title="get /2.0/file_version_retentions">client.file_version_retentions.<a href="./box_sdk_gen/managers/file_version_retentions.py">get_file_version_retentions</a>(file_id?, file_version_id?, policy_id?, disposition_action?, disposition_before?, disposition_after?, limit?, marker?, extra_headers?) -> FileVersionRetentions</code>
- <code title="get /2.0/file_version_retentions/{file_version_retention_id}">client.file_version_retentions.<a href="./box_sdk_gen/managers/file_version_retentions.py">get_file_version_retention_by_id</a>(file_version_retention_id, extra_headers?) -> FileVersionRetention</code>

# File version legal holds

Examples: [docs/file_version_legal_holds.md](docs/file_version_legal_holds.md)

Methods:

- <code title="get /2.0/file_version_legal_holds/{file_version_legal_hold_id}">client.file_version_legal_holds.<a href="./box_sdk_gen/managers/file_version_legal_holds.py">get_file_version_legal_hold_by_id</a>(file_version_legal_hold_id, extra_headers?) -> FileVersionLegalHold</code>
- <code title="get /2.0/file_version_legal_holds">client.file_version_legal_holds.<a href="./box_sdk_gen/managers/file_version_legal_holds.py">get_file_version_legal_holds</a>(policy_id, marker?, limit?, extra_headers?) -> FileVersionLegalHolds</code>

# Shield information barriers

Examples: [docs/shield_information_barriers.md](docs/shield_information_barriers.md)

Methods:

- <code title="get /2.0/shield_information_barriers/{shield_information_barrier_id}">client.shield_information_barriers.<a href="./box_sdk_gen/managers/shield_information_barriers.py">get_shield_information_barrier_by_id</a>(shield_information_barrier_id, extra_headers?) -> ShieldInformationBarrier</code>
- <code title="post /2.0/shield_information_barriers/change_status">client.shield_information_barriers.<a href="./box_sdk_gen/managers/shield_information_barriers.py">update_shield_information_barrier_status</a>(id, status, extra_headers?) -> ShieldInformationBarrier</code>
- <code title="get /2.0/shield_information_barriers">client.shield_information_barriers.<a href="./box_sdk_gen/managers/shield_information_barriers.py">get_shield_information_barriers</a>(marker?, limit?, extra_headers?) -> ShieldInformationBarriers</code>
- <code title="post /2.0/shield_information_barriers">client.shield_information_barriers.<a href="./box_sdk_gen/managers/shield_information_barriers.py">create_shield_information_barrier</a>(enterprise, extra_headers?) -> ShieldInformationBarrier</code>

# Shield information barrier reports

Examples: [docs/shield_information_barrier_reports.md](docs/shield_information_barrier_reports.md)

Methods:

- <code title="get /2.0/shield_information_barrier_reports">client.shield_information_barrier_reports.<a href="./box_sdk_gen/managers/shield_information_barrier_reports.py">get_shield_information_barrier_reports</a>(shield_information_barrier_id, marker?, limit?, extra_headers?) -> ShieldInformationBarrierReports</code>
- <code title="post /2.0/shield_information_barrier_reports">client.shield_information_barrier_reports.<a href="./box_sdk_gen/managers/shield_information_barrier_reports.py">create_shield_information_barrier_report</a>(shield_information_barrier?, extra_headers?) -> ShieldInformationBarrierReport</code>
- <code title="get /2.0/shield_information_barrier_reports/{shield_information_barrier_report_id}">client.shield_information_barrier_reports.<a href="./box_sdk_gen/managers/shield_information_barrier_reports.py">get_shield_information_barrier_report_by_id</a>(shield_information_barrier_report_id, extra_headers?) -> ShieldInformationBarrierReport</code>

# Shield information barrier segments

Examples: [docs/shield_information_barrier_segments.md](docs/shield_information_barrier_segments.md)

Methods:

- <code title="get /2.0/shield_information_barrier_segments/{shield_information_barrier_segment_id}">client.shield_information_barrier_segments.<a href="./box_sdk_gen/managers/shield_information_barrier_segments.py">get_shield_information_barrier_segment_by_id</a>(shield_information_barrier_segment_id, extra_headers?) -> ShieldInformationBarrierSegment</code>
- <code title="delete /2.0/shield_information_barrier_segments/{shield_information_barrier_segment_id}">client.shield_information_barrier_segments.<a href="./box_sdk_gen/managers/shield_information_barrier_segments.py">delete_shield_information_barrier_segment_by_id</a>(shield_information_barrier_segment_id, extra_headers?) -> None</code>
- <code title="put /2.0/shield_information_barrier_segments/{shield_information_barrier_segment_id}">client.shield_information_barrier_segments.<a href="./box_sdk_gen/managers/shield_information_barrier_segments.py">update_shield_information_barrier_segment_by_id</a>(shield_information_barrier_segment_id, name?, description?, extra_headers?) -> ShieldInformationBarrierSegment</code>
- <code title="get /2.0/shield_information_barrier_segments">client.shield_information_barrier_segments.<a href="./box_sdk_gen/managers/shield_information_barrier_segments.py">get_shield_information_barrier_segments</a>(shield_information_barrier_id, marker?, limit?, extra_headers?) -> ShieldInformationBarrierSegments</code>
- <code title="post /2.0/shield_information_barrier_segments">client.shield_information_barrier_segments.<a href="./box_sdk_gen/managers/shield_information_barrier_segments.py">create_shield_information_barrier_segment</a>(shield_information_barrier, name, description?, extra_headers?) -> ShieldInformationBarrierSegment</code>

# Shield information barrier segment members

Examples: [docs/shield_information_barrier_segment_members.md](docs/shield_information_barrier_segment_members.md)

Methods:

- <code title="get /2.0/shield_information_barrier_segment_members/{shield_information_barrier_segment_member_id}">client.shield_information_barrier_segment_members.<a href="./box_sdk_gen/managers/shield_information_barrier_segment_members.py">get_shield_information_barrier_segment_member_by_id</a>(shield_information_barrier_segment_member_id, extra_headers?) -> ShieldInformationBarrierSegmentMember</code>
- <code title="delete /2.0/shield_information_barrier_segment_members/{shield_information_barrier_segment_member_id}">client.shield_information_barrier_segment_members.<a href="./box_sdk_gen/managers/shield_information_barrier_segment_members.py">delete_shield_information_barrier_segment_member_by_id</a>(shield_information_barrier_segment_member_id, extra_headers?) -> None</code>
- <code title="get /2.0/shield_information_barrier_segment_members">client.shield_information_barrier_segment_members.<a href="./box_sdk_gen/managers/shield_information_barrier_segment_members.py">get_shield_information_barrier_segment_members</a>(shield_information_barrier_segment_id, marker?, limit?, extra_headers?) -> ShieldInformationBarrierSegmentMembers</code>
- <code title="post /2.0/shield_information_barrier_segment_members">client.shield_information_barrier_segment_members.<a href="./box_sdk_gen/managers/shield_information_barrier_segment_members.py">create_shield_information_barrier_segment_member</a>(shield_information_barrier_segment, user, type?, shield_information_barrier?, extra_headers?) -> ShieldInformationBarrierSegmentMember</code>

# Shield information barrier segment restrictions

Examples: [docs/shield_information_barrier_segment_restrictions.md](docs/shield_information_barrier_segment_restrictions.md)

Methods:

- <code title="get /2.0/shield_information_barrier_segment_restrictions/{shield_information_barrier_segment_restriction_id}">client.shield_information_barrier_segment_restrictions.<a href="./box_sdk_gen/managers/shield_information_barrier_segment_restrictions.py">get_shield_information_barrier_segment_restriction_by_id</a>(shield_information_barrier_segment_restriction_id, extra_headers?) -> ShieldInformationBarrierSegmentRestriction</code>
- <code title="delete /2.0/shield_information_barrier_segment_restrictions/{shield_information_barrier_segment_restriction_id}">client.shield_information_barrier_segment_restrictions.<a href="./box_sdk_gen/managers/shield_information_barrier_segment_restrictions.py">delete_shield_information_barrier_segment_restriction_by_id</a>(shield_information_barrier_segment_restriction_id, extra_headers?) -> None</code>
- <code title="get /2.0/shield_information_barrier_segment_restrictions">client.shield_information_barrier_segment_restrictions.<a href="./box_sdk_gen/managers/shield_information_barrier_segment_restrictions.py">get_shield_information_barrier_segment_restrictions</a>(shield_information_barrier_segment_id, marker?, limit?, extra_headers?) -> ShieldInformationBarrierSegmentRestrictions</code>
- <code title="post /2.0/shield_information_barrier_segment_restrictions">client.shield_information_barrier_segment_restrictions.<a href="./box_sdk_gen/managers/shield_information_barrier_segment_restrictions.py">create_shield_information_barrier_segment_restriction</a>(shield_information_barrier_segment, restricted_segment, type?, shield_information_barrier?, extra_headers?) -> ShieldInformationBarrierSegmentRestriction</code>

# Device pinners

Examples: [docs/device_pinners.md](docs/device_pinners.md)

Methods:

- <code title="get /2.0/device_pinners/{device_pinner_id}">client.device_pinners.<a href="./box_sdk_gen/managers/device_pinners.py">get_device_pinner_by_id</a>(device_pinner_id, extra_headers?) -> DevicePinner</code>
- <code title="delete /2.0/device_pinners/{device_pinner_id}">client.device_pinners.<a href="./box_sdk_gen/managers/device_pinners.py">delete_device_pinner_by_id</a>(device_pinner_id, extra_headers?) -> None</code>
- <code title="get /2.0/enterprises/{enterprise_id}/device_pinners">client.device_pinners.<a href="./box_sdk_gen/managers/device_pinners.py">get_enterprise_device_pinners</a>(enterprise_id, marker?, limit?, direction?, extra_headers?) -> DevicePinners</code>

# Terms of services

Examples: [docs/terms_of_services.md](docs/terms_of_services.md)

Methods:

- <code title="get /2.0/terms_of_services">client.terms_of_services.<a href="./box_sdk_gen/managers/terms_of_services.py">get_terms_of_service</a>(tos_type?, extra_headers?) -> TermsOfServices</code>
- <code title="post /2.0/terms_of_services">client.terms_of_services.<a href="./box_sdk_gen/managers/terms_of_services.py">create_terms_of_service</a>(status, text, tos_type?, extra_headers?) -> TermsOfService</code>
- <code title="get /2.0/terms_of_services/{terms_of_service_id}">client.terms_of_services.<a href="./box_sdk_gen/managers/terms_of_services.py">get_terms_of_service_by_id</a>(terms_of_service_id, extra_headers?) -> TermsOfService</code>
- <code title="put /2.0/terms_of_services/{terms_of_service_id}">client.terms_of_services.<a href="./box_sdk_gen/managers/terms_of_services.py">update_terms_of_service_by_id</a>(terms_of_service_id, status, text, extra_headers?) -> TermsOfService</code>

# Terms of service user statuses

Examples: [docs/terms_of_service_user_statuses.md](docs/terms_of_service_user_statuses.md)

Methods:

- <code title="get /2.0/terms_of_service_user_statuses">client.terms_of_service_user_statuses.<a href="./box_sdk_gen/managers/terms_of_service_user_statuses.py">get_terms_of_service_user_statuses</a>(tos_id, user_id?, extra_headers?) -> TermsOfServiceUserStatuses</code>
- <code title="post /2.0/terms_of_service_user_statuses">client.terms_of_service_user_statuses.<a href="./box_sdk_gen/managers/terms_of_service_user_statuses.py">create_terms_of_service_status_for_user</a>(tos, user, is_accepted, extra_headers?) -> TermsOfServiceUserStatus</code>
- <code title="put /2.0/terms_of_service_user_statuses/{terms_of_service_user_status_id}">client.terms_of_service_user_statuses.<a href="./box_sdk_gen/managers/terms_of_service_user_statuses.py">update_terms_of_service_status_for_user_by_id</a>(terms_of_service_user_status_id, is_accepted, extra_headers?) -> TermsOfServiceUserStatus</code>

# Collaboration allowlist entries

Examples: [docs/collaboration_allowlist_entries.md](docs/collaboration_allowlist_entries.md)

Methods:

- <code title="get /2.0/collaboration_whitelist_entries">client.collaboration_allowlist_entries.<a href="./box_sdk_gen/managers/collaboration_allowlist_entries.py">get_collaboration_whitelist_entries</a>(marker?, limit?, extra_headers?) -> CollaborationAllowlistEntries</code>
- <code title="post /2.0/collaboration_whitelist_entries">client.collaboration_allowlist_entries.<a href="./box_sdk_gen/managers/collaboration_allowlist_entries.py">create_collaboration_whitelist_entry</a>(domain, direction, extra_headers?) -> CollaborationAllowlistEntry</code>
- <code title="get /2.0/collaboration_whitelist_entries/{collaboration_whitelist_entry_id}">client.collaboration_allowlist_entries.<a href="./box_sdk_gen/managers/collaboration_allowlist_entries.py">get_collaboration_whitelist_entry_by_id</a>(collaboration_whitelist_entry_id, extra_headers?) -> CollaborationAllowlistEntry</code>
- <code title="delete /2.0/collaboration_whitelist_entries/{collaboration_whitelist_entry_id}">client.collaboration_allowlist_entries.<a href="./box_sdk_gen/managers/collaboration_allowlist_entries.py">delete_collaboration_whitelist_entry_by_id</a>(collaboration_whitelist_entry_id, extra_headers?) -> None</code>

# Collaboration allowlist exempt targets

Examples: [docs/collaboration_allowlist_exempt_targets.md](docs/collaboration_allowlist_exempt_targets.md)

Methods:

- <code title="get /2.0/collaboration_whitelist_exempt_targets">client.collaboration_allowlist_exempt_targets.<a href="./box_sdk_gen/managers/collaboration_allowlist_exempt_targets.py">get_collaboration_whitelist_exempt_targets</a>(marker?, limit?, extra_headers?) -> CollaborationAllowlistExemptTargets</code>
- <code title="post /2.0/collaboration_whitelist_exempt_targets">client.collaboration_allowlist_exempt_targets.<a href="./box_sdk_gen/managers/collaboration_allowlist_exempt_targets.py">create_collaboration_whitelist_exempt_target</a>(user, extra_headers?) -> CollaborationAllowlistExemptTarget</code>
- <code title="get /2.0/collaboration_whitelist_exempt_targets/{collaboration_whitelist_exempt_target_id}">client.collaboration_allowlist_exempt_targets.<a href="./box_sdk_gen/managers/collaboration_allowlist_exempt_targets.py">get_collaboration_whitelist_exempt_target_by_id</a>(collaboration_whitelist_exempt_target_id, extra_headers?) -> CollaborationAllowlistExemptTarget</code>
- <code title="delete /2.0/collaboration_whitelist_exempt_targets/{collaboration_whitelist_exempt_target_id}">client.collaboration_allowlist_exempt_targets.<a href="./box_sdk_gen/managers/collaboration_allowlist_exempt_targets.py">delete_collaboration_whitelist_exempt_target_by_id</a>(collaboration_whitelist_exempt_target_id, extra_headers?) -> None</code>

# Storage policies

Examples: [docs/storage_policies.md](docs/storage_policies.md)

Methods:

- <code title="get /2.0/storage_policies">client.storage_policies.<a href="./box_sdk_gen/managers/storage_policies.py">get_storage_policies</a>(fields?, marker?, limit?, extra_headers?) -> StoragePolicies</code>
- <code title="get /2.0/storage_policies/{storage_policy_id}">client.storage_policies.<a href="./box_sdk_gen/managers/storage_policies.py">get_storage_policy_by_id</a>(storage_policy_id, extra_headers?) -> StoragePolicy</code>

# Storage policy assignments

Examples: [docs/storage_policy_assignments.md](docs/storage_policy_assignments.md)

Methods:

- <code title="get /2.0/storage_policy_assignments">client.storage_policy_assignments.<a href="./box_sdk_gen/managers/storage_policy_assignments.py">get_storage_policy_assignments</a>(resolved_for_type, resolved_for_id, marker?, extra_headers?) -> StoragePolicyAssignments</code>
- <code title="post /2.0/storage_policy_assignments">client.storage_policy_assignments.<a href="./box_sdk_gen/managers/storage_policy_assignments.py">create_storage_policy_assignment</a>(storage_policy, assigned_to, extra_headers?) -> StoragePolicyAssignment</code>
- <code title="get /2.0/storage_policy_assignments/{storage_policy_assignment_id}">client.storage_policy_assignments.<a href="./box_sdk_gen/managers/storage_policy_assignments.py">get_storage_policy_assignment_by_id</a>(storage_policy_assignment_id, extra_headers?) -> StoragePolicyAssignment</code>
- <code title="put /2.0/storage_policy_assignments/{storage_policy_assignment_id}">client.storage_policy_assignments.<a href="./box_sdk_gen/managers/storage_policy_assignments.py">update_storage_policy_assignment_by_id</a>(storage_policy_assignment_id, storage_policy, extra_headers?) -> StoragePolicyAssignment</code>
- <code title="delete /2.0/storage_policy_assignments/{storage_policy_assignment_id}">client.storage_policy_assignments.<a href="./box_sdk_gen/managers/storage_policy_assignments.py">delete_storage_policy_assignment_by_id</a>(storage_policy_assignment_id, extra_headers?) -> None</code>

# Zip downloads

Examples: [docs/zip_downloads.md](docs/zip_downloads.md)

Methods:

- <code title="post /2.0/zip_downloads">client.zip_downloads.<a href="./box_sdk_gen/managers/zip_downloads.py">create_zip_download</a>(items, download_file_name?, extra_headers?) -> ZipDownload</code>
- <code>client.zip_downloads.<a href="./box_sdk_gen/managers/zip_downloads.py">get_zip_download_content</a>(download_url, extra_headers?) -> ByteStream</code>
- <code>client.zip_downloads.<a href="./box_sdk_gen/managers/zip_downloads.py">get_zip_download_status</a>(status_url, extra_headers?) -> ZipDownloadStatus</code>
- <code>client.zip_downloads.<a href="./box_sdk_gen/managers/zip_downloads.py">download_zip</a>(items, download_file_name?, extra_headers?) -> ByteStream</code>

# Sign requests

Examples: [docs/sign_requests.md](docs/sign_requests.md)

Methods:

- <code title="post /2.0/sign_requests/{sign_request_id}/cancel">client.sign_requests.<a href="./box_sdk_gen/managers/sign_requests.py">cancel_sign_request</a>(sign_request_id, extra_headers?) -> SignRequest</code>
- <code title="post /2.0/sign_requests/{sign_request_id}/resend">client.sign_requests.<a href="./box_sdk_gen/managers/sign_requests.py">resend_sign_request</a>(sign_request_id, extra_headers?) -> None</code>
- <code title="get /2.0/sign_requests/{sign_request_id}">client.sign_requests.<a href="./box_sdk_gen/managers/sign_requests.py">get_sign_request_by_id</a>(sign_request_id, extra_headers?) -> SignRequest</code>
- <code title="get /2.0/sign_requests">client.sign_requests.<a href="./box_sdk_gen/managers/sign_requests.py">get_sign_requests</a>(marker?, limit?, senders?, shared_requests?, extra_headers?) -> SignRequests</code>
- <code title="post /2.0/sign_requests">client.sign_requests.<a href="./box_sdk_gen/managers/sign_requests.py">create_sign_request</a>(signers, source_files?, signature_color?, parent_folder?, is_document_preparation_needed?, redirect_url?, declined_redirect_url?, are_text_signatures_enabled?, email_subject?, email_message?, are_reminders_enabled?, name?, prefill_tags?, days_valid?, external_id?, template_id?, external_system_name?, extra_headers?) -> SignRequest</code>

# Workflows

Examples: [docs/workflows.md](docs/workflows.md)

Methods:

- <code title="get /2.0/workflows">client.workflows.<a href="./box_sdk_gen/managers/workflows.py">get_workflows</a>(folder_id, trigger_type?, limit?, marker?, extra_headers?) -> Workflows</code>
- <code title="post /2.0/workflows/{workflow_id}/start">client.workflows.<a href="./box_sdk_gen/managers/workflows.py">start_workflow</a>(workflow_id, flow, files, folder, type?, outcomes?, extra_headers?) -> None</code>

# Sign templates

Examples: [docs/sign_templates.md](docs/sign_templates.md)

Methods:

- <code title="get /2.0/sign_templates">client.sign_templates.<a href="./box_sdk_gen/managers/sign_templates.py">get_sign_templates</a>(marker?, limit?, extra_headers?) -> SignTemplates</code>
- <code title="get /2.0/sign_templates/{template_id}">client.sign_templates.<a href="./box_sdk_gen/managers/sign_templates.py">get_sign_template_by_id</a>(template_id, extra_headers?) -> SignTemplate</code>

# Integration mappings

Examples: [docs/integration_mappings.md](docs/integration_mappings.md)

Methods:

- <code title="get /2.0/integration_mappings/slack">client.integration_mappings.<a href="./box_sdk_gen/managers/integration_mappings.py">get_slack_integration_mapping</a>(marker?, limit?, partner_item_type?, partner_item_id?, box_item_id?, box_item_type?, is_manually_created?, extra_headers?) -> IntegrationMappings</code>
- <code title="post /2.0/integration_mappings/slack">client.integration_mappings.<a href="./box_sdk_gen/managers/integration_mappings.py">create_slack_integration_mapping</a>(partner_item, box_item, options?, extra_headers?) -> IntegrationMapping</code>
- <code title="put /2.0/integration_mappings/slack/{integration_mapping_id}">client.integration_mappings.<a href="./box_sdk_gen/managers/integration_mappings.py">update_slack_integration_mapping_by_id</a>(integration_mapping_id, box_item?, options?, extra_headers?) -> IntegrationMapping</code>
- <code title="delete /2.0/integration_mappings/slack/{integration_mapping_id}">client.integration_mappings.<a href="./box_sdk_gen/managers/integration_mappings.py">delete_slack_integration_mapping_by_id</a>(integration_mapping_id, extra_headers?) -> None</code>
- <code title="get /2.0/integration_mappings/teams">client.integration_mappings.<a href="./box_sdk_gen/managers/integration_mappings.py">get_teams_integration_mapping</a>(partner_item_type?, partner_item_id?, box_item_id?, box_item_type?, extra_headers?) -> IntegrationMappingsTeams</code>
- <code title="post /2.0/integration_mappings/teams">client.integration_mappings.<a href="./box_sdk_gen/managers/integration_mappings.py">create_teams_integration_mapping</a>(partner_item, box_item, extra_headers?) -> IntegrationMappingTeams</code>
- <code title="put /2.0/integration_mappings/teams/{integration_mapping_id}">client.integration_mappings.<a href="./box_sdk_gen/managers/integration_mappings.py">update_teams_integration_mapping_by_id</a>(integration_mapping_id, box_item?, extra_headers?) -> IntegrationMappingTeams</code>
- <code title="delete /2.0/integration_mappings/teams/{integration_mapping_id}">client.integration_mappings.<a href="./box_sdk_gen/managers/integration_mappings.py">delete_teams_integration_mapping_by_id</a>(integration_mapping_id, extra_headers?) -> None</code>

# Ai

Examples: [docs/ai.md](docs/ai.md)

Methods:

- <code title="post /2.0/ai/ask">client.ai.<a href="./box_sdk_gen/managers/ai.py">create_ai_ask</a>(mode, prompt, items, dialogue_history?, include_citations?, ai_agent?, extra_headers?) -> Optional[AiResponseFull]</code>
- <code title="post /2.0/ai/text_gen">client.ai.<a href="./box_sdk_gen/managers/ai.py">create_ai_text_gen</a>(prompt, items, dialogue_history?, ai_agent?, extra_headers?) -> AiResponse</code>
- <code title="get /2.0/ai_agent_default">client.ai.<a href="./box_sdk_gen/managers/ai.py">get_ai_agent_default_config</a>(mode, language?, model?, extra_headers?) -> Union[AiAgentAsk, AiAgentTextGen, AiAgentExtract, AiAgentExtractStructured]</code>
- <code title="post /2.0/ai/extract">client.ai.<a href="./box_sdk_gen/managers/ai.py">create_ai_extract</a>(prompt, items, ai_agent?, extra_headers?) -> AiResponse</code>
- <code title="post /2.0/ai/extract_structured">client.ai.<a href="./box_sdk_gen/managers/ai.py">create_ai_extract_structured</a>(items, metadata_template?, fields?, ai_agent?, extra_headers?) -> AiExtractStructuredResponse</code>

# Ai studio

Examples: [docs/ai_studio.md](docs/ai_studio.md)

Methods:

- <code title="get /2.0/ai_agents">client.ai_studio.<a href="./box_sdk_gen/managers/ai_studio.py">get_ai_agents</a>(mode?, fields?, agent_state?, include_box_default?, marker?, limit?, extra_headers?) -> AiMultipleAgentResponse</code>
- <code title="post /2.0/ai_agents">client.ai_studio.<a href="./box_sdk_gen/managers/ai_studio.py">create_ai_agent</a>(name, access_state, type?, icon_reference?, allowed_entities?, ask?, text_gen?, extract?, extra_headers?) -> AiSingleAgentResponseFull</code>
- <code title="put /2.0/ai_agents/{agent_id}">client.ai_studio.<a href="./box_sdk_gen/managers/ai_studio.py">update_ai_agent_by_id</a>(agent_id, name, access_state, type?, icon_reference?, allowed_entities?, ask?, text_gen?, extract?, extra_headers?) -> AiSingleAgentResponseFull</code>
- <code title="get /2.0/ai_agents/{agent_id}">client.ai_studio.<a href="./box_sdk_gen/managers/ai_studio.py">get_ai_agent_by_id</a>(agent_id, fields?, extra_headers?) -> AiSingleAgentResponseFull</code>
- <code title="delete /2.0/ai_agents/{agent_id}">client.ai_studio.<a href="./box_sdk_gen/managers/ai_studio.py">delete_ai_agent_by_id</a>(agent_id, extra_headers?) -> None</code>

# Docgen template

Examples: [docs/docgen_template.md](docs/docgen_template.md)

Methods:

- <code title="post /2.0/docgen_templates">client.docgen_template.<a href="./box_sdk_gen/managers/docgen_template.py">create_docgen_template_v2025_r0</a>(file, box_version?, extra_headers?) -> DocGenTemplateBaseV2025R0</code>
- <code title="get /2.0/docgen_templates">client.docgen_template.<a href="./box_sdk_gen/managers/docgen_template.py">get_docgen_templates_v2025_r0</a>(marker?, limit?, box_version?, extra_headers?) -> DocGenTemplatesV2025R0</code>
- <code title="delete /2.0/docgen_templates/{template_id}">client.docgen_template.<a href="./box_sdk_gen/managers/docgen_template.py">delete_docgen_template_by_id_v2025_r0</a>(template_id, box_version?, extra_headers?) -> None</code>
- <code title="get /2.0/docgen_templates/{template_id}">client.docgen_template.<a href="./box_sdk_gen/managers/docgen_template.py">get_docgen_template_by_id_v2025_r0</a>(template_id, box_version?, extra_headers?) -> DocGenTemplateV2025R0</code>
- <code title="get /2.0/docgen_templates/{template_id}/tags">client.docgen_template.<a href="./box_sdk_gen/managers/docgen_template.py">get_docgen_template_tags_v2025_r0</a>(template_id, template_version_id?, marker?, limit?, box_version?, extra_headers?) -> DocGenTagsV2025R0</code>
- <code title="get /2.0/docgen_template_jobs/{template_id}">client.docgen_template.<a href="./box_sdk_gen/managers/docgen_template.py">get_docgen_template_job_by_id_v2025_r0</a>(template_id, marker?, limit?, box_version?, extra_headers?) -> DocGenJobsV2025R0</code>

# Docgen

Examples: [docs/docgen.md](docs/docgen.md)

Methods:

- <code title="get /2.0/docgen_jobs/{job_id}">client.docgen.<a href="./box_sdk_gen/managers/docgen.py">get_docgen_job_by_id_v2025_r0</a>(job_id, box_version?, extra_headers?) -> DocGenJobV2025R0</code>
- <code title="get /2.0/docgen_jobs">client.docgen.<a href="./box_sdk_gen/managers/docgen.py">get_docgen_jobs_v2025_r0</a>(marker?, limit?, box_version?, extra_headers?) -> DocGenJobsFullV2025R0</code>
- <code title="get /2.0/docgen_batch_jobs/{batch_id}">client.docgen.<a href="./box_sdk_gen/managers/docgen.py">get_docgen_batch_job_by_id_v2025_r0</a>(batch_id, marker?, limit?, box_version?, extra_headers?) -> DocGenJobsV2025R0</code>
- <code title="post /2.0/docgen_batches">client.docgen.<a href="./box_sdk_gen/managers/docgen.py">create_docgen_batch_v2025_r0</a>(file, input_source, destination_folder, output_type, document_generation_data, file_version?, box_version?, extra_headers?) -> DocGenBatchBaseV2025R0</code>

# Hubs

Examples: [docs/hubs.md](docs/hubs.md)

Methods:

- <code title="get /2.0/hubs">client.hubs.<a href="./box_sdk_gen/managers/hubs.py">get_hubs_v2025_r0</a>(query?, scope?, sort?, direction?, marker?, limit?, box_version?, extra_headers?) -> HubsV2025R0</code>
- <code title="post /2.0/hubs">client.hubs.<a href="./box_sdk_gen/managers/hubs.py">create_hub_v2025_r0</a>(title, description?, box_version?, extra_headers?) -> HubV2025R0</code>
- <code title="get /2.0/enterprise_hubs">client.hubs.<a href="./box_sdk_gen/managers/hubs.py">get_enterprise_hubs_v2025_r0</a>(query?, sort?, direction?, marker?, limit?, box_version?, extra_headers?) -> HubsV2025R0</code>
- <code title="get /2.0/hubs/{hub_id}">client.hubs.<a href="./box_sdk_gen/managers/hubs.py">get_hub_by_id_v2025_r0</a>(hub_id, box_version?, extra_headers?) -> HubV2025R0</code>
- <code title="put /2.0/hubs/{hub_id}">client.hubs.<a href="./box_sdk_gen/managers/hubs.py">update_hub_by_id_v2025_r0</a>(hub_id, title?, description?, is_ai_enabled?, is_collaboration_restricted_to_enterprise?, can_non_owners_invite?, can_shared_link_be_created?, box_version?, extra_headers?) -> HubV2025R0</code>
- <code title="delete /2.0/hubs/{hub_id}">client.hubs.<a href="./box_sdk_gen/managers/hubs.py">delete_hub_by_id_v2025_r0</a>(hub_id, box_version?, extra_headers?) -> None</code>
- <code title="post /2.0/hubs/{hub_id}/copy">client.hubs.<a href="./box_sdk_gen/managers/hubs.py">copy_hub_v2025_r0</a>(hub_id, title?, description?, box_version?, extra_headers?) -> HubV2025R0</code>

# Hub collaborations

Examples: [docs/hub_collaborations.md](docs/hub_collaborations.md)

Methods:

- <code title="get /2.0/hub_collaborations">client.hub_collaborations.<a href="./box_sdk_gen/managers/hub_collaborations.py">get_hub_collaborations_v2025_r0</a>(hub_id, marker?, limit?, box_version?, extra_headers?) -> HubCollaborationsV2025R0</code>
- <code title="post /2.0/hub_collaborations">client.hub_collaborations.<a href="./box_sdk_gen/managers/hub_collaborations.py">create_hub_collaboration_v2025_r0</a>(hub, accessible_by, role, box_version?, extra_headers?) -> HubCollaborationV2025R0</code>
- <code title="get /2.0/hub_collaborations/{hub_collaboration_id}">client.hub_collaborations.<a href="./box_sdk_gen/managers/hub_collaborations.py">get_hub_collaboration_by_id_v2025_r0</a>(hub_collaboration_id, box_version?, extra_headers?) -> HubCollaborationV2025R0</code>
- <code title="put /2.0/hub_collaborations/{hub_collaboration_id}">client.hub_collaborations.<a href="./box_sdk_gen/managers/hub_collaborations.py">update_hub_collaboration_by_id_v2025_r0</a>(hub_collaboration_id, role?, box_version?, extra_headers?) -> HubCollaborationV2025R0</code>
- <code title="delete /2.0/hub_collaborations/{hub_collaboration_id}">client.hub_collaborations.<a href="./box_sdk_gen/managers/hub_collaborations.py">delete_hub_collaboration_by_id_v2025_r0</a>(hub_collaboration_id, box_version?, extra_headers?) -> None</code>

# Hub items

Examples: [docs/hub_items.md](docs/hub_items.md)

Methods:

- <code title="get /2.0/hub_items">client.hub_items.<a href="./box_sdk_gen/managers/hub_items.py">get_hub_items_v2025_r0</a>(hub_id, marker?, limit?, box_version?, extra_headers?) -> HubItemsV2025R0</code>
- <code title="post /2.0/hubs/{hub_id}/manage_items">client.hub_items.<a href="./box_sdk_gen/managers/hub_items.py">manage_hub_items_v2025_r0</a>(hub_id, operations?, box_version?, extra_headers?) -> HubItemsManageResponseV2025R0</code>

# Shield lists

Examples: [docs/shield_lists.md](docs/shield_lists.md)

Methods:

- <code title="get /2.0/shield_lists">client.shield_lists.<a href="./box_sdk_gen/managers/shield_lists.py">get_shield_lists_v2025_r0</a>(box_version?, extra_headers?) -> ShieldListsV2025R0</code>
- <code title="post /2.0/shield_lists">client.shield_lists.<a href="./box_sdk_gen/managers/shield_lists.py">create_shield_list_v2025_r0</a>(name, content, description?, box_version?, extra_headers?) -> ShieldListV2025R0</code>
- <code title="get /2.0/shield_lists/{shield_list_id}">client.shield_lists.<a href="./box_sdk_gen/managers/shield_lists.py">get_shield_list_by_id_v2025_r0</a>(shield_list_id, box_version?, extra_headers?) -> ShieldListV2025R0</code>
- <code title="delete /2.0/shield_lists/{shield_list_id}">client.shield_lists.<a href="./box_sdk_gen/managers/shield_lists.py">delete_shield_list_by_id_v2025_r0</a>(shield_list_id, box_version?, extra_headers?) -> None</code>
- <code title="put /2.0/shield_lists/{shield_list_id}">client.shield_lists.<a href="./box_sdk_gen/managers/shield_lists.py">update_shield_list_by_id_v2025_r0</a>(shield_list_id, name, content, description?, box_version?, extra_headers?) -> ShieldListV2025R0</code>

# Archives

Examples: [docs/archives.md](docs/archives.md)

Methods:

- <code title="get /2.0/archives">client.archives.<a href="./box_sdk_gen/managers/archives.py">get_archives_v2025_r0</a>(limit?, marker?, box_version?, extra_headers?) -> ArchivesV2025R0</code>
- <code title="post /2.0/archives">client.archives.<a href="./box_sdk_gen/managers/archives.py">create_archive_v2025_r0</a>(name, box_version?, extra_headers?) -> ArchiveV2025R0</code>
- <code title="delete /2.0/archives/{archive_id}">client.archives.<a href="./box_sdk_gen/managers/archives.py">delete_archive_by_id_v2025_r0</a>(archive_id, box_version?, extra_headers?) -> None</code>
