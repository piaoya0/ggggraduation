#-*-coding:utf8-*-

import jieba.posseg as pseg


class make_word(object):
    # self.word = {}

    def __get_res_list(self, string):
        res = pseg.cut(string)
        return res

    def _get_fre(self,data):
        word_dict = {}
        for s in data:
            for word, flag in self.__get_res_list(s):
                word = word.encode('utf8')
                if word in word_dict:
                    word_dict[word][1] += 1
                else:
                    word_dict[word] = [flag,1]
        return word_dict
