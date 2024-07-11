import random
import discord
import os
from dotenv import load_dotenv
from commands import Commands

BOT_NAME = "BroncoBot"
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


# Helper method to check if message is a command
def check_command(message):
    if message.content.startswith('>'):
        return True
    return False


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.commands = None


    async def handle_command(self, signal):
        self.commands = Commands(signal=signal)

        match self.commands.split_command[0]:
            case "coinflip":
                await self.commands.coinflip()
            case "roll":
                await self.commands.roll()
            case "prompt":
                await self.commands.prompt()
            case _:
                await signal.channel.send("You tried to issue me a command?!")

    # Executions on startup
    async def on_ready(self):
        server_count = 0

        print(f"Logged on as {self.user}")
        for server in bot.guilds:
            print(f"Connected to: {server.id} (name: {server.name})")
            server_count += 1

        print(f"{BOT_NAME} connected to {server_count} servers")

    async def on_message(self, message):
        # Prevents BroncoBot from spontaneous response to self or on commands
        if message.author.id == self.user.id:
            return
        elif check_command(message):  # If message is a command, handle it
            await self.handle_command(message)

intents = discord.Intents.default()
intents.message_content = True
bot = MyClient(command_prefix='>', intents=intents)

bot.run(DISCORD_TOKEN)
