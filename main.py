import discord
from discord import message
from dotenv import load_dotenv
import os
from discord.ext import commands



load_dotenv()

bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
    print("Activated")

@bot.command()
async def hello(ctx):
    await ctx.send("It's me Ducky")


bot.load_extension("cogs.moderation")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.reddit")
bot.load_extension("cogs.better_programming")
bot.load_extension("cogs.dev")
bot.load_extension("cogs.gsearch")
bot.load_extension("cogs.wikipedia_search")
bot.load_extension("cogs.music")








bot.run(os.getenv("TOKEN"))