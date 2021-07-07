import os
'''
os.chdir("c:\\")
dir = os.popen("dir")
print(dir.read())
'''
# 디렉터리 이름 , 파일이름 - 리스트 반환

dirnames = os.listdir('c:\\pyworks/exercise')

print(dirnames)  #리스트 출력

print(dirnames[0])
print(dirnames[-1])

#요소 값 출력
for dirname in dirnames:
    print(dirname)