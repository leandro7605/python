import turtle
import time
a = 0
def schildkroete():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

turtle.shape("turtle")
turtle.color("black")
turtle.width(300)
turtle.up()
turtle.goto(-350,250)
turtle.down()
turtle.forward(620)
turtle.right(90)
turtle.forward(270)
turtle.right(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(600)
turtle.width(15)
turtle.up()
turtle.goto(0,0)
turtle.down()
turtle.color("blue")
turtle.width(10)

while a < 32:
    schildkroete()
    turtle.right(11.25)
    a += 1
