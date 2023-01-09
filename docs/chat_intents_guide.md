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
    "response": {
        "fes": [
            "Happy new year! I hope next year would be a great year!"
        ],
        "nonfes": [
            "It's not new year yet."
        ]
    },
    "list_of_words": ["happy", "new", "year"],
    "is_single_response": false,
    "required_word": ["new", "year"],
    "date": 31,
    "month": 12
}
```

* **response**: A response object with two keys, fes and nonfes, each corresponding to a list of messages. If the current date is the same as the festival date, the bot will respond with a message from the fes list. If not, it will reply with a message from the nonfes list.
* **list_of_word**: A keyword list that you want to detect in the input message
* **is_single_response**: Is that those keywords are only available as single words?
* **required_word**: A list of words that must be typed in order for the response to occur.
* **date**: the day the festival is held
* **month**: the month in which the festival is held.

### Variable-length festival

```json
"new_year2_en": {
    "response": {
        "fes": [
            "Happy new year! I hope next year would be a great year!"
        ],
        "nonfes": [
            "It's not new year yet."
        ]
    },
    "list_of_words": ["happy", "new", "year"],
    "is_single_response": false,
    "required_word": ["new", "year"],
    "date": [1, 2],
    "month": 1
}
```

* **response**: A response object with two keys, fes and nonfes, each corresponding to a list of messages. If the current date is in festival date range, the bot will respond with a message from the fes list. If not, it will reply with a message from the nonfes list.
* **list_of_word**: A keyword list that you want to detect in the input message
* **is_single_response**: Is that those keywords are only available as single words?
* **required_word**: A list of words that must be typed in order for the response to occur.
* **date**: a date range for which the festival is held(For this example, the date range is January 1 to January 2.)
* **month**: the month in which the festival is held.

## Special variable

Special variables are variables that have a predefined with the data of the bot.

These special variables can be used in the response field of a JSON object to include dynamic information in the chatbot's responses.

Using special variables allows the chatbot to provide more relevant and personalized responses to the user, and can make the conversation feel more dynamic and interactive.

### List of variables

* `$age`: The number of years since the first commit (or "birthday" of the system).
* `$time`: The current 24-hour local time in the format "HH:MM:SS" of the server running Celestial.
* `$timezone`: The local timezone of the server running Celestial.

To implement these variables, you can use them in the response field of your JSON object, like this:

```json
"age": {
    "response": [
      "I'm $age year old now!"
    ],
    "list_of_words": ["how", "old", "are", "you"],
    "is_single_response": false,
    "required_word": ["old"]
  }
```

```json
"time": {
    "response": [
      "It's $time in my timezone now (UTC $timezone). How about you?"
    ],
    "list_of_words": ["what", "time"],
    "is_single_response": false,
    "required_word": ["time"]
  }
```
