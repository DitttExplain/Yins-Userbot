""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/Contoldisini)"
        "\n[Repo](https://github.com/AyiinXd/Yins-Userbot)"
        "\n[Instagram](instagram.com/ayiin.xd)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/AyiinXd/Yins-Userbot/Yins-Userbot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "`.lhelp`\
\nUsage: Bantuan Untuk Yins-Userbot.\
\n`.vars`\
\nUsage: Melihat Daftar Vars."
})
