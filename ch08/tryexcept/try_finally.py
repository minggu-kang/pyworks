# try ~ except ~ finally

def divide(x, y):
    try:
        div = x / y

    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    else:
        print(div)
    finally:
        print("강제 실행 부분")
#divide(2,5)
divide(2,0)