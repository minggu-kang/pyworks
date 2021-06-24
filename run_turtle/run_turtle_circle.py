# 여러개의 원 만들기
import turtle as t
t.shape('turtle')
t.speed(0) # speed 1~9 , 0이 가장 빠름 
t.color('red')
t.bgcolor('black')
n = 60
for x in range(n):
    t.circle(80)
    t.left(360/n)
for x in range(n):
    t.circle(100)
    t.right(360/n)
for x in range(n):
    t.circle(200)
    t.right(360/n)

