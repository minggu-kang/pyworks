import re

str = "park 010-1234-5678"
pat = re.compile("(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
m = re.search(pat, str)
'''
print(m.group(0))       #전체 문자열 반환
print(m.group(1))
print(m.group(2))
'''

# sub 메서드 사용

#s = pat.sub("\g<name>  \g<phone>", str)
pat = re.compile("(\w+)\s+(\d+[-]\d+[-]\d+)")
s = pat.sub("\g<1>  \g<2>", str)  #참조 번호 사용

print(s)