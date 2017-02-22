from bs4 import BeautifulSoup
import requests

response = requests.get("http://www.aizhufu.cn/duanxinku/column/68/1.html")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.find("span", {"class": "w2 readContent"}))
