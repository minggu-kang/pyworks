with open('scorelist.txt','r') as f:
    d2 = [] # 이차원 리스트 준비
    for i in range(3):
        d2.append(f.readline().split())

    '''
    [
    ['짱구', '70', '88'], 
    ['훈이', '45', '33'], 
    ['철수', '97', '98']
    ]
    '''
    for i in range(3):
        d2[i][1] = int(d2[i][1]) # 국어(숫자형 변경)
        d2[i][2] = int(d2[i][2]) # 수학(숫자형 변경)
        d2[i].append(d2[i][1] + d2[i][2]) # 총점 - 4열
        d2[i].append(d2[i][3] / 2) #평균 -5열



    print("    ******** 성 적 표 ********    ")
    print("  ============================== ")
    print("이름    국어    수학    총점     평균")
    for i in range(3):
        print("{}     {}     {}     {}     {}".format(d2[i][0], d2[i][1], d2[i][2], d2[i][3], d2[i][4]))
    print("  ============================== ")
    print("  **********과목별 평균************")
    kor_sun = 0
    math_sum = 0
    for i in range(3):
        kor_sun += d2[i][1] # 국어 총점
        math_sum += d2[i][2] # 수학 총점
    print(" 국어 : %.2f, 수학 : %.2f" % (kor_sun/3, math_sum/3))