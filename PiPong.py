import turtle

wn = turtle.Screen()
wn.title("PiPong")
wn.bgcolor('black')
wn.setup(width=600, height=800)
wn.tracer(0)
print('lol')

#Score
score_a = 0
score_b = 0



# Игрок 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=1, stretch_len=5)
paddle_a.penup()
paddle_a.goto(0, -350)
# Игрок 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=1, stretch_len=5)
paddle_b.penup()
paddle_b.goto(0, 350)
# Мяч
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.3
ball.dy = 0.3

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,370)
pen.write('Player A: {} Player B: {}'.format(score_a,score_b), align='center', font=('Courier',20,'normal'))


# Functions

def paddle_a_left():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)

def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)

def paddle_b_left():
    x = paddle_b.xcor()
    x -= 20
    paddle_b.setx(x)

def paddle_b_right():
    x = paddle_b.xcor()
    x += 20
    paddle_b.setx(x)

# Controls

wn.listen()
wn.onkeypress(paddle_a_left,'a')
wn.onkeypress(paddle_a_right,'d')
wn.onkeypress(paddle_b_left,'Left')
wn.onkeypress(paddle_b_right,'Right')

# Main game loop
while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border
    if ball.xcor()> 290:
        ball.setx(290)
        ball.dx *= -1
    if ball.xcor()< -290:
        ball.setx(-290)
        ball.dx *= -1

    if ball.ycor()>390:
        ball.goto(0,0)
        ball.dy *= -1
        score_a +=1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 20, 'normal'))

    if ball.ycor()<-390:
        ball.goto(0,0)
        ball.dy *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 20, 'normal'))

    # paddle and ball collisions
    if ball.ycor() >340 and ball.ycor() < 350  and ball.xcor() < paddle_b.xcor() +40 and ball.xcor() > paddle_b.xcor() -40:
        ball.sety(340)
        ball.dy *=-1
    if ball.ycor()<-340 and ball.ycor()>-350  and ball.xcor() < paddle_a.xcor() +40 and ball.xcor() > paddle_a.xcor() -40:
        ball.sety(-340)
        ball.dy *=-1