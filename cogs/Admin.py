import discord, asyncio
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
    @commands.command(aliases=['cl','Clear','purge','clr','cls'])
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)
        return

    # -----MUTE----- #
    @commands.command(aliases=['Mute','MUTE'])
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, time=int(0), unit=None, *, reason=None):
        muted = discord.utils.get(ctx.message.guild.roles, name="Muted")

        await member.add_roles(muted)

        if time == 0 and unit == None:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.add_field(name=f"Muted {member.nick} until the mods umute him/her", value=f"Reason: {reason}")
            await ctx.send(embed=embed)

        # Mute per sec
        elif unit == 's':
            wait = 1 * time
            embed = discord.Embed(colour=discord.Colour.red())
            embed.add_field(name=f"Muted {member.nick} for {time} Second", value=f"Reason: {reason}")
            await ctx.send(embed=embed)
            await asyncio.sleep(wait)
            await member.remove_roles(muted)

        # Mute per min
        elif unit == 'm':
            wait = 60 * time
            embed = discord.Embed(colour=discord.Colour.red())
            embed.add_field(name=f"Muted {member.nick} for {time} Minute", value=f"Reason: {reason}")
            await ctx.send(embed=embed)
            await asyncio.sleep(wait)
            await member.remove_roles(muted)


        # Mute per hour
        elif unit == 'h':
            wait = 3600 * time
            embed = discord.Embed(colour=discord.Colour.red())
            embed.add_field(name=f"Muted {member.nick} for {time} Hour", value=f"Reason: {reason}")
            await ctx.send(embed=embed)
            await asyncio.sleep(wait)
            await member.remove_roles(muted)


        # Mute per day
        elif unit == 'd':
            wait = 86400 * time
            embed = discord.Embed(colour=discord.Colour.red())
            embed.add_field(name=f"Muted {member.nick} for {time} Day", value=f"Reason: {reason}")
            await ctx.send(embed=embed)
            await asyncio.sleep(wait)
            await member.remove_roles(muted)

    # -----UNMUTE----- #
    @commands.command(aliases=['um'])
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        unmute = discord.utils.get(ctx.message.guild.roles, name="Muted")
        embed = discord.Embed(title=f"Unmuted {member.nick}", colour=discord.Color.red())

        await member.remove_roles(unmute)
        await ctx.send(embed=embed)

    # -----GIVE ROLES----- #
    @commands.command(aliases=['addrole','addroles','giveroles','grole'])
    @commands.has_permissions(administrator=True)
    async def giverole(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"Successfully given")

    # -----REMOVE ROLES----- #
    @commands.command(aliases=['rrole','Rrole'])
    @commands.has_permissions(administrator=True)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send(f"Successfully removed")


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

    # -----ERROR CHECK----- #
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error):
            raise error

def setup(client):
    client.add_cog(Admin(client))