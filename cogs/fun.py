
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    

    @commands.command(pass_context=True)
    async def ducky_say(self,ctx, *args):
        await ctx.send('{}'.format(' '.join(args)))
        await ctx.message.delete()

def setup(bot):
        bot.add_cog(fun(bot))
    

