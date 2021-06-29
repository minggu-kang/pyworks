# kbo 구단을 1개씩 랜덤 추출
import random
try:
    f = open("c:/pyfile/2021kbo.txt","r")
    data =f.read().split()
    team = random.choice(data)  #숫자 >random.randint()
                                #문자 >random.choice()
    print(team)
    f.close()
except FileNotFoundError as e:
    print(e)