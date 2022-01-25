# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from userbot import CMD_HELP
from userbot.events import register

GCAST_BLACKLIST = [
    -1001675396283,  # AyiinXdSupport
    -1001473548283,  # SharingUserbot
    -1001433238829,  # TedeSupport
    -1001476936696,  # AnosSupport
    -1001327032795,  # UltroidSupport
    -1001294181499,  # UserBotIndo
    -1001419516987,  # VeezSupportGroup
    -1001209432070,  # GeezSupportGroup
    -1001296934585,  # X-PROJECT BOT
    -1001481357570,  # UsergeOnTopic
    -1001459701099,  # CatUserbotSupport
    -1001109837870,  # TelegramBotIndonesia
    -1001752592753,  # Skyzusupport
    -1001788983303,  # KayzuSupport
    -1001380293847,  # NastySupport
]


@register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("**Berikan Sebuah Pesan atau Reply**")
        return
    kk = await event.edit("`𝙇𝙖𝙜𝙞 𝙉𝙜𝙞𝙧𝙞𝙢 𝙏𝙤𝙙, 𝙆𝙖𝙡𝙤 𝙇𝙞𝙢𝙞𝙩 𝙅𝙖𝙣𝙜𝙖𝙣 𝙎𝙖𝙡𝙖𝙝𝙞𝙣 𝙂𝙪𝙖 !!!`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                await event.client.send_message(chat, msg)
                done += 1
            except BaseException:
                er += 1
    await kk.edit(
        f"**𝘼𝙡𝙝𝙖𝙢𝙙𝙪𝙡𝙞𝙡𝙡𝙖𝙝 𝘽𝙚𝙧𝙝𝙖𝙨𝙞𝙡 𝙉𝙜𝙞𝙧𝙞𝙢 𝙋𝙚𝙨𝙖𝙣 𝙆𝙚** `{done}` **𝙂𝙧𝙪𝙥, 𝙎𝙤𝙧𝙧𝙮 𝙏𝙤𝙙 𝙂𝙖𝙜𝙖𝙡 𝙈𝙚𝙣𝙜𝙞𝙧𝙞𝙢 𝙋𝙚𝙨𝙖𝙣 𝙆𝙚** `{er}` **𝙂𝙧𝙪𝙥**"
    )


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("**Berikan Sebuah Pesan atau Reply**")
        return
    kk = await event.edit("`𝙇𝙖𝙜𝙞 𝙉𝙜𝙞𝙧𝙞𝙢 𝙏𝙤𝙙, 𝙆𝙖𝙡𝙤 𝙇𝙞𝙢𝙞𝙩 𝙅𝙖𝙣𝙜𝙖𝙣 𝙎𝙖𝙡𝙖𝙝𝙞𝙣 𝙂𝙪𝙖 !!!`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await event.client.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(
        f"**𝘼𝙡𝙝𝙖𝙢𝙙𝙪𝙡𝙞𝙡𝙡𝙖𝙝 𝘽𝙚𝙧𝙝𝙖𝙨𝙞𝙡 𝙉𝙜𝙞𝙧𝙞𝙢 𝙋𝙚𝙨𝙖𝙣 𝙆𝙚** `{done}` **𝘾𝙝𝙖𝙩𝙨, 𝙎𝙤𝙧𝙧𝙮 𝙏𝙤𝙙 𝙂𝙖𝙜𝙖𝙡 𝙈𝙚𝙣𝙜𝙞𝙧𝙞𝙢 𝙋𝙚𝙨𝙖𝙣 𝙆𝙚** `{er}` **𝘾𝙝𝙖𝙩𝙨**"
    )


CMD_HELP.update(
    {
        "gcast": "**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `.gcast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": "**Plugin : **`gucast`\
        \n\n  •  **Syntax :** `.gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
