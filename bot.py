import os
import discord
import random

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


@bot.command(name='register-hero', help="Creates a hero")
async def register_hero(ctx, hero_name: str):
    await ctx.send(f"hero {hero_name} created")

print("bot is running...")
bot.run(TOKEN)
