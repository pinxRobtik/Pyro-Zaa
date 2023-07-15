from platform import python_version as py

from pyroza import *
from pyroza.pyroza import *
from pyroza.pyroza.load import *
from pyroza.pyroza.utils import *
from pyroza.pyroza.utils.db import *
from pyroza.version import __version__ as nay
from pyroza.version import kynay_version as nan
from pyrogram import __version__ as pyro
from pyrogram import idle
from uvloop import install

from Zaa import *
from Zaa.config import *

MSG_ON = """
**Zaa-Pyro Actived ✅**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
◉ **Versi** : `{}`
◉ **Phython** : `{}`
◉ **Pyrogram** : `{}`
◉ **PyroZa** : `{}`
**Ketik** `{}alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    LOGGER("Startup").info("Memulai Zaa-Pyro Premium..")
    for bot in botlist:
        try:
            await bot.start()
            ex = bot.me
            user = ex.id
            await ajg(bot)
            await babi(bot)
            botlog = await get_botlog(user)
            LOGGER("✓").info(f"Started as {ex.first_name} | {ex.id} ")
            try:
                await bot.send_message(botlog, MSG_ON.format(nan, py(), pyro, nay, cmd))
            except BaseException as a:
                LOGGER("Info").warning(f"{a}")

            ids.append(ex.id)
            LOGGER("Info").info("Startup Completed")

        except Exception as e:
            LOGGER("X").info(f"{e}")
    await loadprem()
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    install()
    heroku()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        LOGGER("Logger").info("Stopping Bot! GoodBye")
