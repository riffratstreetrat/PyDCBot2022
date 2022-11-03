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
        await message.channel.send('Do you have a dead uncle? ($yes/$no)')
        y["counter"]+=1
        return


    if message.content.startswith('$yes') and y["counter"] == 1:
        await message.channel.send('I am sorry to hear that...*cough* *cough*...did he die by choking on a meatball parm? ($yes/$no)')
        y["counter"]+=1
        return

    if message.content.startswith('$no') and y["counter"] == 1:
        await message.channel.send('I am shocked! Perhaps I have lost my gift for communicating with the dead. Goodbye!')


    elif message.content.startswith('$yes') and y["counter"] == 2:
        await message.channel.send('Figures...That is how most of us die here on Long Island. Just know that your Uncle is at peace and very proud of you. Goodbye!')
        y["counter"]+=1
        return

    if message.content.startswith('$no') and y["counter"] == 2:
        await message.channel.send('Hmm perhaps it was *cough* ravioli?. ($yes)')
        y["counter"]+=1
        return

    if message.content.startswith('$yes') and y["counter"] == 3:
        await message.channel.send('AHA! You can never stump the Long Island Medium. Goodbye!')
        

    if message.content.startswith('Theresa tell me your life story'):
        await message.channel.send('AHA! You can never stump the Long Island Medium. Goodbye!')
        

client.run(os.getenv('TOKEN'))
