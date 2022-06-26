# Celestial

a Python Discord chat bot who can talk with you in English and Thai.

Invite our bot **[here](https://discord.com/api/oauth2/authorize?client_id=927573556961869825&permissions=283669424144&scope=bot)**.

## Usage

You can talk to the bot by DM the bot or invite the bot to your server and type

```txt
<usr> your message goes here
```

to send your message to the bot.

### Examples

<img src = https://github.com/StrixzIV/Celestial/raw/master/Preview.png />

## Dependencies & Tools

this project required Python 3.8 or newer and **[Nextcord](https://github.com/nextcord/nextcord)** asDiscord API wrapper and **[PyThaiNLP](https://github.com/PyThaiNLP/pythainlp)** for word tokenizing.

You can download the dependencies for development by using command:

```sh
pip install --upgrade -r requirements.txt
```

## Testing & Debugging

You can test the outcome of your intents by running **[this](https://github.com/StrixzIV/Celestial/blob/master/cli_tester.py)** testing python file.

This testing file show the tokenized input messages and how the bot is responding back to you in command-line interface.

```sh
python cli_tester.py
```

## Contributions

You can contribute to this project by updating the **[responses.json](https://github.com/StrixzIV/Celestial/blob/master/responses.json)**, **[responses_th.json](https://github.com/StrixzIV/Celestial/blob/master/responses_th.json)** and **[badwords.json](https://github.com/StrixzIV/Celestial/blob/master/badwords.json)**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

* **[MIT License](https://github.com/StrixzIV/Celestial/blob/master/LICENSE)**
