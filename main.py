import os
import sys
from dotenv import load_dotenv
from nextcord.ext import commands
from chat_response import get_response
from dotenv import load_dotenv

client = commands.Bot(command_prefix = '<')

load_dotenv()

modList = [int(os.getenv('ID1'))]

def is_owner(ctx):
    if ctx.author.id in modList:
        return ctx.author.id in modList
    

@client.event
async def on_ready():
    os.system('clear')
    print(f'\u001b[45;1m ** \u001b[0m Successfully logged in as: {client.user}')
    

@client.command(name = 'usr>')
async def answer(ctx, *msg):
    await ctx.send(get_response(' '.join(list(msg))))
    
    
@client.command(name = 'reload>')
@commands.check(is_owner)
async def reload(ctx):
    os.system('clear')
    print('\u001b[45;1m ** \u001b[0m Reloading...')
    os.execl(sys.executable, sys.executable, *sys.argv)
        
        
client.run(os.getenv('TOKEN'))