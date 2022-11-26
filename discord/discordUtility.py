import logging
import discord
from discord.ext import commands
from app_local import secret


SECRET_KEY = secret
intents = discord.Intends.all()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def get_channel(ctx, *, given_name=None):
    for channel in ctx.guild.channels:
        if channel.name == given_name:
            wanted_channel_id = channel.id

    await ctx.send(wanted_channel_id) # this is just to check 

bot.run(SECRET_KEY)

print('Yerr')