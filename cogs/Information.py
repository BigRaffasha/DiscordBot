import discord
from discord.ext import commands
from discord.utils import get

class Information(commands.Cog):
    def __init__(self, client):
        self.client = client

    # -----ON READY----- #
    @commands.Cog.listener()
    async def on_ready(self):
        print('Information cogs is ready')

# ========================= COMMANDS ========================= #

    # ----- PING ----- #
    @commands.command(aliases=["PING","Ping"])
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: Pong! {round(self.client.latency * 1000)}ms')

    # ----- USER INFO ----- #
    @commands.command(aliases=['user','info','User','Info','UserInfo'])
    async def userinfo(self, ctx, *, member:discord.Member=None):
        embed = discord.Embed(color = discord.Colour.green(), timestamp=ctx.message.created_at)
        member = ctx.author if not member else member
        
        # Field
        embed.set_author(name=member, icon_url=member.avatar_url)
        # Line 1
        embed.add_field(name="User ID:", value=member.id, inline=True)
        embed.add_field(name="\n\u200b", value="\n\u200b", inline=True)
        embed.add_field(name="Nickname:", value=member.nick, inline=True)
        # Line 2
        embed.add_field(name="Highest Role:", value=member.top_role.mention, inline=True)
        embed.add_field(name="\n\u200b", value="\n\u200b", inline=True)
        embed.add_field(name="Is a bot?", value=member.bot, inline=True)
        # Line 3
        embed.add_field(name="Account created:", value=member.created_at.strftime("%a, %B %d %Y @ %H:%M:%S %p"), inline=False)
        embed.add_field(name="Joined this server:", value=member.joined_at.strftime("%a, %B %d %Y @ %H:%M:%S %p"), inline=False)
        # ----- Thumbnail ----- #
        embed.set_thumbnail(url=member.avatar_url)
        # ----- Footer ----- #
        embed.set_footer(text=f"Request by {ctx.author.name}")

        await ctx.send(embed=embed)
        return

    # ----- AVATAR ----- #
    @commands.command(aliases=['Avatar','AVATAR'])
    async def avatar(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member
        embed = discord.Embed(color = discord.Colour.green())

        # Field
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.set_image(url=member.avatar_url)

        await ctx.send(embed=embed)

    # ----- DONATE ----- #
    @commands.command(aliases=['Donate','DONATE'])
    async def donate(self, ctx):
        embed = discord.Embed(
            title = ":moneybag: Donate",
            description = 'Donate my creator to support him!',
            color = discord.Colour.blue()
        )

        # ----- Saweria ----- #
        embed.add_field(name="Saweria: ", value="*https://saweria.co/bigraffasha*", inline=False)
        # ----- Trakteer ----- #
        embed.add_field(name="Trakteer: ", value="*https://trakteer.id/big-raffasha*", inline=False)
        # ----- Empty field ----- #
        embed.add_field(name="\n\u200b", value="\n\u200b")
        # ----- Footer ----- #
        embed.set_footer(text = "Thanks for donating!")

        await ctx.send(embed=embed)
        return
        
# ========================= ERRORS ========================= #

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"That's not an user!")
            return

def setup(client):
    client.add_cog(Information(client))