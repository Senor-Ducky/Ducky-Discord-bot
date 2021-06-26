from discord.ext import commands
import praw
from dotenv import load_dotenv
import os
import discord
from praw.models.listing.mixins import submission

load_dotenv()

reddit = praw.Reddit(
    client_id = os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
    user_agent="ducky-bot"
)

class reddit_scraper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Fetch programming articles from any programming subreddit")
    async def article(self, ctx, *args):
        submission = next(x for x in reddit.subreddit('{}'.format(' '.join(args))).hot() if not x.stickied)
        for submission in reddit.subreddit('{}'.format(' '.join(args))).hot(limit=10):
            em = discord.Embed(title=submission.title, description=submission.selftext[:2048], url = submission.url, color=0xFF4301)        
            em.add_field(name="Upvotes", value=submission.score, inline=False)
            em.add_field(name="Comments", value=submission.num_comments, inline=False)
            await ctx.send(embed = em)

    @commands.command(description="fetch memes from any subreddit")
    async def meme(self, ctx, *args):
        submission = reddit.subreddit('{}'.format(' '.join(args))).random()
        em = discord.Embed(title=submission.title, description=submission.selftext[:2048], url = submission.url, color=0xFF4301)        
        em.set_image(url=submission.url)
        await ctx.send(embed = em)

   

def setup(bot):
        bot.add_cog(reddit_scraper(bot))
            