#-*-coding:utf-8-*-

from mysql import connector
import random

class sql:
    def __init__(self, database):
        try:
            self.test = connector.connect(host = 'localhost', user = 'root', password = '123456', database = database, charset = 'utf8')
            self.cursor = self.test.cursor()
        except Exception, e:
            print e

    def get_nw(self):
        sql = "select area_name, lng, lat from area where area_level = 2"
        self.cursor.execute(sql)
        value = self.cursor.fetchall()
        return value

    def get_usermap(self):
        sql = "SELECT area_name, count(`user`.user_uid) FROM area,`user` WHERE `user`.user_area = area.area_id GROUP BY area_id;"
        # FROM_UNIXTIME(bbs_threads.dateline)
        self.cursor.execute(sql)
        value = self.cursor.fetchall()
        return value

    def insert(self):
        sql = ""

    def close(self):
        self.cursor.close()
        self.test.close()
