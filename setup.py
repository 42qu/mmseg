#coding:utf-8



import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from  setuptools import   find_packages
from distutils.core import Extension, setup
setup(
    name='mmseg',
    description='MMseg中文分词 Chinese Segment On MMSeg Algorithm',
    version='1.3.0',
    author_email='zsp007@gmail.com',
    packages=find_packages(),
package_data={
    'mmseg.data':[ '*.dic',], 
    'mmseg.mmseg_cpp':[ 'mmseg_cpp/*.h' ],
},
long_description="""
MMseg中文分词 Chinese Segment On MMSeg Algorithm
-------------------------------
original edition

pymmseg-cpp
    by pluskid
    http://code.google.com/p/pymmseg-cpp/

This package is Chinese Segment , I think only chinese need it, so the description is chinese . 

If you have interesting , have a look a the original edition

-------------------------------

全文索引用，配合 xapian ( http://xapian.org/ ) 可以很方便的做全文索引

~:python -m mmseg.search
----------
哈尔罗杰历险记(套)
哈尔
罗杰
历险
历险记
----------
卡拉马佐夫兄弟
卡拉
马
佐夫
兄弟
----------
银河英雄传说
银河
英雄
传说
银河英雄传说
----------
张无忌在光明顶
无忌
张无忌
光明
光明顶
----------
韦帅望的江湖(Ⅲ众望所归)
韦帅
帅望
韦帅望
江湖
众望
望所
所归
众望所归
----------
少年韦帅望之童年结束了
少年
韦帅
帅望
望之
韦帅望之
童年
结束
----------
　　 　晋江文学网站驻站作家，已出版多部作品。
晋江
文学
网站
文学网站
驻站
作家
出版
多部
作品
-------------------------------
分词用，适用于聚类等等

from mmseg import seg_txt
for i in seg_txt("最主要的更动是：张无忌最后没有选定自己的配偶。"):
    print i

-------------------------------
配合xapian做索引

#coding:utf-8
#!/usr/bin/env python

import xapian
import sys
import string
from collections import defaultdict

from mmseg.search import seg_txt_search,seg_txt_2_dict

import xapian
SEARCH_DB = xapian.WritableDatabase(DBPATH, xapian.DB_CREATE_OR_OPEN)
SEARCH_ENQUIRE = xapian.Enquire(SEARCH_DB)

def index_txt(id, txt):
    doc = xapian.Document()
    for word, value in seg_txt_2_dict(txt).iteritems():
        doc.add_term(word, value)
    key = ":%s"%id
    doc.add_term(key)
    SEARCH_DB.replace_document(key, doc)


def flush_db():
    SEARCH_DB.flush()
    
if __name__ == "__main__":
    txt = \"\"\"
    治安署地最高长官站在街头，皱眉看着一队近卫军飞快地走过，他心中满是疑惑，立刻回到了治安署里地办公室，然后喊来了自己地一个部下，让他立刻去军方统帅部请示一下.
    \"\"\"

    index_txt(1, txt)
    flush_db()

-------------------------------
配合xapian做搜索

#coding:utf-8
from mmseg.search import seg_txt_search,seg_txt_2_dict

import xapian
SEARCH_DB = xapian.WritableDatabase(DBPATH, xapian.DB_CREATE_OR_OPEN)
SEARCH_ENQUIRE = xapian.Enquire(SEARCH_DB)

def search(keywords, offset=0, limit=35, enquire=SEARCH_ENQUIRE):
    query_list = []
    for word, value in seg_txt_2_dict(keywords).iteritems():
        query = xapian.Query(word, value)
        query_list.append(query)
    if len(query_list) != 1:
        query = xapian.Query(xapian.Query.OP_AND, query_list)
    else: 
        query = query_list[0]

    enquire.set_query(query)
    matches = enquire.get_mset(offset, limit, None)
    return matches

if __name__ == "__main__":
    matches = search( "治安")

    # Display the results.
    print "%i results found." % matches.get_matches_estimated()
    print "Results 1-%i:" % matches.size()

    for m in matches:
        print "%i: %i%% docid=%i [%s]" % (m.rank + 1, m.percent, m.docid, m.document.get_data())
-------------------------------
张沈鹏(zsp007@gmail.com) 修改版 rmmseg-cpp

""",
ext_modules=[
    Extension(
    'mmseg',
"""
mmseg/mmseg_cpp/algor.cpp  mmseg/mmseg_cpp/dict.cpp  mmseg/mmseg_cpp/memory.cpp  mmseg/mmseg_cpp/mmseg.cpp
""".split(),
    extra_compile_args=['-O3'],
    depends="""
mmseg/mmseg_cpp/algor.h  mmseg/mmseg_cpp/dict.h    mmseg/mmseg_cpp/rules.h
mmseg/mmseg_cpp/word.h
mmseg/mmseg_cpp/chunk.h  mmseg/mmseg_cpp/memory.h  mmseg/mmseg_cpp/token.h
    """.split(),
    )
],
)

