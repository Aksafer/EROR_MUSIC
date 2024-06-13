
from pyrogram.types import CallbackQuery
import asyncio
from asyncio import gather
import os
import time
import requests
from pyrogram import enums
from pyrogram import types
import aiohttp
from pyrogram.types import CallbackQuery
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from ErorMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ErorMusic import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait



##############################################################
##############################################################
          
     
@app.on_message(filters.command(["سورس","السورس"], ""), group=221213)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/llle_rus/2",
        caption=f"""• [⌯𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄⌯](https://t.me/Y_D_ll) •\n
 [⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐄𝐑𝐎𝐑⌯](https://t.me/SOURCE_EROR)\n
 [⌯𝐒𝐔𝐏𝐏𝐔𝐑𝐓.𝐒𝐎𝐔𝐑𝐂𝐄⌯](https://t.me/SOPER_EROR)\n""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ 𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄 › ", url=f"https://t.me/Y_D_ll"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐒𝐎𝐔𝐑𝐂𝐄 ›", url=f"https://t.me/SOURCE_EROR"), 
                    InlineKeyboardButton(
                        "‹ 𝐒𝐔𝐏𝐏𝐔𝐑𝐓 ›", url=f"https://t.me/SOPER_EROR"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️ ⋅ ›", url=f"http://t.me/d_r_n_bot?startgroup=new"),
            ]
        ]
         ),parse_mode=enums.ParseMode.MARKDOWN)



@app.on_message(filters.command(["ايرور","مطور السورس"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/920066d3e118edcba1982.jpg",
        caption=f"""• ⌯ Developer Name : ˛ 𝙴𝚁𝙾𝚁 ⌯ •\n- Devloper Username : @Y_D_ll Devloper id : 6092147148 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/SOURCE_EROR"),
                ],[
                    InlineKeyboardButton(
                        "𓄼⦁ 𝗲𝗿𝗼𝗿 ⦁𓄹", url=f"https://t.me/Y_D_ll"), 
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/d_r_n_bot?startgroup=new"),
            ]
        ]
         ),
     )

               
@app.on_message(filters.command(["اسمي","اسمي اي","قول اسمي"], ""), group=123222)
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""- اسمك » ⦗ {message.from_user.mention} ⦘ 💘 ⋅""") 


##############################################################
##############################################################
##############################################################
  


