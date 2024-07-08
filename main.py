import random
import discord
import os
from dotenv import load_dotenv
from commands import Commands

BOT_NAME = "BroncoBot"
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Helper method to check if message is a command
    def check_command(self, message):
        if message.content.startswith('>'):
            return True
        return False

    async def handle_command(self, message):
        commands = Commands(msg=message)

        match commands.getCommand()[0]:
            case "coinflip":
                await commands.coinflip()
            case "roll":
                await commands.roll()
            case "prompt":
                await commands.prompt()
            case _:
                await message.channel.send("You tried to issue me a command?!")

    # Executions on startup
    async def on_ready(self):
        server_count = 0

        print(f"Logged on as {self.user}")
        for server in bot.guilds:
            print(f"Connected to: {server.id} (name: {server.name})")
            server_count += 1

        print(f"{BOT_NAME} connected to {server_count} servers")

    # Random chance for every message that BroncoBot chooses to respond
    async def on_message(self, message):
        # Prevents BroncoBot from spontaneous response to self or on commands
        if message.author.id == self.user.id:
            return
        elif self.check_command(message):  # If message is a command, handle it
            await self.handle_command(message)
        elif random.random() < 1:  # probability that bot responds
            await message.channel.send('"' + message.content + '"')


intents = discord.Intents.default()
intents.message_content = True
bot = MyClient(command_prefix='>', intents=intents)

bot.run(DISCORD_TOKEN)
