# 랜덤 위치

import turtle as t
import random as r

t.shape('turtle')
t.speed(0)
t.bgcolor("pink")
t.setup(1500,1500) # setup : 작업 영역의 크기 

for x in range(1500): # 거북이 행동수
    angle = r.randint(1, 360) # 거북이 머리 방향
    t.setheading(angle)
    t.forward(20) 
