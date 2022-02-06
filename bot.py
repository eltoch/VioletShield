#!/usr/bin/env python3

# import libraries
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import discord
import asyncio
import os


# Bot Token
load_dotenv('C:/Users/matth/Violet Shield/.env')
TOKEN = os.environ['TOKEN']
bot = commands.Bot(command_prefix = "!", case_insensitive = True)
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

global send
send = False
# message read 



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
    await ctx.channel.send('Heavy mode selected')

@bot.command(name = 'elevel_light')
@has_permissions(administrator = True) 
async def elevel_light(ctx):
    global banned
    banned = light
    await ctx.channel.send('Light mode selected')

@bot.command(name = 'channel_id')
@has_permissions(administrator = True) 
async def choose_channel_id(ctx, cid):
    channel_id = cid.lower()
    channel_id = cid.replace('o','0')
    channel_id = cid.replace('l','1')
    channel_id = cid.replace('i','1')
    await ctx.channel.send('Channel Name assigned!')

@bot.event
async def on_message(message):

    global banned
    global send

    msg = message.content.lower()
    msg = msg.replace('@', 'a')
    msg = msg.replace('$', 's')
    msg = msg.replace('\'', '')
    msg = msg.replace('+', 't')
    #msg = msg.replace('0', 'o')
    msg = msg.replace('1', 'i')
    mgs = msg.replace('_', '')
    mgs = msg.replace('-', '')

    print(msg)
   
    await bot.process_commands(message)

    for word in banned:

        # prevents the bot from replying to itself
        

        #if message.author == client.user:
        #    return

        if msg.__contains__(word):
            response = '{0.author.mention} message has been blocked. Please be respectful'.format(message)
            await message.channel.send(response)
            await message.delete()
            send  = True

@bot.command(name = 'send')
@has_permissions(administrator = True)
async def embed(ctx):
    global channel_id
    print('hi')
    channel = bot.get_channel(channel_id)
    embed = discord.Embed(title="Embed test", description="A test for my discord bot", color=0x5bcdee)
    embed.add_field(name="Hello!", value="Hello World!", inline=False)
    await channel.send(embed=embed)


bot.run(TOKEN)