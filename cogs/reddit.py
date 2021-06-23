from discord.ext import commands
import praw
from dotenv import load_dotenv
import os
import discord

load_dotenv()

reddit = praw.Reddit(
    client_id = os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
    user_agent="ducky-bot"
)

class reddit_scraper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def python(self, ctx):
        for submission in reddit.subreddit("python").hot(limit=10):
            em = discord.Embed(title=submission.title, description=submission.selftext[:2048], url = submission.url, color=0xFF4301)
            em.add_field(name="Upvotes", value=submission.score, inline=False)
            em.add_field(name="Comments", value=submission.num_comments, inline=False)
            await ctx.send(embed = em)

    @commands.command()
    async def react(self, ctx):
        for submission in reddit.subreddit("react").hot(limit=10):
            em = discord.Embed(title=submission.title, description=submission.selftext[:2048], url = submission.url, color=0xFF4301)
            em.add_field(name="Upvotes", value=submission.score, inline=False)
            em.add_field(name="Comments", value=submission.num_comments, inline=False)
            await ctx.send(embed = em)

    @commands.command()
    async def learn_programming(self, ctx):
        for submission in reddit.subreddit("learnprogramming").hot(limit=10):
            em = discord.Embed(title=submission.title, description=submission.selftext[:2048], url = submission.url, color=0xFF4301)
            em.add_field(name="Upvotes", value=submission.score, inline=False)
            em.add_field(name="Comments", value=submission.num_comments, inline=False)
            await ctx.send(embed = em)

def setup(bot):
        bot.add_cog(reddit_scraper(bot))
            