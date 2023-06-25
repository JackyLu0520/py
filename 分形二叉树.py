import turtle
t=turtle.Pen()
t.left(90)
def tree(l,lv):
    if(lv!=4):
        t.forward(l)
    if(lv==0):
        t.back(l)
    else:
        t.right(30)
        tree(l-6,lv-1)
        t.left(60)
        tree(l-6, lv-1)
        t.right(30)
        t.penup()
        t.back(l)
        t.pendown()


tree(60, 4)
turtle.done()
