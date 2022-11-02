import discord
import os
import json
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

data = '{"counter": 0}'

y = json.loads(data)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

   
        
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Do you have a dead uncle?')
        y["counter"]+=1
        await message.channel.send(y["counter"])
        


       


client.run(os.getenv('TOKEN'))
