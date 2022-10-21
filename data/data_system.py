import time
import requests
import json

# 現在時間
now = time.localtime()
nowDate = time.strftime("%Y%m%d", now)

file_path = "./template.json"
new_file = (f"./{nowDate}.json")

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

#data['地點'] = input('地點: ')
for block in data["blocks"]:
    for title, value in block.items():
        print(f"{title}: ", end='')
        block[title] = input()

#print(data)
with open(new_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)  # 包含非ASCII字符

