import requests
from bs4 import BeautifulSoup

headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
	'Connection':'keep-alive',
	'Cookie':'PSID_WEB=6a2tbfqcj9f80ek1bktuqqlov7; ckBUY_item18UP=18UP; __gads=ID=dc9a1f71e234f8ef:T=1449622861:S=ALNI_MY7R3cehjIJcZ7DompGCILy7WGxgQ; __auc=f3733328151389b7a182e2a601f; ckBH_lastBoard=11177@@@%25u79D8%25u5883%25u63A2%25u96AA%2520%25u7CFB%25u5217%2C%2C%2C24460@@@%25u6E6F%25u59C6%25u514B%25u862D%25u897F%25uFF1A%25u5168%25u5883%25u5C01%25u9396%2C%2C%2C08859@@@%25u516C%25u4E3B%25u4E4B%25u5195%25u3001%25u5967%25u4E01%25u9818%25u57DF%2C%2C%2C30069@@@%25u795E%25u5947%25u5BF6%25u8C9D%2520%25u6230%25u68CB%25u5927%25u5E2B%2C%2C%2C29618@@@%25u904A%25u6232%25u738B%2520%25u6C7A%25u9B25%25u9023%25u7DDA%2C%2C%2C24044@@@%25u7210%25u77F3%25u6230%25u8A18%25uFF1A%25u9B54%25u7378%25u82F1%25u96C4%25u50B3%2C%2C%2C00725@@@%25u904A%25u6232%25u738B%2520%25u7CFB%25u5217%2C%2C%2C28833@@@%25u6578%25u78BC%25u5BF6%25u8C9D%2520Linkz%2C%2C%2C46485@@@%25u7532%25u9435%25u57CE%25u7684%25u5361%25u5DF4%25u5167%25u91CC%2C%2C%2C29730@@@BBTAN; BAHAID=neilshih; BAHANICK=%E7%85%89%E7%8D%84%E6%B3%95%E9%A8%8E%E7%B4%8D%E5%A8%81; BAHARUNE=0510ef683c73f942c4619370f4b26a695295ba1b52b9a19e14013dd36b3d7b15a1c1de01172b4e756970; BAHALV=28; BAHAFLT=1081056248; ckFORUM_setting=113112222121113223; ckGilu=0; ckSERVER=buy.gamer.com.tw; ckFORUM_bsn=0; ckBUY_FOOTPRINT=0%3A25%3A0%3Agc1%3D25%26tnum%3D157%26page%3D1; _ga=GA1.3.1572971602.1448353692; ckBahaAd=8--0-00---------',
	'Host':'buy.gamer.com.tw',
	'Referer':'http://buy.gamer.com.tw/indexList.php?gc1=25',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

Target = "http://buy.gamer.com.tw/atmHistory.php?_t=f2e7911e830f28393778acce06668b37"
res = requests.get(Target, headers = headers)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, "html.parser")
#print soup.select('.ES-lbox7')
print res.text

