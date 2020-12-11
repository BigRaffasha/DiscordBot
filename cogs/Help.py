import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    # -----ON READY----- #
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help cogs is ready')

    # ========================= INFORMATION ========================= #


    # ========================= FUN COMMANDS ========================= #


    # ========================= ADMINISTRATOR ========================= #
    

def setup(client):
    client.add_cog(Help(client))