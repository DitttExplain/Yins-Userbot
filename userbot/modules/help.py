# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("`Command` **Tidak Valid**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t ✗  "
        await event.edit("**✨𝚈𝙸𝙽𝚂-𝚄𝚂𝙴𝚁𝙱𝙾𝚃✨**\n\n"
                         f"**◉ 𝙱𝙾𝚃 𝙾𝙵 {DEFAULTUSER}**\n**◉ 𝙼𝙾𝙳𝚄𝙻𝙴𝚂 : {len(modules)}**\n\n"
                         "**• 𝙼𝙰𝙸𝙽 𝙼𝙴𝙽𝚄 :**\n"
                         f"◉ {string}◉\n\n✐ **ɴᴏᴛᴇꜱ :**  `.help animasi`\n☞  sᴜᴘᴘᴏʀᴛ : @AyiinXdSupport")
        await asyncio.sleep(1000)
        await event.delete()
