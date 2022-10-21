import time
import requests
import json


keys = []
with open("./keys_use.json", "r", encoding="utf-8") as keyFile:
    keys = json.load(keyFile)
print(keys)

# 訊息推播
message = u""
i = input('功能: 1/地震即時推播, 2/地震災防告警, 0/其他消息推播 => ')

# 現在時間
now = time.localtime()
nowTime = time.strftime("%Y-%m-%d, %H:%M:%S", now)

if( i == '1' ): #若要測試請開啟測試訊息並關閉KNY消息來源
    #message += "\n***測試訊息***\n"
    message += "即時地震消息⚠️\n台灣"
    
    earthquake = input('快速選項: 1/東北近海, 2/東近海, 3/東南近海, 4/東北, 5/東, 6/北, 7/中, 8/南, 0/輸入其他區域 => ')
    if( earthquake == '1' ):
        message += "東北部近海"
    elif( earthquake == '2' ):
        message += "東部近海"
    elif( earthquake == '3' ):
        message += "東南部近海"
    elif( earthquake == '4' ):
        message += "東北部地區"
    elif( earthquake == '5' ):
        message += "東部地區"
    elif( earthquake == '6' ):
        message += "北部地區"
    elif( earthquake == '7' ):
        message += "中部地區"
    elif( earthquake == '8' ):
        message += "南部地區"
    else:
        message += input('請輸入區域: => ')

    feeling = input('提示為有感地震? (Y/任意鍵不提示) => ')
    if( feeling == 'Y' or feeling =='y' ):
        message += "發生有感地震，慎防搖晃\n\n"   
        message += "請保持冷靜、立刻保護頭頸部並就地趴下尋找掩護\n"
        message += "地震後若要進行疏散，請先關閉電源火源，且勿搭乘電梯\n"
    else :
        message += "發生地震，詳情請參閱中央氣象局地震消息\n"

    message += "\n消息來源: KNY台灣天氣,地震速報"

elif( i == '0' ):
    message += input("請直接輸入訊息: ") + '\n'

elif( i == '2' ):
    message += "***災防告警***\n\n 台灣地區正發生顯著有感地震\n"

message += "\n系統時間標記: " + nowTime

# 發送通知
print(message)

print("\n確定發送? (Y/任意鍵終止)")
check = input()
if( check=='Y' or check=='y' ) :
    print("Start Broadcast:")
else :
    print("終止程序")
    quit()

for name, key in keys.items():
    print(f"[{name}]")
    status = requests.get(url="https://notify-api.line.me/api/status",
                          headers={"Authorization": "Bearer " +
                                   key})
    status = status.json()
    print(f"BOT狀態: {status['message']}\n群組名稱: {status['target']}\n", end="")
    result = requests.post(url="https://notify-api.line.me/api/notify",
                           headers={"Authorization": "Bearer " +
                                    key},
                           data={"message": message})
    if(result.status_code == 200):
        print("發送成功")
    else:
        print("發送失敗")
