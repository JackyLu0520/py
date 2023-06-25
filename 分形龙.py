from turtle import *
from math import cos,radians
def l(lv,size):
    if lv==0:
        fd(size)
    else:
        lt(45)
        l(lv-1,size*cos(radians(45)))
        rt(90)
        r(lv-1, size*cos(radians(45)))
        lt(45)
def r(lv,size):
    if lv==0:
        fd(size)
    else:
        rt(45)
        l(lv-1,size*cos(radians(45)))
        lt(90)
        r(lv-1,size*cos(radians(45)))
        rt(45)
tracer(0)
setheading(45)
pu()
goto(-100,-100)
pd()
l(19,500)
done()