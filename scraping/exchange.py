from urllib import request
from bs4 import BeautifulSoup

# find 로 찾기
html = request.urlopen("https://finance.naver.com/marketindex/")
code = html.read().decode('euc-kr', 'replace').encode('utf-8', 'replace')
contents = BeautifulSoup(code, 'html.parser')
ul = contents.find('div', {'class': 'market_data'})
lis = ul.find_all('li')

for li in lis:
    ex = li.find('span', {'class': 'blind'})        #환율 종류
   #ex = li.select_one('span.blind')                #환율 종류

    val = li.find('span', {'class': 'value'})       #환율 지수
   #val = li.select_one('span.vlue')                #환율 지수
    #print(ex)
    #print(val)
    print(ex.string.split(' '[-1]), ':', val.string)