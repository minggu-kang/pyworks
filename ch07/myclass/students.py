class Student:
    def __init__(self):
        self.name = input("이름 : ")
        self.sid = int(input("학번 : "))

    def showinfo(self):
        print(self.sid, self.name)


li = []
for i in range(3):
    li.append(Student())

for i in li:
    i.showinfo()