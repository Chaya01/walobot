import discord
import random
import os
import requests
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from discord.ext import commands

# Define your bot's command prefix
#bot_prefix = "!"

# Define the intents for your bot (in this case, both intents are used)
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

# Create a bot instance with the intents parameter
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Connected to the following guilds:')
    for guild in bot.guilds:
        print(f'- {guild.name} (ID: {guild.id})')

@bot.command()
async def random_number(ctx):
    print(f"Received command: !random_number")
    # Generate and send a random number
    random_num = random.randint(1, 100)
    print(f"Generated random number: {random_num}")
    await ctx.send(f"Random Number: {random_num}")

@bot.event 
async def on_message(message): 
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name) 
    user_message = str(message.content) 
  
    print(f'Message {user_message} by {username} on {channel}') 
  
    if message.author == bot.user: 
        return
  
    if channel == "shipoppin": 
        if user_message.lower() == "hello" or user_message.lower() == "hi": 
            await message.channel.send(f'Hello {username}') 
            return
        elif user_message.lower() == "bye": 
            await message.channel.send(f'Bye {username}') 
        elif user_message.lower() == "tell me a joke": 
            jokes = [" Can someone please shed more light on how my lamp got stolen?", "Why is she called llene? She stands on equal legs.", "What do you call a gazelle in a lions territory? Denzel."] 
            await message.channel.send(random.choice(jokes)) 

    await bot.process_commands(message)

@bot.command()
async def ping(ctx): 
  await ctx.send('pong!')

@bot.command()
async def xualo(ctx): 
  username = ctx.author.name
  await ctx.send('xualo ' + str(username))


@bot.command()
async def danbooru_image(ctx, *query_words):
    # Combine the query words with underscores to form the query
    query = "_".join(query_words)

    # Danbooru API URL to fetch a random image with the specified query
    danbooru_api_url = f"https://danbooru.donmai.us/posts/random.json?tags={query}"

    try:
        # Make a request to the Danbooru API
        response = requests.get(danbooru_api_url)

        if response.status_code == 200:
            danbooru_data = response.json()

            if not danbooru_data:
                await ctx.send(f"Tag '{query}' not found.")
            else:
                image_url = danbooru_data["file_url"]
                await ctx.send(image_url)
        else:
            await ctx.send("Unable to find an image for the specified query.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command()
async def tmr(ctx,):
    # Combine the query words with underscores to form the query
    query = "_".join(query_words)

    # Danbooru API URL to fetch a random image with the specified query
    danbooru_api_url = f"https://danbooru.donmai.us/posts/random.json?tags={query}"

    try:
        # Make a request to the Danbooru API
        response = requests.get(danbooru_api_url)

        if response.status_code == 200:
            danbooru_data = response.json()

            if not danbooru_data:
                await ctx.send(f"Tag '{query}' not found.")
            else:
                image_url = danbooru_data["file_url"]
                await ctx.send(image_url)
        else:
            await ctx.send("Unable to find an image for the specified query.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
# Run the bot with your bot token
bot.run('MTE2MjI2MjI1NTM0NjQwMTI4MA.GlKx-S.MPsVB0oXecrOKDtENJXkIGlJxQs5aDly2K8beI')
