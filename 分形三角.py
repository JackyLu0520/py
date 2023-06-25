from turtle import *
def tr(lv,length):
    if lv!=0:
        if lv==1:
            begin_fill()
        for i in range(3):
            tr(lv-1,length/2)
            left(120)
            pd()
            fd(length)
            pu()
        if lv==1:
            end_fill()
pencolor("green")
fillcolor("green")
tr(6,200)
done()