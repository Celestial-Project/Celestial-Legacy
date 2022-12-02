# Chat Intent Development Manual

This is a guide for Celestial's chat intent development.

## Non-festival chat intents

This kind of chat intent is used for normal chat responses that do not require datetime data.

```json
"thanks": {
    "response": ["Thank you!"],
    "list_of_words": [
        "i", "love", "like", "this", "bot"
    ],
    "is_single_response": false,
    "required_word": ["love", "bot"]
}
```

* **response**: a list of messages that the bot will respond to.
* **list_of_word**: A keyword list that you want to detect in the input message
* **is_single_response**: Is that those keywords are only available as single words?
* **required_word**: A list of words that must be typed in order for the response to occur.

## Festival chat intents

A chat intent that outputs a cetrain message by combining datetime and keyword detection.

### A one-day festival

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
}
```

* **response**: A list of messages to which the bot will respond If the dates are the same, the bot will respond with its first response. If not, it will reply with the second response.
* **list_of_word**: A keyword list that you want to detect in the input message
* **is_single_response**: Is that those keywords are only available as single words?
* **required_word**: A list of words that must be typed in order for the response to occur.
* **date**: the day the festival is held
* **month**: the month in which the festival is held.

### Variable-length festival

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

* **response**: A list of messages to which the bot will respond If the dates are the same, the bot will respond with its first response. If not, it will reply with the second response.
* **list_of_word**: A keyword list that you want to detect in the input message
* **is_single_response**: Is that those keywords are only available as single words?
* **required_word**: A list of words that must be typed in order for the response to occur.
* **date**: a date range for which the festival is held(For this example, the date range is January 1 to January 2.)
* **month**: the month in which the festival is held.
