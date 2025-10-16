import discord
import asyncio
import os

# Hämta token och kanal-ID från miljövariabler
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Inloggad som {client.user}")
    channel = client.get_channel(CHANNEL_ID)

    # Loopa och skicka meddelande varje sekund
    while True:
        await channel.send("🔁 Meddelande varje sekund!")
        await asyncio.sleep(1)  # Vänta 1 sekund

client.run(TOKEN)
