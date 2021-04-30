import discord
from sqlitedict import SqliteDict

async def level(message, user):
    with SqliteDict('./db/levels.sqlite', autocommit=True) as level_db:
        if level_db.get(user.mention) == None:
            level_db[user.mention] = 0
        level_db[user.mention] += 1
        if level_db[user.mention] % 10 == 0:
            await message.channel.send("woah, " + user.mention + ", you're now level " + str(int(level_db[user.mention] / 10)) + ". crazy shit.")

def get_level(user):
    with SqliteDict('./db/levels.sqlite', autocommit=True) as level_db:
        return(level_db.get(user.mention))
