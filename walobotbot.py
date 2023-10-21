import discord
import random
import os
import requests
from discord.ext import commands
import re
from Fetcher import FetchImages as fetcher
from Booru import Fetchbooru
import Pepe

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
async def danbooru(ctx, *query_words):
    query = Fetchbooru(query_words)
    image = await query.find_rand_img(ctx)
    await ctx.message.delete()
    await ctx.send(image)


@bot.command()
async def tmr(ctx):
    final_string = '';
    rand_number = random.randint(1, 6)
    #Generate a int based on a random nuumber
    switch_dict = {
        1: "@everyone {} Ha hecho el llamado a la DOTA",
        2: "@everyone {} dice AGG KGADAS NO SABEN JUGAR (VENGAN AL DOTA)",
        3: "@everyone {} dice a tiltearse cabros",
        4: "@everyone {} dice que carrea",
        5: "@everyone Cabros me mataron - {}",
        6: "@everyone EKIS DE - {}",
    }

    final_string = switch_dict.get(rand_number, "{}").format(ctx.author.mention)
    image = fetcher("peru serrano")

    await ctx.message.delete()
    await ctx.send(final_string)
    message = await ctx.send(image.find_random_image_tenor())
    await message.add_reaction("🇵🇪")


@bot.command()       
async def yapocarlos(ctx):
    carlos = 'fate_(series)'
    query = Fetchbooru(carlos)
    image = await query.find_rand_img(ctx)
    await ctx.message.delete()
    # Create a Rich Embed
    embed = discord.Embed(
        title="Ya po carlos bajate el fate",
        description="Fgo.",
        color=0x0072b3  # You can specify your desired color here.
    )
    # Add the image URL to the card
    embed.set_image(url=image)

    await ctx.send(embed=embed)
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


@bot.command()
async def r34(ctx, *query_words):
    # Combine the query words with underscores to form the query
    query = "_".join(query_words)

    # Danbooru API URL to fetch a random image with the specified query
    r34_url = f"https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&limit=50&tags={query}&json=1"
    
    try:
        # Make a request to the Danbooru API
        response = requests.get(r34_url)
        if response.text != '':
            r34_data = response.json()
            rando_number = random.randint(0, len(r34_data))
            if not r34_data:
                await ctx.send(f"Tag '{query}' not found.")
            else:

                
                if r34_data[rando_number]["file_url"].endswith('.mp4'):
                    await ctx.send("Salsa {}".format(r34_data[rando_number]["source"]))
                    await ctx.send(r34_data[rando_number]["file_url"])

                else:
                    embed = discord.Embed(
                    title="Rule 34",
                    description="Salsa "+ r34_data[rando_number]["source"],
                    color=discord.Color.blue()  # You can set the color of the embed.
                )
                    embed.set_image(url=r34_data[rando_number]["file_url"])
                    await ctx.send(embed=embed)
                    

        else:
            await ctx.send("Unable to find an image for the specified query.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command()       
async def gei(ctx): 
  username = ctx.author.name
  pasta = 'No soy gay pero soy peruano y tengo una fantasia donde Perú invade Chile y Chile tiene que exportar esclavos femboys para satisfacer oficiales peruanos de alto rango. Me imagino que soy un comandante poderoso alto, con una mandibula cuadrada y con músculos masivos. Mi femboy es un pequeño chileno timido con piel palida que viene a mi habitacion. Lo agarro con mis poderosos brazos y lo beso a la fuerza, presionando su pecho contra el mio. Lo tiro contra la cama con mis grandes brazos quitándole sus pequeños calzones vírgenes. Le muestro mi masivo mastodonte peruano, y despues se la meto con todo, follándolo con una fuerza inhumana. Cada movimiento lo hace gemir, y finalrnente me corro en su pequeño culito chileno, dejando el semen corriendole por sus pequeñas nalgas, y después lo abrazo con mis grandes y fuertes brazos peruanos haciendolo dormir en mi pecho ¿Algún otro hetero tiene este tipo de fantasias?'
  await ctx.message.delete()
  await ctx.send(pasta)

@bot.command()
async def speak(ctx, channel_name, *, text_to_speak):
    # Find the voice channel by name
    for guild in bot.guilds:
        for voice_channel in guild.voice_channels:
            if voice_channel.name == channel_name:
                voice_channel_to_join = voice_channel
                break

    if 'voice_channel_to_join' in locals():
        voice_client = await voice_channel_to_join.connect()
        await ctx.send(text_to_speak, tts=True)
        await voice_client.disconnect()
    else:
        await ctx.send(f"Voice channel '{channel_name}' not found.")
        
@bot.command()
async def pepe(ctx):
  pepes = Pepe.Pepe()

  where_da_pepes_at = bot.get_channel(1162571489581744128)
  await ctx.message.delete()
  await where_da_pepes_at.send(pepes.pick_random())

@bot.command()       
async def peru(ctx): 
  username = ctx.author.name

  await ctx.message.delete()
  message = await ctx.send("VIVA EL PERU CARAJO")
  await message.add_reaction("🇵🇪")


# Run the bot with your bot token
bot.run('MTE2MjI2MjI1NTM0NjQwMTI4MA.GlKx-S.MPsVB0oXecrOKDtENJXkIGlJxQs5aDly2K8beI')


