# 온도변환기 클래스

class Converters:
    def __init__(self,units_from, units_to, factor, offset):
        self.units_form = units_from    #바꿀 단위
        self.unuits_to = units_to       #결과 단위
        self.factor = factor            #요소
        self.offset = offset            #요소2

    def convert(self,value):
        return self.factor * value + self.offset

if __name__ == "__main__":
    conv = Converters('C','F',1.8,32)
    print(str(conv.convert(23))+ conv.unuits_to)