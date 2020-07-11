# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech (Game 1 Code Along @ https://www.freecodecamp.org/news/learn-python-by-building-5-games/)
# Part 1: Getting Started

#Make sure to uncomment/comment out the correct Files according to Mac, Windows Linux (notes provided)💚💚💚


import turtle #built in graphics
import winsound #for windows
#import os #forMac

win = turtle.Screen() # win == window
win.title("Pong by @TokyoEdTech")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

#Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("#00ff00")
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("#00ff00")
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#00ff00")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("#00ff00")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 | Player B: 0", align="center", font=("Courier", 24, "bold"))



#Functions
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




# Keyboard Bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
  win.update()

  #Move the Ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor()+ ball.dy)

  #Border Checking
  if ball.ycor()>290:
    ball.sety(290)
    ball.dy *= -1
    winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC) #for Windows
    #os.system("afplay sound/bounce.wav&") #for Mac (for Linux chang afplay to aplay)


  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1
    winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC) #for Windows
    #os.system("afplay sound/bounce.wav&") #for Mac (for Linux chang afplay to aplay)

  if ball.xcor() > 390:
    ball.goto(0,0)
    ball.dx *= -1
    score_a += 1
    pen.clear()
    pen.write(f"Player A: {score_a} | Player B: {score_b}", align="center", font=("Courier", 24, "bold"))
    winsound.PlaySound("sound/oops.wav", winsound.SND_ASYNC) #for Windows
    #os.system("afplay sound/oops.wav&") #for Mac (for Linux chang afplay to aplay)

  if ball.xcor() < -390:
    ball.goto(0,0)
    ball.dx *= -1
    score_b += 1
    pen.clear()
    pen.write(f"Player A: {score_a} | Player B: {score_b}", align="center", font=("Courier", 24, "bold"))
    winsound.PlaySound("sound/oops.wav", winsound.SND_ASYNC) #for Windows
    #os.system("afplay sound/oops.wav&") #for Mac (for Linux chang afplay to aplay)

  # Paddle & Ball Bounce
  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
    ball.setx(340)
    ball.dx *= -1
    winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC) #for Windows
    #os.system("afplay sound/bounce.wav&") #for Mac (for Linux chang afplay to aplay)

  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40):
    ball.setx(-340)
    ball.dx *= -1
    winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC) #for Windows
    #os.system("afplay sound/bounce.wav&") #for Mac (for Linux chang afplay to aplay)