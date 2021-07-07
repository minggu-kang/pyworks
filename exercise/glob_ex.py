import glob

#data 를 리스트형으로 반환
data=glob.glob('c:/pyworks/exercise/*.py')

print(data)

#요소값 출력
print(data[0])
print(data[-1])


for i in data:
    print(i)