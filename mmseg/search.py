#coding:utf-8
from collections import defaultdict
from __init__ import seg_txt
from word2 import WORD2

SMALLCHAR = set(
(u'很', u'则', u'该', u'次', u'给', u'又', u'里', u'号', u'着', u'名', u'可', u'更', u'由', u'下', u'至', u'或', u'多', u'大', u'新', u'并', u'让', u'她', u'已', u'向', u'其', u'股', u'点', u'们', u'所', u'会', u'要', u'于', u'前', u'来', u'万', u'比', u'只', u'及', u'地', u'队', u'个', u'不', u'说', u'第', u'元', u'人', u'一', u'分', u'被', u'我', u'这', u'到', u'都', u'从', u'等', u'时', u'以', u'上', u'后', u'就', u'将', u'而', u'还', u'他', u'但', u'对', u'也', u'与', u'为', u'中', u'年', u'月', u'日', u'有', u'和', u'是', u'在', u'了', u'的', )
)

STOPWORD = set(u"的了是在有而以但一我你他它个啊这")

def seg_txt2(txt):
    for i in seg_txt(txt):
        i = i.lower()
        if len(i) > 3:
            yield i
        else:
            i = i.decode("utf-8","ignore")
            if len(i) == 1:
                if u"一" <= i <= u"龥" and i not in STOPWORD:
                    yield i
            else:
                yield i 

def seg_txt_2_dict(txt):
    result = defaultdict(int)
    for word in seg_txt_search(txt):
        result[word] += 1
    return result

def word_len2(s):
    tmp = [u""]
    for i in s:
        if u"一" <= i <= u"龥" and i not in STOPWORD:
            tmp[-1] += i
        elif tmp[-1]:
            tmp.append(u"")
    result = []
    tmp_word = []
    for y in tmp:
        if y:
            for i in xrange(len(y)-1):
                w = y[i:i+2]
                if w in WORD2:
                  #  if len(tmp) >= 2:
                    result.extend(tmp_word)
                    result.append(w)
                    tmp_word = []
                else:
                    tmp_word.append(w)
            #if len(tmp_word) >= 2:
            result.extend(tmp_word)
            if len(y) <= 5:
                result.append(y)
    return result

def seg_title_search(txt):
    result = []
    buffer = []
    for word in seg_txt(txt):
        word = word.decode("utf-8", "ignore")

        if len(word) == 1:
            buffer.append(word)
        else:
            for i in buffer:
                result.append(i)
            if len(buffer) > 1:
                result.extend(word_len2("".join(buffer)))
            buffer = []
            if len(word) <= 16:
                word = word.lower()
                utf8_word = word.encode("utf-8", "ignore")
                if utf8_word.isalnum():
                    result.append(word)
                else:
                    for i in word:
                        result.append(i)
                    if len(word) <= 2:
                        result.append(utf8_word)
                    else:
                        result.extend(word_len2(word))

    if len(buffer) > 1:
        result.extend(word_len2("".join(buffer)))
    elif buffer:
        if u"一" <= buffer[0] <= u"龥":
            if buffer[0] not in SMALLCHAR:
                result.append(buffer[0])


    result = [i.encode("utf-8", "ignore") if type(i) is unicode else i for i in result]
#    txt = txt.decode("utf-8", "ignore")

    return result

def seg_keyword_search(txt):
    return  sorted(seg_title_search(txt),key=lambda x:-len(x))

def seg_txt_search(txt):
    result = []
    buffer = []
    def _():
        if len(buffer) > 1:
            result.extend(word_len2(u"".join(buffer)))
        elif buffer:
            if u"一" <= buffer[0] <= u"龥":
                if buffer[0] not in SMALLCHAR:
                    result.append(buffer[0])

    for word in seg_txt(txt):
        word = word.decode("utf-8", "ignore")
        if len(word) == 1:
            buffer.append(word)
        else:
            _()
            buffer = []
            if len(word) <= 16:
                word = word.lower()
                utf8_word = word.encode("utf-8", "ignore")
                if utf8_word.isalnum():
                    result.append(word)
                elif len(word) <= 2:
                    result.append(utf8_word)
                else:
                    result.extend(word_len2(word))

    _()

    result = [i.encode("utf-8", "ignore") if type(i) is unicode else i for i in result]

    return result



if __name__ == "__main__":
    for i in word_len2("是：张无忌"):
        print i
