async def log_command(message):
    print(message.author.mention + " "  + message.author.name + "#" + message.author.discriminator + ": " + message.content)
