import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv



client = commands.Bot(command_prefix = '!!')

@client.event
async def on_ready():
    print('Jimmy is alive')

@client.command(aliases=['p'])
async def ping(ctx):
    await ctx.send('!Pong')


@client.command(aliases=['8b'])
async def eightball(ctx,*,question):
    responses = [
        'Hell no.',
        'Prolly not.',
        'Idk bro.',
        'Prolly.',
        'Hell yeah my dude.',
        'It is certain.',
        'It is decidedly so.',
        'Without a Doubt.',
        'Yes - Definitaly.',
        'You may rely on it.',
        'As i see it, Yes.',
        'Most Likely.',
        'Outlook Good.',
        'Yes!',
        'No!',
        'Signs a point to Yes!',
        'Reply Hazy, Try again.',
        'IDK but u should subscribe to Exotix On Youtube and Follow Him On Insta mahad.ali.khan.',
        'Better not tell you know.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't Count on it.",
        'My reply is No.',
        'My sources say No.',
        'Outlook not so good.',
        'Very Doubtful']
    await ctx.send(f':8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)} ')

load_dotenv()
client.run(os.getenv('TOKEN'))

