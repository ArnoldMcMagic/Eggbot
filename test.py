import discord
from discord.ext import commands
import pynacl

app_id = "848920633508495431"
pub_key = "58c3be3ed3b3ffbceeab4979ad30032b3128532b22b54ffe94c8a1b4b80756bf"
token = "ODQ4OTIwNjMzNTA4NDk1NDMx.YLTo8w.PODBA-zejIWVlh5wXfkiLOIrVWA"
permissions = "68608"

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("bot ready")


@client.command(pass_context = True)
async def join(ctx):
    if(ctx.message.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await "Get in a voice channel cucklord!"

client.run(token)