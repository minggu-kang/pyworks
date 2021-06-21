# 중첩 for 문
# 5행 5열


for i in range(1,6):
    for j in range(1,6):
        print("가", end=' ')
    print()

print("="*50)
#1부터 1씩 증가

for i in range(0,6):
    for j in range(1,6):
        num = i*5+j
        if i<2 :
            print(num,end='  ')
        else:
            print(num, end=' ')
    print()
