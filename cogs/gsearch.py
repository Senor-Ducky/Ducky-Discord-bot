import discord
from discord.ext import commands
from googlesearch import search

class google_search(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def gsearch(self,ctx,*args):
        results = search('{}'.format(' '.join(args)),num_results=5, lang="en")
        em = discord.Embed(title="Google Search", color=0x212121)
        for links in results:
            em.add_field(name="Result",value=links, inline=False)
        await ctx.send(embed=em)
            


def setup(bot):
    bot.add_cog(google_search(bot))

