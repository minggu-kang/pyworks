
# 파일 열기(open()) > 파일 쓰기(write()) > 파일 닫기(close())

f = open("C:/pyfile/hello.txt", 'w')
f.write("Hello~ python\n")
#f.write(1000) # 숫자는 입력 불가 > 포맷 방식으로 입력 해야함

num = "%d" % 1000000
f.write("%.2f\n" % 6.7)
f.write(num)
f.write("\n한글입력\n")

f.close()