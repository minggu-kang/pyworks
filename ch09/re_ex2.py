import re

# 296페이지 참고

# {m} m은 반복 횟수
# {n , m}   n = 최소  m = 최대 횟수
str = "123?45yy7890 hi 999 Hello"
m1 = re.findall("\d{1,3}",str)

print(m1)

m2 = re.findall("[A-z]+",str)

print(m2)

m3 = re.findall("[1-5]{1,2}", str)

print(m3)