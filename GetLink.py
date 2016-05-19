import requests
from bs4 import BeautifulSoup
Target = "https://www.miramarcinemas.com.tw/"
res = requests.get(Target)
soup = BeautifulSoup(res.text, "html.parser")
for navi in soup.select('.index-nav'):
    for link in navi.findAll('a'):
        url = "%s%s" % (Target,link.get('href'))
        print url