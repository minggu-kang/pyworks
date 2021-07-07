from tkinter import *

def click():
    try:
        word = entry.get()      #입력상자 내용 가져오기
        text.delete(0.0, END)   # 0행의 0열을 END로 초기화
        definition = dic[word]  #dic 딕셔너리의 value
        text.insert(END, definition)
    except KeyError:
        text.insert(END, "단어의 정의를 찾을 수 없습니다.")
root = Tk()
root.title("용어 사전")

Label(root, text="정의되어 있는 단어를 입력하고 엔터 키를 누르세요").grid(row=0, column=0, sticky=W)
entry = Entry(root, width=20)
entry.grid(row=1, column=0, sticky=W)
Button(root, text="제출",command=click).grid(row=2, column=0, sticky=W)



Label(root, text = "정의 : ").grid(row=3, column=0, sticky=W)
text = Text(root, width=80, height=10, bg="pink")
text.grid(row=4, column=0, sticky=W)


dic = {
    "이진수": "2진법으로 나타낸 숫자, 0과 1로 구성됨",
    "버그": "프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동착하지 않는 원인을 제공하는 코드",
    "함수": "재사용 가능한 명령어 코드 조각",
    "장고": "파이썬으로 작성하는 웹 프레임워크로 웹사이트를 제작할 수 있는 프로그램."
}

root.mainloop()