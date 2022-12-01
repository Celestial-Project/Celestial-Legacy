# Chat intents development guide

This is a guide for Celestial's chat intents development

## Non-festival chat intents

This kind of chat intents is use for normal chat responses that does not required a datetime data

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

* **response**: List of message that the bot will replied (If the date is match, the bot will reply with first response. If not, it will reply with the second response)
* **list_of_word**: A keyword list that you want to detect in the input message
* **is_single_response**: Is those keyword only come in a single word input
* **required_word**: A keyword list that required for the response to happened

## Festival chat intents

A chat intents that uses datetime with the keyword detection to output a cetrain message

### Single-day festival

```json
"new_year_en": {
    "response": [
        "Happy new year! I hope next year would be a great year!",
        "It's not new year yet."
    ],
    "list_of_words": ["happy", "new", "year"],
    "is_single_response": false,
    "required_word": ["new", "year"],
    "date": 31,
    "month": 12
},
```

* **response**: List of message that the bot will replied (If the date is match, the bot will reply with first response. If not, it will reply with the second response)
* **list_of_word**: A keyword list that you want to detect in the input message
* **is_single_response**: Is those keyword only come in a single word input
* **required_word**: A keyword list that required for the response to happened
* **date**: a date that the festival is taken
* **month**: a month that the festival is taken

### Multiple-day (ranged) festival

```json
"new_year2_en": {
    "response": [
        "Happy new year! I hope this year would be a great year!",
        "It's not new year yet."
    ],
    "list_of_words": ["happy", "new", "year"],
    "is_single_response": false,
    "required_word": ["new", "year"],
    "date": [1, 2],
    "month": 1
}
```

* **response**: List of message that the bot will replied (If the date is match, the bot will reply with first response. If not, it will reply with the second response)
* **list_of_word**: A keyword list that you want to detect in the input message
* **is_single_response**: Is those keyword only come in a single word input
* **required_word**: A keyword list that required for the response to happened
* **date**: a date range that the festival is taken (For this example, the date range is 1st January to 2nd January)
* **month**: a month that the festival is taken
