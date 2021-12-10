import discord
import asyncio

token = "45ca05c1c8428ebafeffc64a29b29262445e45b902b6f75e6b6b7b963a28d501"

client = discord.Client()

@client.event
async def on_message(message):
    #do a thing with message
    print(message.content)
    pass

@client.event
async def on_ready():
    print("bot is running")

client.run("45ca05c1c8428ebafeffc64a29b29262445e45b902b6f75e6b6b7b963a28d501")



#https://discord.com/api/oauth2/authorize?client_id=848896415556304907&scope=bot&permissions=68608