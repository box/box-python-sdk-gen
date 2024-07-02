# AiManager

- [Send AI question request](#send-ai-question-request)
- [Send AI request to generate text](#send-ai-request-to-generate-text)

## Send AI question request

Sends an AI request to supported LLMs and returns an answer specifically focused on the user's question given the provided context.

This operation is performed by calling function `create_ai_ask`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-ai-ask/).

<!-- sample post_ai_ask -->

```python
client.ai.create_ai_ask(
    CreateAiAskMode.MULTIPLE_ITEM_QA.value,
    "Which direction sun rises?",
    [
        CreateAiAskItems(
            id=file_to_ask_1.id,
            type=CreateAiAskItemsTypeField.FILE.value,
            content="Earth goes around the sun",
        ),
        CreateAiAskItems(
            id=file_to_ask_2.id,
            type=CreateAiAskItemsTypeField.FILE.value,
            content="Sun rises in the East in the morning",
        ),
    ],
)
```

### Arguments

- mode `CreateAiAskMode`
  - The mode specifies if this request is for a single or multiple items. If you select `single_item_qa` the `items` array can have one element only. Selecting `multiple_item_qa` allows you to provide up to 25 items.
- prompt `str`
  - The prompt provided by the client to be answered by the LLM. The prompt's length is limited to 10000 characters.
- items `List[CreateAiAskItems]`
  - The items to be processed by the LLM, often files. **Note**: Box AI handles documents with text representations up to 1MB in size, or a maximum of 25 files, whichever comes first. If the file size exceeds 1MB, the first 1MB of text representation will be processed. If you set `mode` parameter to `single_item_qa`, the `items` array can have one element only.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `AiResponse`.

A successful response including the answer from the LLM.

## Send AI request to generate text

Sends an AI request to supported LLMs and returns an answer specifically focused on the creation of new text.

This operation is performed by calling function `create_ai_text_gen`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-ai-text-gen/).

<!-- sample post_ai_text_gen -->

```python
client.ai.create_ai_text_gen(
    "Parapharse the document.s",
    [
        CreateAiTextGenItems(
            id=file_to_ask.id,
            type=CreateAiTextGenItemsTypeField.FILE.value,
            content="The Earth goes around the sun. Sun rises in the East in the morning.",
        )
    ],
    dialogue_history=[
        CreateAiTextGenDialogueHistory(
            prompt="What does the earth go around?",
            answer="The sun",
            created_at=date_time_from_string("2021-01-01T00:00:00Z"),
        ),
        CreateAiTextGenDialogueHistory(
            prompt="On Earth, where does the sun rise?",
            answer="East",
            created_at=date_time_from_string("2021-01-01T00:00:00Z"),
        ),
    ],
)
```

### Arguments

- prompt `str`
  - The prompt provided by the client to be answered by the LLM. The prompt's length is limited to 10000 characters.
- items `List[CreateAiTextGenItems]`
  - The items to be processed by the LLM, often files. The array can include **exactly one** element. **Note**: Box AI handles documents with text representations up to 1MB in size. If the file size exceeds 1MB, the first 1MB of text representation will be processed.
- dialogue_history `Optional[List[CreateAiTextGenDialogueHistory]]`
  - The history of prompts and answers previously passed to the LLM. This provides additional context to the LLM in generating the response.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `AiResponse`.

A successful response including the answer from the LLM.
