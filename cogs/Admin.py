import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    # -----ON READY----- #
    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin cogs is ready')

# ========================= COMMANDS ========================= #

    # -----CLEAR CHAT----- #
    @commands.command(aliases=['cl','Clear','purge'])
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)
        return

    # ------KICK----- #
    @commands.command(aliases=['remove', 'Kick', 'Remove'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        await ctx.guild.kick(member)
        await ctx.send(f"Kicked {member.mention}")
        return

    # -----BAN----- #
    @commands.command(aliases=['Ban','BAN'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned')
        return

    # -----UNBAN----- #
    @commands.command(aliases=['Unban'])
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

# ========================= ERRORS ========================= #

    # -----KICK ERROR----- #
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please specify a member')
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(f"Sorry, I can't find that user")
        else:
            await ctx.send(f"You can't kick an Admin!")

    # -----BAN ERROR----- #
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please specify a member')
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(f"Sorry, I can't find that user")
        else:
            await ctx.send(f"Are you sick?")

def setup(client):
    client.add_cog(Admin(client))