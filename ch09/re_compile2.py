# 정규 표현식
import re

p = re.compile('\w+ \w+')  # 공백이 있을시 똑같이 공백을 넣어 주어야 한다.
m = p.match("2021 incheon")  # 처음에 일치하는 문자가 없어서 None
print(m)

s = p.search("2021 incheon") # 전체로 검색해서 일치된 문자를 검색
print(s)
