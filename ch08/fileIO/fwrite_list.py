
f = open("c:/pyfile/2021kbo.txt", "w")

team = ['KIA', '삼성', 'SSG', 'LG', 'NC', 'KT', '키움', '한화']

'''
for i in team:
    f.write(i+" ")
f.close()
'''
# range()함수 사용
#n  = len(team)
for i in range(len(team)):
    f.write(team[i] + " ")

f.close


f = open("c:/pyfile/2021kbo.txt", "r")
data = f.read()
print(data)
f.close()