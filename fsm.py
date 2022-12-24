from transitions.extensions import GraphMachine
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, ImageSendMessage
from utils import send_text_message, send_message
import requests
canmessage = TemplateSendMessage(
                                alt_text ='Buttons template',
                                template = ButtonsTemplate(
                                    thumbnail_image_url='https://1.bp.blogspot.com/-cM_JOEo9Q5E/X-x1jogQw8I/AAAAAAAALDA/VsbwTKQ2U6o8Da0wPv2vnyt9jBxWhlQmQCNcBGAsYHQ/s647/gaitubao_KU%2Bbasic_jpg1.jpg',
                                    title = '請問需要什麼服務?',
                                    text = '如需更多功能請按下一頁鍵或輸入"下一頁"',
                                    actions=[
                                        MessageTemplateAction(
                                            label = '今日各地天氣預報',
                                            text = '今日各地天氣預報'
                                        ),
                                        MessageTemplateAction(
                                            label = '今日運勢',
                                            text = '今日運勢'
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
# canmessage1 = TemplateSendMessage(
#                                 alt_text ='Buttons template',
#                                 template = ButtonsTemplate(
#                                     thumbnail_image_url='https://1.bp.blogspot.com/-cM_JOEo9Q5E/X-x1jogQw8I/AAAAAAAALDA/VsbwTKQ2U6o8Da0wPv2vnyt9jBxWhlQmQCNcBGAsYHQ/s647/gaitubao_KU%2Bbasic_jpg1.jpg',
#                                     title = '這一頁還沒開發完成，在此獻上最高的歉意。',
#                                     text = '如需返回上一頁請按返回鍵或輸入"返回"',
#                                     actions=[
#                                         MessageTemplateAction(
#                                             label = '對不起',
#                                             text = '對不起'
#                                         ),
#                                         MessageTemplateAction(
#                                             label = '這一頁還沒開發完成喔',
#                                             text = '這一頁還沒開發完成喔'
#                                         ),
#                                         MessageTemplateAction(
#                                             label = '網站表',
#                                             text = '網站表'
#                                         ),
#                                         MessageTemplateAction(
#                                             label = '返回',
#                                             text = '返回'
#                                         )
                                        
#                                     ]
#                                 )
#                             )
keyword = ["牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座", "摩羯座", "水瓶座", "雙魚座", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

keywordc = ["台北市", "新北市", "桃園縣", "新竹市", "苗栗縣", "台中市", "彰化縣", "雲林縣", "嘉義縣", "台南市", "高雄市", "屏東縣", "花蓮縣", "台東縣", "宜蘭縣", "基隆市", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
urlc = ["https://weather.com/zh-TW/weather/today/l/fe7393b7f2c8eed2cf692bd079361df362d9f0c1c0f896e6e46a649295e15c7d", "https://weather.com/zh-TW/weather/today/l/202fab9acca1bbb5edc387b8e8da03beeb7bcef4b4744f237fad2b5ed06ccc9b", "https://weather.com/zh-TW/weather/today/l/2063dc93d721d794396441c2473f2d3e6e5b335903034198829e1e86eb9e83e0", "https://weather.com/zh-TW/weather/today/l/7ceb69e37a100e138b92e592f2bd6619cfa4626f7315d0877b5061494e83bb77", "https://weather.com/zh-TW/weather/today/l/98898840824a2ce5e45198b2a770ac6e8f106f7f5da8d4188342d9a0eb7b4646", "https://weather.com/zh-TW/weather/today/l/dd5ff859897b2c4c4e6685a991f36c262d87df06e83cacbdcc661952cf42f76c", "https://weather.com/zh-TW/weather/today/l/5ab68825e5707d9ae97fff0ce6a466143da423d852b96cacfe685321841852c7", "https://weather.com/zh-TW/weather/today/l/d19a8ded0b14929d05697c400dcfb0fb3e183af6d272d7b3e7c9bffce9ec56b6", "https://weather.com/zh-TW/weather/today/l/10aef81155ecc24e4e5921212f57b57370388c49b9bfe22d4cdf68463ff6b497", "https://weather.com/zh-TW/weather/today/l/428a16ac8864a5387146aa0d8046b67fe787856453e5d97fd86a84b287678ba4", "https://weather.com/zh-TW/weather/today/l/ab6a0d440cf29997c96b86e11b647c285d3a489a623ea04d29fdefe0ea3534b2", "https://weather.com/zh-TW/weather/today/l/0f2fe653d8fc4305e214c9ee0d128f10f8db0658565e7ddd456b5c1ab9bb8dad", "https://weather.com/zh-TW/weather/today/l/00929a4113c22c58c9313b19844bbb6b2df815f80eb2cb96128e68933a503284", "https://weather.com/zh-TW/weather/today/l/55e9e1bcfd283aaa0e2456699b82ef892359d560f1ec47a38a3eeba59ef15b5b", "https://weather.com/zh-TW/weather/today/l/5206d5e441522dd7e4aa1e4197038aae536b860e1e8e8235e2e66cb2f9434128", "https://weather.com/zh-TW/weather/today/l/047be26b6fbb01ad1ce1353c8a1586474caf4949b1d53a4898d598c52954ad72"]
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

        pos = res.text[res.text.find('class="CurrentConditions--tempValue--3KcTQ')+44:res.text.find('class="CurrentConditions--tempValue--3KcTQ')+47]
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

        str_arr = str_arr +"凌晨 " + pos+"C 降雨機率 "+pos1+"\n\n資料來源:weather.com"

        reply_arr.append(TextSendMessage(str_arr))
        reply_arr.append(canmessage)

        send_message(reply_token , reply_arr)
        self.go_back()
    #####天氣#####

    #####FSM圖#####
    def is_going_to_showfsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def on_enter_showfsm(self, event):
        print("I'm entering showfsm")
        reply_token = event.reply_token
        reply_arr = []
        reply_arr.append(TextSendMessage("This is my FSM diagram"))
        # reply_arr.append(ImageSendMessage(original_content_url='https://imbotku.herokuapp.com/show-fsm'))
        reply_arr.append(canmessage)
        send_message(reply_token, reply_arr)
        self.go_back()
    #####FSM圖#####

    #####星座運勢#####
    def is_going_to_fortune(self, event):
        text = event.message.text
        return text.lower() == "今日運勢"

    def on_enter_fortune(self, event):
        print("I'm entering fortune")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入你的星座:\n牡羊座 請輸入0\n金牛座 請輸入1\n雙子座 請輸入2\n巨蟹座 請輸入3\n獅子座 請輸入4\n處女座 請輸入5\n天秤座 請輸入6\n天蠍座 請輸入7\n射手座 請輸入8\n摩羯座 請輸入9\n水瓶座 請輸入10\n雙魚座 請輸入11\n輸入12返回上一頁")

    def is_going_to_fortune2(self, event):
        print("INFUNCTION")
        text = event.message.text
        
        return text.lower() in keyword

    def on_enter_fortune2(self, event):
        print(event.message.text)
        i=0
        if(len(event.message.text)==3):
            i=0
            for key in keyword:
                if(key == event.message.text):
                    break
                i=i+1
        else :
            i=int(event.message.text)

        reply_token = event.reply_token
        if (i==12):
            send_message(reply_token, canmessage)
            self.go_back()
            return
        reply_arr = []

        str_arr = keyword[i]+"\n\n"

        res = requests.get("https://astro.click108.com.tw/daily_"+str(i)+".php?iAstro="+str(i))
        
        pos = res.text[res.text.find('love.png'):res.text.find('love.png')+200]
        pos = pos[pos.find('LIGHT">'):pos.find('LIGHT">')+100]

        star =""
        for i in range (0, int(pos[pos.find('icon')+5:pos.find('.png')])):
            star =star+"★"
        for i in range (0, 5-int(pos[pos.find('icon')+5:pos.find('.png')])):
            star =star+"☆"
        str_arr = str_arr + "愛情運勢: "+star+"\n\n"

        pos = res.text[res.text.find('work.png'):res.text.find('work.png')+200]
        pos = pos[pos.find('LIGHT">'):pos.find('LIGHT">')+100]

        star =""
        for i in range (0, int(pos[pos.find('icon')+5:pos.find('.png')])):
            star =star+"★"
        for i in range (0, 5-int(pos[pos.find('icon')+5:pos.find('.png')])):
            star =star+"☆"
        str_arr = str_arr +"工作運勢: "+star+"\n\n"

        pos = res.text[res.text.find('all.png'):res.text.find('all.png')+200]
        pos = pos[pos.find('LIGHT">'):pos.find('LIGHT">')+100]

        star =""
        for i in range (0, int(pos[pos.find('icon')+5:pos.find('.png')])):
            star =star+"★"
        for i in range (0, 5-int(pos[pos.find('icon')+5:pos.find('.png')])):
            star =star+"☆"
        str_arr = str_arr + "整體運勢: "+star+"\n\n"

        str_arr = str_arr + "幸運數字: "+res.text[res.text.find('"NUMERAL">')+10:res.text.find('"NUMERAL">')+11]+"\n\n"

        pos = res.text[res.text.find('title02.png')+52:res.text.find('title02.png')+90]

        str_arr = str_arr + "幸運顏色: "+pos[pos.find("<h4>")+4:pos.find("</h4>")]+"\n\n資料來源:科技紫微網" 

        reply_arr.append(TextSendMessage(str_arr))
        reply_arr.append(canmessage)
        send_message(reply_token, reply_arr)
        self.go_back()
    #####星座運勢#####

    # #####顯示第二頁#####
    # def is_going_to_page2(self, event):
    #     text = event.message.text
    #     return text.lower() == "下一頁"

    # def on_enter_page2(self, event):
    #     print("I'm entering page2")

    #     reply_token = event.reply_token

    #     send_message(reply_token, canmessage1)
    #     self.go_back()
    # #####顯示第二頁#####

    #####顯示網站表#####
    def is_going_to_website(self, event):
        text = event.message.text
        return text.lower() == "websites"

    def on_enter_website(self, event):
        print("I'm entering website")

        reply_token = event.reply_token
        str_arr = "火車訂票網站 https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query\n"
        str_arr += "高鐵訂票網站 https://irs.thsrc.com.tw/IMINT/?locale=tw" 
        reply_arr = []
        reply_arr.append(TextSendMessage(str_arr))
        reply_arr.append(canmessage)
        send_message(reply_token, reply_arr)
        self.go_back()
    #####顯示網站表#####
        