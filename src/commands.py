import discord
from src.extensions.level import *
import config
import re

class Commands(discord.Bot):
    # @slash_command
    # async def help(ctx):
    #     help_embed = discord.Embed (
    #         title="help",
    #         color=0x000000,
    #         description = "prefix: `" + config.prefix + "`"
    #     )
    #     help_embed.set_thumbnail(url="https://ashiix.dev/files/img/eclipse.png")
    #     help_embed.set_footer(text="overseer")

    #     await ctx.respond(embed = help_embed)

# elif command == "about":
#     await message.channel.send(embed=
#             discord.Embed(
#             title="about",
#             color=0x000000,
#             description = "**overseer** is an open-source and self-hosted multipurpose bot."
#         )
#         .set_author(
#             name="Ashiix#6225",
#             url="https://ashiix.dev",
#             icon_url="https://ashiix.dev/files/img/moon.png"
#         )
#         .set_thumbnail(url="https://ashiix.dev/files/img/eclipse.png")
#         .set_footer(text="overseer")
#     )

    @slash_command()
    async def hello(ctx):
        await ctx.respond(f"Hello {ctx.author}!")

# elif command == "level":
#     await message.channel.send(message.author.mention + " is level " + str(get_level(message.author)) + ". they require " + str(24 - (get_level_xp(message.author) % config.level_curve)) + " more messages for the next level.")

# elif command == "leaderboard":
#     await leaderboard(self, message)

# elif command == "ice":
#     await message.channel.send("https://cdn.discordapp.com/attachments/750181456420274256/838277499480965150/image0.png")

# elif command == "levelnotif":
#     await toggle_notif(self, message.author)
#     await message.channel.send("toggled levelup notifications for user " + message.author.mention)
