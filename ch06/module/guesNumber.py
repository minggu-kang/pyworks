# 숫자 추측 게임
import random as r

com = r.randint(1,30)  # 컴이 추측 숫자
while True:
    guess = int(input("맞혀보세요 (1~30) : ")) # 사용자가 추측 숫   
    if guess > com:
        print("너무 커요!!")
    elif guess < com:
        print("너무 작아요!")
    else:
        print("정답!!")
        break
        
        
