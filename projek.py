import discord
from discord.ext import commands
import os, random
from sampah import sampah_anorganik, sampah_organik

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'bot has been logged with username {bot.user}')

@bot.command()
async def organik(ctx):
    await ctx.send(sampah_organik())

@bot.command()
async def anorganik(ctx):
    await ctx.send(sampah_anorganik())

    bot.run("undetified")
