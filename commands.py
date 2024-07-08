import random
import transponder

class Commands:


    def __init__(self, msg):
        global command
        global message

        message = msg
        command = message.content[1:].split(" ")

        print(command)

    def getCommand(self):
        return command

    async def coinflip(self):
        if random.random() >= 0.5:
            await message.channel.send("Heads!")
        else:
            await message.channel.send("Tails!")


    async def roll(self):
        await message.channel.send(random.randint(0, int(command[1])))


    async def prompt(self):
        await message.channel.send(
            transponder.Transponder().prompt(message.content[1:].split(" "))
        )
