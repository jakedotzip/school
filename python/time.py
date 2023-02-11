import urllib.request
from discord.ext import tasks
import discord
import datetime

TOKEN = 'OTkwNDQ0MDI3MjE0MTgwNDQy.GIkGFe.ryf0pYxLJ_bB9s8OgSnyOGfzbE70ehshkj6SnU'
channel_id = 991469606919229440
message_id = 991484751397539950
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
client = discord.Client()



client.run(TOKEN)