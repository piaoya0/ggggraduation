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

    def __get_id(self, city):
        sql = "select area_id from area where area_name=(%s)"
        self.cursor.execute(sql, (city,))
        return self.cursor.fetchall()

    def insert(self, data, level = 2):
        if isinstance(data, list):
            sql = "insert into area (area_name, area_level) values (%s, 1)"
            for x in data:
                self.cursor.execute(sql, (x,))
        if isinstance(data, dict):
            sql = "insert into area (area_name, area_level, upid) values (%s, %s, %s)"
            for key in data:
                # print [key]
                area_id = self.__get_id(key)[0][0]
                for city in data[key]:
                    self.cursor.execute(sql, (city, level, area_id))

        self.test.commit()

    def update(self, data):
        sql = "UPDATE area SET lng=(%s),lat=(%s) WHERE area_name=(%s) AND area_level = 2"
        for key in data:
            value = [float(a) for a in data[key]]
            value.append(key)
            # print value
            self.cursor.execute(sql, value)

        self.test.commit()

    def get_nw(self):
        sql = "select area_name, lng, lat from area where area_level = 2"
        self.cursor.execute(sql)
        value = self.cursor.fetchall()
        return value


    def close(self):
        self.cursor.close()
        self.test.close()


a = sql('cs')
data = a.get_nw()

for x in data:
    # print '"' + x[0].encode('utf8') + '":', list(x[1:]),","
    x = '{ name: "' + x[0].encode('utf8') + '", value: ' + str(random.randint(0, 150)) + ' },'
    print x