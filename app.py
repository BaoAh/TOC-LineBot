import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction
from fsm import TocMachine
from utils import send_text_message, send_message

load_dotenv()

machine = TocMachine(
    states=["user", "weather", "weather2", "air", "air2", "showfsm", "website"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "weather",
            "conditions": "is_going_to_weather",
        },
        {
            "trigger": "advance",
            "source": "weather",
            "dest": "weather2",
            "conditions": "is_going_to_weather2",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "showfsm",
            "conditions": "is_going_to_showfsm",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "air",
            "conditions": "is_going_to_air",
        },
         {
            "trigger": "advance",
            "source": "air",
            "dest": "air2",
            "conditions": "is_going_to_air2",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "website",
            "conditions": "is_going_to_website",
        },
        
        {"trigger": "go_back", "source": [ "showfsm", "air", "air2", "weather", "weather2", "website"], "dest": "user" },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "輸入\"今日各地天氣預報\"以獲得天氣最新資訊\n輸入\"今日各地空氣品質\"以獲得空氣品質最新資訊\n輸入\"FSM\"查看FSM diagram\n輸入\"Website\"前往訂票")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
