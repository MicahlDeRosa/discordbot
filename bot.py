import os
import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '!!')

@client.event
async def on_ready():
    print('Jimmy is alive')

@client.command(aliases=['p'])
async def ping(ctx):
    await ctx.send('!Pong')



#bot.py
client.run(os.getenv('TOKEN'))

