# 리스트를 매개변수로 전달하기
# 점수의 평균 계산하기

def avg(a):
    sum=0
    count = len(a)
    
    for i in a:
        sum += i
        
    avge = sum / count
    return avge

avg = avg([70,80,60,90,100])
print('평균 점수 : ',avg)
