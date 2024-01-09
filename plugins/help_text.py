# Modified by @LISA_FAN_LK | @UploadLinkToFileBot

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import re

from config import Config
# the Strings used for this "thing"
from plugins.startmsg import Translation

from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as Hxbots
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Hxbots.on_message(filters.private & filters.command(["cancel"]))
async def cancel_process(bot, update):
   global cancel
    cancel = True
    await editable.edit("cancled")
    return
    else:
    save_ytdl_json_path = Config.DOWNLOAD_LOCATION + "/" + str(update.chat.id) + ".json"
    if os.path.exists(save_ytdl_json_path):
        os.remove(save_ytdl_json_path)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.PROCESS_CANCELLED,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
        )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.NO_PROCESS_FOUND,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
        )

@Hxbots.on_message(filters.private & filters.reply & filters.text)
async def edit_caption(bot, update):
    try:
        await bot.send_cached_media(
            chat_id=update.chat.id,
            file_id=update.reply_to_message.video.file_id,
            reply_to_message_id=update.message_id,
            caption=update.text
        )
    except:
        try:
            await bot.send_cached_media(
                chat_id=update.chat.id,
                file_id=update.reply_to_message.document.file_id,
                reply_to_message_id=update.message_id,
                caption=update.text
            )
        except:
            pass

@Hxbots.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
        [
          [
          InlineKeyboardButton('📍 JOIN CHANNEL 📍', url='https://t.me/HxBots'),
          ]
        ]
       ),
       reply_to_message_id=update.message_id
     )

@Hxbots.on_message(filters.private & filters.command(["caption"]))
async def add_caption_help(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ADD_CAPTION_HELP,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Hxbots.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
        [
          [
          InlineKeyboardButton('📍 JOIN CHANNEL 📍', url='https://t.me/HxBots'),
          ]
        ]
       ),
       reply_to_message_id=update.message_id
     )

@Hxbots.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
        [
          [
          InlineKeyboardButton('📍 CHANNEL', url='https://t.me/HxBots'),
      ],
      [
          InlineKeyboardButton('👨‍💻 DEVELOPER', url='https://t.me/kirodewal'),
          InlineKeyboardButton('🌝 SOURCE', url='https://github.com/oVo-HxBots'),
          ]
        ]
      ),
      reply_to_message_id=update.message_id
    )

@Hxbots.on_message(filters.private & filters.command(["info"]))
async def add_info_help(bot, update):
    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None"
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.INFO_TEXT.format(update.from_user.first_name, last_name, update.from_user.username, update.from_user.id, update.from_user.mention, update.from_user.dc_id, update.from_user.language_code, update.from_user.status),
        #parse_mode="html",
        reply_to_message_id=update.message_id
    )
  
@Hxbots.on_message(filters.command("restart"))
async def restart_handler(bot, update):
    await m.reply_text("Bot Successfully Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
