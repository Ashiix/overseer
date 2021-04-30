import discord
import re
from sqlitedict import SqliteDict

async def level(self, message, user):
    with SqliteDict('./db/levels.sqlite', autocommit=True) as level_db:
        if level_db.get(user.id) == None:
            level_db[user.id] = 0
        level_db[user.id] += 1
        if level_db[user.id] % 10 == 0:
            await self.get_channel(837692972161957898).send("woah, " + user.mention + ", you're now level " + str(int(level_db[user.id] / 10)) + ". crazy shit.")

def get_level(user):
    with SqliteDict('./db/levels.sqlite', autocommit=True) as level_db:
        return int(level_db[user.id] / 10)

def get_level_xp(user):
    with SqliteDict('./db/levels.sqlite', autocommit=True) as level_db:
        return level_db[user.id]

def parse_level(level):
    return int(level / 10)

async def leaderboard(self, message, user):
    with SqliteDict('./db/levels.sqlite', autocommit=True) as level_db:
        sorted_levels = {}
        leaderboard = "```\nLeaderboard:\n\n"
        sorted_keys = sorted(level_db, key=level_db.get)
        for e in sorted_keys:
            sorted_levels[e] = level_db[e]
        for i in range(min(10, len(level_db))):
            user = await self.fetch_user(sorted_keys[len(level_db) - i - 1])
            leaderboard += user.name + "#" + user.discriminator + ": " + str(parse_level(sorted_levels.get(sorted_keys[len(level_db) - i - 1]))) + "\n"
        leaderboard += "...\n" + message.author.name + "#" + message.author.discriminator + ": " + str(get_level(message.author)) + "\n```"
        await message.channel.send((leaderboard))
