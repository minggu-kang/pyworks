# 도형의 넓이 계산하기

#정사각형의 넓이
size = int(input("한변의 길이 : "))

area = size * size

#print("정사각형의 넓이 : ",area,"cm")
print("정사각형의 넓이 : %dcm" % area)

#삼각형의 넓이

width = int(input("밑변의 길이 : " ))
height = int(input("높이 : "))

area = width * height / 2

#print("삼각형의 넓이 : " , area,"cm")
print("삼각형의 넓이 : %dcm" % area)

# %d(정수) = 문자열 포맷 코드 
