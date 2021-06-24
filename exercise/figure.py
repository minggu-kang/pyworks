#도형 면적 계

def square(w, h):
    area = w * h
    return area

def triangle(w,h):
    area = w * h /2
    return area

print('사각형의 면적 : ',square(5,4))
print('삼각형의 면적 : ',triangle(4,7))
