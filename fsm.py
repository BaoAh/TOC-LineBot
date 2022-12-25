from transitions.extensions import GraphMachine
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, ImageSendMessage
from utils import send_text_message, send_message,send_image_url
import requests
canmessage = TemplateSendMessage(
                                alt_text ='Buttons template',
                                template = ButtonsTemplate(
                                    title = '請問需要什麼服務?',
                                    text = '',
                                    actions=[
                                        MessageTemplateAction(
                                            label = '今日各地天氣預報',
                                            text = '今日各地天氣預報'
                                        ),
                                        MessageTemplateAction(
                                            label = '今日各地空氣品質',
                                            text = '今日各地空氣品質'
                                        ),
                                        MessageTemplateAction(  #fsm
                                            label = 'FSM',
                                            text = 'FSM'
                                        ),
                                        MessageTemplateAction(  #website
                                            label = 'Websites',
                                            text = 'Websites'
                                        )
                                        
                                    ]
                                )
                            )

keywordc = ["台北市", "新北市", "桃園縣", "新竹市", "苗栗縣", "台中市", "彰化縣", "雲林縣", "嘉義縣", "台南市", "高雄市", "屏東縣", "花蓮縣", "台東縣", "宜蘭縣", "基隆市", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
urlc = ["https://weather.com/zh-TW/weather/today/l/fe7393b7f2c8eed2cf692bd079361df362d9f0c1c0f896e6e46a649295e15c7d", "https://weather.com/zh-TW/weather/today/l/202fab9acca1bbb5edc387b8e8da03beeb7bcef4b4744f237fad2b5ed06ccc9b", "https://weather.com/zh-TW/weather/today/l/2063dc93d721d794396441c2473f2d3e6e5b335903034198829e1e86eb9e83e0", "https://weather.com/zh-TW/weather/today/l/7ceb69e37a100e138b92e592f2bd6619cfa4626f7315d0877b5061494e83bb77", "https://weather.com/zh-TW/weather/today/l/98898840824a2ce5e45198b2a770ac6e8f106f7f5da8d4188342d9a0eb7b4646", "https://weather.com/zh-TW/weather/today/l/dd5ff859897b2c4c4e6685a991f36c262d87df06e83cacbdcc661952cf42f76c", "https://weather.com/zh-TW/weather/today/l/5ab68825e5707d9ae97fff0ce6a466143da423d852b96cacfe685321841852c7", "https://weather.com/zh-TW/weather/today/l/d19a8ded0b14929d05697c400dcfb0fb3e183af6d272d7b3e7c9bffce9ec56b6", "https://weather.com/zh-TW/weather/today/l/10aef81155ecc24e4e5921212f57b57370388c49b9bfe22d4cdf68463ff6b497", "https://weather.com/zh-TW/weather/today/l/428a16ac8864a5387146aa0d8046b67fe787856453e5d97fd86a84b287678ba4", "https://weather.com/zh-TW/weather/today/l/ab6a0d440cf29997c96b86e11b647c285d3a489a623ea04d29fdefe0ea3534b2", "https://weather.com/zh-TW/weather/today/l/0f2fe653d8fc4305e214c9ee0d128f10f8db0658565e7ddd456b5c1ab9bb8dad", "https://weather.com/zh-TW/weather/today/l/00929a4113c22c58c9313b19844bbb6b2df815f80eb2cb96128e68933a503284", "https://weather.com/zh-TW/weather/today/l/55e9e1bcfd283aaa0e2456699b82ef892359d560f1ec47a38a3eeba59ef15b5b", "https://weather.com/zh-TW/weather/today/l/5206d5e441522dd7e4aa1e4197038aae536b860e1e8e8235e2e66cb2f9434128", "https://weather.com/zh-TW/weather/today/l/047be26b6fbb01ad1ce1353c8a1586474caf4949b1d53a4898d598c52954ad72"]
# url_air = ["https://weather.com/zh-TW/weather/today/l/fe7393b7f2c8eed2cf692bd079361df362d9f0c1c0f896e6e46a649295e15c7d", "https://weather.com/zh-TW/weather/today/l/202fab9acca1bbb5edc387b8e8da03beeb7bcef4b4744f237fad2b5ed06ccc9b", "https://weather.com/zh-TW/weather/today/l/2063dc93d721d794396441c2473f2d3e6e5b335903034198829e1e86eb9e83e0", "https://weather.com/zh-TW/weather/today/l/7ceb69e37a100e138b92e592f2bd6619cfa4626f7315d0877b5061494e83bb77", "https://weather.com/zh-TW/weather/today/l/98898840824a2ce5e45198b2a770ac6e8f106f7f5da8d4188342d9a0eb7b4646", "https://weather.com/zh-TW/weather/today/l/dd5ff859897b2c4c4e6685a991f36c262d87df06e83cacbdcc661952cf42f76c", "https://weather.com/zh-TW/weather/today/l/5ab68825e5707d9ae97fff0ce6a466143da423d852b96cacfe685321841852c7", "https://weather.com/zh-TW/weather/today/l/d19a8ded0b14929d05697c400dcfb0fb3e183af6d272d7b3e7c9bffce9ec56b6", "https://weather.com/zh-TW/weather/today/l/10aef81155ecc24e4e5921212f57b57370388c49b9bfe22d4cdf68463ff6b497", "https://weather.com/zh-TW/weather/today/l/428a16ac8864a5387146aa0d8046b67fe787856453e5d97fd86a84b287678ba4", "https://weather.com/zh-TW/weather/today/l/ab6a0d440cf29997c96b86e11b647c285d3a489a623ea04d29fdefe0ea3534b2", "https://weather.com/zh-TW/weather/today/l/0f2fe653d8fc4305e214c9ee0d128f10f8db0658565e7ddd456b5c1ab9bb8dad", "https://weather.com/zh-TW/weather/today/l/00929a4113c22c58c9313b19844bbb6b2df815f80eb2cb96128e68933a503284", "https://weather.com/zh-TW/weather/today/l/55e9e1bcfd283aaa0e2456699b82ef892359d560f1ec47a38a3eeba59ef15b5b", "https://weather.com/zh-TW/weather/today/l/5206d5e441522dd7e4aa1e4197038aae536b860e1e8e8235e2e66cb2f9434128", "https://weather.com/zh-TW/weather/today/l/047be26b6fbb01ad1ce1353c8a1586474caf4949b1d53a4898d598c52954ad72"]

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    #####天氣#####
    def is_going_to_weather(self, event):
        text = event.message.text
        return text.lower() == "今日各地天氣預報"

    def on_enter_weather(self, event):
        print("I'm entering weather")
        reply_token = event.reply_token

        send_text_message(reply_token, "請輸入要查詢的縣市:\n台北市 請輸入0\n新北市 請輸入1\n桃園縣 請輸入2\n新竹市 請輸入3\n苗栗縣 請輸入4\n台中市 請輸入5\n彰化縣 請輸入6\n雲林縣 請輸入7\n嘉義縣 請輸入8\n台南市 請輸入9\n高雄市 請輸入10\n屏東縣 請輸入11\n花蓮縣 請輸入12\n台東縣 請輸入13\n宜蘭縣 請輸入14\n基隆市 請輸入15\n輸入16返回上一頁")

    def is_going_to_weather2(self, event):
        text = event.message.text
        return text.lower() in keywordc

    def on_enter_weather2(self, event):
        print("I'm entering weather2")
        reply_token = event.reply_token
        i =0
        if(len(event.message.text) == 3):
            for key in keywordc:
                if(event.message.text == key):
                    break
                i=i+1
        else :
            i = int(event.message.text)

        if(i == 16):
            send_message(reply_token, canmessage)
            self.go_back()

        reply_arr = []
        str_arr = []
        str_arr = keywordc[i]+"\n"
        # print(keywordc[i])
        # print(urlc[i])
        res = requests.get(urlc[i])

        pos = res.text[res.text.find('class="CurrentConditions--tempValue--MHmYY')+44:res.text.find('class="CurrentConditions--tempValue--MHmYY')+47]
        str_arr = str_arr +"目前氣溫 "+pos+"C\n"
        print("目前氣溫 "+pos+"C")
        pos = res.text[res.text.find('午前'):res.text.find('午前')+1000]
        pos1 = pos[pos.find("降雨機率")+11:pos.find("降雨機率")+14]
        pos = pos[pos.find('"TemperatureValue"')+19:pos.find('"TemperatureValue"')+22]
        if(pos1[2]!="%"):
            #100% and 0~9%
            if("%" in pos1):
                pos1 = pos1 [0:2]
            elif(pos1 == "100"):
                pos1 = pos1+"%"
            else:
                pos1 = "0%"
        str_arr = str_arr +"早上 " + pos+"C 降雨機率 "+pos1+"\n"


        pos = res.text[res.text.find('午後'):res.text.find('午後')+2000]
        pos1 = pos[pos.find("降雨機率")+11:pos.find("降雨機率")+14]
        pos = pos[pos.find('"TemperatureValue"')+19:pos.find('"TemperatureValue"')+22]
        if(pos1[2]!="%"):
            #100% and 0~9%
            if("%" in pos1):
                pos1 = pos1 [0:2]
            elif(pos1 == "100"):
                pos1 = pos1+"%"
            else:
                pos1 = "0%"

        str_arr = str_arr +"下午 " + pos+"C 降雨機率 "+pos1+"\n"


        pos = res.text[res.text.find('傍晚'):res.text.find('傍晚')+2000]
        pos1 = pos[pos.find("降雨機率")+11:pos.find("降雨機率")+14]
        pos = pos[pos.find('"TemperatureValue"')+19:pos.find('"TemperatureValue"')+22]
        if(pos1[2]!="%"):
            #100% and 0~9%
            if("%" in pos1):
                pos1 = pos1 [0:2]
            elif(pos1 == "100"):
                pos1 = pos1+"%"
            else:
                pos1 = "0%"

        str_arr = str_arr +"傍晚 " + pos+"C 降雨機率 "+pos1+"\n"


        pos = res.text[res.text.find('徹夜'):res.text.find('徹夜')+2000]
        pos1 = pos[pos.find("降雨機率")+11:pos.find("降雨機率")+14]
        pos = pos[pos.find('"TemperatureValue"')+19:pos.find('"TemperatureValue"')+22]
        if(pos1[2]!="%"):
            #100% and 0~9%
            if("%" in pos1):
                pos1 = pos1 [0:2]
            elif(pos1 == "100"):
                pos1 = pos1+"%"
            else:
                pos1 = "0%"

        str_arr = str_arr +"凌晨 " + pos+"C 降雨機率 "+pos1+"\n\n更多詳細資料:weather.com"

        reply_arr.append(TextSendMessage(str_arr))
        reply_arr.append(canmessage)

        send_message(reply_token , reply_arr)
        self.go_back()
    #####天氣#####

    #####air#####
    def is_going_to_air(self, event):
        text = event.message.text
        return text.lower() == "今日各地空氣品質"

    def on_enter_air(self, event):
        print("I'm entering weather")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入要查詢的縣市:\n台北市 請輸入0\n新北市 請輸入1\n桃園縣 請輸入2\n新竹市 請輸入3\n苗栗縣 請輸入4\n台中市 請輸入5\n彰化縣 請輸入6\n雲林縣 請輸入7\n嘉義縣 請輸入8\n台南市 請輸入9\n高雄市 請輸入10\n屏東縣 請輸入11\n花蓮縣 請輸入12\n台東縣 請輸入13\n宜蘭縣 請輸入14\n基隆市 請輸入15\n輸入16返回上一頁")

    def is_going_to_air2(self, event):
        text = event.message.text
        return text.lower() in keywordc

    def on_enter_air2(self, event):
        print("I'm entering air2")
        reply_token = event.reply_token
        i =0
        if(len(event.message.text) == 3):
            for key in keywordc:
                if(event.message.text == key):
                    break
                i=i+1
        else :
            i = int(event.message.text)

        if(i == 16):
            send_message(reply_token, canmessage)
            self.go_back()

        reply_arr = []
        str_arr = []
        str_arr = keywordc[i]+"\n"

        res = requests.get(urlc[i])
        # print(res.text)

        air_cond = res.text[res.text.find('class="AirQualityText--severity--1smy9')+73:res.text.find('class="AirQualityText--severity--1smy9')+75]
        # print(air_cond)
        

        pos = res.text[res.text.find('class="CurrentConditions--tempValue--3KcTQ')+44:res.text.find('class="CurrentConditions--tempValue--3KcTQ')+47]
        str_arr = str_arr +"空氣品質: "+air_cond+"\n"
        print("空氣品質 "+air_cond)

        if air_cond == '中等':
            str_arr=str_arr +"★"+"★"+"★"+"☆"+"☆"+"\n"
        elif air_cond == '良好':
            str_arr=str_arr +"★"+"★"+"★"+"★"+"★"+"\n"
        else:
            str_arr = str_arr + "☆"+"☆"+"☆"+"☆"+"☆"+"\n"

        reply_arr.append(TextSendMessage(str_arr))
        reply_arr.append(canmessage)

        send_message(reply_token , reply_arr)
        self.go_back()

    #####air#####

    #####FSM#####
    def is_going_to_showfsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def on_enter_showfsm(self, event):
        print("I'm entering showfsm")
        reply_token = event.reply_token
        reply_arr = []
        reply_arr.append(TextSendMessage("This is my FSM diagram"))
        reply_arr.append(ImageSendMessage(original_content_url='https://github.com/BaoAh/TOC-LineBot/blob/master/fsm.png?raw=true',preview_image_url='https://github.com/BaoAh/TOC-LineBot/blob/master/fsm.png?raw=true'))
        reply_arr.append(canmessage)
        send_message(reply_token, reply_arr)
        self.go_back()
    #####FSM#####


    #####Website list#####
    def is_going_to_website(self, event):
        text = event.message.text
        return text.lower() == "websites"

    def on_enter_website(self, event):
        print("I'm entering website")

        reply_token = event.reply_token
        str_arr = "火車訂票網站 🚂 https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query\n"
        str_arr += "高鐵訂票網站 🚄 https://irs.thsrc.com.tw/IMINT/?locale=tw\n" 
        str_arr += "和欣客運 🚌 https://www.ebus.com.tw/\n"
        reply_arr = []
        reply_arr.append(TextSendMessage(str_arr))
        reply_arr.append(canmessage)
        send_message(reply_token, reply_arr)
        self.go_back()
    #####Website list#####
        