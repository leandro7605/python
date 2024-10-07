import turtle
import random
import math

score = 0
window = turtle.Screen()
window.setup(600,462)
window.bgpic("Star.gif")
turtle1 = turtle.Turtle()


def col(i,j):
    global score
    turtle2 = turtle.Turtle()
    turtle1.hideturtle()
    turtle1.penup()
    turtle1.speed(100)
    score += 1
    turtle2.penup()
    turtle2.hideturtle()
    turtle2.goto(-280,180)
    turtle2.color("yellow")
    style = ('Courier', 30, 'italic')
    turtle2.pendown()
    turtle2.write("Points: " + str(score), font=style)
    turtle2.penup()
    turtle1.goto(random.randint(-260,260),random.randint(-200,200))
    turtle1.showturtle()
    turtle1.pendown()
    turtle1.speed(1)
    turtle1.color(random.choice(colors))
    
turtle1.shape("turtle")
colors = ["lime green", "dark orange", "green yellow"   , "gold", "dark violet", "red", "blue"]

direction =[0, 90, 180, -90, -180, 45, -45]
turtle1.color("blue")
step =[20,40,60,80]
turtle1.speed(1)

for _ in range(50):
    turtle1.onclick(col)
    turtle1.pensize(7)
    turtle1.forward(random.choice(step))
    if turtle1.xcor() > 290:
        turtle1.setheading(180)
        turtle1.forward(150)
    if turtle1.xcor() < -290:
        turtle1.setheading(0)
        turtle1.forward(150)
    if turtle1.ycor() > 221:
        turtle1.setheading(270)
        turtle1.forward(150)
    if turtle1.ycor() < -221:
        turtle1.setheading(90)
        turtle1.forward(150)
    turtle1.setheading(random.choice(direction))
turtle1.onclick(col)



    
turtle2.clear()
