import random
import discord
import os
from dotenv import load_dotenv

BOT_NAME = "BroncoBot"
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        server_count = 0
        
        print(f"Logged on as {self.user}")
        for server in bot.guilds:
            print(f"Connected to: {server.id} (name: {server.name})")
            server_count += 1

        print(f"{BOT_NAME} connected to {server_count} servers")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if random.random() < 0.15:
            await message.channel.send('"' + message.content + '"')


intents = discord.Intents.default()
intents.message_content = True
bot = MyClient(intents=intents)
bot.run(DISCORD_TOKEN)
