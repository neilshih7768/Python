import requests
from bs4 import BeautifulSoup
payload = {
    'from':'/bbs/gossiping/index.html',
    'yes':'yes'
}
rs = requests.session()
res = rs.post('https://www.ptt.cc/ask/over18', data=payload)
res = rs.get("https://www.ptt.cc/bbs/gossiping/index.html")
soup = BeautifulSoup(res.text, "html.parser")
for entry in soup.select('.r-ent'):
    print entry.select('.title')[0].text, entry.select('.date')[0].text, entry.select('.author')[0].text
