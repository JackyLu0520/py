from turtle import *
from time import *
from calendar import *


def draw_pointer(pointer,deg,length): 
    pointer.ht()
    pointer.width(4)
    pointer.color("white", "white")
    pointer.seth(deg)
    pointer.fd(length)
    pointer.begin_fill()
    pointer.left(90)
    pointer.fd(10)
    pointer.left(240)
    pointer.fd(20)
    pointer.left(240)
    pointer.fd(20)
    pointer.left(240)
    pointer.fd(10)
    pointer.end_fill()


def draw_clock():
    color("orange", "#FFBB00")
    goto(0, -250)
    begin_fill()
    width(50)
    circle(250)
    end_fill()
    color("white")
    pu()
    width(5)
    for i in range(1,61):
        home()
        seth(-i/5*30+90)
        fd(248)
        if int(i/5) == i/5:
            seth(-90)
            fd(14)
            write(str(int(i/5)), False, 'center', ('Arial', 22, 'normal'))
        else:
            pd()
            fd(1)
            pu()

    goto(0,0)
    dot(20, "#FFFFFF")
    ht()

def loop():
    tracer(0)
    draw_txt.reset()
    hour_pointer.reset()
    min_pointer.reset()
    sec_pointer.reset()
    h=localtime().tm_hour
    m=localtime().tm_min
    s=localtime().tm_sec
    hour_deg = -360/(12*60)*(60*h+m)+90
    draw_pointer(hour_pointer,hour_deg,160)
    min_deg = -6*m+90+s/6
    draw_pointer(min_pointer,min_deg,210)
    sec_deg = -6*s+90
    draw_pointer(sec_pointer, sec_deg, 240)
    draw_txt.pu()
    draw_txt.color("#FFFFFF")
    draw_txt.ht()
    draw_txt.goto(0,-120)
    draw_txt.write(wdays[localtime().tm_wday]+'\n\n\n\n\n\n' +
            str(strftime("%Y-%m-%d",localtime())),False,'center',('Arial',22,'normal'))
    tracer(1)
    ontimer(loop,500)


tracer(0)
print(month(localtime().tm_year,localtime().tm_mon))
hour_pointer = Turtle()
min_pointer=Turtle()
sec_pointer=Turtle()
draw_txt = Turtle()
wdays = ['  Monday ', '  Tuesday ', 'Wednesday',
         '  Thursday ', '    Friday ', '  Saturday', '   Sunday ']
draw_clock()
loop()
done()
