import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from translation import Translation

from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Config.UPDATE_CHANNEL = Config.UPDATES_CHANNEL

@Client.on_message(filters.command(["help"]))
async def help_user(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ JOIN OUR CHANNEL ⭕️", url=f"https://t.me/{Config.UPDATES_CHANNEL}")]]),
   )

@Client.on_message(filters.command(["upgrade"]))
async def upgrade(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ CHANNEL ⭕️", url=f"https://t.me/{Config.UPDATES_CHANNEL}")], [InlineKeyboardButton(text="😇 SUPPORT", url="https://t.me/HxSupport"),
                                                    InlineKeyboardButton(text="Donate ♐️", url="https://upayme.vercel.app/kkirodewal@ybl")]]),
    )


@Client.on_message(filters.command(["donate"]))
async def donate(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.DONATE_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="☕ Buy Me A Coffee ☕", url="https://upayme.vercel.app/kkirodewal@ybl")]]),
   )
    
@Client.on_message(filters.command(["about"]))
def about(bot, update):
    
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True   
    ) 
        
