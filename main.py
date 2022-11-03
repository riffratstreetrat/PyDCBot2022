import discord
import os
import json
from dotenv import load_dotenv
load_dotenv()

#imports required files and data

intents = discord.Intents.default()
intents.message_content = True
#Defines the types of data that the bot responds to or interacts with (I think)

client = discord.Client(intents=intents)

data = '{"counter": 0}' #Uses json to define counter variable at 0

y = json.loads(data) #sets y variable equal to counter variable (0)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    #When the bot is online, alert the user in the terminal

@client.event
async def on_message(message):
#When a message appears in the chat...
   
        
    if message.author == client.user:
        return
        #If the message is from the user

    if message.content.startswith('$hello'): #If the message is $hello 
        await message.channel.send('Do you have a dead uncle? ($yes/$no)') #reply
        y["counter"]+=1 #increase counter by 1
        return #keeps action from repeating
        


    if message.content.startswith('$yes') and y["counter"] == 1: #if message is $yes and counter = 1
        await message.channel.send('I am sorry to hear that...*cough* *cough*...did he die by choking on a meatball parm? ($yes/$no)') #reply
        y["counter"]+=1 #increase counter by 1
        return

    if message.content.startswith('$no') and y["counter"] == 1: #if message is $no and counter = 1
        await message.channel.send('I am shocked! Perhaps I have lost my gift for communicating with the dead. Goodbye!') #reply


    elif message.content.startswith('$yes') and y["counter"] == 2: #if message is $yes and counter = 2
        await message.channel.send('Figures...That is how most of us die here on Long Island. Just know that your Uncle is at peace and very proud of you. Goodbye!') #reply
        y["counter"]+=1 #increase counter by 1
        return

    if message.content.startswith('$no') and y["counter"] == 2: #if message is $no and counter = 2
        await message.channel.send('Hmm perhaps it was *cough* ravioli?. ($yes)') #reply
        y["counter"]+=1 #increase counter by 1
        return

    if message.content.startswith('$yes') and y["counter"] == 3: #if message is $yes and counter = 3
        await message.channel.send('AHA! You can never stump the Long Island Medium. Goodbye!') #reply
        
        

client.run(os.getenv('TOKEN')) #fetches the bot's token from the .env file
