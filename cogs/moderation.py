from discord.ext import commands
import discord
from discord.ext.commands import bot
from discord.ext.commands.core import has_permissions

class moderation(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
        
    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members = True, ban_members = True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        await ctx.send(f"{ctx.author.mention} muted {user.mention} for {reason}")
        await user.kick(reason=reason)

    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members = True, ban_members = True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        await ctx.send(f"{ctx.author.mention} muted {user.mention} for {reason}")
        await user.ban(reason=reason)

    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members = True, ban_members = True)
    async def mute(self, ctx, user: discord.Member, *, reason=None):
        await ctx.send(f"{ctx.author.mention} muted {user.mention} for {reason}")
        role = discord.utils.get(ctx.guild.roles, name = 'Muted')
        await user.add_roles(role)
        
    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members = True, ban_members = True)
    async def unmute(self, ctx, user: discord.Member, *, reason=None):
        await ctx.send(f"{ctx.author.mention} unmuted {user.mention} for {reason}")
        role = discord.utils.get(ctx.guild.roles, name = 'Muted')
        await user.remove_roles(role)





def setup(bot):
    bot.add_cog(moderation(bot))
