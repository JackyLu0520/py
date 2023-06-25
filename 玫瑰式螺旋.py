import turtle

t = turtle.Pen()


sides = int(turtle.numinput('sides', 'sides=?', 6, 1, 9))
t.speed(100)
turtle.bgcolor('black')
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple', 'skyblue', 'pink', 'white']
for i in range(100):
    t.forward((i * 4))
    pos = t.position()
    heading = t.heading()
    for x in range(sides):
        t.pensize((i / 7))
        t.pendown()
        t.pencolor(colors[(x % sides)])
        t.circle(int((i / 5)))
        t.left((360 / sides))
        t.penup()
    t.setx(pos[0])
    t.sety(pos[1])
    t.setheading(heading)
    t.left((360 / sides + 2))
turtle.done()
