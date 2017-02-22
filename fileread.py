# coding=gbk
import codecs

f = codecs.open('text\\t1.txt', 'a', 'utf-8')
# f.write(u'中文')
s = '中文'
f.write(s)
f.close()
