import os
import discord
import random
import asyncio

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='admin', help="Tests if you are an admin")
@commands.has_role('ADM')
async def check_admin(ctx):
    await ctx.send("yes, you are an admin =)")


@bot.command(name='rand', help="Says something random")
async def check_admin(ctx):
    quotes = [
        "rand 1",
        "rand 2",
        "rand 3"
    ]

    await ctx.send(random.choice(quotes))


# getting some arguments
@bot.command(name='register-hero', help="Creates a hero")
@commands.cooldown(2.0, 30.0, commands.BucketType.guild)
async def register_hero(ctx, hero_name: str):
    await ctx.send(f"hero {hero_name} created!")


# getting confirmation
@bot.command(name="delete-hero", help="Deletes a hero")
async def delete_hero(ctx, hero_name: str):
    member = ctx.message.author
    confirm_emoji = '\u2705'
    cancel_emoji = '\u274c'
    reactions = [confirm_emoji, cancel_emoji]

    bot_message = await ctx.send(f"are you sure you want to delete {hero_name}? [{confirm_emoji}]yes/[{cancel_emoji}]no")

    for emoji in reactions:
        await bot_message.add_reaction(emoji)

    def check_answer(reaction, user):
        return user == member and str(reaction.emoji) in reactions

    try:
        reaction, user = await bot.wait_for('reaction_add', check=check_answer, timeout=30.0)
    except asyncio.TimeoutError:
        return await ctx.channel.send(f'Sorry, you took too long to answer.')
    if str(reaction) == str(confirm_emoji):
        await ctx.send(f"deleting hero {hero_name}")
    elif str(reaction) == str(cancel_emoji):
        await ctx.send("cancel")


@bot.command(name="impossible-permission")
@commands.has_role('none')
async def test_impossible_permission(ctx):
    await ctx.send("wow O_O")


@bot.command(name="exception", help="test exceptions")
async def test_exceptions(ctx):
    raise Exception("failed successfully :')")


@bot.command(name="user-ids")
async def test_user_ids(ctx, target: discord.User):
    await ctx.send(f"data\n your name: {ctx.message.author.display_name}\n" +
                   f"your unique id: {ctx.message.author.id}\n" +
                   f"target name: {target.display_name}\n" +
                   f"target unique id: {target.id}")


# The code in this event is executed every time a valid commands catches an error
@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title="Error!",
            description="This command is on a %.2fs cool down" % error.retry_after
        )
        await context.send(embed=embed)
    elif isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            title="Error!",
            description="you don't have the necessary role"
        )
        await context.send(embed=embed)
    elif isinstance(error, commands.CommandError):
        embed = discord.Embed(
            title="Error!",
            description=f"there was an error running the command :( {error}"
        )
        await context.send(embed=embed)

    raise error

print("bot is running...")
bot.run(TOKEN)
