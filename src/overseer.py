import discord
from src.commands import *
from src.extensions.log import *
from src.extensions.level import *
import config

class Overseer(discord.Client):
    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Game("in the overseer's office."))
        print("overseer ready.")
        print("---------------\n")

    async def on_message(self, message):
        if message.content == "" or message.author == self.user or message.author.id in config.ignored_users:
            return

        if message.content[0] == config.prefix:
            await log_command(message)
            await execute_command(self, message)

        if message.guild.id == config.home_server:
            await level(self, message, message.author)