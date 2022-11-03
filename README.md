# PyDCBot2022
Python Discord Bot

The function of my bot is that it interacts with you in the chat and impersonates Theresa Caputo otherwise known as the Long Island Medium. The bot first responds
if you type $hello into the chat. From there it will ask yes or no questions to which you can reply with $yes/$no to get a response. The main goal of doing this specific
task was I wanted to challenge myself to make it so that the user can say $yes twice and Theresa would have a different response to each yes. If I were just coding in
javascript this would be an easy task, but because I was coding according to Python and Discord, this task was much more difficult. At first, I wanted to tackle this
challenge by creating different functions for each response, but I quickly realized that this method would not work. This is because I struggled to adapt to how functions
work in python. After asking Liam, who is much more well-versed in Python, he reccomended using a counter variable instead. I thought this was a great idea because it was much simpler
and seemed like it would be similar to javascript. Unfortunately after struggling to create and alter a counter variable, I realized that declaring and changing a variable
would not be as straightforward as it is in Javascript. After working with Mush to figure out the proper notation, Liam realized he had experienced a similar problem and
solved it by using a json file to reference his variables. Therefore, my code works according to the following process:

1. Imports all of the proper data
2. Sets the discord intents to default (Intents are what define what data the bot recieves, analyzes, and responds to (I think)) https://discordjs.guide/popular-topics/intents.html#privileged-intents 
3. Uses a json file to define the counter variable and sets it equal to the y value
4. Notifies the user when the bot has logged in by printing it in the terminal
5. When the bot recieves a message from the user, it reads what the message says, and if it meets the guidlines and required counter value, it responds with a corresponding
answer
6. With each message that does not end the conversation, the counter value increases by 1 so the user can say yes or no for a second time without getting the same response,
and the function is ended so it does not repeat.
7. The bot's token is accessed from the .env file

Sources:
https://www.freecodecamp.org/news/create-a-discord-bot-with-python/ This amazing tutorial helped me set up the basic bot in which the user types something in the chat, and if
it meets the guidelines the bot will respond

https://www.w3schools.com/python/python_json.asp This link and Liam Gibbons helped me understand and utilize Json files

Mush, Isa, and Jibraan were extremely helpful throughout the entire process and provided both support and guidance, thank you guys!

Special thank you to David for collaborating with me on the basic bot setup while following the python bot tutorial. I had a lot of fun working with you, and I could not
not have done it without you!

Thank you Liam for all of your Python wisdon, you are amazing!
