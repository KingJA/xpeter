# coding=gbk
import codecs

f = codecs.open('text\\t1.txt', 'a', 'utf-8')
# f.write(u'����')
s = '����'
f.write(s)
f.close()
