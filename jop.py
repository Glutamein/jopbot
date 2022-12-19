from ast import alias
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from dotenv import load_dotenv
import os
import random, glob
import discord

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('!jop'))
    for guild in client.guilds:
        print(f'{guild.name} (id: {guild.id})')



@client.command(help='sends the anthem', aliases=['JOP'])
async def jop(ctx):
    await ctx.send('https://www.youtube.com/watch?v=pAnK1y7qjuE')


@tasks.loop(hours=24)
async def daily():
    channel = client.get_channel(884139972108636210)
    await channel.send('Have you jopped today?')

@daily.before_loop
async def before_daily():
    await client.wait_until_ready()

daily.start()
client.run(TOKEN)