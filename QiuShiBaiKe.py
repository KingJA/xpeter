import urllib.request
import re
import mysql.connector
import time


class QiuShiBaiKe:
    # 初始化
    def __init__(self):
        self.pageIndex = 1
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
                        'Referer': 'http://www.qiushibaike.com/text/'}  # 加Referer 模拟真实访问，防盗链
        self.conn = mysql.connector.connect(user='root', password='', database='qsbk')
        self.cursor = self.conn.cursor()

    # 获取html
    def getPageHtml(self, pageIndex):
        url = "http://www.qiushibaike.com/text/page/%d" % pageIndex
        req = urllib.request.Request(url)
        for i in self.headers:
            req.add_header(i, self.headers[i])
        html = urllib.request.urlopen(req).read().decode("utf8")
        return html

    # 获取所需数据-单线程
    def getData(self, html):
        reg = r'<div class="author clearfix">.*?<a.*?>.*?<img src="(.*?)" alt="(.*?)"/>.*?</a>.*?<a.*?>.*?<h2>.*?</h2>.*?</a>.*?<div.*?>.*?</div>.*?</div>.*?<a.*?>.*?<div class="content">.*?<span>(.*?)</span>'
        pattern = re.compile(reg, re.S)
        duanzis = re.findall(pattern, html)
        for duanzi in duanzis:
            print(duanzi[0], "\n", duanzi[1], "\n", duanzi[2])
            self.cursor.execute('insert into duanzi (icon,author ,content) values (%s, %s, %s)',
                                [duanzi[0], duanzi[1], duanzi[2]])
            self.conn.commit()
        self.cursor.close()

    def start(self):
        print("开始爬取糗事百科")
        time1 = time.time()
        self.getData(self.getPageHtml(1))
        time2 = time.time()
        print('单线程耗时 : ' + str(time2 - time1) + ' s')


baike = QiuShiBaiKe()
print(baike.start())
