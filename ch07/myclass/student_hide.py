# 학생 클래스 생성과 사용
class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

    def showinfo(self):
        print(self.sid, self.name)

if __name__ =="__main__":
    s1 = Student(1001, "철수")
    s1.showinfo()
    s2 = Student(1002, "영희")
    s2.showinfo()