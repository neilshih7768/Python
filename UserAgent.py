import requests
from bs4 import BeautifulSoup
head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
res = requests.get("https://buy.yungching.com.tw/region", headers = head)
#res.encoding = res.apparent_encoding

print res.text.encode('UTF-8', 'strict')
