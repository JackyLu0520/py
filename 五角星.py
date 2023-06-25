import turtle
#import ramdom


def setup():
    turtle.penup()
    turtle.shape("turtle")
    turtle.speed(7)
    turtle.screensize(800,600)
def star(x,y,size):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for i in range(5):
        turtle.left(144)
        turtle.forward(size)
        turtle.right(72)
        turtle.forward(size)
    turtle.end_fill()
    turtle.penup()
setup()
star(0,0,100)