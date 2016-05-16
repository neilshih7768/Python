import requests
from bs4 import BeautifulSoup
res = requests.get("http://rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm")
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, "html.parser")
title = soup.select('.titleLeft')
decimal = soup.select('.decimal')
print '%11s %15.5s %15.5s' % ('Currency', "Buy", 'Sell')

for index, element in enumerate(title):
    print '%11s %15.5s %15.5s' % (element.text, decimal[index*4].text, decimal[index*4+1].text)
