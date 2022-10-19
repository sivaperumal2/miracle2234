from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from SweetyMusic import app
    

# Kanged By © @ITZ_STAR_BOY
# Owner Sambodhiraj
# All rights reserved. © Alisha © Sweety © Sweety



from SweetyMusic.core.call import Sweety
from SweetyMusic.utils.database import set_loop
from SweetyMusic.utils.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Sweety.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention)
    )
