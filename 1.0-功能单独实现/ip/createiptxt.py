#coding:utf8

import requests
import re
import time

req = requests.Session()
url = "http://www.kuaidaili.com/free/inha/"
header = {
    'Upgrade-Insecure-Requests':1,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
limit = '''<td data-title="IP">(.*?)<\/td>\s*<td data-title="PORT">(.*?)<\/td>'''
cc=re.compile(limit)
l = []
# print cc.findall(res)

for i in range(1, 5):
    time.sleep(1)
    ip_url = url + str(i)
    res = req.get(ip_url, headers=header).content
    s = cc.findall(res)
    for x in s:
        ip = ":".join(x) + '\n'
        l.append(ip)
with open('ip.txt', 'a') as f1:
    f1.writelines(l)