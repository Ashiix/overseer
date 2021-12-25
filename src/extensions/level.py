from sqlitedict import SqliteDict
import config

async def level(self, message, user):
    with SqliteDict('./db/level.sqlite', autocommit=True) as level_db, SqliteDict('./db/notif.sqlite', autocommit=True) as notif_db:
        if level_db.get(user.id) == None:
            level_db[user.id] = 0
        level_db[user.id] += 1
        if level_db[user.id] % config.level_curve == 0:
            if notif_db.get(str(user.id)+"_level") == None or notif_db[str(user.id)+"_level"] == 1:
                await self.get_channel(config.level_channel).send("woah, " + user.mention + ", you're now level " + str(get_level(user)) + ". crazy shit.")
            else:
                await self.get_channel(config.level_channel).send("woah, " + user.name + ", you're now level " + str(get_level(user)) + ". crazy shit.")

def parse_level(level):
    return int(level / config.level_curve)

def get_level(user):
    with SqliteDict('./db/level.sqlite', autocommit=True) as level_db:
        return parse_level(level_db[user.id])

def get_level_xp(user):
    with SqliteDict('./db/level.sqlite', autocommit=True) as level_db:
        return level_db[user.id]

async def leaderboard(self, message):
    with SqliteDict('./db/level.sqlite', autocommit=True) as level_db:
        await message.channel.send("sorting levels...")
        sorted_levels = {}
        leaderboard = "```\nLeaderboard:\n\n"
        sorted_keys = sorted(level_db, key=level_db.get)
        for e in sorted_keys:
            sorted_levels[e] = level_db[e]
        for i in range(min(10, len(level_db))):
            user = await self.fetch_user(sorted_keys[len(level_db) - i - 1])
            leaderboard += str(i + 1) + ". " + user.name + "#" + user.discriminator + ": " + str(parse_level(sorted_levels.get(sorted_keys[len(level_db) - i - 1]))) + "\n"
        leaderboard += "...\n" + message.author.name + "#" + message.author.discriminator + ": " + str(get_level(message.author)) + "\n```"
        await message.channel.send((leaderboard))

async def toggle_notif(self, user):
    with SqliteDict('./db/notif.sqlite', autocommit=True) as notif_db:
        if notif_db.get(str(user.id)+"_level") == None or notif_db[str(user.id)+"_level"] == 0:
            notif_db[str(user.id)+"_level"] = 1
        else:
            notif_db[str(user.id)+"_level"] = 0
