import requests
import re
url = input("输入你的url:")
r = requests.get(url)
res = str(r.content)
if re.search("syntax", res):
    print("存在sql注入")
else:
    print("不存在")
