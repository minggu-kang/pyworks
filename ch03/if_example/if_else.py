# 조건 : 나이가 15세 이상이면 '드라마 관람가' , 아니면 '관람 불가'

age = int(input("나이를 입력해 주세요 :" ))
if age >= 15:
    print("드라마 관람가")
else:
    print("관람 불가")
    
print("나이는 %d 세입니다" % age)
