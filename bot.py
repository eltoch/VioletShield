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
heavy = {'anal', 'anus', 'arse', 'ass', 'smack my ass', 'ballsack', 'balls', 'blowjob', 'blow job', 'bollock', 'boner', 'boob','boobies', 'booby', 'cunt',  'butt', 
'buttplug', 'clitoris', ' cock', 'dick', 'diddle', 'dildo', 'feck', 'fuck', 'flange', 'jizz', 'knobend', 'penis', 'prick', 'pussy', 'sex', 'shit', 'sh1t', 'tit', 'titty', 
'tittie', 'twat', 'vagina', 'wank', 'whore', 'little boy', 'little girl', 'masturbate', 'jack off', 'kitty', 'kitten', 'porn', 
'sex', 'horny', 'sexy', 'h0rny', 's3x', 'seggsy', 's3ggsy', 'im hard', 'cum', 'daddy', 'princess', 'suck', 'slut', 'swallow', 'chode', 'nipple', 'lick', 'vag', 
'virgin', 'tight', 'wet', 'semen', 'you made me cum', 'you make me cum' 'how old are you', 'pegging', 'facial', 'buttfuck', 'butt fuck', 'but tfuck', 'little'}
medium = {'Anal', 'smack my ass', 'ballsack', 'balls', 'blowjob', 'blow job', 'boner', 'boob', 'boobies', 'booby', 'cunt', 'buttplug', 'clitoris', 'cock', 'dildo', 'fuck', 
'jizz', 'knobend', 'penis', 'prick', 'pussy', 'sex','tit', 'titty', 'tittie', 'twat', 'vagina', 'wank', 'whore', 'little boy', 'little girl', 'masturbate', 'jack off', 'kitty', 
'kitten', 'porn', 'sex', 'horny', 'sexy', 'h0rny', 's3x', 'seggsy', 's3ggsy', 'im hard', 'cum', 'daddy', 'princess', 'suck', 'slut', 'swallow', 
'chode', 'nipple', 'lick', 'vag', 'virgin', 'tight', 'wet', 'semen', 'you made me cum', 'you make me cum' 'how old are you', 'pegging', 'facial'}
light = {'horny', 'blowjob', 'boner', 'little girl', 'kitten', 'kitty', 'masturbate', 'porn', 'im hard', 'im hard', 'daddy', 'cum', 'princess', 
'slut', 'you make me hard', 'you make me cum', 'you made me cum', 'how old are you', 'pegging', 'peg'}
global banned
banned = {}

@client.event
async def on_message(message):
    msg = message.content.lower()

    global banned

    if message.content == "!elevel_heavy":
        banned = heavy
        await message.channel.send('Heavy mode selected')
    elif message.content == "!elevel_medium":
        banned = medium
        await message.channel.send('Medium mode selected')
    elif message.content == "!elevel_light":
        banned = light
        await message.channel.send('Light mode selected')
    
    for word in banned:

        # prevents the bot from replying to itself
        if message.author == client.user:
            return

        if msg.__contains__(word):
            response = 'Hello {0.author.mention} pls no horny'.format(message)
            # await message.channel.send(msg)
            await message.channel.send(response)
            



# Bot Login
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)