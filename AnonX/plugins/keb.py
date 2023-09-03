import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from strings import get_filters.regex
from strings.filters import filters.regex
from config import BANNED_USERS
from config.config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest



REPLY_MESSAGE = "**صلي علي اشرف خلق الله 🥹✨**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس"),
    ],
    [
        ("افتار شباب"),
        ("افتار بنات")
    ],
    [
        ("استوريهات. 🥹")
    ],
    [
        ("النقشبندي"),
        ("قران")
    ],
    [
        ("فيلمك. 🎥")
    ],
    [
        ("اقتباسات"),
        ("هيدرات")
    ],
    [
        ("غنيلي")
    ],
    [
        ("صوره"),
        ("انميي")
    ],
    [
        ("متحركه. 🎬")
    ],
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("الالعاب"),
        ("كتبات")
    ],
    [
        ("اذكار")
    ],
    [
        ("حساب العمر"),
        ("ابراج")
        
    ],
    [
        ("لو خيروك"),
        ("انصحني")
        
    ],
    [
        ("حساب العمر"),
        ("ابراج")
        
    ],
    [
        ("اخفاء الازرار . 🕷")
    ]
]

@app.on_message(filters.regex(["/Almortagel"]))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.regex("^اخفاء الازرار . 🕷$") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_text(text="تم الازرار بنجاح .🕷",
        reply_markup=ReplyKeyboardRemove()
    )
    
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
    rl = random.randint(2,90)
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
    rl = random.randint(2,90)
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
    rl = random.randint(2,90)
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
    rl = random.randint(2,90)
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
    rl = random.randint(2,90)
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
    rl = random.randint(2,90)
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
    
@app.on_message(command(["سوره", "قران"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/opuml/{rl}"
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
    rl = random.randint(1,90)
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
    rl = random.randint(1,50)
    url = f"https://t.me/telawatnader/{rl}"
    await client.send_audio(message.chat.id,url,caption="🐉 ¦ تـم اختيـار الشيخ عبدالباسط لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )