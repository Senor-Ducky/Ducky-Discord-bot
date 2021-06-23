
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    

    @commands.command()
    async def ducky_say(self,ctx, *args):
        await ctx.send('{}'.format(' '.join(args)))

def setup(bot):
        bot.add_cog(fun(bot))
    

