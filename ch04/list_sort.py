# 리스트의 최대 , 최솟값 

score = [70,80,50,65,90,45]
max = score[0]
n = len(score)
score.sort()
print(score)

for i in range(1,n):
    if max < score[i]:
        max = score[i]
print("최고 점수 {}점".format(max))



# 오름차순 정렬

#score.sort()
#print(score)
for i in range(0,n):
    for j in range(0,n-1):
        if score[j] >score[j+1]:
            score[j],score[j+1] = score[j+1],score[j]
    '''
        # 1행
          70 50 65 80 45 90
        # 2 행
          50 65 70 45 80 90
        # 3 행
          50 65 45 70 80 90
        # 4 행  
          50 45 65 70 80 90
        # 5 행
          45 50 65 70 80 90 
    '''
for i in score:
    print(i,end=' ')

