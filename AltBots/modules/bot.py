import sys
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl

from os import execl, getenv
from telethon import events
from datetime import datetime


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply(f"ﮩ٨ـﮩﮩ٨ـ ❤️ﮩ٨ـﮩﮩ٨ـ❥❤️ har har mahadevﮩ٨ـﮩﮩ٨ـﮩ٨")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f" ﮩ٨ـﮩﮩ٨ـ HAR HAR MAHADEV❤️ﮩ٨ـﮩﮩ٨ـ❥❤️ﮩ٨ـﮩﮩ٨ـﮩ٨ [꧁༒★ཌﮩ٨ـﮩﮩ٨ـ ❤️ﮩ٨ـﮩﮩ٨ـ❥ DEVIL❤️ﮩ٨ـﮩﮩ٨ـﮩ٨★༒꧂](https://t.me/@its_innocent_boy_2926)", mp)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
async def stop(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"`TU ROK MAT AAJ ISKI MAR LU...`")
        try:
            await X1.disconnect()
        except Exception:
            pass
        try:
            await X2.disconnect()
        except Exception:
            pass
        try:
            await X3.disconnect()
        except Exception:
            pass
        try:
            await X4.disconnect()
        except Exception:
            pass
        try:
            await X5.disconnect()
        except Exception:
            pass
        try:
            await X6.disconnect()
        except Exception:
            pass
        try:
            await X7.disconnect()
        except Exception:
            pass
        try:
            await X8.disconnect()
        except Exception:
            pass
        try:
            await X9.disconnect()
        except Exception:
            pass
        try:
            await X10.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"» __A҉D҉D҉I҉N҉G҉ ⏤͟͞𐏓🇩𝐄𝐕𝚰𝐋»🅢𝐏𝗔𝐌𝄀꯭𝄄꯭™⎯꯭ͯ⟶ sᴜᴅᴏ....__")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» ᴛᴀɢ ᴋᴀʀ ᴋᴇ ᴋᴀʀO SUR !!")
            return

        if str(target) in sudousers:
            await ok.edit(f"▄︻┻ 𝙏𝙃𝙄𝙎 𝙐𝙎𝙀𝙍 𝙄𝙎 𝘼𝙇𝙍𝙀𝘼𝘿𝙔 𝘼 ⏤͟͞𐏓🇩𝐄𝐕𝚰𝐋»🅢𝐏𝗔𝐌𝄀꯭𝄄꯭™⎯꯭ͯ⟶ 乃ⓞ𝐓 𝐒𝐔𝐃𝐎 𝐔𝐒𝐄𝐑 ︻┳═─- !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» `🤗🤗💀Ruko jara  ⏤͟͞𐏓🇩𝐄𝐕𝚰𝐋»🅢𝐏𝗔𝐌𝄀꯭𝄄꯭™⎯꯭ͯ⟶ 乃ⓞ𝐓 𝒔𝒖𝒓𝒖 𝒉𝒐 𝒓𝒂𝒉𝒂 𝒉𝒂𝒊...`")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("» 𝗔ʋκααт Μαι Янσ Beta ")



@X1.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
async def removesudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)
        ok = await event.reply(f" 𝗡𝗜𝗞𝗔𝗟 𝗗𝗜𝗬𝗔 𝗠𝗔𝗗𝗥𝗖𝗛𝗢𝗗 𝗞𝗢...")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:\nPlease set up your HEROKU_APP_NAME`")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("Reply to a message to remove the user.")
            return
        if str(target) not in sudousers:
            await ok.edit("User is not in the sudo list.")
        else:
            new_sudo_users = " ".join([user for user in sudousers.split() if user != str(target)])
            await ok.edit(f"Removed sudo user: `{target}`")
            heroku_var["SUDO_USERS"] = new_sudo_users
    else:
        await event.reply("𝗢𝗡𝗟𝗬 𝗢𝗪𝗡𝗘𝗥 𝗖𝗔𝗡 𝗥𝗘𝗠𝗢𝗩𝗘 𝗦𝗨𝗗𝗢 𝗨𝗦𝗘𝗥𝗦.")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
async def show_sudo_users(event):
    if event.sender_id == OWNER_ID:
        sudo_users_list = "⏤͟͞𐏓🇩𝐄𝐕𝚰𝐋»🅢𝐏𝗔𝐌𝄀꯭𝄄꯭™⎯꯭ͯ⟶ 乃ⓞ𝐓 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗦𝗨𝗗𝗢 𝗨𝗦𝗘𝗥𝗦 𝗟𝗜𝗦𝗧:\n"
        for user_id in SUDO_USERS:
            sudo_users_list += f"- {user_id}\n"
        await event.reply(sudo_users_list)
    else:
        await event.reply("🇴𝗡𝗟𝗬 ⏤͟͞𐏓🇩𝐄𝐕𝚰𝐋»🅢𝐏𝗔𝐌𝄀꯭𝄄꯭™⎯꯭ͯ⟶ 乃ⓞ𝐓 𝗢𝗪𝗡𝗘𝗥.")
