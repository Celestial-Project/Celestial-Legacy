# Celestial

![Build Status](https://github.com/StrixzIV/Celestial/actions/workflows/test-and-lint.yml/badge.svg)

a Python Discord chat bot who can talk with you in English and Thai.

This project use **[LST20 Corpus](https://huggingface.co/datasets/lst20)** dataset from NECTEC as a base for the chat processing module.

The full documentation of the corpus is available **[here](https://arxiv.org/pdf/2008.05055.pdf)** for more details.

Invite our bot **[here](https://discord.com/api/oauth2/authorize?client_id=927573556961869825&permissions=283669424144&scope=bot)**.

## Usage

You can talk to the bot by DM the bot or invite the bot to your server and type

```txt
<usr> your message goes here
```

to send your message to the bot.

### Examples

![Preview](./assets/Preview.png)

## Dependencies & Tools

This project required Python 3.9 or higher.
This project uses **[Nextcord](https://github.com/nextcord/nextcord)** as Discord API wrapper and **[PyThaiNLP](https://github.com/PyThaiNLP/pythainlp)** for word tokenizing.

You can take a look of a dependencies list **[here](./requirements.txt)**.

You can download the dependencies for development by using command:

```sh
pip install --upgrade -r requirements.txt
```

## Testing & Debugging

You can test the outcome of your intents by running interactive intents tester from **[this](./cli_tester.py)** file.

This testing file show the tokenized input messages and how the bot is responding back to you in command-line interface.

```sh
python cli_tester.py
```

### Examples of intents tester

![command-line tester](./assets/cli-test-preview.png)

### Unit testing

This project use pytest for testing.

You can update the test case by editing files in **[tests](./tests/)** directory.

To run the unit testing, use command:

```sh
pytest
```

## Contributions

You can contribute to this project by updating the intents JSON files in **[responses](./responses)** folder.

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Make sure to read our code of conduct **[here](./CODE_OF_CONDUCT.md)** before start contributing to our project.

Please make sure to update tests as appropriate.

## License

* **[MIT License](./LICENSE)**
