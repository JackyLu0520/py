import turtle

__Pen = turtle.Pen()


def tr1(lv, size):

    if (lv == 0):
        __Pen.forward(size)
    else:
        tr1(lv - 1, size / 4)
        __Pen.left(60)
        tr2(lv - 1, size / 4)
        __Pen.left(60)
        tr1(lv - 1, size / 4)
        __Pen.right(60)
        tr2(lv - 1, size / 4)
        __Pen.right(60)
        tr1(lv - 1, size / 4)
        __Pen.right(60)
        tr2(lv - 1, size / 4)
        __Pen.right(60)
        tr1(lv - 1, size / 4)
        __Pen.left(60)
        tr2(lv - 1, size / 4)
        __Pen.left(60)
        tr1(lv - 1, size / 4)

def tr2(lv, size):

    if (lv == 0):
        __Pen.forward(size)
    else:
        tr2(lv - 1, size / 4)
        __Pen.right(60)
        tr1(lv - 1, size / 4)
        __Pen.right(60)
        tr2(lv - 1, size / 4)
        __Pen.left(60)
        tr1(lv - 1, size / 4)
        __Pen.left(60)
        tr2(lv - 1, size / 4)
        __Pen.left(60)
        tr1(lv - 1, size / 4)
        __Pen.left(60)
        tr2(lv - 1, size / 4)
        __Pen.right(60)
        tr1(lv - 1, size / 4)
        __Pen.right(60)
        tr2(lv - 1, size / 4)
turtle.tracer(0)
tr1(6, 200)
turtle.done()
