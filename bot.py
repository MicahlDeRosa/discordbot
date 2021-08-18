import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '!!')

@client.event
async def on_ready():
    print('Jimmy is alive')

@client.command(aliases=['p'])
async def ping(ctx):
    await ctx.send('!Pong')

client.run('ODc3Mzc5ODk4MjYyNTY0ODc0.YRxxtA.aXsXy6PobY4d-JPaiT4Rwalo7Uw')
