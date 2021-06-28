import turtle as t
import random as r

def turn_right():  #오른쪽 화살키
    t.setheading(0)


def turn_up():      #위쪽 화살키
    t.setheading(90)


def turn_left():    #왼쪽 화살키
    t.setheading(180)


def turn_down():    #아래쪽 화살키
    t.setheading(270)

def play():
    t.forward(10)
    te.forward(9)

    #적 거북 > 주인공 거북 쫓아감
    ang = te.towards(t.pos())
    te.setheading(ang)

    #주인공 거북 > 먹이 먹음 > 먹이 랜덤이동
    if t.distance(tf) < 12:
        x = r.randint(-250, 250)
        y = r.randint(-250, 250)
        tf.goto(x, y)

    if t.distance(te) >= 12:  # 12보다 작으면 작동x

        t.ontimer(play, 100)  # 0.1초 간격으로 작동




# 메인 영역
t.setup(500,500)
t.title("Turtle Run")
t.bgcolor("pink")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white") #주인공 거북

#적 거북

te = t.Turtle() #Turtle() 클래스에서 te 인스턴스 생성
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

#먹이
tf = t.Turtle()
tf.shape("circle")
tf.color("green")
tf.speed(0)
tf.up()
tf.goto(0, -200)

#키보드 연동
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")

t.listen()
play()

t.mainloop()




