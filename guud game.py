from pygame import *
import random
init ()
WHITE=(111,1,20)
BLACK=(0,0,0)
iii=(250,44,90)
rrr=(10,87,250)
www=(111,1,200)
win=display.set_mode((400,450))
x = random.randint(25,375)
draw.circle(win,WHITE,(x,20),25)
y = 20
display.set_caption('Привет!')
display.update()
clock = time.Clock()
while True:
    ev = event.get()
    for i in ev:
        if i.type == QUIT:
            quit()
    for i in range(380):
        win.fill(BLACK)
        y=y+1
        draw.circle(win,WHITE,(x,y),25)
        clock.tick(70)
        display.update()
        if y==400:
            y=20
            x = random.randint(25,375)