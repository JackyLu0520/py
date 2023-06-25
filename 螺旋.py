import turtle


t = turtle.Pen()
sides = int(turtle.numinput("sides","size=?",6,1,6))
t.speed(100)
turtle.bgcolor('black')
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple', 'skyblue', 'pink', 'white']
for x in range(0, 270):
    t.pencolor(colors[(x % sides)])
    t.forward((x * 2))
    t.left((360 / sides + 1))
    t.pensize(((x * sides) / 150))
turtle.done()
