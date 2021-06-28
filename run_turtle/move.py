import turtle as t
import random as r


t.shape("turtle")
t.up()
t.speed(0)
#t.goto(400, -350) # 위치 지정 x값 y 값

# 생성위치 랜덤
x = r.randint(-250, 250)
y = r.randint(-250, 250)
t.goto(x,y)


t.mainloop()