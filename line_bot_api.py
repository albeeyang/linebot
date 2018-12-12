from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage , LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction
)


line_bot_api = LineBotApi('mOUh/jKcHn5BDSD6gAH3Yeiwm0Yw3S/RKNK+vX5gKMKl4XPaTHPEK2e6FMRnvTkxvnrCaaxjwEQq/Ox+W07ow6fW4pRJzhtj2mFvAYst+zVnHtnbYEqDKHtwOGzWWbLYwIiVQQ/y0td8NGXK6ZaTtgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('db5556cc9409d63c39d33241d3123233')
