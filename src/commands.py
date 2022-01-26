import discord
from discord.commands import slash_command
from discord.ext import commands
from src.extensions.level import *
import config
import re

class Commands(commands.Cog):
    def __init__(self, overseer):
        self.overseer = overseer

    @slash_command(guild_ids=[config.home_server], name="about", description="return information about overseer.")
    async def about(self, ctx):
        await ctx.respond(embed=
                discord.Embed(
                title="about",
                color=0x000000,
                description = "**overseer** is an open-source and self-hosted multipurpose bot."
            )
            .set_author(
                name="Ashiix#6225",
                url="https://ashiix.dev",
                icon_url="https://ashiix.dev/files/img/moon.png"
            )
            .set_thumbnail(url="https://ashiix.dev/files/img/eclipse.png")
            .set_footer(text="overseer")
        )

    @slash_command(guild_ids=[config.home_server], name="hello", description="say hello.")
    async def hello(self, ctx):
        await ctx.respond(f"hi, {ctx.author.nick}.")

    # @slash_command(guilds_ids=[config.home_server], name="level", description="get users current level.")
    # async def level(self, ctx):
    #     await ctx.respond(ctx.author.mention + " is level " + str(get_level(ctx.author.id)) + ". they require " + str(24 - (get_level_xp(ctx.author.id) % config.level_curve)) + " more messages for the next level.")

    # @slash_command(guilds_ids=[config.home_server], name="leaderboard", description="display level leaderboard.")
    # async def leaderboard(self, ctx):
    #     await toggle_notif(self, ctx)

    # @slash_command(guilds_ids=[config.home_server], name="levelnotif", description="toggle levelup notifications.")
    # async def levelnotif(self, ctx):
    #     await toggle_notif(self, ctx.author)
    #     await ctx.respond("toggled levelup notifications for user " + message.author.mention)
