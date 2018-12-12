from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage , LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction
)


line_bot_api = LineBotApi('HtqPSH1DZtA+3qG/kas2x5Gh+LjR4K6pR7sNgcgTaJ4hLOtbQEcjGfjr2IU8BMMPQXkfGaJYf94LmBfQBLF/UEpj1MMegVFiGSjDQquWSdspt8mEFtvzLE2m4/qqBsEn2f3d3UJivGH2gcPf/r7NNQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('45514a7408ec2e4026880341666a83be')
