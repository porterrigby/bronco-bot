import random
import discord
import os
from dotenv import load_dotenv
from commands import Commands
from transponder import Transponder

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
BOT_NAME = "BroncoBot"


# Helper method to check if message is a command
def check_command(message):
    if message.content.startswith('>'):
        return True
    return False


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.commands = None
        self.transponder = Transponder()

    async def handle_command(self, signal):
        """
        Parses discord channel message, and triggers the appropriate command

        :param signal: The structure representing a discord channel message.
        """
        self.commands = Commands(self.transponder, signal)

        match self.commands.split_content[0]:
            case "coinflip":
                await self.commands.coinflip()
            case "roll":
                await self.commands.roll()
            case "prompt":
                await self.commands.prompt()
            case _:
                await signal.channel.send("You tried to issue me a command?!")

    # Executes on startup
    async def on_ready(self):
        server_count = 0

        print(f"Logged on as {self.user}")
        for server in bot.guilds:
            print(f"Connected to: {server.id} (name: {server.name})")
            server_count += 1

        print(f"{BOT_NAME} connected to {server_count} servers")

    # Interprets and handles messages sent in a discord channel.
    async def on_message(self, message):
        if message.author.id == self.user.id:  # Prevents bot self-responding
            return
        elif check_command(message):  # Handles commands
            await self.handle_command(message)


intents = discord.Intents.default()
intents.message_content = True
bot = MyClient(command_prefix='>', intents=intents)
bot.run(DISCORD_TOKEN)
