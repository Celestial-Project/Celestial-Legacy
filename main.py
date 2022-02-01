import os
from dotenv import load_dotenv
from nextcord.ext import commands
from chat_response import get_response
from dotenv import load_dotenv

client = commands.Bot(command_prefix = '<')

@client.event
async def on_ready():
    print(f'Successfully logged in as: {client.user}')
    

@client.command(name = 'usr>')
async def answer(ctx, *msg):
    await ctx.send(get_response(' '.join(list(msg))))
        
        
load_dotenv()

client.run(os.getenv('TOKEN'))