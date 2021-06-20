import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('Discord_Token')

client = commands.Bot(command_prefix= '!')

@client.event
async def on_ready():
    print('we are ready')

client.run(TOKEN)




