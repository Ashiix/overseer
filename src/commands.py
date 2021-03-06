import discord
from src.extensions.level import *
import config
import re

commands = {
"help":"show this message",
"about":"show info about overseer",
"hello":"say hello",
"level":"get your current level",
"leaderboard":"show the server level leaderboard",
"levelnotif":"toggle levelup notifications",
"hug":"give the specified value a hug"
}

async def execute_command(self, message):
    command = message.content.split()[0][1:]

    args = message.content.split()[1:]

    if command == "help":
        help_embed = discord.Embed (
            title="help",
            color=0x000000,
            description = "prefix: `" + config.prefix + "`"
        )
        help_embed.set_thumbnail(url="https://ashiix.dev/files/img/eclipse.png")
        help_embed.set_footer(text="overseer")

        for command, help in commands.items():
            help_embed.add_field(name=command, value=help+".", inline=True)

        await message.channel.send(embed = help_embed)

    elif command == "about":
        await message.channel.send(embed=
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

    elif command == "hello":
        await message.channel.send("hello, " + message.author.mention + ".")

    elif command == "level":
        await message.channel.send(message.author.mention + " is level " + str(get_level(message.author)) + ". they require " + str(24 - (get_level_xp(message.author) % config.level_curve)) + " more messages for the next level.")

    elif command == "leaderboard":
        await leaderboard(self, message)

    elif command == "ice":
        await message.channel.send("https://cdn.discordapp.com/attachments/750181456420274256/838277499480965150/image0.png")

    elif command == "levelnotif":
        await toggle_notif(self, message.author)
        await message.channel.send("toggled levelup notifications for user " + message.author.mention)

    elif command == "hug":
        try:
            await message.channel.send(message.author.mention + " gives " + args[0] + " a hug.")
        except:
            await message.reply("please specific the target of the hug.")

    else:
        await message.reply("that is not a valid command.")
