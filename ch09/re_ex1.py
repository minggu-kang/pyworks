import re

# ' * ' ' + ' 의 차이 비교


# ' * ' 는 * 앞의 문자가 0개 이상 반복(없어도 가능)
pat = re.compile("ca*t")
m1 = re.findall(pat, "caaat")

print(m1)

m2 = re.findall(pat, "ct")

print(m2)


# ' + ' 는  +앞의 문자가 1개 이상 반복 (없으면 찾을수 없음)


pat2 = re.compile("ca+t")
m3 = re.findall(pat2, "caat")

print(m3)

pat2 = re.compile("ca+t")
m4 = re.findall(pat2, "ct")

print(m4)
