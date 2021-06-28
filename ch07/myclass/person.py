# Person 클래스 생성과 사용

class Person:
    def __init__(self): # 초기자(생성자 함수)
        self.__name = "철수"
        self.__age = "30"


    def getname(self):      #매개 변수에 직접 접근하지 않도록 get()을 사용
        return self.__name


    def getage(self):
        return self.__age


p = Person() # 객체변수 - 인스턴스

p.name = "영희"
print(p.getname(),p.getage())