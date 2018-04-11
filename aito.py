import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot (command_prefix=".")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if "ALIENS" in message.content.upper():
        await client.send_message (message.channel, "HEY IKUTO!")
    elif message.content.upper().startswith("AITO!QUOTE"):
        await client.send_message(message.channel,random.choice(["I like tea~!",
                                                                 "It's getting dark... aaghhh ;;;",
                                                                 "Kiiro is so mean","Can I burn stuff",
                                                                 "Seiji is such a buzzkill","Ikuto is angrier than usual",
                                                                 "Hima is such a fun person to hang around with~...not like oTHER PEOPLE.",
                                                                 "Karma looks so worried about me lol",
                                                                 "Get rekt","What do you mean minecraft isn't cool?"]))
    elif "I LOVE AITO" in message.content.upper():
        await client.send_message (message.channel, "Thanks. I love me too.")
    elif "RUDE" in message.content.upper():
        await client.send_message (message.channel, "Why yuzuru-de?")
    elif "AITO NO" in message.content.upper():
        await client.send_message (message.channel, "aito yes")

client.run ("NDMzNzA5OTIwMjc4NDEzMzEy.DbAEuA.CAxnEXFlNL1eWI-EWbhys0claRk")
client.login (process.env.BOT_TOKEN)
