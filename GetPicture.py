import requests
from bs4 import BeautifulSoup
res = requests.get("http://www.gamebase.com.tw/forum/64172/topic/96278769/1")
soup = BeautifulSoup(res.text, "html.parser")
for img in soup.select('.img'):
    fname = img['src'].split('/')[-1]
    res2 = requests.get(img['src'], stream=True)
    f = open('Pictures//' + fname, 'wb')
    shutil.copyfileobj(res2.raw, f)
    f.close()
    del res2