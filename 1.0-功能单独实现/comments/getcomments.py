#coding:utf8

import re
import time

class GethotComments():
    def __init__(self, req, *args):
        self.album_id = args[0]   # 传入专辑id
        self.req = req

    def _getMusic(self):
        all_music = []
        for i in self.album_id:
            # 改一下对应url
            album_url = "http://music.163.com/album?id=" + str(i)
            r = self.req.get(album_url)
            limit = r"href=\"/song\?id=(\d+?)\">"
            res = re.findall(limit, r.content, re.DOTALL)
            all_music = all_music + res
            
        for music_id in all_music:
            comments_url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + music_id + '?csrf_token=' # 返回歌曲页面
            self._gethotComments(comments_url)


    def _gethotComments(self, comments_url):
        headers = {
            'Cookie': 'appver=1.5.0.75771;',
            'Referer': 'http://music.163.com/'
        }
        # 加密修改encText
        encText = 'sPYFRQ33FTNVK11X+JXEEKLu+ETCLZYEUWVM/WDq9MJk4t35FJBLD7pF02JoBTc12g8mLT+2gV5bjIK6aUdVn59GwMyjl64byYRnNw15j8nC2w+x2dicw2VjyjKlXv84RnsCoqkDO/XImxAXcqmL4dEqGeHJ8TFjh04sKVp0sWFztMYw9rHbX6QM7q7X4woZA2Hys+ujvZOaZyD/AeAUfgSV3TGdS921yJ/RAn9A0hs='
        # 加密修改encSecKey
        encSecKey = 'cd9fecf59fd71fc6871efc21889215bd1ae8893a74536beb2f6f732e7a5de5c41415f4d74e86f3e5a3f63ba454f1b649036d7b0a6d057f2775b0de05d43367ed29ff499c420304979cf4a358e6846ce9959a4e76d311d5b11dcc1c9d157c7a32adda66348534fd77e5dae02436bac2a8a1816524acb5caa091365d41d0bb3041'
        # 加密方式挖一下，现在的方式可能会访问失败
        data = {
            'params': encText,
            'encSecKey': encSecKey
        }

        r = self.req.post(comments_url, headers=headers, data=data)
        #########################################
        for content in r.json()['Comments']:
            for replied in content['beReplied']:
                print "被回复人：", replied['user']['nickname'].encode('utf-8')
                print "被回复评论：", replied['content'].encode('utf-8')
            print "评论：", content['content'].encode('utf-8')
            print "昵称：", content['user']['nickname'].encode('utf-8')
        ################################ 返回的部分做个标记
        # 把专辑-歌曲-评论 存入数据库

