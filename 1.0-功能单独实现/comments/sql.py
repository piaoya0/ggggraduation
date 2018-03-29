import MySQLdb

class Sql:

    def __init__(self):
        self.db = MySQLdb.connect("localhost","root","123456","music",charset='utf8')
        self.conn = self.db.cursor()

    def _getfield(self, databasename):
        l = ""
        info = "SHOW COLUMNS FROM " + databasename
        self.conn.execute(info)
        re = self.conn.fetchall()

        for qwe in re:
            l = l + ',' + qwe[0]
        l = '(' + l[1:] + ')'
        t = '(' + ','.join(["%s" for x in re]) + ')'
        return l, t

    def _save(self, databasename, *args):
        field, f = self._getfield(databasename)
        sql = "insert into " + databasename + field + " values" + f
        self.conn.executemany(sql, args)
        self.db.commit()
