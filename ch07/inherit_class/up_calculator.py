from ch07.myclass.calculator import Calculator

class MoreCalculator(Calculator):
    def pow(self):
        result = self.x ** self.y
        return result

    def div(self):
        if self.y == 0:
            return 0
        else:
            return self.x / self.y

cal = MoreCalculator(4, 0)
print(cal.pow())
print(cal.mul())
print(cal.div())
print(cal.add())
print(cal.sub())