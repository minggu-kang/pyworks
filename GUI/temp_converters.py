# 온도 변환기 app

from tkinter import *
from GUI.converters import Converters

class App:
    def __init__(self, master):
        self.conv = Converters('C', 'F', 1.8, 32)
        frame = Frame(master)
        frame.pack()

        #입력
        Label(frame, text='deg C').grid(row=0, column=0)
        self.c = DoubleVar()        #실수형 변수 선언
        Entry(frame, textvariable=self.c).grid(row=0, column=1)

        #출력
        Label(frame, text='def F').grid(row=1, column=0)
        self.f = DoubleVar()
        Label(frame, textvariable=self.f).grid(row=1, column=1)


        #버튼
        Button(frame, text="변환", command=self.convert).grid(row=2,columnspan=2)

    def convert(self):
        c = self.c.get()        # .get() = deg C의 값 가져오기
        c_f = str(self.conv.convert(c))[0:5]      # c -> f 계산값      //   str 문자형 변환후 [:] 인덱싱
        self.f.set(c_f)           #.set() = def F 로 내보내기


root = Tk()
root.title("온도 변환기")
app=App(root)



root.mainloop()