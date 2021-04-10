#программа для рисовання зірки
import turtle
t=turtle.Pen()
t.pencolor("red")
for _ in range(6):
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.right(60)
turtle.done()