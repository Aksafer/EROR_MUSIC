import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from ErorMusic import app

@app.on_message(filters.command(["الرابط","/link","لنك","رابط"], "") & filters.group & ~filters.private)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("- ارفعني مسول الاول يزميلي 😂💘 ⋅")
    await message.reply_text(f"- تم جلب الرابط بنجاح 😂💘 ⋅\n {invitelink}")
    
