# encoding:UTF-8
import urllib.request
import re
import uuid


def getHtml(url):
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')
    return data


def getImg(html, page):
    reg = r'data-original="(.*?)" width='
    imgre = re.compile(reg)
    imgs = re.findall(imgre, html)
    x = (page - 1) * 10
    for img in imgs:
        print('% d- % s ' % (x, img))
        urllib.request.urlretrieve(img, 'shetuwang\\people\\%d.jpg' % uuid.uuid1())
        x += 1


for i in range(1, 400):
    getImg(getHtml("http://699pic.com/people-%d.html" % i), i)
