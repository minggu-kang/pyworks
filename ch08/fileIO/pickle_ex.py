import pickle
# 객체의 형태를 그대로 저장하고 불러오는 모듈

with open('new_data.txt','wb') as f:
    li = ['치킨', '피자', '족발']
    dic = {1:'삼겹살', 2:'갈매기살', 3:'항정살'}
    pickle.dump(li,f)
    pickle.dump(dic,f)


with open('new_data.txt','rb') as f:
    li = pickle.load(f)
    dic = pickle.load(f)
    print(li)
    print(dic)