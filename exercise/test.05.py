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