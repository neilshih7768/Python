import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.ptt.cc/bbs/Food/index.html")
soup = BeautifulSoup(res.text, "html.parser")
for entry in soup.select('.r-ent'):
    print entry.select('.title')[0].text, entry.select('.date')[0].text, entry.select('.author')[0].text