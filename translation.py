import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


class Translation(object):

    START_TEXT = f"""Yo, I am a Powefull URL Upload Bot 🤓!

I can support Hotstar, Google Drive, m3u8 link (Especially for Allen and Physics Wallah Lectures download) and much more Links😌!

Send Me Any Direct Download URL Link, I Can Upload To Telegram As File/Video! 😁

<b> Update Channel : @{Config.UPDATES_CHANNEL}</b>
"""

    HELP_USER = f"""It's not that complicated😅

1. Press /deletthumbnail To Delete Your Current Custom Thumbnail

2. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots


<b> Update Channel : @{Config.UPDATES_CHANNEL}</b>
"""


    ABOUT_TEXT = """🔸<b>My Name🔸       : URL UPLOADBOT</b>

🔸<b>Creator🔸           : <a href='https://GitHub.com/oVo-HxBots'>@oVo-HxBots</a></b>

🔸<b>Language🔸      : Python3</b>

🔸<b>Library🔸            : Pyrogram</b>

🔸<b>Source Code🔸 : <a href='https://t.me/HxBots'>URL UPLOADBOT</a></b>"""



    FORMAT_SELECTION = """<b>Choose appropriate option</b> <a href='{}'>⬇️</a>

🎞  - Stream format
📁  - File format

<i>NOTE : Taking high resolutions may result in files above 2GB and hence cannot Upload to TG. So better select a medium resolution.</i> 😇"""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    UPGRADE_TEXT = """<b>👉 If You Liked Our Bot And Service Please Support Us By Forking Our Repo  <a href='https://GitHub.com/oVo-HxBots/URL-UploadBot'>UrlUpload Bot</a></b>"""
    
    DOWNLOAD_START = """Trying to download your file..."""
    
    UPLOAD_START = "Uploading now...Have a cup of tea till I upload"

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."

    SAVED_CUSTOM_THUMB_NAIL = "Custom thumbnail saved. This will be permanent.\n\nUse /deletethumbnail to clear it."

    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom thumbnail cleared succesfully."

    CUSTOM_CAPTION_UL_FILE = "<b>@HxBots | <a href='https://GitHub.com/oVo-HxBots'>@oVo-HxBots</a> | <a href='https://GitHub.com/oVoIndia'>@oVoIndia</a></b>"

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    NO_VOID_FORMAT_FOUND = "ERROR...<b>Kindly contact at @HxSupport to sort out the problem.</b>"
    
    SHOW_THUMB = "Use /deletethumbnail to clear this thumbnail."
    
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>Thanks for using our Bot.</b>"
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = """<b>Your file has been uploaded. Thanks for using our Bot.\nDownloaded in {} seconds.\nUploaded in {} seconds.</b>"""

    NO_THUMB = "No saved thumbnails Found!!\n\nSend an image to save it as your thumbnail permanently."    

    DONATE_TEXT = "<b>If you like our bot and want to donate you can donate us by below button.</b>"
