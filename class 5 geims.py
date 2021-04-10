from pygame import *
init ()
WHITE=(111,1,20)
BLACK=(250,250,20)
iii=(250,44,90)
rrr=(10,87,250)
www=(111,1,200)
win=display.set_mode((400,300))
win.fill(WHITE)
#font = font.Font(None, 25)
#text=font.render('тут могла біть твоя реклама',True,rrr)
#win.blit(text,(50,150))
#draw.polygon(win,BLACK, [(100,0),(10,100),(100,100)],5)
#draw.polygon(win,BLACK, [(100,0),(200,0),(200,100),(100,100)],5)
#draw.polygon(win,BLACK, [(200,0),(397,0),(397,200),(200,200)],5)
#draw.polygon(win,BLACK, [(10,100),(10,200),(200,200),(200,100)],5)
#draw.polygon(win,BLACK, [(10,200,),(10,250),(397,250),(397,200)],5)
display.set_caption('Привет!')
display.flip()
#draw.polygon(win,BLACK, [(250,100),(370,100),(300,190)],5)
#draw.circle(win,iii,(279,76),30)
#draw.circle(win,rrr,(335,76),30)
#draw.circle(win,www,(305,30),30)
#draw.circle(win,BLACK,(50,250),25)
#draw.circle(win,WHITE,(50,250),15)
#draw.circle(win,BLACK,(345,250),25)
draw.circle(win,WHITE,(345,250),15)
rectangle=draw.rect(win,BLACK,(100,50,50,30))
display.flip()
while True:
    ev = event.get()
    for i in ev:
        if i.type == QUIT:
            quit()
        if i.type==MOUSEBUTTONDOWN:
            if i.button==1:
                if 100<i.pos[0]<150 and 50<i.pos[1]<80:
                    win.fill(rrr)

                    display.update()  
           # if i.button==3:
               # text=font.render (str(i.pos),True,rrr)
               # win.blit(text,i.pos)
               # display.update()