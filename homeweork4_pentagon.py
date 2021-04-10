import turtle
import math
t=turtle.Pen()
for _ in range(4):
    t.pencolor("red")
    t.forward(100)
    t.left(90)
t.left(45)
t.forward(100 * math.sqrt(2))
t.right(135)
t.forward(100)
t.right(135)
t.forward(100 * math.sqrt(2))
for _ in range(2):
    t.right(90)
    t.forward(50 * math.sqrt(2))
turtle.done()