import random
from transponder import Transponder


class Commands:

    def __init__(self, signal):
        self.command = signal
        self.split_command = self.command.content[1:].split(" ")
        self.message = f"Q: {self.command.content[7:]} A: "
        self.transponder = Transponder()

    async def coinflip(self):
        if random.random() >= 0.5:
            await self.command.channel.send("Heads!")
        else:
            await self.command.channel.send("Tails!")

    async def roll(self):
        await self.command.channel.send(
            random.randint(0, int(self.message[1]))
        )

    async def prompt(self):
        self.transponder.prompt(self.message)
        await self.command.channel.send(
            self.transponder.response
        )
