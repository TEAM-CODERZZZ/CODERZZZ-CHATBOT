

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import OWNER_USERNAME
from nexichat import nexichat
from nexichat.database.chats import add_served_chat
from nexichat.database.users import add_served_user
from nexichat.modules.helpers import PNG_BTN


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



@nexichat.on_cmd("ping")
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"𝐇𝐞𝐲 𝐁𝐚𝐛𝐲!!\n{nexichat.name} 𝐈𝐬 𝐀𝐥𝐢𝐯𝐞 🥀 𝐀𝐧𝐝 𝐖𝐨𝐫𝐤𝐢𝐧𝐠 𝐅𝐢𝐧𝐞 𝐖𝐢𝐭𝐡 𝐀 𝐏𝐢𝐧𝐠 𝐎𝐟\n➥ `{ms}` ms\n\n<b>|| 𝐌𝐚𝐝𝐞 𝐖𝐢𝐭𝐡  ❣️ 𝐁𝐲 [𝗜'𝗺 𝗖𝗢𝗗𝗘𝗥𝗭](https://t.me/{OWNER_USERNAME}) ||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
