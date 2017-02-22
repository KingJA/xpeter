# encoding:UTF-8
import urllib.request

url = "http://www.qiushibaike.com/text/page/2"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)
