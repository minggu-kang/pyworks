# 삼성전자주가 찾아오기

from urllib import request
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/item/main.nhn?code=005930'


def getcontent():
    html = request.urlopen(url)
    content = BeautifulSoup(html,'html.parser')
    return content

contents = getcontent()
no_today = contents.find('p',{'class':'no_today'})

#print(no_today)
price = no_today.find('span',{'class':'blind'}) #blind 는 웹에서 표시되지 않음

#print(price)

print("삼성전자 주가 : {}원".format(price.text))
