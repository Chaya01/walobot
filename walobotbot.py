import discord
import random
import os
import requests
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from discord.ext import commands
import re
from Fetcher import FetchImages as fetcher

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
async def loremipsum(ctx): 
  username = ctx.author.name
  lorem = 'Lorem ipsum dolor sit cuchuflí barquillo bacán jote gamba listeilor po cahuín, luca melón con vino pichanga coscacho ni ahí peinar la muñeca chuchada al chancho achoclonar. Chorrocientos pituto ubicatex huevo duro bolsero cachureo el hoyo del queque en cana huevón el año del loly hacerla corta impeque de miedo quilterry la raja longi ñecla. Hilo curado rayuela carrete quina guagua lorea piola ni ahí.'
  await ctx.send('Solicitado por: ' + str(username))
  await ctx.send(lorem)

@bot.command() 
async def wate(ctx, member: discord.Member = None): 
    final_string = '';
    if member is None:
        final_string = 'Oye '+ ctx.author.mention +' Walobot te ha pegado un wate porque no indicaste a quien pegarle'
    elif str(ctx.author.id) == str(member.id):
        final_string = ctx.author.mention+ ' se ha pegado un wate, el muy perkin'
    else:
        final_string = ctx.author.mention+ ' le ha pegado un wate a ' + member.mention

    image = fetcher("slap")

    await ctx.message.delete()
    await ctx.send(final_string)
    await ctx.send(image.find_random_image_tenor())


@bot.command() 
async def combos(ctx, *members: discord.Member):
    final_string = ''
    if len(members) == 0:
        final_string = 'Oye '+ ctx.author.mention +' Walobot te ha pegado unos combos porque no indicaste a quien pegarle'
    elif len(members) == 1:
        if str(ctx.author.id) == str(members[0].id):
            final_string = ctx.author.mention+ ' se ha pegado combos a si mismo, el muy perkin'
        else:
            final_string = ctx.author.mention+ ' le ha pegado combos a ' + members[0].mention
    else:
        users = ''
        for member in members:
            users = users + member.mention + " "
        final_string = ctx.author.mention+ ' ha repartdo combos a ' + users

    image = fetcher("punch")

    await ctx.message.delete()
    await ctx.send(final_string)
    await ctx.send(image.find_random_image_tenor())




# Run the bot with your bot token
bot.run('MTE2MjI2MjI1NTM0NjQwMTI4MA.GlKx-S.MPsVB0oXecrOKDtENJXkIGlJxQs5aDly2K8beI')
