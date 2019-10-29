# bot.py
import os

import discord
import sys
import random
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
facts_list = []

@client.event
async def on_ready():
    print ('---------')
    print ('Loading...')
    with open('data.json') as json_file:
        facts = json.load(json_file)
        for fact in facts['cat_facts']:
            facts_list.append(fact)
    print ('Finished Loading')
    print ('---------')

    print ('---------')
    print ('%s is connected to the following guild:' % client.user)
    for guild in client.guilds:
        print ('%s' % guild.name.encode('utf-8'))
    print ("---------")

    # Print list of all member names
    # print ('Guild Members:\n')
    # for member in guild.members:
    #     print ('%s' % member.name.encode("utf-8"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()
    ack = '(Beep Boop, I am a bot made by Danaxa)'
    response = ''

    if content == '!catinfo':
        opener = 'Currently, I know %d facts about cats' % len(facts_list)
        string_constructor = [opener, ack]
        response = joinStrings(string_constructor)
    elif 'cat' in content or 'cats' in content or 'kitten' in content or 'kittens' in content or 'kitty' in content or 'kitties' in content:
        opener = 'Did you know?'
        middle = random.choice(facts_list)
        string_constructor = [opener, middle, ack]
        response = joinStrings(string_constructor)

    await message.channel.send(response)

def joinStrings(stringList):
    list=''
    for e in stringList:
        list = list + e + '\n'
    return list

client.run(TOKEN)