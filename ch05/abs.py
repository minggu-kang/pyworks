# abs() 직접 정의

# 절대값 알고리즘1
import math #내장함수 math 모듈 호출

def abs_sign(x):

    if x<0 :
        return  -x
    else:
        return x
n1 = abs_sign(-3)
print(n1)


# 절대값2
def abs_square(x):
    y = x * x

    return math.sqrt(y) # 제곱근함

n2 = abs_square(-5)
print(n2)
