# SkillsManager

## List Box Skill cards on file

List the Box Skills metadata cards that are attached to a file.

This operation is performed by calling function `get_file_metadata_global_box_skills_cards`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-metadata-global-box-skills-cards/).

*Currently we don't have an example for calling `get_file_metadata_global_box_skills_cards` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call


### Returns

This function returns a value of type `SkillCardsMetadata`.

Returns all the metadata associated with a file.

This API does not support pagination and will therefore always return
all of the metadata associated to the file.


## Create Box Skill cards on file

Applies one or more Box Skills metadata cards to a file.

This operation is performed by calling function `create_file_metadata_global_box_skills_card`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-files-id-metadata-global-box-skills-cards/).

*Currently we don't have an example for calling `create_file_metadata_global_box_skills_card` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- request_body `CreateFileMetadataGlobalBoxSkillsCardRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `SkillCardsMetadata`.

Returns the instance of the template that was applied to the file,
including the data that was applied to the template.


## Remove Box Skill cards from file

Removes any Box Skills cards metadata from a file.

This operation is performed by calling function `delete_file_metadata_global_box_skills_card`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-files-id-metadata-global-box-skills-cards/).

*Currently we don't have an example for calling `delete_file_metadata_global_box_skills_card` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Returns an empty response when the cards are
successfully deleted.


## Update all Box Skill cards on file

An alternative method that can be used to overwrite and update all Box Skill
metadata cards on a file.

This operation is performed by calling function `update_skill_invocation_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-skill-invocations-id/).

*Currently we don't have an example for calling `update_skill_invocation_by_id` in integration tests*

### Arguments

- skill_id `str`
  - The ID of the skill to apply this metadata for.
  - Used as `skill_id` in path `path` of the API call
- request_body `UpdateSkillInvocationByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `None`.

Returns an empty response when the card has been successfully updated.


