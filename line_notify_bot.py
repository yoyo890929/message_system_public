import time
import requests
import json

# 現在時間
now = time.localtime()
nowDate = time.strftime("%Y%m%d", now)

keys = []
with open("./keys_use.json", "r", encoding="utf-8") as keyFile:
    keys = json.load(keyFile)
print(keys)

# 讀取json
message = u""
with open(f"./data/{nowDate}.json", encoding="utf-8") as f:
    data = json.load(f)
    #message += data["公告"]+"\n"
    for block in data["blocks"]:
        for title, value in block.items():
            if title != '本土' and title != '境外' and title != '死亡' and title != '中症' and title != '重症':
                if int(value) >= 1000:  #設定縣市公布下限
                    message += f"{title} {value}\n"
            else :
                if title == '中症':
                    message += f"新增{title} {value}、"
                else:
                    message += f"{title} {value}\n"
        message += "\n"
    message += data["提醒"]

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
