from turtle import *
from math import cos,radians
import random
global deg
def draw(a):
    if a>5:
        down()
        r=random.randint(1,255)
        g=random.randint(1,255)
        b=random.randint(1,255)
        color(r,g,b)
        begin_fill()
        for i in range(5):
            fd(a)
            right(90)
        end_fill()
        up()
        left(90+deg)
        draw(a*cos(radians(deg)))
        right(90)
        fd(a*cos(radians(deg)))
        draw(a*cos(radians(90-deg)))
        right(90)
        fd(a*cos(radians(90-deg)))
        right(deg)
        fd(a)
        right(90)
        fd(a)
        right(90)
deg=int(numinput("deg","deg=?",45,10,80))
mode('logo')
speed(10)
colormode(255)
seth(0)
up()
goto(-50,-200)
draw(100)
done()
