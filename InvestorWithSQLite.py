import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import sqlite3 as lite

url = 'http://www.twse.com.tw/ch/trading/fund/BFI82U/BFI82U.php?report1=day&input_date={0}&mSubmit=%ACd%B8%DF&yr=2016&w_date=20160627&m_date=20160601'
sql = "insert into InvestorTradingValue(item, total_buy, total_sell, difference, date) values(?,?,?,?,?)"

def money_conversion(input_ele):
    return int(''.join(input_ele.split(',')))

def getTradeValue(cur, today):
    dayary = str(today).split('-')
    dt = '%2F'.join([str(int(dayary[0]) - 1911), dayary[1], dayary[2]])
    res = requests.get(url.format(dt))
    res.encoding = 'big5'
    soup = BeautifulSoup(res.text, "html.parser")
    for tr in soup.select('.board_trad tr')[2:]:
        td = tr.select('td')
        ret = [td[0].text, money_conversion(td[1].text), money_conversion(td[2].text), money_conversion(td[3].text), today]
        cur.execute(sql, ret)
        
con = lite.connect('finance.sqlite')
cur = con.cursor()
   

today = date.today()
for i in range(1,8) :
    today = today + timedelta(days=-1)
    getTradeValue(cur, today)
con.commit()
con.close()
