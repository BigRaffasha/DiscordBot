import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    # -----ON READY----- #
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help cogs is ready')

    @commands.command(aliases=["Help", "HELP"])
    async def help(self, ctx, commands=None):

    # ---------- INFORMATION ---------- #
        # ----- Ping ----- #
        if commands == "ping":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Ping",
                description="""```>ping```
                Returns client latency"""
            )

            await ctx.send(embed=embed)

        # ----- User Info ----- #
        elif commands == 'userinfo':
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="User Info",
                description="""```>userinfo <member>```
                Get a user information"""
            )

            embed.add_field(name="Aliases:", value="user, info")

            await ctx.send(embed=embed)

        # ----- Server Info ----- #
        elif commands == 'serverinfo':
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Server Info",
                description="""```>serverinfo```
                Get a server information"""
            )
            embed.add_field(name="Aliases:", value="server")

            await ctx.send(embed=embed)

        # ----- Avatar ----- #
        elif commands == "avatar":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Avatar",
                description="""```>avatar <member>```
                Get a user's avatar"""
            )

            await ctx.send(embed=embed)

        # ----- Donate ----- #
        elif commands == "donate":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Donate",
                description="""```>donate```
                Get a link to donate to the creator"""
            )

            await ctx.send(embed=embed)        

    # ---------- FUN COMMANDS ---------- #
        # ----- 8 BALL ----- #
        elif commands == "8ball":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="8 Ball",
                description="""```>8ball <question>```
                asks the 8 Ball"""
            )
            embed.add_field(name="Aliases:", value="8b")

            await ctx.send(embed=embed)

        # ----- COIN ----- #
        elif commands == "coin":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Coin",
                description="""```>coin```
                Flips a coin"""
            )
            embed.add_field(name="Aliases:", value="flip, coinflip")

            await ctx.send(embed=embed)

    # ---------- ADMINISTRATOR ---------- #

        # ----- Clear ----- #
        elif commands == "clear":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Clear",
                description="""```>clear <amount>```
                Delete messages. Default amount is 10"""
            )
            embed.add_field(name="Aliases:", value="cl, purge, clr, cls")

            await ctx.send(embed=embed)

        # ----- Mute ----- #
        elif commands == "mute":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Mute",
                description="""```>mute <user> <time> <unit> <reason>```
                Mute the specified user"""
            )

            await ctx.send(embed=embed)

        # ----- Unmute ----- #
        elif commands == "unmute":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Unmute",
                description="""```>unmute <user>```
                Unmute the specified user"""
            )

            await ctx.send(embed=embed)

        # ----- Give Role ----- #
        elif commands == "giverole":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Give Role",
                description="""```>giverole <user> <role name>```
                Give the specified user a role"""
            )
            embed.add_field(name="Aliases:", value="grole")

            await ctx.send(embed=embed)

        # ----- Remove Role ----- #
        elif commands == "removerole":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Remove Role",
                description="""```>removerole <user> <role name>```
                Remove a role from a user"""
            )
            embed.add_field(name="Aliases:", value="rrole")

            await ctx.send(embed=embed)

        # ----- Kick ----- #
        elif commands == "kick":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Kick",
                description="""```>kick <user>```
                Kicks a member out of the server"""
            )
            embed.add_field(name="Aliases:", value="remove")

            await ctx.send(embed=embed)

        # ----- Ban ----- #
        elif commands == "ban":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Ban",
                description="""```>ban <user>```
                Bans a member from the server"""
            )

            await ctx.send(embed=embed)

        # ----- Unban ----- #
        elif commands == "unban":
            embed = discord.Embed(
                color=discord.Color.blue(),
                title="Unban",
                description="""```>unban <user>```
                Unbans a banned member from the server"""
            )

            await ctx.send(embed=embed)

    # ---------- General Help ---------- #
        elif commands is None:
            embed = discord.Embed(
                color=discord.Color.blue(), 
                title="Bot Commands", 
                description="Type `>help [option]` to see detailed information about the commands, \ne.g. `>help ping`", 
                timestamp=ctx.message.created_at)

            admin = "`clear` `mute` `unmute` `giverole` `removerole` `kick` `ban` `unban`"
            fun_commands = "`say` `8ball` `coin`"
            information = "`ping` `userinfo` `serverinfo` `avatar` `donate`"

            # ----- FIELD ----- #
            # Information
            embed.add_field(name=':mag_right: Information', value=f"{information}", inline=False)
            # Fun Commands
            embed.add_field(name=":100: Fun Commands", value=f"{fun_commands}", inline=False)
            # Administrator
            embed.add_field(name=':tools: Administrator', value=f"{admin}", inline=False)

            await ctx.send(embed=embed)

    @help.error
    async def help_error(self, ctx, error):
        if isinstance(error):
            raise error


def setup(client):
    client.add_cog(Help(client))