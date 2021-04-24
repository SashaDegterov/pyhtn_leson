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
x_rect = 160
display.set_caption('Привет!')
display.update()
draw.rect(win,rrr,(x_rect,430,70,30))
display.update()
clock = time.Clock()
while True:
    ev = event.get()
    for i in ev:
        keys = key.get_pressed ()
        if i.type == QUIT:
            quit()
        if i.type==KEYDOWN:
            if keys [K_LEFT] :
                draw.rect(win,BLACK,(x_rect,430,70,30))
                x_rect-=10
                draw.rect(win,rrr,(x_rect,430,70,30))
                display.update()
            if keys [K_RIGHT] :
                draw.rect(win,BLACK,(x_rect,430,70,30))
                x_rect+=10
                draw.rect(win,rrr,(x_rect,430,70,30))
                display.update()
    # for i in range(380):
    draw.circle(win,BLACK,(x,y),25)
    y=y+1
    if y==400:
        y=20
        x = random.randint(25,375)
    draw.circle(win,WHITE,(x,y),25)
    clock.tick(70)
    display.update()