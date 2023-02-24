import os
import git 
import discord
import argparse
import chat_response

from importlib import reload
from dotenv import load_dotenv
from discord.ext import commands

flags_parser = argparse.ArgumentParser()
flags_parser.add_argument('-d', '--debug', action='store_true')

use_debug_mode = flags_parser.parse_args().debug

intents = discord.Intents.default()
intents.message_content = True

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
        print(f'\u001b[45;1m ** \u001b[0m Synced: {len(synced)} commands' if len(synced) != 1 else f'\u001b[45;1m ** \u001b[0m Synced: {len(synced)} command')
        
    except Exception as e:
        print(f'\u001b[41;1m !! \u001b[0m Exception detected: \n{e}')
    
    print(f'\u001b[45;1m ** \u001b[0m Status: {"Debug" if use_debug_mode else "Production"}')
    print(f'\u001b[45;1m ** \u001b[0m Successfully logged in as: {client.user}')


@client.event
async def on_message(message: discord.Message) -> None:

    if message.content.startswith('<usr>'):
        chat_message = message.content.split('<usr>')[1].strip()
        await message.channel.send(chat_response.get_response(chat_message, debug = use_debug_mode))

    await client.process_commands(message)
    
    
@client.tree.command(name = 'help', description = 'Display a help message.')
async def helper(interaction: discord.Interaction) -> None:
    
    help_embed = discord.Embed(
        title = '', 
        description = 'a Python Discord chat bot who can talk with you in English and Thai.', 
        color = 0xd357fe
    )
    
    help_embed.set_author(
        name = 'Celestial#0135', 
        icon_url = 'https://cdn.discordapp.com/app-icons/927573556961869825/b4b624c1cb68fa3a99a24a8e9942d2a5.png'
    )
    
    help_embed.add_field(
        name = 'How can you talk to me?', 
        value = 'You can talk to me by simply type\n`<usr> Your messages` to send me a messages!', 
        inline = False
    )
    
    help_embed.add_field(
        name = 'Report Issue', 
        value = 'If there is a problem with the bot response or any bug with the bot, \nfeel free to report us at: \n**https://github.com/StrixzIV/Celestial/issues/new/choose**', 
        inline = True
    )
    
    help_embed.add_field(
        name = 'Development & Update', 
        value = 'Follow the latest update at: \n**https://github.com/StrixzIV/Celestial**', 
        inline = False
    )
    
    help_embed.set_footer(text = '© 2022 MIT License - StrixzIV#6258, Peachpiggies#9229')
    
    await interaction.response.send_message(embed = help_embed)
    
    
@client.tree.command(name = 'reload', description = '*For developers only*')
@commands.check(is_owner)
async def reload_bot(interaction: discord.Interaction) -> None:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\u001b[45;1m ** \u001b[0m Reloading...')
    
    reload(chat_response)
    
    print('\u001b[45;1m ** \u001b[0m Chat module reload successfully!')
    print(f'\u001b[45;1m ** \u001b[0m Reload command sended from {interaction.user}')
    
    await interaction.response.send_message('Reload completed!')
    

@reload_bot.error
async def on_reload_error(interaction: discord.Interaction, error: commands.errors) -> None:
    
    error_embed = discord.Embed(
        title = '⚠️ Permission Error ⚠️', 
        description = 'Reload attempt from non-authorized user.', 
        color = 0xFF0000
    )
    
    print(f'\u001b[41;1m !! \u001b[0m Error: Reload attempt from {interaction.user} which is not an authorized user.')
    await interaction.response.send_message(embed=error_embed)
    
    
@client.tree.command(name = 'pull', description = '*For developers only*') 
@commands.check(is_owner)
async def pull(interaction: discord.Interaction) -> None:
    
    print('\u001b[45;1m ** \u001b[0m Pulling from origin...')
    
    repo = git.Repo(os.getcwd())
    repo.remote('origin').pull()
    
    print('\u001b[45;1m ** \u001b[0m Pull complete.')
    print('\u001b[45;1m ** \u001b[0m Reloading chat module...')
    
    reload(chat_response)
    
    print('\u001b[45;1m ** \u001b[0m Chat module reload successfully!')
    print(f'\u001b[45;1m ** \u001b[0m Pull command sended from {interaction.user}')
    
    await interaction.response.send_message('Pull completed!')
    
    
@pull.error
async def on_pull_error(interaction: discord.Interaction, error: commands.errors) -> None:
    
    error_embed = discord.Embed(
        title = '⚠️ Permission Error ⚠️', 
        description = 'Pull attempt from non-authorized user.', 
        color = 0xFF0000
    )
    
    print(f'\u001b[41;1m !! \u001b[0m Error: Pull attempt from {interaction.user} which is not an authorized user.')
    await interaction.response.send_message(embed=error_embed)
    

if __name__ == '__main__':

    load_dotenv()
    moderator_ids = set([int(ids) for (key, ids) in os.environ.items() if key.startswith('ID')])
    
    client.run(os.getenv('TOKEN'))