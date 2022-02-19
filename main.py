import discord
from discord.ext import commands

from Token import key

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="&" , intents = intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}' .format(bot))

@bot.event
async def on_message(message):

    if message.channel.id == 943851439288119346:
        otvet = message.content
        channel = bot.get_channel(852590801971970059)
        await channel.send(otvet)
    else:
        pass

bot.run(key)
