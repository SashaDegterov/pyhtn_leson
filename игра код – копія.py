from pygame import *
init ()
WHITE=(111,1,20)
BLACK=(250,250,20)
iii=(250,44,90)
rrr=(10,87,250)
www=(111,1,200)
win=display.set_mode((400,300))
win.fill(WHITE)
draw.rect(win,BLACK,(160,150,70,30))
draw.rect(win,BLACK,(160,200,70,30))
#
font = font.Font('shriwt.ttf', 25)
#шривті
text=font.render('Грати',True,rrr)
win.blit(text,(170,150))
text=font.render('Скіни',True,rrr)
win.blit(text,(170,200))
draw.polygon(win,BLACK, [(300,50),(350,50),(325,100)],5)
draw.circle(win,iii,(100,50),30)
draw.circle(win,iii,(150,50),5)
draw.circle(win,iii,(200,50),5)
draw.circle(win,iii,(250,50),5)
display.set_caption('Привет!')

#загзуска изображения
tank=image.load("tank.png")
#размер
tank_skeil_50=transform.scale(tank,(50,50))
#вівод на єкран
win.blit(tank_skeil_50,(10,100))
display.flip()


while True:
    ev = event.get()
    for i in ev:
        if i.type == QUIT:
            quit()
        if i.type==MOUSEBUTTONDOWN:
            if i.button==1:
                if 160<i.pos[0]<160+70 and 150<i.pos[1]<150+30:
                    win.fill(rrr)
                    display.update()
                if 160<i.pos[0]<160+70 and 200<i.pos[1]<200+30:
                         tank_skeil=transform.scale(tank,(50,50))
                        if 
                    win.fill(www)
                    tank_skeil_100=transform.scale(tank,(100,100))
                    win.blit(tank_skeil_100,(10,100))

                    tanksik=image.load("tanksik.jpg")
                    tanksik_skeil=transform.scale(tanksik,(100,100))
                    win.blit(tanksik_skeil,(200,100))
                    # if tank=image.load("tank.png")
                    #     tank_skeil=transform.scale(tank,(50,50))
                        win.blit(tank_skeil,(10,100))
                    display.flip()
                    display.update()