from termcolor import colored
import threading
import requests
import random
import string
import base64
import json

WEBHOOK_URL = 'YOUR WEBHOOK URL HERE'
valid = 0
invalid = 0
proxy_num = 0
proxies = []

with open('data.json') as fp:
    Base64FakeImages = json.load(fp)

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def grab_proxies():
    global proxies
    proxies = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=5000&country=all&ssl=all&anonymity=all').text.splitlines()
    print("proxies reloaded")


def checkifimageisvalid(arg):
    global valid, invalid
    response = requests.get(arg, headers=headers)
    if response.ok:
        uri = base64.b64encode(response.content).decode("utf-8")
        if uri in Base64FakeImages.values():
            invalid += 1
        else:
            valid += 1
            requests.post(WEBHOOK_URL, data={"content": '[VALID] {}'.format(arg)})
            print("[" + colored('sent to discord', 'green', attrs=['bold']) + "] " + arg)


def main(proxy):
    global valid, invalid
    # all new uploaded images start with 1 and are 7 characters long
    code = "1" + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
    try:
        check = requests.get(f'https://prnt.sc/{code}', headers=headers, proxies={'https': 'http://%s' % (proxy)}).text
        if 'name="twitter:image:src" content="' in check and not '0_173a7b_211be8ff' in check and not 'ml3U3Pt' in check:
            url = check.split('name="twitter:image:src" content="')[1].split('"/> <meta')[0]
            checkifimageisvalid(url)
        else:
            invalid += 1
            print("[" + colored(f'attempts', 'red', attrs=['bold']) + "] " + str(valid + invalid), end="\r")
    except:
        pass


grab_proxies()

while True:
    if threading.active_count() <= 200:
        try:
            threading.Thread(target=main, args=(proxies[proxy_num],)).start()
            proxy_num += 1
            if proxy_num >= len(proxies):
                proxy_num = 0
                proxies.clear()
                grab_proxies()
        except:
            pass
