from turtle import *


def f(lv, l):
    fd(l*0.1)
    if lv!=0:
        lt(60)
        f(lv-1, l*0.3)
        rt(55)
        fd(l*0.1)
        f(lv-1, l*0.9)
        rt(60)
        f(lv-1, l*0.3)
        lt(60)
        bk(l*0.1)
        rt(5)
    bk(l*0.1)

#tracer(0)
pu()
goto(0,-200)
pd()
lt(90)
f(5,400)
done()
