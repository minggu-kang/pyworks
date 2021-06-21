
# Q1

kor = 80
eng = 75
math = 55

sum = kor+eng+math

avg = sum / 3

print("평균 : ",avg)


# Q2

print("="*50)

num = 13
if num % 2 ==1 :
    print("홀수입니다")
else:
    print("짝수입니다")
    
print("="*50)

#Q3

pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
print(yyyymmdd)
print(num)

print("="*50)

#Q4

pin ="881120-1068234"
gender = pin[7]
#print(gender)
if gender =="1":
    print("남자")
else:
    print("여자")

print("="*50)

#Q5

a = "a:b:c:d"
b = a.replace(':','#')
print(b)

print("="*50)

#Q6

a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

print("="*50)

#Q7
a = ['Life','is','too','short']
result =' '.join(['Life','is','too','short'])
print(result)

print("="*50)

# split() 예제
s = "Life is too short"
s= s.split() #구분 기호 공백
print(s)

print("="*50)

s = "a:b:c:d"
s = s.split(':')
print(s)

print("="*50)
#Q8
a = (1,2,3)
a = a+(4,)
print(a)

