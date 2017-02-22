# encoding:UTF-8
import urllib.request
import re


def getHtml(url):
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')
    return data


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imgs = re.findall(imgre, html)
    x = 0
    for img in imgs:
        print(img)
        urllib.request.urlretrieve(img, 'imgs\\%d.jpg' % x)
        x += 1


getImg(getHtml("http://tieba.baidu.com/p/2460150866"))
