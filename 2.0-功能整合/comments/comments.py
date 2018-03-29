#-*-coding:utf8-*-

import requests
import re

class getComments():            # 以歌曲为单位爬取评论并存入
    def __init__(self, req = requests.Session()):
        self._musicurl = []        # 歌曲-信息存表 专辑-歌曲存表 然后歌曲-评论存表
        self._req = req

    def _setmusic(self, music_id):
        for i in music_id:
            url = "http://music.163.com/#/song?id=" + i
            self._musicurl.append(url)

    def getMusic(self, music_id, re_regular, proxy = None):
        self._setmusic(music_id)
        result = []
        regular = re.compile(re_regular)
        for music_url in self._musicurl:
            html = self.req.get(music_url, proxies = proxy).content
            result += regular.findall(html, re.DOTALL)
        return result


    def getComments(self, re_regular, proxy = None):
        result = []
        regular = re.compile(re_regular)
        for 