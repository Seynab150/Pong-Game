import turtle

# first a screen was created with the setting set to my preferences
# tracer(0) was used to stop the window from updating and slowing down the game
wn = turtle.Screen()
wn.title("Pong Game by Saynab")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

# score keeping
score_a = 0
score_b = 0

# first paddle
# the speed is the maximum speed of animation and starting coordinates were set
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# second paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
# there is no need to change the size as 20px is the default size
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# separate the balls movement into two parts
ball.dx = 0.4
ball.dy = -0.4

# pen (hide the turtle as only the text is needed
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))


# function: ycor is a turtle function and it returns the y coordinate
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard bindings
wn.listen()
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")


# main game loop
while True:
    wn.update()

    # moves the ball as it adds dx/dy to the current x coordinate by adding 1px multiple times in each direction
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking using the known height and ball size
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        # if the ball goes off the right side off the screen player 1 gets a point
        score_a += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        # if the ball goes off the left side off the screen player 2 gets a point
        score_b += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# paddle and ball collision using the coordinates of the paddle and ball
# so if the edges are touching (>340) and if its between the top/bottom of the paddle (40) it should count as a bounce
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1