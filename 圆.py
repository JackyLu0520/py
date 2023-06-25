from turtle import *
def fun(lv,r,red):
    if red:
        fillcolor("red")
    else:
        fillcolor("white")
    begin_fill()
    circle(r)
    end_fill()
    if lv!=0:
        for i in range(5):
            circle(r,72)
            fun(lv-1,r/2.7,not red)
        pu()
        left(90)
        fd(r/2.7*2)
        right(90)
        pd()
        fun(lv-1,r-r/2.7*2,not red)
        pu()
        left(90)
        bk(r/2.7*2)
        right(90)
        pd()
#tracer(0)
pencolor("red")
speed(10)
pu()
goto(0,-350)
pd()
fun(4,400,True)
done()
