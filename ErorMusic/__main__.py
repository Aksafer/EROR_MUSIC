import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ErorMusic import LOGGER, app, userbot
from ErorMusic.core.call import EROR
from ErorMusic.misc import sudo
from ErorMusic.plugins import ALL_MODULES
from ErorMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("كود جلسة الحساب المساعد غير مدعوم ...")
        exit()
    await sudo()
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
        importlib.import_module("ErorMusic.plugins" + all_module)
    LOGGER("ميــوزك ايــرور").info("تم تحميل الاضافات ...✓")
    await userbot.start()
    await EROR.start()
    try:
        await EROR.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ميــوزك ايــرور").info(
            "خطأ .. قم بفتح المكالمة في مجموعة السجل الخاصه بك\n\nجارِ ايقاف بوت الميوزك . . ."
        )
        exit()
    except:
        pass
    await EROR.decorators()
    LOGGER("ميــوزك ايــرور").info(
        "\x44\x6f\x6e\x65\x20\x69\x6e\x73\x74\x61\x6c\x6c\x61\x74\x69\x6f\x6e\x20\x5a\x54\x68\x6f\x6e\x20\x4d\x75\x73\x69\x63\x20\xe2\x9c\x93\x0a\x47\x6f\x20\x74\x6f\x20\x79\x6f\x75\x72\x20\x62\x6f\x74\x20\x61\x6e\x64\x20\x73\x65\x6e\x64\x20\x2f\x73\x74\x61\x72\x74\x0a\x43\x68\x61\x6e\x6e\x65\x6c\x20\x3a\x20\x28\x40\x5a\x54\x68\x6f\x6e\x29"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ميــوزك ايــرور").info("جارِ ايقاف بوت الميوزك . . .")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
