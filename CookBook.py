import requests
from bs4 import BeautifulSoup
res = requests.get("http://www.xinshipu.com/zuofa/49391")
soup = BeautifulSoup(res.text, "html.parser")
#print soup
reup = soup.select('.content')[0]
#print reup
print reup.select('.font16.h47.tc.cg1')[0].text

pm12 = soup.select('span')[46].text
print pm12, 'Score'
#for index, element in enumerate(pm12):
#    print '%d %s' % (index, element)