# 함수의 정의 및 호출
# return 이 없고 , 매개변수 없는 함수

def say_hello():
    print("안녕하세요.")

say_hello() # 호출
say_hello()



print('='*50)

# return 이 없고 매개변수 있는 함수

def say_hello2(name):
    print("{}님 반갑습니다.".format(name))

say_hello2("철수")
say_hello2("영희" )
