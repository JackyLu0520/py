n = int(input("个数："))
data,colors,t = [],[],[]
for i in range(n):
    t = input().split(" ")
    data.append(int(t[0]))
    colors.append(t[1])
from turtle import *
for i in range(n):
    begin_fill()
    color(colors[i],colors[i])
    fd(100)
    lt(90)
    circle(100,data[i]*3.6)
    lt(90)
    fd(100)
    lt(180)
    end_fill()
done()
    
