"""
Defines logic for commands parsed from discord channel messages.
"""

import random
from transponder import Transponder


class Commands:

    def __init__(self, signal):
        self.signal = signal
        self.split_content = self.signal.content[1:].split(" ")
        self.message = f"Q: {self.signal.content[7:]} A: "
        self.transponder = Transponder()

    async def coinflip(self):
        """
        Flips an equally weighted, two-sided coin, and sends the result as
        a discord message.
        """
        if random.random() >= 0.5:
            await self.signal.channel.send("Heads!")
        else:
            await self.signal.channel.send("Tails!")

    async def roll(self):
        """
        Rolls an n-sided dice based on the first whitespace-delimited token
        found in after the command indicator. Sends the result of the roll
        as a discord message.
        """
        await self.signal.channel.send(
            random.randint(0, int(self.message[1]))
        )

    async def prompt(self):
        """
        Prompts the LLM for a response, and sends the response as a discord
        message.
        """
        await self.signal.channel.send(
            self.transponder.prompt(self.message)
        )
