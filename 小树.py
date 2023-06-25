from turtle import *
from random import *


def tree(lv,branchlen,branchsize,borf):
    h=heading()
    width(branchsize)
    if lv!=0:
        fd(branchlen)
        lt(randint(20,45))
        tree(lv-1,branchlen*0.8,branchsize*0.8,borf)
        rt(randint(50,75))
        tree(lv-1,branchlen*0.8,branchsize*0.8,borf)
        setheading(h)
        bk(branchlen)
    elif borf==True:
        pencolor('yellow')
        tree(randint(0,2),4,2,False)
        pencolor('sienna')


def petal(m):
    for i in range(m):
        a=(150-300*(random()))
        b=(10-20*(random()))
        penup()
        forward(b)
        left(90)
        forward(a)
        pendown()
        pencolor('yellow')
        circle(1)
        penup()
        backward(a)
        right(90)
        backward(b)
#tracer(0)
ht()
setheading(90)
sety(-100)
speed(10)
pencolor('sienna')
bgcolor('black')
tree(7,50,5,True)
petal(100)
done()
