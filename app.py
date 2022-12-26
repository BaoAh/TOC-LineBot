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

# @app.route("/callback", methods=["POST"])
# def callback():
#     signature = request.headers["X-Line-Signature"]
#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)
    
#     # parse webhook body
#     try:
#         events = parser.parse(body, signature)
#     except InvalidSignatureError:
#         abort(400)
#     keyword = ['網站表', '今日運勢', "下一頁", "今日各地天氣預報", "牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座", "摩羯座", "水瓶座", "雙魚座", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16","返回", "不要按我"]
#     # if event is MessageEvent and message is TextMessage, then echo text
#     for event in events:
#         if not isinstance(event, MessageEvent):
#             continue
#         if not isinstance(event.message, TextMessage):
#             if(str(machine.state) == "user"): 
#                 line_bot_api.reply_message(event.reply_token, canmessage)

#             continue
        
#         for key in keyword:

#             if(key == event.message.text): 
#                 response = machine.advance(event)
#                 if response == False:
#                     #在fortune state發生error input時
#                     if(str(machine.state) == "fortune"): 
#                         send_text_message(event.reply_token, "輸入錯誤，請再確認一次\n請輸入你的星座:\n牡羊座 請輸入0\n金牛座 請輸入1\n雙子座 請輸入2\n巨蟹座 請輸入3\n獅子座 請輸入4\n處女座 請輸入5\n天秤座 請輸入6\n天蠍座 請輸入7\n射手座 請輸入8\n摩羯座 請輸入9\n水瓶座 請輸入10\n雙魚座 請輸入11\n輸入12返回上一頁")
#                     #在weather state發生error input時
#                     elif(str(machine.state) == "weather"):
#                          send_text_message(event.reply_token, "輸入錯誤，請再確認一次\n請輸入要查詢的縣市:\n台北市 請輸入0\n新北市 請輸入1\n桃園縣 請輸入2\n新竹市 請輸入3\n苗栗縣 請輸入4\n台中市 請輸入5\n彰化縣 請輸入6\n雲林縣 請輸入7\n嘉義縣 請輸入8\n台南市 請輸入9\n高雄市 請輸入10\n屏東縣 請輸入11\n花蓮縣 請輸入12\n台東縣 請輸入13\n宜蘭縣 請輸入14\n基隆市 請輸入15\n輸入16返回上一頁")
#                     #在page2 按下返回鍵時
#                     elif(str(machine.state) == "user" and key == "返回"):
#                         send_message(event.reply_token, canmessage)
#                     else:
#                         send_text_message(event.reply_token, "系統忙碌中")
#                 print(f"\nFSM STATE: {machine.state}")
#                 return "OK"
#         if(str(machine.state) == "user"): 
#             line_bot_api.reply_message(event.reply_token, canmessage)
#         elif(str(machine.state) == "fortune"): 
#             send_text_message(event.reply_token, "輸入錯誤，請再確認一次\n請輸入你的星座:\n牡羊座 請輸入0\n金牛座 請輸入1\n雙子座 請輸入2\n巨蟹座 請輸入3\n獅子座 請輸入4\n處女座 請輸入5\n天秤座 請輸入6\n天蠍座 請輸入7\n射手座 請輸入8\n摩羯座 請輸入9\n水瓶座 請輸入10\n雙魚座 請輸入11\n輸入12返回上一頁")
#         elif(str(machine.state) == "weather"):
#              send_text_message(event.reply_token, "輸入錯誤，請再確認一次\n請輸入要查詢的縣市:\n台北市 請輸入0\n新北市 請輸入1\n桃園縣 請輸入2\n新竹市 請輸入3\n苗栗縣 請輸入4\n台中市 請輸入5\n彰化縣 請輸入6\n雲林縣 請輸入7\n嘉義縣 請輸入8\n台南市 請輸入9\n高雄市 請輸入10\n屏東縣 請輸入11\n花蓮縣 請輸入12\n台東縣 請輸入13\n宜蘭縣 請輸入14\n基隆市 請輸入15\n輸入16返回上一頁")
#         else : 
#             send_text_message(event.reply_token, "輸入錯誤，請再確認一次")

#     print(f"\nFSM STATE: {machine.state}")
#     return "OK"


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
