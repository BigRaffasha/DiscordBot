import discord, random, time
from discord.ext import commands
from discord.utils import get

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # -----ON READY----- #
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun cogs is ready')

# ========================= COMMANDS ========================= #

    # ----- 8 BALL COMMAND ----- #
    @commands.command(aliases=['8ball','8b'])
    async def _8ball(self, ctx, *, question=None):
        embed = discord.Embed(colour=discord.Colour.green())
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]

        # Author
        embed.set_author(name=ctx.author.name, icon_url=ctx.message.author.avatar_url)
        # Field
        embed.add_field(name="Question:", value=question, inline=False)
        embed.add_field(name="Responses:", value=f"{random.choice(responses)}")

        if question == None:
            await ctx.send(f'Pleace specify a question')
            return
        else:
            await ctx.send(embed=embed)
            return

    # ----- COIN FLIP ----- #
    @commands.command(aliases=["coin", "flip"])
    async def coinflip(self, ctx):
        embed = discord.Embed(colour=discord.Colour.gold(), timestamp=ctx.message.created_at)
        result = ["**Head!**", "**Tails!**"]

        # Field
        embed.add_field(name=f":coin: {ctx.author.nick} Tossed a coin", value=f"And got {random.choice(result)}")
        await ctx.send(embed=embed)

# ========================= ERRORS ========================= #

def setup(client):
    client.add_cog(Fun(client))