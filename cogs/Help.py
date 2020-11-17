import discord
from discord.ext import commands
from discord.utils import get

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    # -----ON READY----- #
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help cogs is ready')

# ========================= COMMANDS ========================= #
    @commands.command()
    async def help(self, ctx):
        author = ctx.message.author
        embed = discord.Embed(color=discord.Color.blue(), title="Bot Commands", description="Type `>help [option]` to see detailed information about the commands, \ne.g. `>help ping`")
        admin = "`clear` `kick` `ban` `unban`"
        fun_commands = "`8ball` `coin`"
        information = "`ping` `userinfo` `donate`"

        # ----- FIELD ----- #
        # Information
        embed.add_field(name=':mag_right: Information', value=f"{information}", inline=True)
        # Fun Commands
        embed.add_field(name=":100: Fun Commands", value=f"{fun_commands}", inline=True)
        # Administrator
        embed.add_field(name=':tools: Administrator', value=f"{admin}", inline=True)
        # ----- FOOTER ----- #
        embed.set_footer(text=f"Request by {author.name}")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))