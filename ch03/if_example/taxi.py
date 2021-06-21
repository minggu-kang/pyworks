# 조건 : 현금 , 카드 보유시 택시 / 아니면 걷는다.

money = 3000
card = True

if money >= 4000 or not card:
    print("택시를 탄다")
else:
    print("걸어간다")


pocket = ['paper','스마트폰','money']
if 'money' in pocket :
    print("택시를 탄다")
else:
    print("걸어간다")
