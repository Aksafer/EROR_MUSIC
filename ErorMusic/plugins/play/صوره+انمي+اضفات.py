import asyncio
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from ErorMusic import app
from random import  choice, randint

@app.on_message(filters.command(["صوره", "صورة", "صور"], ""))
async def almortagel(client: Client, message: Message):
    rl = random.randint(2,75)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="❤️ ¦ تـم اختيـار صـوره لـك")


@app.on_message(filters.command(["انميي", "انمي"], ""))
async def almortagel(client: Client, message: Message):
    rl = random.randint(3,153)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="🖤 ¦ تـم اختيـار انـمـي لـك")


@app.on_message(filters.command(["متحركه", "متحركة"], ""))
async def almortagel(client: Client, message: Message):
    rl = random.randint(2,926)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption="💙 ¦ تـم اختيـار مـلـصـق لـك")

@app.on_message(filters.command(["صور بنات"], ""))
async def almortagel(client: Client, message: Message):
    rl = random.randint(2,216)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="🖤 ¦ تـم اختيـار صـورة بـنـت لـك")

@app.on_message(filters.command(["صور شباب"], ""))
async def almortagel(client: Client, message: Message):
    rl = random.randint(2,148)
    url = f"https://t.me/vgbmm/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار صـورة شـاب لـك")

@app.on_message(filters.command(["سورة"], ""))
async def almortagel(client: Client, message: Message):
    rl = random.randint(2,82)
    url = f"https://t.me/opuml/{rl}"
    await client.send_voice(message.chat.id,url,caption="❤ ¦ تـم اختيـار ايـه قرآنيه لـك")

@app.on_message(filters.command(["استوري"], ""))
async def almortagel(client: Client, message: Message):
    rl = random.randint(2,148)
    url = f"https://t.me/yoipopl/{rl}"
    await client.send_audio(message.chat.id,url,caption="💚 ¦ تـم اختيـار اســتوري لـك")

