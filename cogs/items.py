from discord.ext import commands


class Items(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="items")
    async def check_admin(self, ctx):
        await ctx.send("there are no items registered yet")


def setup(bot):
    bot.add_cog(Items(bot))
