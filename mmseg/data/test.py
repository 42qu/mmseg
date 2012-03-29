#coding:utf-8
from __future__ import with_statement
word_set = set()
with open("words.dic") as  words:
    for i in words:

        i = i.strip()
        if not i:continue
        b = i.split()
        b = b[-1]
        word_set.add(b)
for i in word_set:
    if i == "这一":
        continue
    do_print = True
    for j in ("是", "的", "了", "有"):
        if i.endswith(j):
            do_print = False
            break
    if do_print:
    #    if i.find("这")>= 0 and len(i.split()[1])<= 6:
    #        do_print = False
        if i.startswith("在"):
            do_print = False
            if i[3:] not in word_set:
                if not len(i)<= 12:
                    do_print = True
    #    if len(i)>= 21:
    #        print i
    if do_print:
        i_len = len(i.decode("utf-8"))
        if not i_len>9:
            print i_len, i

