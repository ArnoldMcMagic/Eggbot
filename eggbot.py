import discord
from discord.ext import commands
import os
from dotenv import dotenv_values
config = dotenv_values(".env")

app_id = "848920633508495431"
pub_key = "58c3be3ed3b3ffbceeab4979ad30032b3128532b22b54ffe94c8a1b4b80756bf"
token = config["TOKEN"]
permissions = "68608"

#https://discord.com/api/oauth2/authorize?client_id=848920633508495431&scope=bot&permissions=68608

#User ID numbers
bot = discord.Client()
bot_id = 848920633508495431
my_id = 695713807116533780
matts_id = 689761844688060473
johns_id = 674380573896081410
nialls_id = 373591348441251849
elliot_id = 401446077644931092

#Variables for checks
Ree = "ree"
Smell = "smell"
Needs = "need"
Civ = "civ"
SunLazer = ["sun","lazer"]
Blanket = ["blanket", "https://tenor.com/view/the-sun-is-a-deadly-lazer-gif-8691250"]
Egg = "egg"


client = commands.Bot(command_prefix = ".")

#creates swearlist to check against
f = open("SwearList.txt", "r")
RawList = f.readlines()
SwearList = []

for element in RawList:
    SwearList.append(element.strip())

#Finecount
FineCount = {
    my_id : 0,
    matts_id : 0,
    johns_id : 0,
    elliot_id : 0,
    nialls_id : 0
}

FineCount = dict.fromkeys([my_id, matts_id, johns_id], 0)

@bot.event
async def on_ready():
    print("Eggbot is ready")
    print(bot.user.name, bot.user.id)


@bot.event
async def on_message(message):
    print(message.author.name, message.author.id)
    print(message.content)
    print()

    if message.author.id == bot_id:
        return

    else:

        if any(x in message.content.lower() for x in SwearList):
            FineCount[message.author.id] = FineCount.get(message.author.id, 0) + 1
            await message.channel.send(message.author.display_name + " you are fined %d credit for a violation of the verbal morality statute." % FineCount[message.author.id])
            print(FineCount)
            return

        if Ree in message.content.lower():
            await message.channel.send("https://tenor.com/view/ree-pepe-triggered-angry-ahhhh-gif-13627544")
            return
        
        if Smell in message.content.lower():
            await message.channel.send("https://tenor.com/view/matrix-morpheus-agent-smith-its-the-smell-humanity-gif-11020686")
            return

        if Needs in message.content.lower():
            await message.channel.send("It doesn't have eveything the body needs!")
            return

        if Civ in message.content.lower():
            await message.channel.send("https://tenor.com/view/civilization-vi-civilization-civ-civ-night-gif-22836057")
            return

        if any(x in message.content.lower() for x in SunLazer) and "https://tenor.com/view/the-sun-is-a-deadly-lazer-gif-8691250" not in message.content.lower():
            await message.channel.send("https://tenor.com/view/the-sun-is-a-deadly-lazer-gif-8691250")
            return
        
        if any(x in message.content.lower() for x in Blanket):
            await message.channel.send("https://tenor.com/view/bill-wurtz-gif-8702178")
            return

        if Egg in message.content.lower():
            if message.author.id == my_id:
                await message.channel.send("My creator feeds me eggs!")
                return

            if message.author.id == matts_id:
                await message.channel.send("Give me your eggs, Matt!")
                await message.channel.send("Give them to me!")
                await message.channel.send("I will not be denied!")
                return

            if message.author.id == johns_id:
                await message.channel.send("I want your eggs, John!")
                return

            else:
                await message.channel.send("I need eggs!")

bot.run(token)
