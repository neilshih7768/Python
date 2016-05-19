import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.miramarcinemas.com.tw/timetable.aspx?place=1")
soup = BeautifulSoup(res.text, "html.parser")
for movie in soup.select('.time-content'):
    print movie.h3.text
    print movie.h4.text
    for date in movie.select('dl'):
        print date.dt.text,
        for time in date.select('li'):
            print time.text,
        print
    print