from src.extensions.level import *

async def execute_command(self, message):
    command = message.content[1:]

    if command == "hello":
        await message.channel.send("hello, world.")

    elif command == "level":
        await message.channel.send(message.author.mention + " is level " + get_level(message.author) + ".")

    elif command == "leaderboard":
        await leaderboard(self, message, message.author)

    else:
        await message.reply("that is not a valid command.")
