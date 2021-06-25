# Person 클래스 생성과 사용

class Person:
    def __init__(self): # 초기자(생성자 함수)
        self.name = "철수"
        self.age = "30"

p = Person() # 객체변수 - 인스턴스

print(p.name)
print(p.age)