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
'buttplug', 'clitoris', ' cock', 'dick', 'diddle', 'dildo', 'feck', 'fuck', 'flange', 'jizz', 'knobend', 'penis', 'prick', 'pussy', 'sex', 'shit', 'tit', 'titty', 
'tittie', 'twat', 'vagina', 'wank', 'whore', 'little boy', 'little girl', 'masturbate', 'jack off', 'kitty', 'kitten', 'porn', 
'sex', 'horny', 'sexy', 'h0rny', 's3x', 'seggsy', 's3ggsy', 'im hard', 'cum', 'daddy', 'princess', 'suck', 'slut', 'swallow', 'chode', 'nipple', 'lick', 'vag', 
'virgin', 'tight', 'wet', 'semen', 'you made me cum', 'you make me cum' 'how old are you', 'pegging', 'facial', 'buttfuck', 'butt fuck', 'but tfuck', 'little', 'kid'}

medium = {'Anal', 'smack my ass', 'ballsack', 'balls', 'blowjob', 'blow job', 'boner', 'boob', 'boobies', 'booby', 'cunt', 'buttplug', 'clitoris', 'cock', 'dildo', 'fuck', 
'jizz', 'knobend', 'penis', 'prick', 'pussy', 'sex','tit', 'titty', 'tittie', 'twat', 'vagina', 'wank', 'whore', 'little boy', 'little girl', 'masturbate', 'jack off', 'kitty', 
'kitten', 'porn', 'sex', 'horny', 'sexy', 'h0rny', 's3x', 'seggsy', 's3ggsy', 'im hard', 'cum', 'daddy', 'princess', 'suck', 'slut', 'swallow', 
'chode', 'nipple', 'lick', 'vag', 'virgin', 'tight', 'wet', 'semen', 'you made me cum', 'you make me cum' 'how old are you', 'pegging', 'facial','kid'}

light = {'horny', 'blowjob', 'boner', 'little girl', 'kitten', 'kitty', 'masturbate', 'porn', 'im hard', 'daddy', 'cum', 'princess', 
'slut', 'you make me hard', 'how old are you', 'pegging', 'peg','kid'}

global banned
banned = {}

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

    if (message.content == "!elevel_heavy") and message.author.guild_permissions.administrator:
        banned = heavy
        await message.channel.send('Heavy mode selected')
    elif (message.content == "!elevel_medium") and message.author.guild_permissions.administrator:
        banned = medium
        await message.channel.send('Medium mode selected')
    elif (message.content == "!elevel_light") and message.author.guild_permissions.administrator:
        banned = light
        await message.channel.send('Light mode selected')
    
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
