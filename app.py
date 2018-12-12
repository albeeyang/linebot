from flask import Flask, request, abort

from line_bot_api import *

from events.about_us import about_us_event
from events.location import location_event
from events.contact import contact_event

app = Flask(__name__)





@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = str(event.message.text).lower()

    if message_text == '@aboutus':
        about_us_event(event)

    elif message_text == '@location':
        location_event(event)
    elif message_text == '@contact':
        contact_event(event)

if __name__ == "__main__":
    app.run()