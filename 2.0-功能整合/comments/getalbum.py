import requests
import re

class getArtist(object):
    def __init__(self, req = requests.Session()):
        self._source_url = []
        self._req = req
        self._artistid = []

    def _set_source(self, ids):
        self._source_url = []
        for i in range(65,91):
            url = "http://music.163.com/discover/artist/cat?id=" + ids + "&initial=" + str(i)
            self._source_url.append(url)
        url = "http://music.163.com/discover/artist/cat?id=" + ids + "&initial=0"
        self._source_url.append(url)
    
    def getartist(self, ids, re_regular, proxy = None, func = None):     # 正则必须第一个筛选歌手id  或者传入函数使结果的第一个项为歌手id
        result = []
        tmp_result = []
        self._set_source(ids)
        regular = re.compile(re_regular)
        for url in self._source_url:
            html = self._req.get(url, proxies = proxy).content
            tmp_result += regular.findall(html, re.DOTALL)       # id-姓名-信息
            if func:
                tmp_result = func(tmp_result)
            result += tmp_result
        
        self._artistid = [x[0] for x in result]
            # map(lambda url: url="http://music.163.com/artist/album?id=" + artist, result)
        return result
    
    def getalbum(self, re_regular, proxy = None):
        pass
        # ressult = []
        # regular = re.compile(re_regular)
        # for artist_id in self._artistid:
        #     url = "http://music.163.com/artist/album?id="+ artist_id +"&limit=108&offset=0"
        #     result += self._req.get(url, proxies = proxy).content)     # 歌手id-专辑id
        # return result

class getAlbumMusic(object):
    def __init__(self, req = requests.Session()):
        self._req = req
        self._album = []

    def _set_album(self, album):
        for tmp in album:
            url = "http://music.163.com/#/album?id=" + tmp
            self._album.append(url)

    def getMusic(self, re_regular, proxy = None):
        result = []
        regular = re.compile(re_regular)
        for album_url in self._album:
            html = self._req.get(album_url, proxies = proxy).content
            result += regular.findall(html, re.DOTALL)
        return result