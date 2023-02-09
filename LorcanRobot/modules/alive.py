import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from LorcanRobot.events import register
from LorcanRobot import telethn as tbot, BOT_USERNAME


PHOTO = "https://te.legra.ph/file/a53d88289d3b96f07e6f0.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}), ɪ ᴀᴍ ʟᴏʀᴄᴀɴ ʀᴏʙᴏᴛ.** \n\n"
  TEXT += " **🥂 ɪ ᴀᴍ ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ  🥂** \n\n"
  TEXT += f"⨀ **ᴍʏ ᴍᴀsᴛᴇʀ  : [ᴜʀᴀɴɪᴜᴍ](https://t.me/THE_URANIUM)** \n\n"
  TEXT += f"⨀ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"⨀ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ  :** `{tlhver}` \n\n"
  TEXT += f"⨀ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ  :** `{pyrover}` \n\n"
  TEXT += "**🍷ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ᴅᴇᴀʀ🍷**"
  BUTTON = [[Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/LORCAN_X_UPDATES"), Button.url("• sᴜᴘᴘᴏʀᴛ  •", "https://t.me/Lorcan_x_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
