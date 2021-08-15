# -*- coding: utf-8 -*-
# Nekotato#3168


#####
# Program Imports
#####


import discord
from discord.ext import commands

from nekotato import Moderation
from interactions import Interactions
from actions import Actions

import json
import nest_asyncio

nest_asyncio.apply()

#####
# Nekotato setup
#####


def get_prefix(my_client: commands.Bot, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    if message.guild:
        target_prefix = prefixes[str(message.guild.id)]
    else:
        target_prefix = ""
    return target_prefix


intents = discord.Intents().default()
intents.members = True


client = commands.Bot(command_prefix=get_prefix, help_command=None, intents=intents)

token = open("token.txt", "r").readlines()[0]


#####
# Discord basic functions
#####


@client.event
async def on_ready():
    global bot_mention_str
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with a ball of yarn"))
    print("Nekotato is online")
    bot_mention_str = client.user.mention.replace("@", "@!")


@client.event
async def on_message(message):
    # We grab the string to detect when a message contains the bot's mention
    global bot_mention_str

    # We really want to avoid processing our own messages
    if message.author != client.user:

        # If the message is in a server
        if message.guild:
            target_prefix = get_prefix(client, message)

            # If the message is for the bot
            if message.content.startswith(target_prefix) or message.content.startswith(target_prefix.upper()):

                # Removes the space after the prefix if there is one
                if message.content[len(target_prefix)] == " ":
                    message.content = target_prefix + message.content[len(target_prefix) + 1:]
                else:
                    message.content = target_prefix + message.content[len(target_prefix):]

            elif client.user.mentioned_in(message) and len(message.content) in [21, 22, 23] and "86243" in message.content:
                # A mention is considered as a search for help
                message.content = target_prefix + "help"

            # To avoid errors when people do typos
            try:
                await client.process_commands(message)
            except:
                pass

        else:
            if client.user.mentioned_in(message) and len(message.content) in [21, 22, 23]:
                await Moderation.help(Moderation(client), message)


#####
# Cogs/More commands
#####


@client.command()
@commands.is_owner()
async def reload(ctx):
    client.remove_cog("Moderation")
    client.remove_cog("Interactions")
    client.remove_cog("Actions")

    client.add_cog(Moderation(client))
    client.add_cog(Interactions(client))
    client.add_cog(Actions(client))
    
    


client.add_cog(Moderation(client))
client.add_cog(Interactions(client))
client.add_cog(Actions(client))

client.run(token)
