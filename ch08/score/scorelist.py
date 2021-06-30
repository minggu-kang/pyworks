with open('scorelist.txt', 'a') as f:
    while True:
        try:
            score = input("성적을 저장할까요?(y/n)")
            if score == "y" or score == "Y":
                    name = input("이름 입력 :")
                    kor = int(input("국어 점수 :"))
                    math = int(input("수학 점수 :"))
                    avg = (kor + math) / 2

                    f.write(name + ' ')
                    f.write(str(kor) + ' ')
                    f.write(str(math) + ' ')
                    f.write(str(avg) + '\n')
            elif score == "n" or score == "N":
                print("입력을 종료합니다.")
                break
            else:
                 print("잘못된 입력입니다. 다시 입력해 주세요 : ")
        except ValueError:
            print("잘못된 입력입니다.")
