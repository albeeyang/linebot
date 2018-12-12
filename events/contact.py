
from  line_bot_api import *

def contact_event(event):
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/UeLbtc0.jpg',
            title='contact',
            text='請選擇',
            actions=[

                URIAction(
                    label='打給我',
                    uri='tel:0908159188'
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token=event.reply_token, messages=[buttons_template_message]
    )