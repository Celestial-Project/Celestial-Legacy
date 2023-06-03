import os
import git 
import discord
import argparse
import chat_response

from importlib import reload
from dotenv import load_dotenv
from discord.ext import commands

from logger import info_log, error_log

flags_parser = argparse.ArgumentParser()
flags_parser.add_argument('-d', '--debug', action='store_true')

use_debug_mode = flags_parser.parse_args().debug

intents = discord.Intents.default()
intents.message_content = True

bot_channel_name = 'legacy-celestial-chat'

client = commands.Bot(
    command_prefix = '::<!' if use_debug_mode else '<!', 
    intents = intents, 
    help_command = None,
    activity = discord.Game(name = '/help for more info.')
)

def is_owner(interaction: discord.Interaction) -> bool:
    
    '''
        Check if the command user is authorized.
    '''
    
    return interaction.user.id in moderator_ids
    

@client.event
async def on_ready() -> None:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    try:
        synced = await client.tree.sync()
        info_log(f'Synced: {len(synced)} commands' if len(synced) != 1 else f'Synced: {len(synced)} command')
        
    except Exception as e:
        error_log(f'Exception detected: \n{e}')
    
    info_log(f'Status: {"Debug" if use_debug_mode else "Production"}')
    info_log(f'Successfully logged in as: {client.user}')


@client.event
async def on_message(message: discord.Message) -> None:

    if message.channel.name == bot_channel_name and message.author != client.user:
        chat_message = message.content.strip()
        await message.channel.send(chat_response.get_response(chat_message, debug = use_debug_mode))

    await client.process_commands(message)


@client.tree.command(name = 'setup-chat', description = 'Setup a text channel for Celestial chat.')
async def setup_chat(interaction: discord.Interaction) -> None:
    
    guild = interaction.guild
    channel_list = [ch.name for ch in guild.text_channels]
    
    if bot_channel_name in channel_list:
        await interaction.response.send_message(f'<#{discord.utils.get(guild.text_channels, name = bot_channel_name).id}> is already existed.')
        return
    
    await guild.create_text_channel(bot_channel_name)
    await interaction.response.send_message('Setup complete!')


@client.tree.command(name = 'help', description = 'Display a help message.')
async def helper(interaction: discord.Interaction) -> None:
    
    help_embed = discord.Embed(
        title = '', 
        description = 'a Python Discord chat bot who can talk with you in English and Thai.', 
        color = 0xd357fe
    )
    
    help_embed.set_author(
        name = 'Celestial#0135', 
        icon_url = client.user.avatar._url
    )
    
    help_embed.add_field(
        name = 'How can you talk to me?', 
        value = 'Use `/setup-chat` to setup text channel for me first and then you could just send me a message now.', 
        inline = False
    )
    
    help_embed.add_field(
        name = 'Report Issue', 
        value = 'If there is a problem with the bot response or any bug with the bot, feel free to **[report](https://github.com/Celestial-Project/Celestial-Legacy/issues/new/choose)** those problems to us.', 
        inline = True
    )
    
    help_embed.add_field(
        name = 'Development & Update', 
        value = 'Follow the latest update on our **[Github repository](https://github.com/Celestial-Project/Celestial-Legacy)**.', 
        inline = False
    )
    
    help_embed.set_footer(text = '© 2022 MIT License - StrixzIV#6258, Peachpiggies#9229')
    
    await interaction.response.send_message(embed = help_embed)
    
    
@client.tree.command(name = 'reload', description = '*For developers only*')
@commands.check(is_owner)
async def reload_bot(interaction: discord.Interaction) -> None:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    info_log('Reloading...')
    
    reload(chat_response)
    
    info_log('Chat module reload successfully!')
    info_log(f'Reload command sended from {interaction.user}')
    
    await interaction.response.send_message('Reload completed!')
    

@reload_bot.error
async def on_reload_error(interaction: discord.Interaction, error: commands.errors) -> None:
    
    error_embed = discord.Embed(
        title = '⚠️ Permission Error ⚠️', 
        description = 'Reload attempt from non-authorized user.', 
        color = 0xFF0000
    )
    
    error_log(f'Error: Reload attempt from {interaction.user} which is not an authorized user.')
    await interaction.response.send_message(embed=error_embed)
    
    
@client.tree.command(name = 'pull', description = '*For developers only*') 
@commands.check(is_owner)
async def pull(interaction: discord.Interaction) -> None:
    
    info_log('Pulling from origin...')
    
    repo = git.Repo(os.getcwd())
    repo.remote('origin').pull()
    
    info_log('Pull complete.')
    info_log('Reloading chat module...')
    
    reload(chat_response)
    
    info_log('Chat module reload successfully!')
    info_log(f'Pull command sended from {interaction.user}')
    
    await interaction.response.send_message('Pull completed!')
    
    
@pull.error
async def on_pull_error(interaction: discord.Interaction, error: commands.errors) -> None:
    
    error_embed = discord.Embed(
        title = '⚠️ Permission Error ⚠️', 
        description = 'Pull attempt from non-authorized user.', 
        color = 0xFF0000
    )
    
    error_log(f'Error: Pull attempt from {interaction.user} which is not an authorized user.')
    await interaction.response.send_message(embed=error_embed)
    

if __name__ == '__main__':

    load_dotenv()
    moderator_ids = set([int(ids) for (key, ids) in os.environ.items() if key.startswith('ID')])
    
    client.run(os.getenv('TOKEN'))