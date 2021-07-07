# raise -> 에러 미뤄둔다 . 사용하는 쪽에서 발생하도록 함
class Bird:
    def fly(self):
        #print("새가 날아갑니다.")
        raise NotImplementedError  #일부러 오류 발생 시키기

class Engle(Bird):
    #pass

    def fly(self):
        print("독수리가 하늘을 높이 납니다")


#bird = Bird()
#bird.fly()
eagle = Engle()
eagle.fly()