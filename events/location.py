

from line_bot_api import *

def location_event(event):
        title_text ='location'
        address_text = 'Westminster, London SW1A 0AA'
        latitude = 51.5007292
        longitude = -0.1268141

        line_bot_api.reply_message(
            event.reply_token,
            LocationSendMessage(title=title_text, address=address_text, latitude=latitude, longitude=longitude))




