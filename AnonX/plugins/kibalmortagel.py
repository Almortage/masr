import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from strings import get_command
from strings.filters import command
from config import BANNED_USERS
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest

@app.on_message(command(["صوره", "🕷", "صورهه", "صور"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار صوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(command(["انميي", "انمي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,153)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار انمي لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(command(["متحركه. 🎬", "متحركه"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,925)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption="🐉 ¦ تـم اختيـار ملصق لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(command(["اقتباسات", "اقتباس"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,102)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار اقتباس لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(command(["هيدرا", "هيدرات"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,152)
    url = f"https://t.me/flflfldld/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار هيدرات لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(command(["صور", "افتار بنات"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,215)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار صوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(command(["صور شباب", "افتار شباب"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,174)
    url = f"https://t.me/vgbmm/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار صوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(command(["استوري", "استوريهات. 🥹"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,147)
    url = f"https://t.me/yoipopl/{rl}"
    await client.send_audio(message.chat.id,url,caption="🐉 ¦ تـم اختيـار استوري لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
    @app.on_message(command(["سوره", "قران"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(7,276)
    url = f"https://t.me/ALMORTAGELRSK/{rl}"
    await client.send_voice(message.chat.id,url,caption="🐉 ¦ تـم اختيـار ايـه قرآنيه لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(command(["الشيخ", "النقشبندي", "نقشبندي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,113)
    url = f"https://t.me/ggcnjj/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ نقشبندي لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
    @app.on_message(command(["عبدالباسط", "عبدالباسط عبدالصمد"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(7,264)
    url = f"https://t.me/telawatnader/{rl}"
    await client.send_audio(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ عبدالباسط لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )