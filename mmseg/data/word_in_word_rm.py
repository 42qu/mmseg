#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from collections import defaultdict
from os.path import dirname, abspath, join

PREFIX = dirname(abspath(__file__))

WORD2 = defaultdict(set)
WORD_LIST = []

with open(join(PREFIX,'words.dic')) as words:
    for line in words:
        word = line.strip().split(" ",1)[1].decode("utf-8")
        if len(word) > 2:
            WORD_LIST.append(word)
            for i in xrange(2,len(word)+1):
                WORD2[word[i-2:i]].add(word)
        else:
            WORD2[word].add(word)

WORD2WORD = defaultdict(set)

for word in WORD_LIST:
    for i in xrange(2,len(word)+1):
        t = word[i-2:i]
        for j in WORD2[t]:
            if j in word and j!=word:
                WORD2WORD[word].add(j)

with open(join(PREFIX,'words.dic')) as words:
    for line in words:
        word = line.strip().split(" ",1)[1].decode("utf-8")
        if word not in WORD2WORD:
            print line.strip()

#def word_min(word):
#    if word not in WORD2WORD:
#        yield word
#    else:
#        for i in WORD2WORD[word]:
#            for j in word_min(i):
#                yield j
#                print word, j
#
#WORD2WORD2 = defaultdict(set)
#
#for i, word_set in WORD2WORD.iteritems():
#    r = set()
#    for j in word_set:
#        for k in word_min(j):
#            r.add(k)
#
#    WORD2WORD2[i] = r
#
#with open("word_in_word.py","w") as word_in_word:
#    word_in_word.write("#coding:utf-8\n")
#    word_in_word.write("WORD_IN_WORD = {\n")
#    
#    for k,v in WORD2WORD2.iteritems():
#        word_in_word.write('"%s": ( '%k)
#        for i in v:
#            word_in_word.write("'%s',"%i) 
#        word_in_word.write("),\n")
#
#    word_in_word.write("\n}")




