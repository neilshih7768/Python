import requests
from bs4 import BeautifulSoup
res = requests.get("https://tw.search.bid.yahoo.com/search/auction/product;_ylt=AlvtFuRIh6qUMjnjbl9q2R1yFbN8;_ylv=3?p=%E7%A7%98%E5%A2%83%E6%8E%A2%E9%9A%AA+%E7%89%B9%E5%88%A5&kw=%E7%A7%98%E5%A2%83%E6%8E%A2%E9%9A%AA+%E7%89%B9%E5%88%A5&property=auction&sub_property=auction&srch=product&aoffset=0&poffset=0&pg=1&sort=curp&nst=1&act=srp&rescheck=1")
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, "html.parser")
for item in soup.select('.srp-pddetail'):
    print item.select('.yui3-u')[0].text
