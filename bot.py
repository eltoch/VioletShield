#!/usr/bin/env python3

# import libraries
from dotenv import load_dotenv
from discord.ext import commands
import discord
import asyncio
import os


# Bot Token
load_dotenv('C:/Users/matth/Violet Shield/.env')
TOKEN = os.environ['TOKEN']
client = discord.Client()

heavy = set(())
medium = set(())
light = set(())

global banned
banned = {}

f = open("light.txt", "r") 
for line in f:
    line = str(f.readline().rstrip('\n'))
    light.add(line)
f.close()
f = open("medium.txt", "r")
for line in f:
    line = str(f.readline().rstrip('\n'))
    medium.add(line)
f.close()
f = open("heavy.txt", "r")
for line in f:
    line = str(f.readline().rstrip('\n'))
    heavy.add(line)
f.close()
global channel_id
channel_id = 0
# message read 

#@client.command(pass_context=True)




@client.event
async def on_message(message):

    msg = message.content.lower()
    msg = msg.replace('@', 'a')
    msg = msg.replace('$', 's')
    msg = msg.replace('\'', '')
    msg = msg.replace('+', 't')
    msg = msg.replace('0', 'o')
    msg = msg.replace('1', 'i')
    mgs = msg.replace('_', '')
    mgs = msg.replace('-', '')

    global banned
    global channel_name

    if (message.content == "!elevel_heavy") and message.author.guild_permissions.administrator:
        banned = heavy
        await message.channel.send('Heavy mode selected')
    elif (message.content == "!elevel_medium") and message.author.guild_permissions.administrator:
        banned = medium
        await message.channel.send('Medium mode selected')
    elif (message.content == "!elevel_light") and message.author.guild_permissions.administrator:
        banned = light
        await message.channel.send('Light mode selected')
    elif (message.content.startswith("!channel_name")) and message.author.guild_permissions.administrator:
        channel_name = message.content.lstrip("!channel_name ")
        print(channel_name)
        await message.channel.send('Channel Name assigned!')

    for word in banned:

        # prevents the bot from replying to itself
        if message.author == client.user:
            return

        if msg.__contains__(word):
            response = '{0.author.mention} message has been blocked. Please be respectful'.format(message)
            await message.channel.send(response)

            

            await message.delete()
            break

            



# Bot Login
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
