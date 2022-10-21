import time
import requests
import json


keys = []
with open("./keys.json", "r", encoding="utf-8") as keyFile:
    keys = json.load(keyFile)
print(keys)

# 訊息推播
message = u""

# 現在時間
now = time.localtime()
nowTime = time.strftime("%Y-%m-%d, %H:%M:%S", now)

#訊息
message += "***災防告警***\n\n 台灣地區正發生顯著有感地震\n"

message += "\n系統時間標記: " + nowTime

# 發送通知
print(message)

#print("\n確定發送? (Y/任意鍵終止)")
#check = input()
#if( check=='Y' or check=='y' ) :
#    print("Start Broadcast:")
#else :
#    print("終止程序")
#    quit()

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
