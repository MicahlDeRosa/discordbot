import os
import discord
from discord.ext import commands
from dotenv import load_dotenv



client = commands.Bot(command_prefix = '!!')

@client.event
async def on_ready():
    print('Jimmy is alive')

@client.command(aliases=['p'])
async def ping(ctx):
    await ctx.send('!Pong')


load_dotenv()
client.run(os.getenv('TOKEN'))

