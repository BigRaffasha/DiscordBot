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