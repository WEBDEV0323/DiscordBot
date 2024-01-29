import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
    )

#
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('!add_role'):
#         # Find role name
#         role_name = message.content.split(' ')[1]
#
#         # search corresponding Discord role
#         role = discord.utils.get(message.guild.roles, name=role_name)
#
#         # Check if the role exists
#         if role is None:
#             await message.channel.send(f'Role "{role_name}" does not exist)
#             return
#
#         # Role assignment
#         await message.author.add_roles(role)
#         await message.channel.send(f'Role "{role_name}" was added to {message.author}')

client.run(TOKEN)
