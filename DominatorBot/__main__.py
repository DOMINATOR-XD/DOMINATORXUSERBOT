import glob
import os
import sys

from pathlib import Path
from telethon import Button, TelegramClient
from telethon.utils import get_peer_id

from DominatorBot import LOGS, bot, tbot
from DominatorBot.clients.session import Dominator, H2, H3, H4, H5
from DominatorBot.config import Config
from DominatorBot.utils import join_it, load_module, logger_check, start_msg, update_sudo, plug_channel
from DominatorBot.version import __dominator__ as dominatorver

hl = Config.HANDLER

DOMINATOR_PIC = "https://telegra.ph/file/93f5cc37e28743aeef809.mp4"
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)


# Client Starter
async def dominators(session=None, client=None, session_name="Main"):
    if session:
        LOGS.info(f"••• Starting Client [{session_name}] •••")
        try:
            await client.start()
            return 1
        except:
            LOGS.error(f"Error in {session_name}!! Check & try again!")
            return 0
    else:
        return 0


# Load plugins based on config UNLOAD
async def plug_load(path):
    files = glob.glob(path)
    for name in files:
        with open(name) as dominator:
            path1 = Path(dominator.name)
            shortname = path1.stem
            if shortname.replace(".py", "") in Config.UNLOAD:
                os.remove(Path(f"DominatorBot/plugins/{shortname}.py"))
            else:
                load_module(shortname.replace(".py", ""))      

if LOAD_ASSISTANT == True:
    path = "DominatorBot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                start_assistant(shortname.replace(".py", ""))
            except Exception as er:
                print(er)
else:
    print("Assitant is Not Loading As U Have Disabled")


# Final checks after startup
async def dominator_is_on(total):
    await update_sudo()
    await logger_check(bot)
    await start_msg(tbot, DOMINATOR_PIC, dominatorver, total)
    await join_it(bot)
    await join_it(H2)
    await join_it(H3)
    await join_it(H4)
    await join_it(H5)


# DominatorBot starter...
async def start_DominatorBot():
    try:
        tbot_id = await tbot.get_me()
        Config.BOT_USERNAME = f"@{tbot_id.username}"
        bot.tgbot = tbot
        LOGS.info("DOMINATOR BOT READY TO RUN")
        C1 = await dominators(Config.DOMINATORBOT_SESSION, bot, "DIMINATORBOT_SESSION")
        C2 = await dominators(Config.SESSION_2, H2, "SESSION_2")
        C3 = await dominators(Config.SESSION_3, H3, "SESSION_3")
        C4 = await dominators(Config.SESSION_4, H4, "SESSION_4")
        C5 = await dominators(Config.SESSION_5, H5, "SESSION_5")
        await tbot.start()
        total = C1 + C2 + C3 + C4 + C5
        LOGS.info("╔════❰𝕯𝖔𝖒𝖎𝖓𝖆𝖙𝖔𝖗 Աʂҽɾβօէ❱═❍⊱❁")
        LOGS.info("║┣⪼ 𝕊𝕥𝕒𝕣𝕥𝕚𝕟𝕘. 𝕯𝖔𝖒𝖎𝖓𝖆𝖙𝖔𝖗 𝕌𝕤𝕖𝕣𝔹𝕠𝕠𝕥")
        LOGS.info("║┣⪼ 𝕊𝕥𝕒𝕣𝕥𝕚𝕟𝕘. 𝕃𝕠𝕕𝕚𝕟𝕘...")
        LOGS.info("╚══════════════════❍⊱")
        await plug_load("DominatorBot/plugins/*.py")
        await plug_channel(bot, Config.PLUGIN_CHANNEL)
        LOGS.info(f"""『🔱𝕯𝖔𝖒𝖎𝖓𝖆𝖙𝖔𝖗 Աʂҽɾβօէ🔱』➙𖤍࿐ IS ON!!! 𝕯𝖔𝖒𝖎𝖓𝖆𝖙𝖔𝖗 Աʂҽɾβօէ VERSION :- 𝕍:𝕒 𝟙.𝟘
                      TYPE :- " .gpromote @N1xDOMINATOR " OR .help OR .ping CHECK IF I'M ON!
                      ╔════❰ 𝕯𝖔𝖒𝖎𝖓𝖆𝖙𝖔𝖗 Աʂҽɾβօէ ❱═❍⊱❁
                      ║┣⪼ OWNER - @N1xDOMINATOR
                      ║┣⪼ Ultra Real Stick Bot 
                      ║┣⪼ CREATOR - @N1xDOMINATOR
                      ║┣⪼ TELETHON - 1.2.0
                      ║┣⪼ ✨ 『🔱𝕯𝖔𝖒𝖎𝖓𝖆𝖙𝖔𝖗🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
                      ║╰━━━━━━━━━━━━━━━➣
                      ╚══════════════════❍⊱""")
        LOGS.info(f"» Total Clients = {str(total)} «")
        await dominator_is_on(total)
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()


bot.loop.run_until_complete(start_DominatorBot())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass


# DominatorBot
