async def log_command(message):
    print(
        str(message.author.id)
        + " "
        + message.author.name
        + "#"
        + message.author.discriminator
        + ": "
        + message.content
    )
