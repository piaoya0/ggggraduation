#coding:utf8

import requests
import time
import multiprocessing
# from multiprocessing import Pool as propool
# from multiprocessing.dummy import Pool as thrpool
# from multiprocessing import cpu_count

from comments import getalbum, getcomments, sql
from ip import IPpool



if __name__ == "__main__":
    req = requests.session()
    l = ["1001","1002","1003","2001","2002","2003","6001","6002","6003","7001","7002","7003","4001","4002","4003"]
    cpu = multiprocessing.cpu_count()
    process = multiprocessing.Pool(processes=cpu)
    for x in l:
        # ip = IPpool.IPpool("./ip/ip.txt")
        artist = getalbum.GetArtist(req, x)
        process.apply_async(artist._getArtist(), ())
    process.close()
    process.join()

