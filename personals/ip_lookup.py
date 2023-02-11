import urllib.request
from discord.ext import tasks
import discord
import datetime

TOKEN = 'OTkwNDQ0MDI3MjE0MTgwNDQy.GIkGFe.ryf0pYxLJ_bB9s8OgSnyOGfzbE70ehshkj6SnU'
channel_id = 991469606919229440
message_id = 991484751397539950
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