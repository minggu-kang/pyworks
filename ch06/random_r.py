# random
import random
def random_pop(data):
    number = random.randint(0,len(data)-1)
    return data.pop(number)

if __name__ =="__main__":
    data = [1,2,3,4,5,6,7,8,9,10]
    while data : print(random_pop(data),end=' ')
