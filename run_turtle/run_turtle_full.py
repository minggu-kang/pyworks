import turtle as t
import random as r

def turn_right():  #오른쪽 방향키
    t.setheading(0)


def turn_up():      #위쪽 방향키
    t.setheading(90)


def turn_left():    #왼쪽 방향키
    t.setheading(180)


def turn_down():    #아래쪽 방향키
    t.setheading(270)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

def message(m1, m2):
    t.clear()
    t.goto(0,100)
    t.write(m1, False, "center", ("",20))
    t.goto(0,-100)
    t.write(m2, False, "center", ("",15))
    t.home()

def play():
    global score
    global playing

    t.forward(10)

    # 적 거북 속도 = 점수 up 속도 up
    if r.randint(1,5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)

    speed = score + 5
    if speed > 15:
        speed = 15
    te.forward(speed)

    #주인공 거북 > 먹이 먹음 > 먹이 랜덤이동
    if t.distance(tf) < 12:
        score += 1
        t.write(score)
        x = r.randint(-250, 250)
        y = r.randint(-250, 250)
        tf.goto(x, y)

    # 주인공 거북 > 적거북 잡히면 게임 종료
    if t.distance(te) < 12:  # 12보다 작으면 작동x
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    if playing:
        t.ontimer(play, 100)





# 메인 영역
# 점수 변수와 플레이 스위치 변수(bool)
score = 0
playing = False


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
t.onkeypress(start, "space")
t.listen()
message("Turtle Run","[Space]")


t.mainloop()




