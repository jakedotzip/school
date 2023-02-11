import discord
client = discord.Client()
channel1id = 935311693737787443
channel2id = 1009885175951413278

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.channel.id == channel1id:
        channeltosend = client.get_channel(channel2id)
        await channeltosend.send(message.content, embed=message.embeds[0])

client.run("MTAyODM4NTA1MzY2MDY3NjE2OA.Gs_XK6.jU-46ACLrEeDFHnpy-VFmfVDwX1e6TupG-fVZ8")