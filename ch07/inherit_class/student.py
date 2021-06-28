from person import Person

# Student 클래스
class Student(Person):
    def __init__(self,name,age, stuid):
        super().__init__(name, age)
        self.stuid = stuid

    def showinfo(self):
        print(self.name, self.age, self.stuid)

s1 = Student("철수", 19, 101)
s1.showinfo()
s2 = Student("영희", 18, 102)
s2.showinfo()