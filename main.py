import os
import nextcord
import chat_response
from dotenv import load_dotenv
from nextcord.ext import commands
from dotenv import load_dotenv
from importlib import reload

intents = nextcord.Intents.default()
intents.message_content = True

use_debug_mode = False

client = commands.Bot(command_prefix = '::<' if use_debug_mode else '<', intents = intents, help_command = None)

load_dotenv()

modList = [int(os.getenv('ID1'))]

def is_owner(ctx: commands.Context) -> bool:
    
    '''
        Check if the command user is authorized.
    '''
    
    if ctx.author.id in modList:
        return ctx.author.id in modList
    

@client.event
async def on_ready() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\u001b[45;1m ** \u001b[0m Successfully logged in as: {client.user}')
    

@client.command(name = 'usr>')
async def answer(ctx: commands.Context, *msg: str) -> None:
    await ctx.send(chat_response.get_response(' '.join(list(msg)), debug = use_debug_mode))
    
    
@client.command(name = '!reload>')
@commands.check(is_owner)
async def reload_bot(ctx: commands.Context) -> None:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\u001b[45;1m ** \u001b[0m Reloading...')
    
    reload(chat_response)
    
    print('\u001b[45;1m ** \u001b[0m Chat module reload successfully!')
    print(f'\u001b[45;1m ** \u001b[0m Reload command sended from {ctx.author}')
    

@reload_bot.error
async def on_reload_error(ctx: commands.Context, error: commands.errors) -> None:
    
    error_embed = nextcord.Embed(title='⚠️ Permission Error ⚠️', description='Reload attempt from non-authorized user.', color=0xFF0000)
    
    print(f'\u001b[41;1m !! \u001b[0m Error: Reload attempt from {ctx.author} which is not an authorized user.')
    await ctx.send(embed=error_embed)
    
client.run(os.getenv('TOKEN'))