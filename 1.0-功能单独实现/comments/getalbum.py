#coding:utf8

import re
import time
import requests

import sql

class GetArtist():

    def __init__(self, req, ids, proxy=None):
        # self.sql = sql()
        self.req = req
        self.cat = []
        self.proxy = {'http':proxy}
        self.url = "http://music.163.com/discover/artist/cat?id=" + ids + "&initial="

    def _getArtist(self):
        l = []
        for i in range(65,91):
            cat_url = self.url + str(i)
            l.append(self._getid(cat_url))
        cat_url = self.url + "0"
        l.append(self._getid(cat_url))
        # sql._save("artist", l)
    
    def _getid(self, cat_url):
        r = self.req.get(cat_url, proxies=self.proxy)
        replace_r = r.content.replace(" ","")                # 莫名其妙因为空格造成匹配不到 先删掉空格  之后排查
        limit = r"<ahref=\"/artist\?id=(\d+?)\"class=\"nmnm-icnf-thides-fc0\"title=\"(.+?)的音乐\">"
        res = re.findall(limit, replace_r, re.DOTALL)
        for i in res:
            print i[0],i[1]
        # return res
        # 获得歌手id
        

class GetAlbum():
    
    def __init__(self, req, artist_id, proxy=None):          # 传入歌手id
        self.req = req
        self.url = "http://music.163.com/artist/album?id="+ artist_id +"&limit=12&offset="
        self.album = []
        self.proxy = proxy
    
    def _getAlbum(self):
        artist_url = ""
        for i in range(0, 108, 12):
            res1 = []
            artist_url = self.url+str(i)
            r = self.req.get(artist_url, proxies=self.proxy)
            limit = r"href=\"/album\?id=(\d+?)\""
            res = re.findall(limit, r.content, re.DOTALL)

            for i in res:          # 保持原顺序并去重
                if i in res1:
                    continue
                else:
                    res1.append(i)
            if not res1:
                break
            
            self.album =self.album + res1 
        print self.album        # 返回专辑id
        # return self.album
        # 把歌手-专辑 存入数据库
