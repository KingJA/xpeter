# encoding:UTF-8
import urllib.request
import re
import codecs


def getHtml(url):
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')
    return data


def getImg(html, page):
    reg = r'class="w2 readContent" original-title=\'(.*?)\'>'
    imgre = re.compile(reg)
    texts = re.findall(imgre, html)
    x = (page - 1) * 10
    f = codecs.open('text\\t1.txt', 'a', 'utf-8')
    for text in texts:
        content = "#%d" % x + text + "\n"
        print(content)
        f.write(content)
        x += 1
    f.close()


for i in range(1, 98):
    getImg(getHtml("http://www.aizhufu.cn/duanxinku/column/67/%d.html" % i), i)
