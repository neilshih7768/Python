import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

url = 'http://www.twse.com.tw/ch/trading/fund/BFI82U/BFI82U.php?report1=day&input_date={0}&mSubmit=%ACd%B8%DF&yr=2016&w_date=20160627&m_date=20160601'

def getTradeValue(dt):
    res = requests.get(url.format(dt))
    res.encoding = 'big5'
    soup = BeautifulSoup(res.text)
    for tr in soup.select('.board_trad tr')[2:]:
        td = tr.select('td')
        print td[0].text, td[1].text, td[2].text, td[3].text
    print '\n'
        
today = date.today()
for i in range(1,8) :
    today = today + timedelta(days=-1)
    dayary = str(today).split('-')
    d = ' / '.join([str(int(dayary[0]) - 1911), dayary[1], dayary[2]])
    print d
    dt = '%2F'.join([str(int(dayary[0]) - 1911), dayary[1], dayary[2]])
    getTradeValue(dt)
