# 주가 찾아오기

from urllib import request
from bs4 import BeautifulSoup


def getcontent(item_code):
    url = 'https://finance.naver.com/item/main.nhn?code=' + item_code
    html = request.urlopen(url)
    content = BeautifulSoup(html, 'html.parser')
    return content


def getprice(item_code):
    content = getcontent(item_code)
    no_today = content.find('p', {"class":"no_today"})
    price = no_today.find('span', {'class':'blind'})
    return price

# 삼성 - 005930 , 카카오 - 035720 , 네이버 - 035420
samsung = getprice("005930")
kakao = getprice("035720")
naver = getprice("035420")


print("samsung : {}원".format(samsung.text))
print("kakao : {}원".format(kakao.text))
print("naver : {}원".format(naver.text))