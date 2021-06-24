# 딕셔너리

person = {}
person['name'] = "철수"
person['age'] = 17
print(person)

person['address'] = '서울'
print(person)


for key in person:
    print(person[key])

#삭제 : dic.pop('address') 와 같음
del person['address']

print(person)
