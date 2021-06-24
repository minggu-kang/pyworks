# vartest 전역 변수와 지역 변수

a= 1 # 전역변수
def vartest(a):
    #global a
    a += 1 # a : 지역변수
    return a


print(vartest(a))
print(a)

