import os
import random

import discord
import asyncio

TOKEN = 'token'
CHANNEL_ID = 0000 # Channel ID to join

intents = discord.Intents.all()  # Enable all intents (This must be done on discord application page as well)
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    # Check if the bot is already in a voice channel
    if bot.voice_clients:
        await bot.voice_clients[0].disconnect()

    # Fetch the voice channel directly by ID
    channel = bot.get_channel(CHANNEL_ID)

    # Join the specified voice channel
    vc = await channel.connect()
    # choose a random sound file from the audio directory
    file = random.choice(os.listdir("audio"))
    while True:
        # get a random sound file from the SOUND_FILES list
        new_file = random.choice(os.listdir("audio"))

        while new_file == file:
            new_file = random.choice(os.listdir("audio"))
        file = new_file
        # Play the local sound file
        vc.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(source="audio/" + file), volume=0.2),
                after=lambda e: print('done', e) if e else None)

        # Wait for the sound to finish playing
        while vc.is_playing():
            await asyncio.sleep(1)

bot.run(TOKEN)
