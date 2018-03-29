#coding:utf8
import requests
import json
import os
import base64
from Crypto.Cipher import AES
from pprint import pprint


class gethotComments():
    def __init__(self, id):
        self.id = id
    
    def aesEncrypt(self, text, secKey):
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        encryptor = AES.new(secKey, 2, '0102030405060708')
        ciphertext = encryptor.encrypt(text)
        ciphertext = base64.b64encode(ciphertext)
        return ciphertext

    def rsaEncrypt(self, text, pubKey, modulus):
        text = text[::-1]
        rs = int(text.encode('hex'), 16)**int(pubKey, 16) % int(modulus, 16)
        return format(rs, 'x').zfill(256)

    def createSecretKey(self, size):
        return (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(size))))[0:16]

    def gethotComments(self):
        url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_'+self.id+'?csrf_token='
        headers = {
            'Cookie': 'appver=1.5.0.75771;',
            'Referer': 'http://music.163.com/'
        }
        text = {
            'username': '邮箱',
            'password': '密码',
            'rememberLogin': 'true'
        }
        modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        nonce = '0CoJUm6Qyw8W8jud'
        pubKey = '010001'
        text = json.dumps(text)
        secKey = self.createSecretKey(16)
        encText = self.aesEncrypt(self.aesEncrypt(text, nonce), secKey)
        encSecKey = self.rsaEncrypt(secKey, pubKey, modulus)
        data = {
            'params': encText,
            'encSecKey': encSecKey
        }

        req = requests.post(url, headers=headers, data=data)
        #pprint(req.json())
        for content in req.json()['hotComments']:
            for replied in content['beReplied']:
                print "被回复人：", replied['user']['nickname'].encode('utf-8')
                print "被回复评论：", replied['content'].encode('utf-8')
            print "评论：", content['content'].encode('utf-8')
            print "昵称：", content['user']['nickname'].encode('utf-8')
            print
        #返回的部分

a = gethotComments('418603077')
a.gethotComments()