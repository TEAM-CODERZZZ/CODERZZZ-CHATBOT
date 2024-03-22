

import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message


from nexichat import nexichat
from nexichat.database.chats import add_served_chat
from nexichat.database.users import add_served_user
from nexichat.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


#----------------IMG-------------#



# Random Start Images
IMG = [
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
    "https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
]


#----------------IMG-------------#


#---------------STICKERS---------------#

# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

#---------------STICKERS---------------#


#---------------EMOJIOS---------------#

EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]


#---------------EMOJIOS---------------#

@nexichat.on_cmd(["start", "aistart"])
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ sтαятιиg.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ sтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**๏ 𝐇𝐞𝐲 ,𝐈'𝐚𝐦 {nexichat.name}**\n**➻ 𝐀𝐧 𝐀𝐈 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 + 𝐕𝐜 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲𝐞𝐫 𝐁𝐨𝐭 + 𝐆𝐫𝐨𝐮𝐩 𝐌𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭 𝐁𝐨𝐭 + 𝐂𝐡𝐚𝐭𝐠𝐩𝐭 𝐁𝐨𝐭.**\n**──────────────**\n**➻ 𝐔𝐬𝐚𝐠𝐞 /chatbot [ᴏɴ/ᴏғғ]**\n<b>||๏ 𝐇𝐢𝐭 𝐇𝐞𝐥𝐩 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐇𝐞𝐥𝐩||</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@nexichat.on_cmd("help")
async def help(client: nexichat, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@nexichat.on_cmd("repo")
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@nexichat.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
