import os
import discord
import random
import asyncio

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

print("using token + " + TOKEN)

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

print("bot is running...")
bot.run(TOKEN)
