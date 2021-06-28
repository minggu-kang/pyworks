# Person class - 맴버변수(name,age)
# Employee 클래스는 Person 을 상속 받음
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

class Employee(Person):
    pass

if __name__ == "__main__":
    c1 = Person("짱구",30)
    print(c1.name,c1.age)


    em = Employee("훈이",30)
    print(em.name, em.age)

    em2 = Employee("맹구",30)
    print(em2.name,em2.age
          )