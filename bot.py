import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv


client = commands.Bot(command_prefix='!!')


@client.event
async def on_ready():
    print('Jimmy is alive')


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
        'IDK...but Anyone can be confident with a full head of hair. But a confident bald man – there’s your diamond in the rough',
        'Better not tell you know.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't Count on it.",
        'My reply is No.',
        'My sources say No.',
        'Outlook not so good.',
        'Very Doubtful']
    await ctx.send(f':8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)} ')


@client.command(aliases=['boot'])
async def kick(ctx, member: discord.Member, *, reason=None):
    if (not ctx.author.guild_permission.kick_members):
        await ctx.send('This command requires ``Ban Members``')
        return
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked')


@client.command(aliases=['banned'])
async def ban(ctx, member: discord.Member, *, reason=None):
    if (not ctx.author.guild_permission.ban_members):
        await ctx.send('This command requires ``Kick Members``')
        return
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned')


@client.command(aliases=['forgive'])
async def unban(ctx, *, member):
    if (not ctx.author.guild_permission.ban_members):
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


load_dotenv('.env')
client.run(os.getenv('TOKEN'))
