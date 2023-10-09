import discord
from discord.ext import commands, tasks 
import datetime
import asyncio

currenttime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

intents = discord.Intents.all()
client = commands.Bot(command_prefix='+', intents=intents)

@client.event
async def on_ready():
    print('Bot ist bereit')

@client.command()  
async def banall(ctx):
    if ctx.message.author.guild_permissions.administrator:
        with open('userids.txt', 'r') as f:
            userids = f.read().splitlines()
        for userid in userids:
            try:
                user = await client.fetch_user(userid)
                await ctx.guild.ban(user, reason='User banned by Ban Wave')
                print(f'{user.name}#{user.discriminator} was banned')
                await ctx.send(f'{user.name}#{user.discriminator} was banned')
                await asyncio.sleep(5) #
            except discord.errors.NotFound:
                print(f'UserID {userid} was banned')
        await ctx.send('All user banned')

client.run('')
