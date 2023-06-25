from turtle import *
def fun(lv,length):
    if lv==0:
        fd(length)
        bk(length)
    else:
        fun(lv-1,length/2)
        fd(length/2)
        left(60)
        fun(lv-1,length/3)
        right(60)
        right(60)
        fun(lv-1,length/3)
        left(60)
        fun(lv-1, length/2)
        bk(length/2)
for i in range(6):
    fun(5,300)
    left(60)
done()
