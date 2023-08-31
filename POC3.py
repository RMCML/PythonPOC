import requests

def test_xss_vulnerability(url):
    payload = "<script>alert('XSS')</script>"
    headers = {"Content-Type": "text/html"}
    response = requests.post(url, data=payload, headers=headers)
    if payload in response.text:
        print("XSS vulnerability detected!")
    else:
        print("No XSS vulnerability found.")

url = "http://192.168.110.123/xss-labs/level1.php"
test_xss_vulnerability(url)