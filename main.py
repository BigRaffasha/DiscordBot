import discord, os, time
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '>', intents = intents)
client.remove_command('help')

# ========================= COGS ========================= #

# LOAD COGS #
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded "{extension}"')
    print(f'Loaded "{extension}"')

# UNLOAD COGS #
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded "{extension}"')
    print(f'Unoaded "{extension}"')

# ========================= BOT STATUS ========================= #
@client.event
async def on_ready():
    channel = client.get_channel(703774381658341377)
    await client.change_presence(status=discord.Status.online, activity=discord.Game('>help'))
    await channel.send(f'Im back online!')
    print('Bot is online!')

# ========================= HELP COMMAND ========================= #
@client.command(aliases=["Help", "HELP"])
async def help(ctx, commands=None):

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
        embed.add_field(name="Aliases:", value="cl, purge")

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

        admin = "`clear` `kick` `ban` `unban`"
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

# ========================= COMMON ERRORS ========================= #
@client.event
async def on_command_error(ctx, error):

    # Unkwonw Commands
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I don't understand what you mean.")
        return
    
    # Missing Permissions
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"You don't have the permission to do that!")
        return

# ========== LOADING COGS ========== #
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded {filename[:-3]}')

# ========== RUN BOT =========== #
load_dotenv('.env')
client.run(os.getenv('BOT_TOKEN'))