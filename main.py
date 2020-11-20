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
async def help(ctx):
    author = ctx.message.author
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
    embed.add_field(name=':mag_right: Information', value=f"{information}", inline=True)
    # Fun Commands
    embed.add_field(name=":100: Fun Commands", value=f"{fun_commands}", inline=True)
    # Administrator
    embed.add_field(name=':tools: Administrator', value=f"{admin}", inline=True)
    # ----- FOOTER ----- #
    embed.set_footer(text=f"Request by {author.name}")

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