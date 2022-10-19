    

# Kanged By © @Pikachu_dolly
# Owner vibes
# All rights reserved. © Alisha © Sweety © Sweety







import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from SweetyMusic import LOGGER, app, userbot
from SweetyMusic.core.call import Sweety
from SweetyMusic.plugins import ALL_MODULES
from SweetyMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("SweetyMusic").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SweetyMusic.plugins" + all_module)
    LOGGER("SweetyMusic.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Sweety.start()
    try:
        await Sweety.stream_call(
            "https://telegra.ph/file/b14297dd43122e179be9a.jpg"
        )
    except NoActiveGroupCall:
        LOGGER("SweetyMusic").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Sweety.decorators()
    LOGGER("SweetyMusic").info("mirachlemusic Bot Started Successfully ❣️")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("SweetyMusic").info("Stopping Music Bot, Ada poda (kai vachitu kamunu irukamatiya)")
