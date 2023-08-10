# SkillsManager


- [List Box Skill cards on file](#list-box-skill-cards-on-file)
- [Create Box Skill cards on file](#create-box-skill-cards-on-file)
- [Update Box Skill cards on file](#update-box-skill-cards-on-file)
- [Remove Box Skill cards from file](#remove-box-skill-cards-from-file)
- [Update all Box Skill cards on file](#update-all-box-skill-cards-on-file)

## List Box Skill cards on file

List the Box Skills metadata cards that are attached to a file.

This operation is performed by calling function `get_file_metadata_global_box_skills_cards`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-metadata-global-box-skills-cards/).

*Currently we don't have an example for calling `get_file_metadata_global_box_skills_cards` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`. Example: "12345"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


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
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`. Example: "12345"
- cards `List[Union[KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]`
  - A list of Box Skill cards to apply to this file.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `SkillCardsMetadata`.

Returns the instance of the template that was applied to the file,
including the data that was applied to the template.


## Update Box Skill cards on file

Updates one or more Box Skills metadata cards to a file.

This operation is performed by calling function `update_file_metadata_global_box_skills_card`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-files-id-metadata-global-box-skills-cards/).

*Currently we don't have an example for calling `update_file_metadata_global_box_skills_card` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`. Example: "12345"
- request_body `List[UpdateFileMetadataGlobalBoxSkillsCardRequestBodyArg]`
  - Request body of updateFileMetadataGlobalBoxSkillsCard method
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `SkillCardsMetadata`.

Returns the updated metadata template, with the
custom template data included.


## Remove Box Skill cards from file

Removes any Box Skills cards metadata from a file.

This operation is performed by calling function `delete_file_metadata_global_box_skills_card`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-files-id-metadata-global-box-skills-cards/).

*Currently we don't have an example for calling `delete_file_metadata_global_box_skills_card` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`. Example: "12345"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


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
  - The ID of the skill to apply this metadata for. Example: "33243242"
- status `UpdateSkillInvocationByIdStatusArg`
  - Defines the status of this invocation. Set this to `success` when setting Skill cards.
- metadata `UpdateSkillInvocationByIdMetadataArg`
  - The metadata to set for this skill. This is a list of Box Skills cards. These cards will overwrite any existing Box skill cards on the file.
- file `UpdateSkillInvocationByIdFileArg`
  - The file to assign the cards to.
- file_version `Optional[UpdateSkillInvocationByIdFileVersionArg]`
  - The optional file version to assign the cards to.
- usage `Optional[UpdateSkillInvocationByIdUsageArg]`
  - A descriptor that defines what items are affected by this call.  Set this to the default values when setting a card to a `success` state, and leave it out in most other situations.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `None`.

Returns an empty response when the card has been successfully updated.


