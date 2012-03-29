#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from collections import defaultdict
from os.path import dirname, abspath, join

PREFIX = dirname(abspath(__file__))

WORD_LIST = []

with open(join(PREFIX,'words.dic')) as words:
    for line in words:
        word = line.strip().split(" ",1)[1].decode("utf-8")
        if len(word) == 2:
            WORD_LIST.append(word)

with open(join(dirname(PREFIX),"word2.py"),"w") as word_in_word:
    word_in_word.write("#coding:utf-8\n")
    word_in_word.write("WORD2 = set((\n")
    for i in WORD_LIST:
        word_in_word.write("u'%s',\n"%i)

    word_in_word.write("\n))")




