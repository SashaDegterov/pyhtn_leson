from pygame import *
init ()
WHITE=(111,1,20)
BLACK=(0,0,0)
iii=(250,44,90)
rrr=(10,87,250)
www=(111,1,200)
win=display.set_mode((400,300))
display.set_caption('Привет!')

#загзуска изображения
tank=image.load("tank.png")
#размер
tank_skeil_50=transform.scale(tank,(50,50))
#вівод на єкран
win.blit(tank_skeil_50,(10,100))
display.flip()
X=10
y=100
while True:
    ev = event.get()
    for i in ev:
        if i.type == QUIT:
            quit()
        if i.type==KEYDOWN:
            if i.key==K_d:
                X+=10
                win.fill(BLACK)
                win.blit(tank_skeil_50,(X,y))
                display.flip()
                if X==400:X=-20
            if i.key==K_a:
                X-=10
                win.fill(BLACK)
                win.blit(tank_skeil_50,(X,y))
                display.flip()
                if X==-20:X=400
            if i.key==K_w:
                y-=10
                win.fill(BLACK)
                win.blit(tank_skeil_50,(X,y))
                display.flip()
                if y==0:y=300
            if i.key==K_s:
                y+=10
                win.fill(BLACK)
                win.blit(tank_skeil_50,(X,y))
                display.flip()
                if y==300:y=0
            if i.key==K_RIGHT:
                X+=10
                win.fill(BLACK)
                win.blit(tank_skeil_50,(X,y))
                display.flip()
                if X==400:X=-20
            if i.key==K_LEFT:
                X-=10
                win.fill(BLACK)
                win.blit(tank_skeil_50,(X,y))
                display.flip()
                if X==-20:X=400
            if i.key==K_UP:
                y-=10
                win.fill(BLACK)
                win.blit(tank_skeil_50,(X,y))
                display.flip()
                if y==0:y=300
            if i.key==K_DOWN:
                y+=10
                win.fill(BLACK)
                win.blit(tank_skeil_50,(X,y))
                display.flip()
                if y==300:y=0