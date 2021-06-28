# 매개변수가 있는 상속
from person import Person

class Employee(Person):
    def __init__(self, name, age, empid):
        super().__init__(name, age)     #부모 매개변수는 super()를 사용
        self.empid = empid

    def getname(self):  #캡슐화 (정보은닉) - get()매서드 사용
        return self.name

    def getage(self):
        return self.age

    def getempid(self):
        return self.empid


e1 = Employee("철수", 30, 123467)
print("이름 : ", e1.getname())
print("나이 : ", e1.getage())
print("사번 : ", e1.getempid())

e2 = Employee("영희", 30, 474564)
print("이름 : ", e2.getname())
print("나이 : ", e2.getage())
print("사번 : ", e2.getempid())
