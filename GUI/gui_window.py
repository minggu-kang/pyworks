 # 윈도우(폼) 만들기

from tkinter import *

root = Tk() # TK() 클래스의 객체 생성
root.title("window")
root.geometry("200x200+500+500")    #geometry("") - width x height  문자열로 써야함 + x좌표 + y 좌표

frame = Frame(root) # root 위에 위치하는 프레임
frame.pack()        # 레이아웃을 담당하는 pack() 메서드

# 문자열 출력 - Label 클래스
Label(frame, text="Hi").grid(row=0, column=0)   #grid(row=0, column=0) 레이아웃 위치( 행 열 )

#버튼 클래스
Button(frame, text="확인").grid(row=1, column=0)

root.mainloop()