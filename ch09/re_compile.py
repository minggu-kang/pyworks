# 정규 표현식
import re

p = re.compile('[a-z]+')  # + 반복을 의미하는 메타 문자
m = p.match('aftternoon')

print(m)

