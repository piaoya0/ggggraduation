#coding:utf8
import requests
import random

class IPpool:

    def __init__(self, file_name, ban_ip=None):   #存ip的文件  刚刚使用的ip
        self.i = 0
        with open(file_name, 'r') as file1:
            self.ip_list = file1.readlines()
        try:
            self.ip_list.remove(ban_ip)
        except:
            pass

    def _use_ip(self):
        if not self.ip_list:
            return "gg  换组IP"

        ip = random.choice(self.ip_list)
        agent_ip = "http://" + ip.replace('\n','')
        self.ip_list.remove(ip)
        try:
            res = requests.get("http://www.baidu.com", proxies={"http": agent_ip}, timeout=0.5)
            return agent_ip
        except:
            return self._use_ip()

# s = IPpool('ip.txt')
# print s._use_ip()