import requests as rq
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/NBA/index.html"  # PTT NBA 板
response = rq.get(url)  # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

# 一些屬性或方法
print(soup.title)  # 把 tag 抓出來
print("---")
print(soup.title.name)  # 把 title 的 tag 名稱抓出來
print("---")
print(soup.title.string)  # 把 title tag 的內容欻出來
print("---")
print(soup.title.parent.name)  # title tag 的上一層 tag
print("---")
print(soup.a)  # 把第一個 <a></a> 抓出來
print("---")
print(soup.find_all("a"))  # 把所有的 <a></a> 抓出來
