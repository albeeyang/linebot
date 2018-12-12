

from line_bot_api import *

def about_us_event(event):
        about_us_text = '關於我'
        about_us_img = 'https://i.imgur.com/wpviICN.jpg'

        line_bot_api.reply_message(
            event.reply_token,
                [TextSendMessage(text=about_us_text),
                ImageSendMessage(original_content_url=about_us_img, preview_image_url=about_us_img), StickerSendMessage(package_id=2,sticker_id=28)])



