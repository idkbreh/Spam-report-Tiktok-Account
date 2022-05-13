import requests
from requests.sessions import session
import json
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()
session = requests.session()
print( "Made with finger by SIMP#2712")
x = input('Url in f12 : ')
while True:
    req = session.post(x)
    print(req.text)
    print(Fore.GREEN +'SUCCESS REPORT SUCCESS REPORT SUCCESS REPORT ')

    time.sleep(1) #เอาออกได้ถ้าอยากทำเเต่มี ratelimit
input()
