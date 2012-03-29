from collectins
with open('/home/z32/down/mmseg-1.2.5/mmseg/data/words.dic') as words:
    for line in words:
        word = line.strip().split(" ",1)[1]

