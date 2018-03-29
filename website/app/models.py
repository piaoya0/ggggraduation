#-*-coding:utf8-*-

class artisit(object):
    
    def __init__(self, value):
        self._artisit_id = value[0]
        self.name = value[1]
        self._jpg_path = value[2]
        self.__info = value[3]
    

class album(object):

    def __init__(self, value, artisit_obj = None):
        self._album_id = value[0]
        self.name = value[1]
        self.__info = value[2]
        self._jpg_path = value[3]
        self.artisit = artisit_obj

class music(object):
    
    def __init__(self, value, album = album_boj, artisit = artisit_obj):
        self.artist = artisit_obj
        self.album = album_boj
        self._music_id
        self.name
        self.iframe



