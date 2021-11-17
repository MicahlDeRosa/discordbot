import os
import discord
import random
import platform
from discord.ext import commands
from discord import Intents, Member
from dotenv import load_dotenv
import json


os.chdir('C:\\Users\\Micahl DeRosa\\Desktop\\Bot_folder')



intents = discord.Intents().all() 
client = commands.Bot(command_prefix='!!', intents=intents)


@client.event
async def on_ready():
    print('Jimmy is alive')


#memeber has joined sever 
@client.event 
async def on_member_join(member):
    responses = [
        " If it tastes funny, don't eat it. If it looks funny, call a doctor. If it is funny, it must have been something I said.",
        "Welcome out of the cave, my friend. It’s a bit colder out here, but the stars are just beautiful",
        "For each and all I bid thee a grateful welcome",
        "There is little in life so reassuring as a genuine welcome",
        "Welcome to the present moment. Here. Now. The only moment there ever is.",
    ]
    print(f' Good Day {member}, {random.choice(responses)} ')   


#say hello 
@client.command(aliases=['hello'])
async def hi(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!!')


@client.command(aliases=['p'])
async def ping(ctx):
    await ctx.send('!Pong')


@client.command(aliases=['8b'])
async def eightball(ctx, *, question):
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
        'I do not have an asnswer...but Anyone can be confident with a full head of hair. But a confident bald man – there’s your diamond in the rough',
        'Better not tell you know.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't Count on it.",
        'My reply is No.',
        'My sources say No.',
        'Outlook not so good.',
        'Very Doubtful']
    await ctx.send(f':8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)} ')


@client.command(aliases=['q'])
async def quotes(ctx):
    responses2 = [
        'Where was ya, Wang? We was worried.',
        "Shut that cunt's mouth or I'll come over there and fuckstart her head!",
        'How am I not myself?',
        'Welcome to Debbie Country.',
        "I feel like I'm taking crazy pills!",
        "Well, this piece is called 'Lick My Love Pump.'",
        'This is the guy behind the guy behind the guy.',
        "It ain't white boy day is it?"]
    await ctx.send(f'{random.choice(responses2)}')


@client.command(aliases=['boot'])
async def kick(ctx, member: discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.kick_members):
        await ctx.send('This command requires ``Ban Members``')
        return
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked')


@client.command(aliases=['banned'])
async def ban(ctx, member: discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send('This command requires ``Kick Members``')
        return
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned')


@client.command(aliases=['forgive'])
async def unban(ctx, *, member):
    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send('This command requires ``Ban Members``')
        return
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbannerd {user.mention}')
            return


@client.command(aliases=['purge'])
async def clear(ctx, amount=11):
    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send('This command requires ``Manage Messages``')
        return
    if amount > 101:
        await ctx.send('Can not delete more than 100 messages')
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send('Cleared Messages')



@client.command(aliases=['trump_in_the_silky'])
async def silky(ctx):
    await ctx.send(file=discord.File('img/silky.jpeg'))


@client.command()
async def merica(ctx):
    await ctx.send(file=discord.File(random.choice(('img2/joe.jpg', 'img2/trump.jpg', 'img2/wood.jpg', 'img2/america.webp'))))
    


@client.command()
async def stats(ctx):
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    servercount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))
    await ctx.send(f'Looks like I am in {servercount} servers with a total of {memberCount} members.\nI am currently running {pythonVersion} and discord.py {dpyVersion}')


load_dotenv('.env')
client.run(os.getenv('TOKEN'))
