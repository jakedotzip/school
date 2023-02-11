import urllib.request
from discord.ext import tasks
import discord
import datetime

TOKEN = '' # put bot token in the ''
channel_id = 123 # replace 123 with channel id
message_id = 456 # replace 456 with message id, this requires the bot to send a message first 
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
client = discord.Client()


@tasks.loop(seconds=5)
async def ip_lookup():
  channel = client.get_channel(channel_id)
  msg = await channel.fetch_message(message_id)
  embedVar = discord.Embed(
    title = "Current External IP Address",
    description = f"{external_ip}",
    color=0x00ff00,
    timestamp = datetime.datetime.utcnow()
  )
  await channel.send(embed = embedVar)
  

@ip_lookup.before_loop
async def before():
  await client.wait_until_ready()

ip_lookup.start()
client.run(TOKEN)
