# threading 모듈
import threading

def function_a():
    print("5초 간격으로 반복 실행")
    timer = threading.Timer(5,function_a) #함수이름> 괄호 생략
    timer.start()

function_a()