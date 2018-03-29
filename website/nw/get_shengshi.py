#-*-coding:utf-8-*-

import re
import sys
import time

import requests

import sql

reload(sys)
sys.setdefaultencoding('utf-8') 

if __name__ == "__main__":
    url = "http://jingwei.supfree.net/"
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    
    #-----初始化正则表达式
    get_con = r'<div class="cdiv">(.+?)</div>'   #获取主体内容部分
    get_sheng = r'botitle14(.+?)bred'            #获取省市部分
    get_shengshi = r'>(.+?)<'             #获取省市内容
    get_url = r'href="(.*?)"'             #获取目标url
    get_nwdata = r'class="cdiv">(.+?)<div class="cdiv">'
    get_nwcity = r'<strong>(.+?)</strong>'
    get_nw = r'[1-9]\d*\.\d*|0\.\d*[1-9]\d*' #获取经纬度
    #----------------------

    r = requests.Session()
    res = r.get(url, headers = header)
    html = res.content

    re1 = re.compile(get_con, re.MULTILINE|re.DOTALL)
    # re2 = re.compile(get_sheng, re.MULTILINE|re.DOTALL)
    # re3 = re.compile(get_shengshi)
    re4 = re.compile(get_url)
    re_getnwdata = re.compile(get_nwdata, re.MULTILINE|re.DOTALL)
    re_getnwcity = re.compile(get_nwcity)
    re_getnw = re.compile(get_nw)

    all_data = re1.findall(html)[0]

    city_nw = {}

    url2 = re4.findall(all_data)          #获取到了每一个市的url
    url2 = [url+x for x in url2]
    # print time.clock()
    for a in url2:
        res_a = r.get(a, headers = header)
        try:
            city_data = re1.findall(res_a.content)[0]
            nw_url = url + re4.findall(city_data)[0]
            # print time.clock()
            nw_1 = r.get(nw_url, headers = header)
            # print time.clock()
            nw_2 = re_getnwdata.findall(nw_1.content)[0]
            # print time.clock()
            #print nw_2
            city = re_getnwcity.findall(nw_2)[0]
            nw = re_getnw.findall(nw_2)
            city = city.split(' ')[-1]
            city_nw[city.decode('gbk')] = nw
            # print time.clock()
        except:
            print a

    # for key in city_nw:
    #     print key, city_nw[key]

    go_data = sql.sql('cs')
    go_data.update(city_nw)
    go_data.close()




#### 存了各省市的数据
    # level_1 = []
    # level_2 = {}
    # all_data = re1.findall(html)[0]

    # # print len(re2.findall(all_data))

    # for x in re2.findall(all_data):
    #     # print x
    #     # print "-------------"
    #     shengshi = re3.findall(x)
    #     # print shengshi[0]
    #     level_1.append(shengshi[0].decode('gbk'))
    #     level_2[shengshi[0].decode('gbk')] = [x.decode('gbk') for x in shengshi[1:]]

    # go_data = sql.sql('cs')
    # go_data.insert(level_1)
    # go_data.close()
