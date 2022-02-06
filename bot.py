#!/usr/bin/env python3

# import libraries
from dotenv import load_dotenv
import discord
import asyncio
import os

# Bot Token
load_dotenv('C:/Users/matth/Violet Shield/.env')
TOKEN = os.environ['TOKEN']
client = discord.Client()

# Banned word levels
heavy = ['sex', 'horny', 'sexy', 'h0rny', 's3x', 'seggsy', 's3ggsy', 'I\'m hard']
medium = ['boner', '']
light = []


@client.event
async def on_message(message):
    # prevents the bot from replying to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        # await message.channel.send(msg)
        await message.channel.send(heavy[3])



# Bot Login
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
