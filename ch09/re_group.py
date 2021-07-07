import re

# () 로 구분해서 이름과 전화번호를 분리해서 구분

p = re.compile("(\w+)\s(\d+[-]\d+[-]\d{4})")
s = p.search("jang 010-1234-5678")
print(s.group(1))
print(s.group(2))