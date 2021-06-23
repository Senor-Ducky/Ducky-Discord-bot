import discord
from discord import message
from dotenv import load_dotenv
import os
from discord.ext import commands



load_dotenv()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Activated")

@bot.command()
async def hello(ctx):
    await ctx.send("It's me Ducky")

bot.load_extension("cogs.fun")








bot.run(os.getenv("TOKEN"))