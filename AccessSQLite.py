import sqlite3 as lite
con = lite.connect('finance.sqlite')
cur = con.cursor()
#cur.execute("select * from InvestorTradingValue")
#ret = cur.fetchone()
#print ret
cur.execute("insert into InvestorTradingValue(item, total_buy, total_sell, difference, date) values('foreign', 80, 60, -10, '2016-6-27')")
con.commit()
con.close()
