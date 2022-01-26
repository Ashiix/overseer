import discord
from src.extensions.log import *
from src.extensions.level import level
import config


class Overseer(discord.Bot):
    async def on_ready(self):
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Game("in the overseer's office."),
        )
        print("overseer ready.")
        print("---------------\n")

    # async def on_message(self, message):
    #     if message.guild.id == config.home_server:
    #         await level(self, message, message.author)
