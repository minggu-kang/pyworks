
def oneup2(x):
    return x + 1

# 매개변수가 1개있는 lambda 함수 ( 익명 함수 )
# 1 증가 함수

oneup1 = lambda x : x + 1

print(oneup1(2))   # lambda 함수 호출

print((lambda x : x + 1)(2))  #lambda 한줄식

#print(oneup2(2))  #일반 함수 호출


# 3의 배수 계산 함수

times = lambda n : n * 3

print(times(2))
print((lambda n : n * 3)(2))