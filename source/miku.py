import os
import discord
my_secret = os.environ['Token']

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == 'Pizza is so good':
   await message.channel.send('Go get your pizza!')

  if message.content == 'Pizza':
   await message.channel.send('Go get your pizza!')

  if message.content == 'I love pizza':
   await message.channel.send('Go get your pizza!')

  if message.content == 'Pizza is amazing':
   await message.channel.send('Go get your pizza!')

client.run(os.getenv('Token'))
