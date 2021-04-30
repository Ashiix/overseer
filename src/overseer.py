import discord
from src.commands import *
from src.extensions.log import *
from src.extensions.level import *

class Overseer(discord.Client):
    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Game("with drifters."))
        print("overseer ready.")
        print("---------------\n")

    async def on_message(self, message):
        if message.content == "" or message.author == self.user:
            return

        if message.content[0] == '~':
            await log_command(message)
            await execute_command(message)

        await level(message, message.author)
