import discord
from discord.ext import commands
from random import randrange
import os

DISCORD_TOKEN =''
PREFIX = '!'

sussy = commands.Bot(command_prefix=PREFIX)

@sussy.event 
async def on_ready():
	print("SUS CONNECTED TO SUSCORD! (100% imposter very sus no cap)")

@sussy.command()
async def sus(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.message.author
    susness = randrange(101)
    convertedsus = str(susness)
    convertedmember = str(member)
    embed=discord.Embed(title="SUSY BOTY", url="https://opensus.wtf", description=convertedmember + " is `" + convertedsus + "%` sus")
    embed.set_thumbnail(url="https://www.amonghelper.tk/among_us.png")
    embed.set_footer(text=ctx.message.author)
    await ctx.send(embed=embed)

    
sussy.run(DISCORD_TOKEN)
