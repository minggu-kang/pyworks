
'''
# Q1 ~Q2

class Calculator:
    def __init__(self):
        self.value = 0


    def add(self, val):
        self.value += val
        return self.value
class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val
        return self.value
class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value


#부모 클래스의 인스턴스
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)



cal2 = MaxLimitCalculator()
print(cal2.add(50))
print(cal2.add(60))

print(cal2.value)
'''

#Q3 >콘솔

# Q4

li = [1, -2, 3, -5, 8, -3]
'''
def positive(l)
    result = []
    for i in l:
        if i >0:
            result.append(i)
    :return result
    
    
'''
print(list(filter(lambda x : x >= 0,li)))


# Q5 콘솔

int(0xea)

# Q6

def times(a):
    a2 = []
    for i in a:
        a2.append(i*3)
    return a2
li = [1,2,3,4]
li2 = times(li)
print(li2)

print(list(map(lambda x: x*3,[1,2,3,4])))


# Q7
# 함수사용(max값)
def find_max(li):
    max = li[0]     # -8
    for i in li:
        if max < i:
            max = i
    return max
    '''
    n = len(li)
    for i in range(1,n):
        if max < li[i]:
            max = li[i]
            
    return max
    '''

a = [-8, 2, 7, 5, -3, 5, 0, 1]
max2 = find_max(a)
print(max2)

# Q7 최댓값 + 최솟값
'''
max = max(a)
min = min(a)

#max(a) + min(a)
print(max + min)
'''

# Q8
# 콘솔

b = round(17/3,4)
print(b)


# Q12
import time
import datetime

now1 = time.strftime("%Y/%m/%d %H:%M:%S")
print(now1)

now2 = datetime.datetime.now()
print(now2.strftime("%Y/%m/%d %H:%M:%S"))