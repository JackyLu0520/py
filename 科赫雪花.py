import turtle
import random


# 分形雪花
t = turtle.Pen()

def snow(size, n):

    if (n == 0):
        t.forward(size)
    else:
        for angel in [0, 60, (-120), 60]:
            t.left(angel)
            # 函数调用自身，这种调用方式叫做递归
            # 递归时参数变小，画的是更小的雪花
            snow(size / 3, n - 1)

def draw():

    t.fillcolor('white')
    t.speed(0)
    t.penup()
    t.goto((-200), 100)
    t.pendown()
    t.pensize(2)
    level = 3
    for i in range(0, 50):
        turtle.tracer(0)
        t.penup()
        t.goto(random.randint((-340), 340), random.randint((-240), 240))
        t.pendown()
        t.begin_fill()
        snow(50, level)
        t.right(120)
        snow(50, level)
        t.right(120)
        snow(50, level)
        t.end_fill()
        turtle.tracer(1)
    turtle.done()

#开始进入Python的世界
turtle.bgcolor('cyan')
draw()
