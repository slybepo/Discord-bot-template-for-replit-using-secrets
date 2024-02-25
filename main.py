import os
import discord
import requests
from datetime import datetime, timedelta
import discord
import random
import string

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



def generate_random_key():
    key_parts = []
    for _ in range(3):
        part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
        key_parts.append(part)
    return '-'.join(key_parts)


# Event handler for when a message is received
@client.event
async def on_message(message):
    # Check if the message starts with "-getkey" and it's not sent by the bot itself
    if message.content.startswith('-getkey') and not message.author.bot:
        # Generate a random key
        key = generate_random_key()
        # Send the key as a message
        await message.channel.send(f'menu Key: {key}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-invite'):
        await message.channel.send('invite link: https://discord.com/invite/4aZybEna \n make sure to invite your friends!')
    



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="SAPHIRE MENU GET NOW | FREE | DECENT MODS | OPEN FOR COLABS"))
  
try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            ""
        )
    else:
        raise e
      
