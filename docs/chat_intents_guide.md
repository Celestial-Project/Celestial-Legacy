# Chat intents development guide

This is a guide for Celestial's chat intents development

## Non-festival chat intents

This kind of chat intents is use for normal chat responses that does not required a datetime data

### Example

```json
"thanks": {
    "response": ["Thank you!"],
    "list_of_words": [
        "i", "love", "like", "this", "bot"
    ],
    "is_single_response": false,
    "required_word": ["love", "bot"]
},
```

* **response**: Message that the bot will replied
* **list_of_word**: A keyword list that you want to detect in the input message
* **is_single_response**: Is those keyword only come in a single word input
* **required_word**: A keyword list that required for the response to happened
