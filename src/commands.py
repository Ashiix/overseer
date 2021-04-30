from src.extensions.level import *

async def execute_command(message):
    command = message.content[1:]

    if command == "hello":
        await message.channel.send("hello, world.")

    elif command == "level":
        await message.channel.send(message.author.mention + " is level " + str(int(get_level(message.author) / 10)) + ".")
