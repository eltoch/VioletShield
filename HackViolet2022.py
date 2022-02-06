#!/usr/bin/env python3

# import libraries
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import discord
import asyncio
import os


# Bot Token
load_dotenv()
TOKEN = os.environ['TOKEN']
bot = commands.Bot(command_prefix = "!", case_insensitive = True)
client = discord.Client()

# Creaes the necessary sets for each level. 
heavy = set(())
medium = set(())
light = set(())

# Creates the innitial banned value and sets the default=. 
global banned
banned = heavy

# Opens text documents and reads eachline, then adds them as an object on the set. 
with open("light.txt") as f:
    line = f.readline()
    length = len(f.readlines())
    f.seek(0)
    for i in range(length+1):
        line = f.readline()
        light.add(line.rstrip('\n'))
f.close()
with open("medium.txt") as f:
    line = f.readline()
    length = len(f.readlines())
    f.seek(0)
    for i in range(length+1):
        line = f.readline()
        medium.add(line.rstrip('\n'))
f.close()
with open("heavy.txt") as f:
    line = f.readline()
    length = len(f.readlines())
    f.seek(0)
    for i in range(length+1):
        line = f.readline()
        heavy.add(line.rstrip('\n'))
f.close()

# Used later
global channel_id
channel_id = 0
 
# Creates commands for each level. 
@bot.command(name = 'elevel_heavy')
@has_permissions(administrator = True) 
async def elevel_heavy(ctx):
    global banned
    banned = heavy
    await ctx.channel.send('Heavy mode selected')


@bot.command(name = 'elevel_medium')
@has_permissions(administrator = True) 
async def elevel_medium(ctx):
    global banned
    banned = medium
    await ctx.channel.send('Medium mode selected')

@bot.command(name = 'elevel_light')
@has_permissions(administrator = True) 
async def elevel_light(ctx):
    global banned
    banned = light
    await ctx.channel.send('Light mode selected')
# Currently not used, will be implemented later. 
@bot.command(name = 'channel_id')
@has_permissions(administrator = True) 
async def choose_channel_id(ctx, cid):
    channel_id = cid.lower()
    channel_id = cid.replace('o','0')
    channel_id = cid.replace('l','1')
    channel_id = cid.replace('i','1')
    await ctx.channel.send('Channel Name assigned!')

# Runs the help command. 
@bot.command(name = 'helpme')
@has_permissions(administrator = True) 
async def helpme(message):
    response = 'Documentation availiable at https://tinyurl.com/VioletShield'.format(message)
    embedVar = discord.Embed(title="Bot Commands", description=response, color=0xCE9DD9)
    await message.channel.send(embed=embedVar)

# Detects each time a message is sent.
@bot.event
async def on_message(message):

    global banned

    msg = message.content.lower()
    msg = msg.replace('@', 'a')
    msg = msg.replace('$', 's')
    msg = msg.replace('\'', '')
    msg = msg.replace('+', 't')
    msg = msg.replace('0', 'o')
    msg = msg.replace('1', 'i')
    mgs = msg.replace('_', '')
    mgs = msg.replace('-', '')

    print(msg)
   
    await bot.process_commands(message)

    for word in banned:

        # prevents the bot from replying to itself
        

        if message.author.bot:
            return
        # determines if the message contains the banned phrase. 
        if msg.__contains__(word):
            message1 = message
            await message.delete()

            #Creates an embeded message response
            response = '{0.author.mention} message has been blocked. Please be respectful'.format(message1)
            embedVar = discord.Embed(title="Potty word detected", description=response, color=0xB399D4)
            await message1.channel.send(embed=embedVar)

            

bot.run(TOKEN)