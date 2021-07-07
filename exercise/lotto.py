import random as r
'''
dice = []
for i in range(0, 10):
    n = r.randint(1,6)
    dice.append(n)

print(dice)
'''

# 로또 번호 생성

lotto = []

while len(lotto) < 6:
    n = r.randint(1,45)
    if n not in lotto: # 중복 숫자 방지
        lotto.append(n)


print(lotto)
