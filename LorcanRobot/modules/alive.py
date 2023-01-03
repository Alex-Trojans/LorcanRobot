import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from LorcanRobot.events import register
from LorcanRobot import telethn as tbot, BOT_USERNAME


PHOTO = "https://telegra.ph/file/1c1d3914a86a96a363b44.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}), I'ᴍ Lᴏʀᴄᴀɴ Rᴏʙᴏᴛ.** \n\n"
  TEXT += " **✪ I'ᴍ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʀʟʏ ✪** \n\n"
  TEXT += f"❂ **Mʏ Mᴀsᴛᴇʀ  : [ᴇᴅᴡᴀʀᴅ ᴇʟʀɪᴄ ](https://t.me/lI_EDWARD_Il)** \n\n"
  TEXT += f"❂ **Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"❂ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"❂ **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "** Tʜᴀɴᴋs Fᴏʀ Aᴅᴅɪɴɢ Mᴇ Dᴇᴀʀ🍷**"
  BUTTON = [[Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/LORCAN_X_UPDATES"), Button.url("• sᴜᴘᴘᴏʀᴛ  •", "https://t.me/Lorcan_x_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
